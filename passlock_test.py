import unittest
import string
from passlock import User #!this isa an import of a class

class TestUser(unittest.TestCase):

    #!  test on, is if our objects are being instantiated correctly.


    def setUp(self):
        """
        Setup to run before  test case
        """
        self.new_user = User("Joseph","Oderoh","5jko2k1")
    def test_init(self):
        """
        test init to test if the object was initialized properly
        """    
        self.assertEqual(self.new_user.first_name,"Joseph")
        self.assertEqual(self.new_user.last_name,"Oderoh")
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
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_contact.save_contact()
            test_user = User("Test","user","5jko2k1") # new contact
            test_user.save_user()

            self.new_contact.delete_contact()# Deleting a contact object
            self.assertEqual(len(Contact.contact_list),1)    
if __name__ == '__main__':
    unittest.main()    


