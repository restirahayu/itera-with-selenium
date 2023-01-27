import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from random_username.generate import generate_username
from data import isidata

 
class TestLogin(unittest.TestCase):
    def setUp(self):
        chromeOpts = ChromeOptions()
        chromeOpts.add_experimental_option('detacth', True)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_Verify_SignUp_Successfully(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys(generate_username(1)) #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Same_email(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys(generate_username(1)) #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Same_username(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys("restirahayu") #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Blank_email(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys() #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys(generate_username(1)) #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Blank_Firstname(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys() # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys(generate_username(1)) #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Blank_Surname(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys() #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys(generate_username(1)) #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Blank_Mobile(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys(generate_username(1)) #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Blank_Username(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys() #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Blank_Password(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys(generate_username(1)) #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys() #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(isidata.confirmpassword) #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Blank_Passwordconfirm(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys(isidata.Firstname) # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys(isidata.Surname) #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys(isidata.Epost) #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys(isidata.Mobile) #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys(generate_username(1)) #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(isidata.Password) #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys() #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)

    def test_Verify_SignUp_Failed_Blank_All(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click() # buka situs sign up
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"FirstName").send_keys() # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Surname").send_keys() #isi surname
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "E_post").send_keys() #isi email
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Mobile").send_keys() #isi mobile
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys() #isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys() #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "ConfirmPassword").send_keys() #isi Confirm password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep (5)
unittest.main()