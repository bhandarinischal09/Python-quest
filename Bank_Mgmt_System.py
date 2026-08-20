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
    
    def deposite(self):
        accn = input("Enter Your Acc Number :")
        pin = int(input("Enter your Pin :"))
        userdata = [i for i in Bank.data if i['AccNo']==accn and i['Pin'] == pin]
        if not userdata:
             print("Incorrect Credentials!")
        else:
            amount = int(input("Enter the amount you want to deposit \n"))
            if (amount > 20000 or amount < 0):
                print("You can't deposite above 20k and less than 0 !")
            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print('Amount Deposited Successfully !')
    
    def withdraw(self):
        accnum = input("Enter your account number :")
        pin = int(input("Enter your 4 digit PIN : "))
        userdata = [i for i in Bank.data if i['AccNo'] == accnum and i["Pin"] == pin]
        if not userdata:
            print("Incorrect Credentials!")
        else:
            amount = int(input("Enter Amount you wanna withdraw :"))
            if (amount >  userdata[0]['Balance']):
                print("You can't withdraw amount which you dont have !!!")
            else:
                userdata[0]['Balance'] -= amount
                print("Amount Withdrawn Successfully !!!")
                Bank.__update()

    def getdet(self):
        accn = input("Enter Your Acc Number :")
        pin = int(input("Enter your Pin :"))
        userdata = [i for i in Bank.data  if i['AccNo']==accn and i['Pin'] == pin]
        if not userdata:
             print("Incorrect Credentials!")
        else:
            print('Showing Your Details !! \n')
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedet(self):
        accn = input("Enter Your Acc Number :")
        pin = int(input("Enter your Pin :"))
        userdata = [i for i in Bank.data  if i['AccNo']==accn and i['Pin'] == pin]
        if not userdata:
             print("Incorrect Credentials!")
        else:
             new_pin = int(input("Enter Your New 4 digit PIN"))
        if len(str(new_pin))!=4:
            print("Sorry, COULDN'T UPDATE YOUR ACCOUNT !")
        else:
            userdata[0]['Name'] = input("Enter your name !")
            userdata[0]['ContactNo'] = int(input("Enter your Number !"))
            userdata[0]['Email'] = input("Enter your Email !")
            userdata[0]['Address'] = input("Enter your Address !")
            userdata[0]['Pin'] = new_pin
            print("Account Updated Successfully")
            Bank.__update()

    def deleteacc(self):
        accn = input("Enter Your Acc Number :")
        pin = int(input("Enter your Pin :"))
        userdata = [i for i in Bank.data  if i['AccNo']==accn and i['Pin'] == pin]
        if not userdata:
             print("Incorrect Credentials!")
        else:
            check = input("Press Y if you want to delete the account ")
            if check == 'y' or check == 'Y':
                Bank.data.remove(userdata[0])
                Bank.__update()
                print("Account Deleted Successfully !!!")
