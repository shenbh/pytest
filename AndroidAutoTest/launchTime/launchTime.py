#/usr/bin/python
#encoding:utf-8
import csv
import os

import time


#测试 app 启动和关闭时间

class App():
    def __init__(self):
        self.content = ""
        self.startTime = 0


    #启动 App
    def LaunchApp(self):
        cmd='adb shell am start -W -n com.android.browser/.BrowserActivity'
        self.content=os.popen(cmd) #返回内容

    #停止 App
    def StopApp(self):
        #冷启动停止命令
        #cmd='adb shell am force-stop com.android.browser'
        #热启动停止命令
        cmd='adb shell input keyevent 3'
        os.popen(cmd)

    #获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime

#控制类
class Controller():
    def __init__(self, count):
        self.app = App() #获取 app 实例
        self.counter = count #设置循环次数
        self.addData=[{'timestamp', 'elapsedtime'}]


    #单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(5) #等待 5 秒
        elpasedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        time.sleep(3) #等待 3 秒
        currenttime = self.getCurrentTime()
        self.addData.append((currenttime, elpasedtime))

    #多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter -1

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime('%Y-%m-%m %H:%M:%S')
        return currentTime

    #保存数据
    def SaveDataToCSV(self):
        csvfile = file('startTime.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.allData)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSV()