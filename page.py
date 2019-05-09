from selenium.webdriver.common.keys import Keys
from locators import HomePageLocators, SearchResultsPageLocators
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def explicit_wait_by_xpath(self, el):
    WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, el)))

def explicit_wait_by_xpath1(self, *el):
    WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, el)))

def explicit_wait_by_id(self, el):
    WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.ID, el)))


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class Homepage(BasePage):


    def click_find_a_home_search_field(self):
        search = self.driver.find_element(*HomePageLocators.FIND_HOME_SEARCH)
        search.click()

    def submit(self):
        self.driver.send_keys(Keys.ENTER)

    def set_search_text(self, search_input):
        search_field = 'search-box-input'
        search = self.driver.find_element_by_id(search_field)
        search.send_keys(search_input)
        sleep(1)
        search.send_keys(Keys.ENTER)


class SearchResultsPage(BasePage):

    def click_more_filters_btn(self):
        more_filters = self.driver.find_element(*SearchResultsPageLocators.MORE_FILTERS)
        sleep(1)
        more_filters.click()

    def click_condo_filter(self):
        condo_filter = self.driver.find_element(*SearchResultsPageLocators.CONDO_FILTER)
        sleep(1)
        condo_filter.click()

    def click_apply_filters_btn(self):
        apply_filters = self.driver.find_element(*SearchResultsPageLocators.APPLY_FILTERS)
        sleep(1)
        apply_filters.click()

    def click_townhouse_filter(self):
        townhouse_filter = self.driver.find_element(*SearchResultsPageLocators.TOWNHOUSE_FILTERS)
        sleep(1)
        townhouse_filter.click()

    def click_next_btn(self):
        next_btn = self.driver.find_element(*SearchResultsPageLocators.NEXT_BTN)
        sleep(1)
        next_btn.click()
        sleep(2)

    def next_btn(self):
        print(self.driver.find_elements(*SearchResultsPageLocators.NEXT_BTN))









