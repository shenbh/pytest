#/usr/bin/python
#encoding:utf-8
import os
import time
import csv


#电量测试

#控制类
class Controller(object):
    def __init__(self, count):
        #定义测试的次数
        self.counter = count
        #定义手机数据的数组
        self.adddata = [{'timestamp', 'battery'}]

    # 单次测试过程
    def testprocess(self):
        #执行获取电量的命令
        result = os.popen("adb shell dumpsys battery")
        #获取电量的 level
        for line in result:
            if "level" in line:
                power = line.split(":")[1]

        #获取当前时间
        currenttime = self.getCurrentTime()
        #将获取到的数据存到数组中
        self.adddata.append((currenttime, power))

    # 多次执行测试过程
    def run(self):
        #设置手机进入非充电状态
        os.popen("adb shell dumpsys battery set status 1")
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            #每 5 秒钟采集一次数据
            time.sleep(5)

    # 获取当前的时间戳
    def getCurrentTIme(self):
        currentTime = time.strftime('%Y-%m-%m %H:%M:%S')
        return currentTime

    # 保存数据
    def SaveDataToCSV(self):
        csvfile = file('traffic.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.allData)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(3)
    controller.run()
    controller.SaveDataToCSV()