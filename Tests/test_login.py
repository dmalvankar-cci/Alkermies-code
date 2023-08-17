import time

import pytest
from selenium.webdriver import ActionChains, Keys

from Tests import readCreds
from pageObjects.login_page import loginPage
from pageObjects.resource_page import resourcePage


@pytest.fixture
def test_loginToAlkermies(driver):
    # Open Browser
    login_page = loginPage(driver)
    # Navigate to Site URL
    login_page.open()
    # Login to the page
    username = readCreds.read_data(2, 1)
    password = readCreds.read_data(2, 2)
    login_page.perform_login(username, password)

    login_page.click_aristasaCheckOne()

    login_page.click_goBtn()



def test_checkLinksInPdf(driver, test_loginToAlkermies):

    resource_page = resourcePage(driver)
    resource_page.send_textInSearch()
    resource_page.click_eye()
    time.sleep(10)
    # resource_page.click_next()
    # resource_page.enter_pageCount_inPageNoBox()
    resource_page.total_links()
    # resource_page.click_links()
    time.sleep(50)

