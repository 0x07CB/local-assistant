#coding: utf-8

from datetime import datetime

from typing import List
from typing import Dict
from typing import Union
from typing import Tuple
from typing import Optional
from typing import Any

#################
### Fonctions ###
#################

# Fonction pour recuperer la date actuelle
def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

# Fonction pour recuperer l'heure actuelle
def get_current_time():
    return datetime.now().strftime("%H:%M:%S")
  
# Fonction pour verifier l'accessibilite d'un site web
def is_website_accessible(url: str) -> bool:
    try:
        import requests
    except ImportError:
        print("Le module requests n'est pas installé. Veuillez l'installer avec la commande 'pip install requests'.")
        return False
      
    try:
        response = requests.get(url)
        return response.status_code == 200
    except Exception as e:
        return False
      
