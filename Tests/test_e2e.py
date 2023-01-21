import time

from Utilites.BaseClass import BassClass
from PageObject.HomePage import Homepage
from PageObject.JobApplicationPage import Jobapplication

class  TestOne(BassClass):

    def test_e2e(self):
        homepage = Homepage(self.driver)
        jobapplication = Jobapplication(self.driver)


        homepage.getSeatchbar().send_keys("Laptop")
        homepage.getSubmitButton().click()
        homepage.getLaptop().click()
        time.sleep(3)
        homepage.getAddCartbutton().click()
        time.sleep(3)
        homepage.getProcessButton().click()
        time.sleep(3)
        homepage.getMailBox().send_keys('akmamnirjhor47@gmail.com')
        homepage.getCoutinue().click()
        homepage.driver.back()
        homepage.driver.back()
        homepage.geCareer().click()

        jobapplication.getSeachButton().click()
        time.sleep(3)
        jobapplication.getSearchBar().send_keys("Business")
        jobapplication.getLocationBar().send_keys("Denmark")
        jobapplication.geatSearchSingButton().click()
        jobapplication.driver.back()
        jobapplication.driver.back()





       # jobapplication.getSearchBar().send_keys("Marketibg")
         #jobapplication.getLocationBar().send_keys("Denmark")

