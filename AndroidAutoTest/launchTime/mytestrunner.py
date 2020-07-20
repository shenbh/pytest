import unitestdemo
import unittest

#指定执行某几条测试用例
# mysuite = unittest.TestSuite()
# mysuite.addTest(unitestdemo.MyTestCase("test_loginFail"))
# mysuite.addTest(unitestdemo.MyTestCase("test_loginOK"))

#一次执行类中所有的测试用例
cases=unittest.TestLoader().loadTestsFromTestCase(unittest.MyTestCase)
mysuite=unittest.TestSuite(cases) #有多个cases的话用逗号“,”隔开
#单独设置一个测试用例
mysuite.addTest(unitestdemo.MyTestCase("test_loginFail")) #上面会执行两条测试用例，这条是单独设置的测试用例

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
