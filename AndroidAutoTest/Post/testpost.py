#coding=utf-8

import requests
import unittest


class testClass(unittest.TestCase):
    def testPost(self):
        keyword = {
            "version":"3.3.1",
            "city": "110100",
            "requestTime": "1472980321726",
            "deviceType":"android",
            "device_id":"d3c1d53d0a8a378f",
            "w":{"widgets":[{"defaultParams":{"pageType":"1","isDraft":"false","pageId":"1030","widgetId":"34","city": "110100"},"sortId":"0","preview":"false","id":"34","type":"0","widgetId":"0"},{"defaultParams":{"pageType":"1","isDraft":"false","pageId":"1030","widgetId":"34","city": "110100"},"sortId":"0","preview":"false","id":"34","type":"0","widgetId":"0"},{"defaultParams":{"pageType":"1","isDraft":"false","pageId":"1030","widgetId":"34","city": "110100"},"sortId":"0","preview":"false","id":"34","type":"0","widgetId":"0"}]}
        }

        headers = {
            'User-Agent':"hlj-android/3.3.1",
            'Host':'customer-api.helijia.com',
            'Connection':'keep-alive',
            'Accept-Encoding':'gzip'
        }

        cookies = dict(
            beacon_id='MTAxLjI1MS4xOTUuMTESLTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
            search_test='1',
            search_r='32'
        )

        res = requests.post(
            'https://customer-api.helijia.com/app-customer/config/staticHost/get?version=3.3.1&city=110101&requestTime=1472980320170&deviceType=android&device_id=d3c1d530a8a378f',
            data=keyword,
            headers=headers,
            cookies = cookies)

        print(res.text)
        print(res.status_code)
        self.assertTrue(u"今日上新" in res.text)

if __name__ == '__main__':
    unittest.main()
