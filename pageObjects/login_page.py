from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class loginPage:
    __url = "https://dbriefcase-stage.alkermes.info/resources"
    __username_textField = (By.ID, 'username')
    __password_textField = (By.ID, 'pwd')
    __login_button = (By.XPATH, "//span[normalize-space()='Sign In']")

    __checkbox = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/label[1]")
    __checkbox2 = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/label[1]/span[1]")
    __goBtn = (By.ID, "go-btn")


    __treatment = (By.XPATH, "(//div[@class='resources-icon'])[3]")
    __all_links = (By.TAG_NAME, "a")
    __aristadaCheckboxOne = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/label[1]/span[1]")
    __eye = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-basic-layout[1]/main[1]/dbc-resources[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/div[1]/div[1]/div[23]/div[1]/div[2]/div[1]/span[1]")
    __branded = (By.XPATH, "//div[@id='mat-tab-label-22-1']//div[@class='mat-tab-label-content'][normalize-space()='BRANDED']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def perform_login(self, username, password):
        pass_username = self._driver.find_element(*self.__username_textField)
        pass_password = self._driver.find_element(*self.__password_textField)
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__login_button))
        press_loginBtn = self._driver.find_element(*self.__login_button)

        pass_username.send_keys(username)
        pass_password.send_keys(password)
        press_loginBtn.click()

    def click_goBtn(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__goBtn))
        self._driver.find_element(*self.__goBtn).click()



    def click_checkbox(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__checkbox))
        self._driver.find_element(*self.__checkbox).click()

    def click_aristasaCheckOne(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__aristadaCheckboxOne))
        self._driver.find_element(*self.__aristadaCheckboxOne).click()


    def click_checkbox2(self):
        wait = WebDriverWait(self._driver, 15)
        wait.until(ec.presence_of_element_located(self.__checkbox2))
        self._driver.find_element(*self.__checkbox2).click()



