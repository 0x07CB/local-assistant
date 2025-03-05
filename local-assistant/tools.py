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
    'parameters': {
      'type': 'object',
      'required': [],
      'properties': {
      },
    },
  },
}

is_website_accessible_tool = {
  'type': 'function',
  'function': {
    'name': 'is_website_accessible',
    'description': 'Check if a website is accessible',
    'parameters': {
      'type': 'object',
      'required': ['url'],
      'properties': {
        'url': {'type': 'string', 'description': 'The URL of the website to check'}
      },
    },
  },
}


get_temperature_and_humidity_tool = {
  'type': 'function',
  'function': {
    'name': 'get_temperature_and_humidity',
    'description': 'Get the temperature and humidity',
    'parameters': {
      'type': 'object',
      'required': ['host', 'port', 'BCM_PIN'],
      'properties': {
        'host': {'type': 'string', 'description': 'The IP address of the Raspberry Pi'},
        'port': {'type': 'integer', 'description': 'The port of the Raspberry Pi'},
        'BCM_PIN': {'type': 'integer', 'description': 'The BCM pin of the DHT11 sensor'},
      },
    },
  },
}