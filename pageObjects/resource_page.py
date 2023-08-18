import time

from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v113.tracing import end
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class resourcePage:


    __treatment = (By.XPATH, "//a[normalize-space()='Treatment']")
    __all_links = (By.XPATH, "//section[@class='linkAnnotation']/a")
    __next_page = (By.XPATH, "//button[@id='next']")
    __pages = (By.XPATH, "//input[@id='pageNumber']")
    __pageNumberBox = (By.XPATH, "//input[@id='pageNumber']")
    __searchBar = (By.XPATH, "//input[@placeholder='Search']")
    __aristada = (By.XPATH, "//a[@id='id-ARISTADA']")
    __eye = (By.XPATH, "//i[@class='fa fa-eye']")
    __eye_view = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-basic-layout[1]/main[1]/dbc-resources[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/span[1]/i[1]")
    __branded = (By.XPATH, "//div[@id='mat-tab-label-6-1']//div[@class='mat-tab-label-content'][normalize-space()='BRANDED']")


    __pdf_id = (By.XPATH, "//small[@class='text-red-100 pl-3']")
    def __init__(self, driver: WebDriver):
        self._driver = driver


    @property
    def current_url(self):
        return self._driver.current_url


    def click_branded(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__branded))
        self._driver.find_element(*self.__branded).click()

    def click_treatment(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__treatment))
        self._driver.find_element(*self.__treatment).click()

    def enter_pageCount_inPageNoBox(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__pageNumberBox))
        Page_count = self._driver.find_element(*self.__pages).get_attribute("max")
        # page_count_int = int(Page_count)
        Add_Page_No = self._driver.find_element(*self.__pageNumberBox)
        Add_Page_No.send_keys(Keys.BACKSPACE)
        Add_Page_No.send_keys(Page_count)
        Add_Page_No.send_keys(Keys.ENTER)

    def click_next(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__next_page))
        Page_count = self._driver.find_element(*self.__pages).get_attribute("max")
        page_count_int = int(Page_count)
        for page_count_int in range(1, page_count_int):
            next_btnClick = self._driver.find_element(*self.__next_page)
            next_btnClick.click()



    def click_eye(self):
        wait = WebDriverWait(self._driver, 15)
        wait.until(ec.visibility_of_element_located(self.__eye))
        self._driver.find_element(*self.__eye).click()


    def send_textInSearch(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__searchBar))
        self._driver.find_element(*self.__searchBar).send_keys(self.get_pdf_id)
        self._driver.find_element(*self.__searchBar).send_keys(Keys.ENTER)

    def click_aristada(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__aristada))
        self._driver.find_element(*self.__aristada).click()

    def total_links(self):
        wait = WebDriverWait(self._driver, 15)
        wait.until(ec.presence_of_element_located(self.__next_page))
        Page_count = self._driver.find_element(*self.__pages).get_attribute("max")
        page_count_int = int(Page_count)
        for page_count_int in range(1, page_count_int):
            next_btnClick = self._driver.find_element(*self.__next_page)
            next_btnClick.click()
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.visibility_of_all_elements_located(self.__all_links))
        links = self._driver.find_elements(*self.__all_links)
        print("No of links found:", len(links))
        for link in links:
                print("The href:",link.get_attribute("href"))

    @property
    def get_pdf_id(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_all_elements_located(self.__pdf_id))
        pdfs = self._driver.find_elements(*self.__pdf_id)
        # print("type of:", pdfs)
        for pdf in pdfs:
            return pdf.text




    def click_links(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.visibility_of_all_elements_located(self.__all_links))
        links = self._driver.find_elements(*self.__all_links)
        for link in links:
            link.click()

        # for page_count_int in range(1, page_count_int):
        #     for link in links:
        #         link.click()
        #         next_btnClick = self._driver.find_element(*self.__next_page)
        #         next_btnClick.click()









