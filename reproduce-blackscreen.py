#coding=utf-8
__author__ = 'Junior'

from appium import webdriver


def time(self):
    driver.implicitly_wait(self)



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
time(20)

driver.find_element_by_id('com.shishike.calm:id/negative_button').click()
time(1)
driver.find_element_by_name('admin').click()
time(1)
for i in range(1,7):
    driver.find_element_by_id('com.shishike.calm:id/eight').click()
    i=i+1

time(1)


driver.find_element_by_xpath("//android.widget.GridView[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]").click()

time(1)

#
# for i in range(50):
driver.find_element_by_xpath("//android.view.View[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.FrameLayout[9]").click()
time(1)

driver.find_element_by_id('com.shishike.calm:id/btn_order_dish_right_cash').click()
time(1)

driver.find_element_by_name('扫码').click()
time(1)
driver.find_element_by_name('二维码').click()
time(10)

driver.find_element_by_id('com.shishike.calm:id/pay_back').click()
time(3)

driver.find_element_by_id('com.shishike.calm:id/cashier_title_bar_menu_btn').click()
time(3)

driver.find_element_by_id('com.shishike.calm:id/ordercenter').click()
time(3)

driver.find_element_by_id('com.shishike.calm:id/un_payment').click()
time(3)

driver.find_element_by_id('com.shishike.calm:id/unpay_order_detail_un_use').click()
time(3)

driver.find_element_by_xpath("////android.widget.Button[1]").click()
time(3)

driver.find_element_by_id('com.shishike.calm:id/cashier_title_bar_menu_btn').click()
time(3)

driver.find_element_by_id('com.shishike.calm:id/orderdishes').click()
time(3)



    # def tearDown(self):
driver.quit()
#
# if __name__=='__main__':
#     unittest.main()