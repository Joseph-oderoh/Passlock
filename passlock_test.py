import pyperclip
import unittest
from passlock import User #!this isa an import of a class
from passlock import Credentials #!

class TestUser(unittest.TestCase):

    #!  test on, is if our objects are being instantiated correctly.


    def setUp(self):
        """
        Setup to run before  test case
        """
        self.new_user = User("Joseph Oderoh","5jko2k1")
    def test_init(self):
        """
        test init to test if the object was initialized properly
        """    
        self.assertEqual(self.new_user.username,"Joseph Oderoh")
        self.assertEqual(self.new_user.password,"5jko2k1")

        #! test to let us save our user data
    def test_save_user(self):
        """
         test if the users objects  are saved in the user list
        """
        self.new_user.save_user() #!saving a new user
        self.assertEqual(len(User.user_list),1)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []    
    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save mutiple users
        """    
        self.new_user.save_user()
        test_user =User("Test","user", "5jko2k1")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","5jko2k1") #!new user
            test_user.save_user()

            self.new_user.delete_user()#! Deleting a user object
            self.assertEqual(len(User.user_list),1) 
          
class TestCredentials(unittest.TestCase):

    def setUp(self):
        """
        Setup to run before  test case
        """
        self.new_credentials = Credentials("Twitter","JK-~black","5jko2k1")
    def test_init(self):
        """
        test the creds are properly initialized
        """
        self.assertEqual(self.new_credentials.account,"Twitter")
        self.assertEqual(self.new_credentials.username,"JK-~black")
        self.assertEqual(self.new_credentials.password,"5jko2k1")
    def test_save_credentials(self):
        """
        test to save credential into the credential list
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_save_mutiple_credentials(self):
        """
        test create mutiple credentials
        """   
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","JK-~black","5jko2k1") #!new creds
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    def test_delete_credentials(self):
        """
        test_delete_credentials to test if we can remove it
        """    
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","JK-~black","5jko2k1")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()#!deleting object
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_find_credentialr(self):
        """
        test to check if we can find a credential entry by account  credential
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","JK-~black","5jko2k1") 
        test_credentials.save_credentials()

        the_credentials = Credentials.find_credentials("Twitter")

        self.assertEqual(the_credentials.account,test_credentials.account)
    def test_credentials_exists(self):
        """
        check test to see if credentials return true
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","JK-~black","5jko2k1")
        test_credentials.save_credentials()
        

        credentials_exists = Credentials.if_credentials_exist("Twitter")
        self.assertTrue(credentials_exists)
    def test_display_all_credentials(self):
        """
        test to display all the saved credentials
        """ 
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list) 
    def test_copy_account(self):
        """
        test tocofirm that we arr coping account frome esisting found credentials
        """
        self.new_credentials.save_credentials()
        Credentials.copy_account("Twitter")

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)       
if __name__ == '__main__':
    unittest.main()    



