#coding: utf-8

from datetime import datetime

import time
from typing import List
from typing import Dict
from typing import Union
from typing import Tuple
from typing import Optional
from typing import Any


from sensors import dht
import pigpio

#################
### Fonctions ###
#################

def get_current_date() -> str:
  """
  Get the current date
  """
  return datetime.now().strftime("%Y-%m-%d")

def get_current_time() -> str:
  """
  Get the current time
  """
  return datetime.now().strftime("%H:%M:%S")


def get_temperature_and_humidity(
  host: Optional[str] = "127.0.0.1",
  port: Optional[Union[str, int]] = "8888",
  gpio_pin: Optional[Union[str, int]] = "4"
) -> str:
  pi = pigpio.pi(host=host, port=port)
  sensor = dht.DHT11(pi, gpio_pin)
  for d in sensor:
    try:
      temperature, humidity = d['temperature'], d['humidity']
      return f"Temperature: {temperature}°C, Humidité: {humidity}%"
    except Exception as e:
      print(f"Erreur lors de la lecture du capteur DHT11: {e}, nouvelle tentative")
      time.sleep(1)
      continue
    finally:
      sensor.close()

  
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
      
