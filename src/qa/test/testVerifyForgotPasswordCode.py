import sys, unittest, FlipTixShell

'''
    FlipTix verify forgot password code end point.
    
    Purpose - 
    
    Notes - Only partial automation possible. 

    Method signature:
        def verify_forgot_password_code(self, email='', verificationCode='', userId='', 
                   emailExclude=False, verificationCodeExclude=False, userIdExclude=False):
    
    Required:
        userId
        email
        verificationCode

    Test cases
        UserId missing from request call.
        Null UserId value. 
        Int UserId value.    
        Float UserId value.   
        String UserId value.
        Array UserId value.  

        Email missing from request call.
        Null Email value. 
        Int Email value.    
        Float Email value.   
        String Email value.
        Array Email value.  

        VerificationCode missing from request call.
        Null VerificationCode value. 
        Int VerificationCode value.    
        Float VerificationCode value.   
        String VerificationCode value.
        Array VerificationCode value. 
'''
class TestVerifyUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = FlipTixShell.FlipTix()    

            cls.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                           password = FlipTixShell.data['testPassword'])  
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])




    # *********************************************************************
    # *                         UserId tests                              *
    # *********************************************************************
    
    
        
    # Missing UserId information from request call.
    def test_missingUserId(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = self.user.GetUserId(),
                                                             userIdExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a userId",
                         msg='test_missingUserId assert#1 has failed.')
        
        
        
    # Test a null UserId.
    def test_nullUserId(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = '')

        self.assertEqual(responseBody['error'], "Please submit a userId",
                          msg='test_nullUserId assert#1 has failed.')



    # Test a int UserId.
    def test_intUserId(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = 123456)

        self.assertEqual(responseBody['error'], "User could not be found",
                          msg='test_intUserId assert#1 has failed.')



    # Test a float UserId.
    def test_floatUserId(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = 123.456)

        self.assertEqual(responseBody['error'], "User could not be found",
                          msg='test_floatUserId assert#1 has failed.')
        
        
        
    # Test a string UserId value call.
    @unittest.skip('Cannot automate this due to the fact that the verificationCode will always be wrong.')
    def test_stringUserId(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = 'self.user.GetUserId()')

        self.assertEqual(responseBody[''], "",
                          msg='test_stringUserId assert#1 has failed.')



    # Test an array UserId value call.
    @unittest.skip('Cannot automate this due to the fact that the verificationCode will always be wrong.')
    def test_arrayUserId(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = [self.user.GetUserId()])

        self.assertEqual(responseBody[''], "",
                          msg='test_arrayUserId assert#1 has failed.')



    
    # *********************************************************************
    # *                         Email tests                               *
    # *********************************************************************
    
    
        
    # Missing Email information from request call.
    @unittest.skip('Cannot automate this due to the fact that the verificationCode will always be wrong.')
    def test_missingEmail(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody[''], "",
                         msg='test_missingEmail assert#1 has failed.')
        
        
        
    # Test a null Email.
    @unittest.skip('Cannot automate this due to the fact that the verificationCode will always be wrong.')
    def test_nullEmail(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'],  
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "Please submit an email",
                          msg='test_nullEmail assert#1 has failed.')



    # Test a int Email.
    @unittest.skip('Cannot automate this due to the fact that the verificationCode will always be wrong.')
    def test_intEmail(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'],  
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['message'], "Expected params.Email to be a string",
                          msg='test_intEmail assert#1 has failed.')



    # Test a float Email.
    @unittest.skip('Cannot automate this due to the fact that the verificationCode will always be wrong.')
    def test_floatEmail(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_floatEmail assert#1 has failed.')
        
        
        
    # Test a string Email value call.
    @unittest.skip('Cannot automate this due to the fact that the verificationCode will always be wrong.')
    def test_stringEmail(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_stringEmail assert#1 has failed.')



    # Test an array Email value call.
    @unittest.skip('Cannot automate this due to the fact that the verificationCode will always be wrong.')
    def test_arrayEmail(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_arrayEmail assert#1 has failed.')



    # *********************************************************************
    # *                          VerificationCode tests                   *
    # *********************************************************************
    
    
        
    # Missing VerificationCode information from request call.
    def test_missingVerificationCode(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = FlipTixShell.data['testVerificationCode'], 
                                                             userId = self.user.GetUserId(),
                                                             verificationCodeExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a verification code",
                         msg='test_missingVerificationCode assert#1 has failed.')
        
        
        
    # Test a null VerificationCode.
    def test_nullVerificationCode(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = '', 
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "Please submit a verification code",
                          msg='test_nullVerificationCode assert#1 has failed.')



    # Test a int VerificationCode.
    def test_intVerificationCode(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = 123456789,  
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "Your verification code has expired. Please submit request again.",
                          msg='test_intVerificationCode assert#1 has failed.')



    # Test a float VerificationCode.
    def test_floatVerificationCode(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = 123.456789, 
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "Your verification code has expired. Please submit request again.",
                          msg='test_floatVerificationCode assert#1 has failed.')
        
        
        
    # Test a string VerificationCode value call.
    def test_stringVerificationCode(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = "FlipTixShell.data['testVerificationCode']", 
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "Your verification code has expired. Please submit request again.",
                          msg='test_stringVerificationCode assert#1 has failed.')



    # Test an array VerificationCode value call.
    def test_arrayVerificationCode(self):
        responseBody = self.user.verify_forgot_password_code(email = FlipTixShell.data['testVerifiedEmail'], 
                                                             verificationCode = [FlipTixShell.data['testVerificationCode']],  
                                                             userId = self.user.GetUserId())

        self.assertEqual(responseBody['error'], "Your verification code has expired. Please submit request again.",
                          msg='test_arrayVerificationCode assert#1 has failed.')
    
    




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestVerifyUser('test_missingUserId'))
    suite.addTest(TestVerifyUser('test_nullUserId'))
    suite.addTest(TestVerifyUser('test_intUserId'))
    suite.addTest(TestVerifyUser('test_floatUserId'))
    suite.addTest(TestVerifyUser('test_stringUserId'))
    suite.addTest(TestVerifyUser('test_arrayUserId'))

    suite.addTest(TestVerifyUser('test_missingEmail'))
    suite.addTest(TestVerifyUser('test_nullEmail'))
    suite.addTest(TestVerifyUser('test_intEmail'))
    suite.addTest(TestVerifyUser('test_floatEmail'))
    suite.addTest(TestVerifyUser('test_stringEmail'))
    suite.addTest(TestVerifyUser('test_arrayEmail'))

    suite.addTest(TestVerifyUser('test_missingVerificationCode'))
    suite.addTest(TestVerifyUser('test_nullVerificationCode'))
    suite.addTest(TestVerifyUser('test_intVerificationCode'))
    suite.addTest(TestVerifyUser('test_floatVerificationCode'))
    suite.addTest(TestVerifyUser('test_stringVerificationCode'))
    suite.addTest(TestVerifyUser('test_arrayVerificationCode'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())