from pyclbr import Class


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
    def __init__(self,account,first_name,last_name,password):
       
        self.account = account
        self.first_name = first_name
        self.last_name = last_name
        self.password = password