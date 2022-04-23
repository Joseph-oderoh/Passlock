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
        self.assertAlmostEqual(self.new_user.first_name,"Joseph")
        self.assertAlmostEqual(self.new_user.last_name,"Oderoh")
        self.assertAlmostEqual(self.new_user.password,"5jko2k1")

        #! test to let us save our user deta
if __name__ == '__main__':
    unittest.main()    



