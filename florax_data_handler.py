# Modules/florax_data_handler.py
import json

FLORAX_JSON = "Data/Indian_plants_English.json"

def get_description_by_name(plant_name_query):
    plant_name_query = plant_name_query.lower()

    with open(FLORAX_JSON, "r", encoding="utf-8") as file:
        plants = json.load(file)

    for plant in plants:
        name = plant.get("name", "").lower()
        if plant_name_query in name:
            return json.dumps(plant, indent=2)

    return "❌ No matching plant found for the given name."
