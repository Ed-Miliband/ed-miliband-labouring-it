from Saves import SaveData
import json

print("bornana")

#Utility functions for JSON
def load_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)
      
def save_json(filepath, data):
    with open(filepath, "a") as f:
        json.dump(data, f, indent=4)


def LoadGame():
    saveNum = input("Input save number")
    loadjson(saveNum)
