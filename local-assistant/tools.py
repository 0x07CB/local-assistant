#coding: utf-8

# Tools can still be manually defined and passed into chat
get_current_date_tool = {
    "name": "get_current_date",
    "description": "Get the current date",
    "parameters": {
        "type": "string",
        "description": "The current date"
    }
}

get_current_time_tool = {
    "name": "get_current_time",
    "description": "Get the current time",
    "parameters": {
        "type": "string",
        "description": "The current time"
    }
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
