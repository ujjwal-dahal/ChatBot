import os
import json
from django.conf import settings


if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

def create_json(data, filename="intents.json"):
    try:
        
        json_path = os.path.join(settings.BASE_DIR, filename)
        
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"JSON file '{filename}' generated successfully at {json_path}.")
    except Exception as e:
        print(f"Failed to write JSON file: {e}")
