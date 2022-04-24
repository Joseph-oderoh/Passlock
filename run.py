#!/usr/bin/env python3.8
from passlock import User,Credentials

def create_new_user(first_name,last_name,password):
    """
    function to create with last first  and password
    """
    new_user = User(first_name,last_name,password)
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
def login_user(first_name,last_name,password):
    """
    function to check if a user exists
    """
    check_user  = Credentials.verify_user(first_name,last_name,password)
    return check_user
def create_new_credentials(account,userName,password):
    """
    function that creates a new credentials to user account
    """
    new_credentials = Credentials(account,userName,password)     
    return new_credentials
def save_credentials(credentials):
       """
       function that saves credentials to credentials list
       """ 
       credentials.save_credentials()
def display_accounts_details():
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
    function that 
    """