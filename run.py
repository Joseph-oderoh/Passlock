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