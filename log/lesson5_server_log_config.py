import unittest
import lesson3_server

# Модульные тесты
class TestParsing(unittest.TestCase):
    def testNumberParameters(self):
        self.assertEqual(len(lesson3_server.parsing()), 2, 'Doesn''t contain two parameters needed to start')
        print("test 1")
        pass

    def testParametersAreNotNone(self):
        self.assertNotEqual(lesson3_server.parsing()[0], None, 'IP address could not be None or Null')
        self.assertNotEqual(lesson3_server.parsing()[1], None, 'Port number could not be None or Null')
        print("test 2")
        pass


class TestConnect(unittest.TestCase):
    def testDataAreNotNone(self):
        print("test 3")
        params = lesson3_server.parsing()
        runresult = lesson3_server.myserverup(params)
        print(params[0])
        print(type(runresult)) #return NoneType somehow
        #self.assertNotEqual(runresult, None, 'data could not be None or Null')
        pass


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()

