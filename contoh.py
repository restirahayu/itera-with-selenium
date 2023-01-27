import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

 
class TestLogin(unittest.TestCase):
    def setUp(self):
        chromeOpts = ChromeOptions()
        chromeOpts.add_experimental_option('detacth', True)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"user-name").send_keys("standard_user") # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce") #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep (5)

    def test_Logout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"user-name").send_keys("standard_user") # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce") #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep (5)
        driver.find_element(By.CLASS_NAME,"bm-burger-button").click()
        time.sleep (3)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(5)

    def test_Login_Negatif(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By. ID,"user-name").send_keys("halo") # isi username
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secretsauce") #isi password
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        response_message = driver.find_element(By.CLASS_NAME,"error-message-container").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')
        time.sleep (5)

        


unittest.main()