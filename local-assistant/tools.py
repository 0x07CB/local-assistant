#coding: utf-8

# Tools can still be manually defined and passed into chat
get_current_date_tool = {
  'type': 'function',
  'function': {
    'name': 'get_current_date',
    'description': 'Get the current date',
    'parameters': {
      'type': 'object',
      'required': [],
      'properties': {
      },
    },
  },
}

get_current_time_tool = {
  'type': 'function',
  'function': {
    'name': 'get_current_time',
    'description': 'Get the current time',
  },
}

is_website_accessible_tool = {
    "name": "is_website_accessible",
    "description": "Vérifie si un site web est accessible",
    "parameters": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "L'URL du site web à vérifier"
            }
        },
        "required": ["url"]
    }
}


get_temperature_and_humidity_tool = {
  "name": "get_temperature_and_humidity",
  "description": "Récupère la température et l'humidité",
  "parameters": {
    "type": "object",
    "properties": {
      "host": {"type": "string", "description": "L'adresse IP du Raspberry Pi"},
      "port": {"type": "integer", "description": "Le port du Raspberry Pi"},
      "BCM_PIN": {"type": "integer", "description": "Le numéro de la broche BCM du capteur DHT11"}
    },
    "required": ["host", "port", "BCM_PIN"]
  }
}
