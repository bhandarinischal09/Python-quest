import json
import random
import string
from pathlib import Path

class Bank:

    database = "data.json"
    data = []

    try :
        if Path(database).exists(): 
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No Such File Exists!")
    except Exception as err:
        print(f"error occurred as {err}!")
