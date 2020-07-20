#/usr/bin/python
#encoding:utf-8
#滑动

# from appium import  webdriver
#
# caps = {}
#
# caps['platformName'] = 'Android'
# caps['platformVersion'] = '6.0'
# caps['deviceName'] = 'N79SIV5PVCSODAQC'
# caps['appPackage'] = 'com.tmall.wireless'
# caps['appActivity'] = 'com.tmall.wireless.splash.TMSplashActivity'
# #隐藏键盘
# caps['unicodeKeyboard'] = True
# caps['resetKeyboard'] = True
# driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
#
# driver.swipe()
# if __name__ == '__main__':
#
#     pass


# 测试自带的计算机
# from appium import webdriver
# desired_caps = {}
# desired_caps['platformName'] = 'Android' #所运行的系统 ios
# desired_caps['platformVersion'] = '6.0' #系统版本
# # desired_caps['deviceName'] = 'Android Emulator' #使用的手机类型或模拟器类型
# desired_caps['deviceName'] = 'R8V7N15723011090' #使用的手机类型或模拟器类型
# desired_caps['appPackage'] = 'com.android.calculator2' #你想运行的 Android 应用的包名
# desired_caps['appActivity'] = '.Calculator' #你想要等待启动的 Android Activity 名称
# desired_caps['noReset'] = True #是否跳过过度动画（新安装程序打开时的各种介绍，如本次包含什么新特性什么的）
# desired_caps['automationName'] = 'uiautomator2'
#
# host = 'http://localhost:4723/wd/hub'
# driver = webdriver.Remote(host, desired_caps) #指定到appium desktop所监听的端口
#
# #以下为应用中的元素操作
# driver.find_element_by_id("com.android.calculator2:id/digit1").click()
# driver.find_element_by_id("com.android.calculator2:id/digit5").click()
# driver.find_element_by_id("com.android.calculator2:id/digit9").click()
# driver.find_element_by_id("com.android.calculator2:id/digit9").click()
# driver.find_element_by_id("com.android.calculator2:id/minus").click()
# driver.find_element_by_id("com.android.calculator2:id/plus").click()
# driver.find_element_by_id("com.android.calculator2:id/digit6").click()
# driver.find_element_by_id("com.android.calculator2:id/equal").click()
# driver.quit() #退出



# 测试保意顾客端登录功能
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android' #所运行的系统
desired_caps['platformVersion'] = '6.0' #系统版本
# desired_caps['deviceName'] = 'Android Emulator' #使用的手机类型或模拟器类型
desired_caps['deviceName'] = 'R8V7N15723011090' #使用的手机类型或模拟器类型
desired_caps['appPackage'] = 'app.laidianyi.baoyi' #你想运行的 Android 应用的包名
desired_caps['appActivity'] = 'app.laidianyi.view.login.WelcomeActivity' #你想要等待启动的 Android Activity 名称
desired_caps['noReset'] = True #是否跳过过度动画（新安装程序打开时的各种介绍，如本次包含什么新特性什么的）
desired_caps['unicodeKeyboard'] = True # 使用unicode键盘
desired_caps['resetKeyboard'] = True # 使用unicode键盘后要重置下

host = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(host, desired_caps) #指定到appium desktop所监听的端口

# 以下为应用中的元素操作
time.sleep(5)
driver.find_element_by_id("app.laidianyi.baoyi:id/dialog_base_confirm_btn").click()
driver.find_element_by_id("app.laidianyi.baoyi:id/dynamic_login_tv").click()
driver.find_element_by_id("app.laidianyi.baoyi:id/phone_cet").send_keys("18030045724")
driver.find_element_by_id("app.laidianyi.baoyi:id/password_et").send_keys("123456")
driver.find_element_by_id("app.laidianyi.baoyi:id/login_btn").click()

try:
    if driver.find_element_by_id("app.laidianyi.baoyi:id/login_btn").is_displayed():
        print("fial")
except:
    print("pass")

driver.quit() #退出