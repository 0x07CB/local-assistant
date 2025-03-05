#coding: utf-8

from functions import get_current_date
from functions import get_current_time
from functions import is_website_accessible
from functions import get_temperature_and_humidity

from tools import get_current_date_tool
from tools import get_current_time_tool
from tools import is_website_accessible_tool
from tools import get_temperature_and_humidity_tool

from typing import List
from typing import Dict
from typing import Union
from typing import Tuple
from typing import Optional
from typing import Any


#########################
### Imports externes ###
#########################
import requests

from rich import print as rprint

from ollama import generate
from ollama._types import Options
from ollama import ChatResponse
from ollama import Client
from ollama import chat


#########################
### Fonctions locales ###
#########################
def ollama_client(ollama_base_url: str) -> Client:
    """
    Crée un client Ollama
    
    Args:
        ollama_base_url (str): L'URL de base de l'API Ollama
        
    Returns:
        Client: Le client Ollama
    """
    return Client(
        host=ollama_base_url,
        headers={'x-some-header': 'some-value'}
    )

def model_unload(model: str, ollama_base_url: str) -> None:
    """
    Décharge un modèle spécifié
    
    Args:
        model (str): Le nom du modèle à décharger
        ollama_base_url (str): L'URL de base de l'API Ollama
    """
    url = f"{ollama_base_url}/api/generate"
    payload = {
        "model": model,
        "keep_alive": 0
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        rprint("[bold green]Modèle déchargé avec succès.[/bold green]")
    else:
        rprint(f"[bold red]Erreur[/bold red]: [underline]Lors du déchargement du modèle[/underline]. Status code: {response.status_code}, Response: {response.text}")



def generate_response(
    model: Optional[str] = "llama3.2:3b",
    messages: Optional[List[Dict[str, Any]]] = None,
    tools: Optional[List[Dict[str, Any]]] = None,
    available_functions: Optional[Dict[str, Any]] = None,
    options: Optional[Options] = None,
    prompt: Optional[str] = None,
    client: Optional[Client] = None
) -> str:
    """
    Génère une réponse à partir du modèle
    
    Args:
        model (str): Le nom du modèle à utiliser
        messages (List[Dict[str, Any]]): Les messages à envoyer au modèle
        tools (List[Dict[str, Any]]): Les outils disponibles pour le modèle
        available_functions (Dict[str, Any]): Les fonctions disponibles pour le modèle
        options (Options): Les options pour le modèle
        prompt (str): Le prompt à envoyer au modèle
        ollama_base_url (str): L'URL de base de l'API Ollama
        
    Returns:
        str: La réponse du modèle
    """
    if messages is None:
        messages = [{'role': 'user', 'content': f'{prompt}'}]

    rprint(f'[italic yellow]Prompt:[/italic yellow] \n{messages[-1]["content"]}')

    try:
        if client is None:
            response: ChatResponse = chat(
                model,
                messages=messages,
                tools=tools,
                options=options,
            )
        else:
            response: ChatResponse = client.chat(
                model,
                messages=messages,
                tools=tools,
                options=options,
            )
    except Exception as e:
        rprint(f"[bold red]Erreur[/bold red]: [underline]Lors de l'appel au modèle[/underline]: {e}")
        return f"Erreur: {e}"
  
    output = None
    final_response = response
    
    if response.message.tool_calls:
        rprint(f"[italic yellow]Le modèle a demandé {len(response.message.tool_calls)} appel(s) d'outil[/italic yellow]")
        
        # There may be multiple tool calls in the response
        for tool in response.message.tool_calls:
            # Ensure the function is available, and then call it
            if function_to_call := available_functions.get(tool.function.name):
                rprint(f'[italic yellow]Appel de la fonction:[/italic yellow] {tool.function.name}')
                rprint(f'[italic yellow]Arguments:[/italic yellow] {tool.function.arguments}')
                
                try:
                    output = function_to_call(**tool.function.arguments)
                    rprint(f'[italic yellow]Résultat de la fonction:[/italic yellow] {output}')
                except Exception as e:
                    error_msg = f"Erreur lors de l'appel de la fonction {tool.function.name}: {e}"
                    rprint(f"[bold red]Erreur[/bold red]: [underline]{error_msg}[/underline]")
                    output = error_msg
            else:
                error_msg = f"Fonction {tool.function.name} non trouvée"
                rprint(f"[bold red]Erreur[/bold red]: [underline]{error_msg}[/underline]")
                output = error_msg

        # Add the function response to messages for the model to use
        messages.append(response.message)
        
        if output is not None:
            messages.append({'role': 'tool', 'content': str(output), 'name': tool.function.name})

            # Get final response from model with function outputs
            try:
                if client is None:
                    final_response = chat(model, messages=messages, options=options)
                else:
                    final_response = client.chat(model, messages=messages, options=options)
                # rprint('[italic yellow]Réponse finale:[/italic yellow]', final_response.message.content)
            except Exception as e:
                rprint(f"[bold red]Erreur[/bold red]: [underline]Lors de la génération de la réponse finale[/underline]: {e}")
                return f"Erreur lors de la génération de la réponse finale: {e}"
        else:
            rprint('[italic yellow]Aucun résultat d\'outil à traiter[/italic yellow]')
    else:
        rprint('[italic yellow]Aucun appel d\'outil retourné par le modèle[/italic yellow]')
        

    return final_response.message.content


def ask_agent(
    prompt: Optional[str] = None,
    model: Optional[str] = "qwen2.5:0.5b",
    ollama_base_url: Optional[str] = "http://localhost:11434"
) -> str:
    """
    Ask the agent
    
    Args:
        prompt (str): Le prompt à envoyer au modèle
        chron_description (str): La description de la tâche cron
        execute (str): La commande à exécuter
        model (str): Le nom du modèle à utiliser
        ollama_base_url (str): L'URL de base de l'API Ollama
        
    Returns:
        str: La réponse du modèle
    """
    
    client = ollama_client(ollama_base_url)
    
    host_1 = "192.168.1.47"
    port_1 = 8888
    BCM_PIN_1 = 4
    
    # Message système avec instructions détaillées
    system_message = f"""
    Tu es un assistant qui peut répondre à des questions et exécuter des tâches.
    Tu peux utiliser les outils suivants :
    - get_current_date
    - get_current_time
    - is_website_accessible
    - get_temperature_and_humidity
    
    Dans la chambre le capteur DHT11 est connecté à la broche BCM {BCM_PIN_1} d'un Raspberry Pi avec un service remotegpio sur le port {port_1}, il est accessible sur le reseau local via l'adresse IP {host_1}."
    """

    # Construire le message utilisateur en fonction des paramètres
    user_message = f"{prompt}"

    messages_list = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': user_message}
    ]
    tools_list = [
        get_current_date_tool,
        get_current_time_tool,
        is_website_accessible_tool,
        get_temperature_and_humidity_tool
    ]
    prompt_ = None

    available_functions = {
        'get_current_date': get_current_date,
        'get_current_time': get_current_time,
        'is_website_accessible': is_website_accessible,
        'get_temperature_and_humidity': get_temperature_and_humidity
    }

    # Configuration des options pour Ollama
    mes_options = Options(
        use_mlock=True,  # Utiliser mlock pour garder le modèle en mémoire
        use_mmap=True,   # Utiliser mmap pour charger le modèle
        num_gpu=200,     # Nombre de GPUs à utiliser
        temperature=0.3, # Température pour la génération
        num_thread=1,
        num_predict=300, # Nombre de réponses à générer
        keep_alive="20m",  # Garder le modèle en mémoire pendant 20 minutes (1200 secondes)
    )

    response = generate_response(
        model=model,
        messages=messages_list,
        tools=tools_list,
        available_functions=available_functions,
        options=mes_options,
        prompt=prompt_,
        client=client
    )

    return response