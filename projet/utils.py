from json import load as json_load

def CheckJson(json):
    """Check if the json is a string"""
    if isinstance(json, str):
        file = open(json, "r")
        json = json_load(file)
        file.close()
    return json