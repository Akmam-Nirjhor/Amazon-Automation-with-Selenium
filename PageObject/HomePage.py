from selenium.webdriver.common.by import By
class Homepage:
    def __init__(self,driver):
        self.driver = driver


    Searchbar =(By.XPATH,"//input[@type='text']")
    SubmitButton = (By.ID,"nav-search-submit-button")
    Laptop = (By.XPATH,"//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img")
    AddcaetButton = (By.XPATH,"//input[@type='button']")
    ProcessTochechItemButton = (By.XPATH,"//input[@name='proceedToRetailCheckout']")
    MailBox = (By.ID,"ap_email")
    ContinueButton = (By.CSS_SELECTOR,".a-button-input")
    Career = (By.XPATH,"//*[@id='navFooter']/div[1]/div/div[1]/ul/li[1]/a")


    def getSeatchbar(self):
        return self.driver.find_element(*Homepage.Searchbar)

    def getSubmitButton(self):
        return self.driver.find_element(*Homepage.SubmitButton)

    def getLaptop(self):
        return self.driver.find_element(*Homepage.Laptop)

    def getAddCartbutton(self):
        return self.driver.find_element(*Homepage.AddcaetButton)

    def getProcessButton(self):
        return self.driver.find_element(*Homepage.ProcessTochechItemButton)

    def getMailBox(self):
        return self.driver.find_element(*Homepage.MailBox)

    def getCoutinue(self):
        return self.driver.find_element(*Homepage.ContinueButton)

    def geCareer(self):
        return self.driver.find_element(*Homepage.Career)





