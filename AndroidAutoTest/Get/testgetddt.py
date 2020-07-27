
import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):


    @ddt.data("d3c1d530a8a378f", "", "@!#$", "ASJHDJAHSJD")
    def testGet(self, device_id):
        #header 部分的配置
        header = {
            'User-Agent': 'hlj-android/3.3.1',
            'Host': 'customer-api.helijia.com',
            'Connection': 'keep-alive',
            'Accept': 'gzip'
        }

        #cookies 部分的设置
        cookies = dict(
            beacon_id='MTAxLjI1MS4xOTUuMTESLTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
            search_test='1',
            search_r='32'
        )

        #get请求的构造
        res=requests.get('https://customer-api.helijia.com/app-customer/config/staticHost/get?version=3.3.1&city=110101&requestTime=1472980320170&deviceType=android&device_id='+device_id,
                         headers=header,
                         cookies=cookies)
        print(res.text)
        print(res.status_code)
        self.assertTrue(u"http://img.ucdn.static.helijia.com" in res.text)

if __name__ == '__main__':
    unittest.main()
