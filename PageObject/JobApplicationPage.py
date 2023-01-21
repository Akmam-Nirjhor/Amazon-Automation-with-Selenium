from selenium.webdriver.common.by import By
class Jobapplication:
    def __init__(self,driver):
        self.driver = driver

    SearchButton = (By.CSS_SELECTOR,".btn.location-search.form-control")
    SearchBar = (By.ID,"search_typeahead")
    LocationButton = (By.ID,"location-typeahead")
    SearchSing = (By.CSS_SELECTOR,".button-icon")
    def getSeachButton(self):
        return self.driver.find_element(*Jobapplication.SearchButton)

    def getSearchBar(self):
        return self.driver.find_element(*Jobapplication.SearchBar)

    def getLocationBar(self):
        return self .driver.find_element(*Jobapplication.LocationButton)

    def geatSearchSingButton(self):
        return self.driver.find_element(*Jobapplication.SearchSing)

