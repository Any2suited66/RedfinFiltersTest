from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    FIND_HOME_SEARCH = (By.ID, 'search-box-input')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    MORE_FILTERS = (By.XPATH, '//*[@id="wideSidepaneFilterButtonContainer"]')
    CONDO_FILTER = (By.XPATH, '//*[contains(text(), "Condo")]')
    TOWNHOUSE_FILTERS = (By.XPATH, '//*[contains(text(), "Townhouse")]')
    APPLY_FILTERS = (By.XPATH, '//*[contains(text(), "Apply Filters")]')
    KEY_DETAILS = (By.XPATH, "//div[@class='keyDetailsList']")
    NEXT_BTN = (By.XPATH, "//*[@data-rf-test-id='react-data-paginate-next']")
    HOUSE_FILTER = (By.XPATH, '//*[@data-rf-test-name="uipt1"]')
