#coding=utf-8
__author__ = 'Junior'

from appium import webdriver
# import unittest
#
# class reproduceblackscreen(unittest.TestSuite):
#     def setUp(self):
desired_caps = {}#这里其实也可以把下面的参数,放到caps里面,通过字典的结构模式
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'

desired_caps['deviceName'] = '0e1669d4e315e2b5'
desired_caps['appPackage'] = 'com.shishike.calm'
desired_caps['appActivity'] = '.calmlauncher.CalmHomeActivity_'

    # def test(self):

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)#默认写法

i=1

#下面就开始找元素找点了
driver.implicitly_wait(20)

driver.find_element_by_id('com.shishike.calm:id/negative_button').click()
driver.implicitly_wait(3)
driver.find_element_by_name('admin').click()
driver.implicitly_wait(1)
for i in range(1,7):
    driver.find_element_by_id('com.shishike.calm:id/eight').click()
    i=i+1

driver.implicitly_wait(3)


# driver.find_element_by_xpath("//android.widget.GridView[1]/android.widget.LinearLayout[contains(@index,1)]").click()
driver.find_element_by_xpath("//android.widget.GridView[1]/android.widget.LinearLayout[0]").click()

driver.implicitly_wait(3)

#
# for i in range(50):
driver.find_element_by_name('餐盒关联').click()

driver.find_element_by_id('com.shishike.calm:id/btn_order_dish_right_cash').click()
driver.implicitly_wait(3)

driver.find_element_by_name('扫码').click()
driver.implicitly_wait(3)

driver.find_element_by_name('二维码').click()
driver.implicitly_wait(10)

driver.find_element_by_id('com.shishike.calm:id/pay_back').click()
driver.implicitly_wait(3)

driver.find_element_by_id('com.shishike.calm:id/cashier_title_bar_menu_btn').click()
driver.implicitly_wait(3)

driver.find_element_by_id('com.shishike.calm:id/ordercenter').click()
driver.implicitly_wait(3)

driver.find_element_by_id('com.shishike.calm:id/un_payment').click()
driver.implicitly_wait(3)

driver.find_element_by_id('com.shishike.calm:id/unpay_order_detail_un_use').click()
driver.implicitly_wait(3)

driver.find_element_by_id('com.shishike.calm:id/btn_ok')
driver.implicitly_wait(5)

driver.find_element_by_id('com.shishike.calm:id/cashier_title_bar_menu_btn').click()
driver.implicitly_wait(3)

driver.find_element_by_id('com.shishike.calm:id/orderdishes').click()
driver.implicitly_wait(5)



    # def tearDown(self):
driver.quit()
#
# if __name__=='__main__':
#     unittest.main()