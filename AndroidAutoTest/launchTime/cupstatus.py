#/usr/bin/python
#encoding:utf-8
import csv
import os
import time

#cpu 占用测试

#控制类
class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.adddata=[{'timestamp', 'cpustatus'}]

    #单次测试过程
    def testprocess(self):
        result = os.popen("db shell dumpsys cpuinfo | grep com.android.browser")
        for line in result.readlines():
            cupvalue = line.split("%")[0]

        currenttime = self.getCurrentTime()
        self.adddata.append((currenttime, cupvalue))

    #多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(5)

    #获取当前的时间戳
    def getCurrentTIme(self):
        currentTime = time.strftime('%Y-%m-%m %H:%M:%S')
        return currentTime

    # 保存数据
    def SaveDataToCSV(self):
        csvfile = file('cpustatus.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.allData)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSV()
