import re

def get_session_id(session_string : str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_string)

    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

def get_food_string(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])