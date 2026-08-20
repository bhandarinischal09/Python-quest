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

    @classmethod
    def __accnum(cls):
        letters = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spc = random.choices("!@#$%^&*",k=2)
        accno = letters + num+ spc
        random.shuffle(accno)
        return "".join(accno)
    
    @classmethod
    def __update(cls):
        with open(Bank.database,"w") as fs:
            fs.write(json.dumps(Bank.data))

    def createaccount(self):
        info = {
            "Name": input("Enter your name :"),
            "Age": int(input("Enter your Age :")),
            "ContactNo":int(input("Enter your Phone Number :")),
            "Email": input("Enter Your Email :"),
            "Address": input("Enter Your Address :"),
            "Pin": int(input("Enter your 4 digit PIN :")),
            "AccNo": Bank.__accnum(),
            "Balance": 0
        }

        if info['Age'] < 18 or len(str(info['Pin']))!=4:
            print("Sorry, COULDN'T CREATE YOUR ACCOUNT !")
        else:
            print('Account Created Succesfully !')
            for i in info:
                print(f"{i} : {info[i]}")
            print('Please Note Down Your ACCOUNT NUMBER !!')
            Bank.data.append(info)
            Bank.__update()
    