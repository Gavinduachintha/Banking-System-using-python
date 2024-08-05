#Banking System
import json
import random
import os

accounts_file = 'accounts.json'
transaction_file = 'transactions.json'

print("Banking System V 1.1")
print("Welcome to Bank Of Silon")

#Function to load data from JSON file
def load_data(filename):
    if os.path.exists(filename):
        with open(filename,'r') as file:
            return json.load(file)
    else:
        return{}
    

#Function to save data to JSON file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent = 4)
        
        
#Function to log transactions
def log_transactions(acc_no, trans_type, amount):
    transactions = load_data(transaction_file)
    transaction ={"acc_no":acc_no,
                   "trans_type": trans_type,
                   "amount":amount,
                   "date":None #You can add a time stamp if needed
                   }
    if isinstance (transactions, list):
        transactions.append(transaction)
    else:
        transactions = [transaction]
    save_data(transaction_file,transactions)
    
    
    
def accountOpen():
    accounts = load_data(accounts_file)
    name = input("Enter your name: ")
    acc_no = random.randint(1000,9999)
    while str(acc_no) in accounts:
        acc_no = random.randint(1000,9999) 
    accounts[acc_no]= {"name":name, "balance":0}
    save_data(accounts_file, accounts)
    print("Account created succesfully !")
    print("Hello", name)
    print("Your account number is:", acc_no)
    
    

def depositMoney():
    accounts = load_data(accounts_file)
    acc_no = int(input("Enter your account number: "))
    if str(acc_no) in accounts:
       money = float(input("Enter deposit amount: "))
       if money > 0:
           accounts[str(acc_no)]["balance"]+=money
           save_data(accounts_file, accounts)
           log_transactions(acc_no, "deposit", money)
           print("Deposit Succesful !")
           print("Your current account balance is: ", accounts[str(acc_no)]["balance"])
       else:
           print("Invalid deposit amount..")
    else:
        print("Account not found")



def withdrawMoney():
    accounts = load_data(accounts_file)
    acc_no = int(input("Enter your account number: "))  
    if str(acc_no) in accounts:
        money = float(input("Enter the withdraw amount: "))
        if 0< money <= accounts[str(acc_no)]["balance"]:
            accounts[str(acc_no)]["balance"] -=money
            save_data(accounts_file, accounts)
            log_transactions(acc_no, "withdrawal", money)
            print("Withdrawal successful !")
            print("Remainig Balance: ", accounts[str(acc_no)]["balance"])
        else:
            print("Invalid or insufficent funds.")
    else:
        print("Account not found !")


def checkBalance():
    accounts = load_data(accounts_file)
    acc_no = int(input("Enter the account number: "))
    if str(acc_no) in accounts:
        print("Your current balace is ", accounts[str(acc_no)]["balance"])
    else:
        print("Account not found")
        
        
running = True
while running:
    print('1',"Account Openning")
    print('2',"Deposit Money")
    print('3',"withdraw Money")
    print('4',"Check Balnce")
    print('5',"Exit")

    user_input = int(input("Select your option "))
    

    if user_input == 1:
        accountOpen()
    elif user_input == 2:
        depositMoney()
    elif user_input == 3:
        withdrawMoney()
    elif user_input == 4:
        checkBalance()
    elif user_input == 5:
        running = False
    else:
        print("Invalid option, Pls selct a number between 1-5")

print("<<<<<<<<<<Thank you for banking with us>>>>>>>>>>>")
print("_________Have a nice day !_________")
print(load_data(accounts_file))