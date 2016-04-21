#coding=utf-8
from appium import webdriver

# desired_caps={
#     'platformName':'Android',
#     'platformVersion':"4.4.2",
#     'deviceName':'127.0.0.1:62001',
#     'appPackage':'com.shishike.calm',
#     'appActivity':'.calmlauncher.CalmHomeActivity_'
# }
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# print driver
# driver.implicitly_wait(10)
# driver.find_element_by_id('com.shishike.calm:id/negative_button').click()
# driver.quit()


desired_caps = {}  # 这里其实也可以把下面的参数,放到caps里面,通过字典的结构模式
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = "4.4.2"

desired_caps['deviceName'] = "127.0.0.1:62001"
desired_caps['appPackage'] = "com.shishike.calm"
desired_caps['appActivity'] = ".calmlauncher.CalmHomeActivity_"
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id('com.shishike.calm:id/negative_button').click()
# driver.quit()

