from pyclbr import Class

from requests import delete


class User:
    """
    This class generates new instance  of user accounts
    """
    user_list = [] # Empty contact list
    def __init__(self,first_name,last_name,password):
        
        self.first_name = first_name
        self.last_name = last_name
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
    def find_credentials(cls,account):
        found_credentials = Credentials.find_credentials
        """
        
        """    