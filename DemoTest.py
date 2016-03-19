#coding=utf-8
__author__ = 'Junior'

from appium import webdriver
# import unittest
#
# class reproduceblackscreen(unittest.TestSuite):
#     def setUp(self):
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'

desired_caps['deviceName'] = '0e1669d4e315e2b5'
desired_caps['appPackage'] = 'com.shishike.calm'
desired_caps['appActivity'] = '.calmlauncher.CalmHomeActivity_'

    # def test(self):

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()



    # def tearDown(self):
driver.quit()
#
# if __name__=='__main__':
#     unittest.main()