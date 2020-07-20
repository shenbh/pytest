@@ -0,0 +1,58 @@
# unitestdemo.py文件中
#/usr/bin/python
#encoding:utf-8

import unittest
from appium import webdriver
import time
from ddt import ddt, data, unpack

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 所运行的系统
        desired_caps['platformVersion'] = '6.0'  # 系统版本
        # desired_caps['deviceName'] = 'Android Emulator' #使用的手机类型或模拟器类型
        desired_caps['deviceName'] = 'R8V7N15723011090'  # 使用的手机类型或模拟器类型
        desired_caps['appPackage'] = 'app.laidianyi.baoyi'  # 你想运行的 Android 应用的包名
        desired_caps['appActivity'] = 'app.laidianyi.view.login.WelcomeActivity'  # 你想要等待启动的 Android Activity 名称
        desired_caps['noReset'] = True  # 是否跳过过度动画（新安装程序打开时的各种介绍，如本次包含什么新特性什么的）
        desired_caps['unicodeKeyboard'] = True  # 使用unicode键盘
        desired_caps['resetKeyboard'] = True  # 使用unicode键盘后要重置下

        host = 'http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(host, desired_caps)  # 指定到appium desktop所监听的端口


    @data(("18030045724", "123456", False),
          ("18030045724", "234567", True))
    @unpack
    def test_login(self, username, password, expectedresult):
        print("test_something")
        # self.assertEqual(True, False)
        # 以下为应用中的元素操作
        time.sleep(5)
        self.driver.find_element_by_id("app.laidianyi.baoyi:id/dialog_base_confirm_btn").click()
        self.driver.find_element_by_id("app.laidianyi.baoyi:id/dynamic_login_tv").click()
        self.driver.find_element_by_id("app.laidianyi.baoyi:id/phone_cet").click()
        self.driver.find_element_by_id("app.laidianyi.baoyi:id/phone_cet").send_keys(username)
        self.driver.find_element_by_id("app.laidianyi.baoyi:id/password_et").send_keys(password)
        self.driver.find_element_by_id("app.laidianyi.baoyi:id/login_btn").click()

        try:
            if self.driver.find_element_by_id("app.laidianyi.baoyi:id/login_btn").is_displayed():
                print("fial")
                exist = True
        except:
            print("pass")
            exist = False
        self.assertEqual(exist,expectedresult)


    def tearDown(self):
        print("tearDown")
        self.driver.quit()  # 退出

if __name__ == '__main__':
    unittest.main()
No newline at end of file
