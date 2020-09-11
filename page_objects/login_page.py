from selenium.webdriver.common.by import By


class LoginPage:

    search_bar = (By.ID, "twotabsearchtextbox")
    search_button = (By.XPATH, "//input[@value='Go']")

    def __init__(self, driver):
        self.driver = driver

    def get_search_bar(self):
        return self.driver.find_element(*LoginPage.search_bar)

    def get_search_button(self):
        return self.driver.find_element(*LoginPage.search_button)
