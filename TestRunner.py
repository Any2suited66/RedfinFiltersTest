from selenium import webdriver
import unittest
from time import sleep
import page
import re
from locators import SearchResultsPageLocators

class TestRunner(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/tyler/PycharmProjects/RedFin/chromedriver')
        self.driver.get('https://www.redfin.com')

    def tearDown(self):
        self.driver.quit()

    def test_Chrome(self):
        home_page = page.Homepage(self.driver)
        home_page.click_find_a_home_search_field()
        home_page.set_search_text('Ivine, CA, USA')
        search_results_page = page.SearchResultsPage(self.driver)
        page.explicit_wait_by_xpath(self, '//*[@id="wideSidepaneFilterButtonContainer"]')
        search_results_page.click_more_filters_btn()
        page.explicit_wait_by_xpath(self, '//*[contains(text(), "Condo")]')
        search_results_page.click_condo_filter()
        page.explicit_wait_by_xpath(self, '//*[contains(text(), "Apply Filters")]')
        search_results_page.click_apply_filters_btn()
        sleep(1)
        while True:
            resultSet = self.driver.find_element_by_class_name('HomeViews')
            ids = resultSet.find_elements_by_xpath('//*[contains(@id, "MapHomeCard")]')
            sleep(2)
            for id in ids:
                main_window = self.driver.current_window_handle
                page.explicit_wait_by_xpath(self, '//*[contains(@id, "MapHomeCard")]')
                sleep(1)
                self.driver.find_element_by_id(id.get_attribute('id')).click()
                try:
                    windows = self.driver.window_handles
                    self.driver.switch_to.window(windows[1])
                    page.explicit_wait_by_xpath(self, "//div[@class='keyDetailsList']")
                    details = self.driver.find_element(*SearchResultsPageLocators.KEY_DETAILS)
                    text = details.get_attribute('innerHTML')
                    condominium = re.search('Condominium', text)
                    condo = re.search('Condo', text)
                    all_others = re.search('All Other Attached', text)
                    self.assertNotEqual(condominium or all_others or condo, None)
                    sleep(1)
                    if len(windows) > 1:
                        self.driver.switch_to.window(windows[1])
                        self.driver.close()
                    self.driver.switch_to.window(main_window)

                except:
                    print('test failed, check manually')
                    self.driver.get_screenshot_as_file('/Users/tyler/PycharmProjects/RedFin/failed_test.png')
                    exit(1)
            try:
                search_results_page.next_btn()
                search_results_page.click_next_btn()

            except:
                exit(1)


if __name__ == '__main__':
    unittest.main()