#!/usr/bin/env python3.8
from enum import auto

from passlock import User,Credentials

def create_new_user(username,password):
    """
    function to create with last first  and password
    """
    new_user = User(username,password)
    return new_user
def save_user(user):
    """
    save a new user
    """
    user.save_user()
def delete_user(user):
    """
    function to delet user
    """
    user.delete_user()    
def display_user():
    """
    function to display existing user 
    """
    return User.display_user() 
def login_user(username,password):
    """
    function to check if a user exists
    """
    check_credentials  = Credentials.verify_user(username,password)
    return check_credentials
def create_new_credentials(account,username,password):
    """
    function that creates a new credentials to user account
    """
    new_credentials = Credentials(account,username,password)     
    return new_credentials

def save_credentials(credentials):
       """
       function that saves credentials to credentials list
       """ 
       credentials.save_credentials()
def display_accounts_credentials():
    """
    function that returns saved credentials
    """
    return Credentials.display_credentials()
def delete_credentials(credentials):
    """
    function to delete credentials from credentials list
    """
    credentials.delete_credentials()
def find_credentials(account):
    """
    function to find credentials by account
    """
    return Credentials.find_credentials(account)               
def check_credentials(account):
    """
    function that check if credentials  exists
    """
    return Credentials.credentials_exist(account)
def generate_password():
    """
    generate a random password for the user
    """
    auto_password = Credentials.generate_password()
    return auto_password
def copy_password(account):
    """
    function to copy password by the use of pyperclip
    """
    return Credentials.copy_password(account)

def main():
        print("Hello Welcome to your Passlock App. What is your name?")
        nickname = input()
        print(f"Hello {nickname}. what would you like to do?")

        print("Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
       
        print('\n')
        short_code=input("").lower()
        if short_code == "ca":
            print("SIGN UP")
            print('*' * 50)
            username = input("Username: ")
            while True:
                print("TP - to input own password: \n GP - generate  a random password")      
                password_choice = input().lower() 
                if password_choice  == "tp":
                    password =  input("Password Enter\n")
                    break
                elif generate_password == "gp":
                    password = generate_password()
                else:
                    print("Invalid try again\n")  
            save_user(create_new_user(username,password))
            print("*"*85)
            print(f"Hello {username},succesfully created an account! Your password is: {password}")
                
        elif short_code == "li": 
            print("*" *40)
            print("Enter your User name and your Password to log in:")
            username = input("User_name: ")
            password = input("password: ")
            login = login_user(username,password)
            if login_user == login:
                print("Hello {username} this is Your passlock app ")
                print("\n")
        while True:
            print(" user this short codes :\n CC - Create  a new credentials \n DC - Display credentials \n FC- Find credentials \n GP - Generate  random  password \n D- Delete credentials \n EX - Exit app")            
            short_code = input().lower()
            if short_code == "cc":
                print("*" *20)
                print("New cridentials")
                print("*" *40)
                print("Name of your Account")
                print("Your Username")
                username = input()
                account = input()
                while True:
                    print("TP - to input own password: \n GP - generate  a random password") 
                    password_choice = input().lower() 
                    if password_choice  == "tp":
                        password =  input("Password Enter\n")
                        break
                    elif generate_password == "gp":
                        password = generate_password()
                    else:
                        print("*"  *50)
                        print("Invalid try again\n")
                save_credentials(create_new_credentials(account,username,password))
                print('\n')
                print(f"Account Credential for: {account} - UserName: {username} - Password:{password} created succesfully")
                print('\n')        
            elif short_code == "dc":
                print("*" *50)  
                if display_accounts_credentials():
                    print("Your account Information: ")

                print(" \n")
                for account in display_accounts_credentials():
                    print(f"Account is! {account.account} \n Username!{username} \n Password is! {password}")
                    print("*" *100)
                else :
                    print("You seem you dont have any credentials.................................. ")       

            elif short_code ==  "fc":
                print("*" *50)
                print("Enter your account  name")
                account = input().lower
                if find_credentials(account):
                    check_credentials = find_credentials(account)
                    print(f"Account {check_credentials.account}")
                    print(f"username {check_credentials.username}  Password {check_credentials.password}")
                else:
                    print("Seemes Credential does not exist")
                    print('\n') 
                    print("*" *50)
            elif short_code == "d":
                    print("Enter the account name  delete")
                    search_name = input().lower()
                    if find_credentials(search_name):
                        search_credential = find_credentials(search_name)

                        search_credential.delete_credentials()
                        print('\n')
                        print(f"Your credentials for : {search_credential.account} successfully deleted!!!")
                        print("*" *50)
                    else:
                        print("That Credential you want to delete does not exist in your store yet")
            elif short_code == 'gp':

                    password = generate_password()
                    print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
            elif short_code == 'ex':
                    print("Thanks See you next time!")
                    break
           
if __name__ == '__main__':
    main()                