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
  host: str,
  port: Optional[int] = 8888,
  BCM_PIN: Optional[int] = 4
) :
  pi = pigpio.pi(host=host, port=port)
  sensor = dht.DHT11(pi, BCM_PIN)
  for d in sensor:
    print("temperature: {}".format(d['temperature']))
    print("humidity: {}".format(d['humidity']))
    time.sleep(1)
  sensor.close()
  return {
    "temperature": d['temperature'],
    "humidity": d['humidity']
  }

  
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
      
