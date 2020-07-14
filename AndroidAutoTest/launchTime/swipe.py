#/usr/bin/python
#encoding:utf-8
#滑动

from appium import  webdriver

caps = {}

caps['platformName'] = 'Android'
caps['platformVersion'] = '6.0'
caps['deviceName'] = 'N79SIV5PVCSODAQC'
caps['appPackage'] = 'com.tmall.wireless'
caps['appActivity'] = 'com.tmall.wireless.splash.TMSplashActivity'
#隐藏键盘
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

driver.swipe()
if __name__ == '__main__':

    pass