import unittest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from drivers.driver import driver, chrome

sys.path.insert(1, 'page/')
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = driver()

    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        main_page.navigate()
        #Checks if the word "Python" is in title
        self.assertEqual(main_page.title(), "Welcome to Python.org")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertEqual(search_results_page.is_results_found(), True)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
