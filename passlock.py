import string
import pyperclip
import random
class User:

    """
    This class generates new instance  of user accounts
    """
    user_list = [] # Empty contact list
    def __init__(self,username,password):
        
        self.username = username
        self.password = password
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)    
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
class Credentials:
    credentials_list = []
    def __init__(self,account,username,password):
       
        self.account = account
        self.username = username
        self.password = password
    def save_credentials(self):
        """
        test to save credentials in the credentials list
        """   
        Credentials.credentials_list.append(self) 
    def delete_credentials(self):
        """
        delete credentials methode to test
        """    
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_credentials(cls, account):
        # find_credentials = Credentials.find_credentials
        """
        test method thsat takes account and returns credentials
        """  
        for credentials in cls.credentials_list:
            if  credentials.account == account:
                return credentials
    @classmethod
    def credentials_exist(cls,account):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            account: account to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                    return True

        return False
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        current_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    current_user = user.username
        return  current_user   
    @classmethod
    def display_credentials(cls):
        """
        method to diplay credentials
        """ 
        return cls.credentials_list
    @classmethod
    def copy_account(cls,account):
        credentials_found = Credentials.find_credentials (account)
        pyperclip.copy(credentials_found.account)                  
    def generate_password(stringLength=8):
        """
        generate pass words
        """  
        password = string.ascii_uppercase +  string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return "".join(random.choice(password)
        for i in range(stringLength))