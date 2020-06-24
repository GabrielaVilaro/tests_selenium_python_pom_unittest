from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class PageCreateAccount:
    def __init__(self, driver):
        self.driver = driver
        self.title_of_create_authentication = (By.XPATH, '//*[@id="noSlide"]/h1')

    def return_title_of_create_authentication(self):
        title_of_page_create_account_authentication = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located
                                                                           (self.title_of_create_authentication))
        title = title_of_page_create_account_authentication.text

        return title
