from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class BookTest(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="C:\\Users\\mrhuz\\PycharmProjects\\PythonProject1\\echoserver\\tests\\chromedriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.url = "http://127.0.0.1:8000/"

    def login(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1.5)

        login = driver.find_element(By.ID, "login-link")
        login.click()
        time.sleep(1.5)

        input_login = driver.find_element(By.ID, "id_username")
        input_password = driver.find_element(By.ID, "id_password")
        input_login.send_keys("test")
        input_password.send_keys("123456")
        time.sleep(1.5)

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    def test_01_page_launch(self):
        driver = self.driver
        driver.get(self.url)

        self.assertIn("Главная страница",driver.title)
        time.sleep(1.5)

    def test_02_login_and_order(self):
        self.login()
        self.assertNotIn("Войти", self.driver.page_source)
        time.sleep(1.5)

    def test_03_order(self):
        self.login()
        driver = self.driver

        add_to_cart = driver.find_element(By.XPATH, "//*[@id=\"books-list\"]/li[1]/a")
        add_to_cart.click()
        time.sleep(1.5)

        cart = driver.find_element(By.ID, "cart-link")
        cart.click()
        time.sleep(1.5)

        make_order = driver.find_element(By.XPATH, "/html/body/div/a[2]")
        make_order.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()