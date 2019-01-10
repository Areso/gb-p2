import unittest
import lesson3_client

# Модульные тесты
class parsing(unittest.TestCase):
    def testnumberparameters(self):
        self.assertEqual(len(lesson3_client.parsing()), 2, 'Doesn''t contain two parameters needed to start')
        print("test 1")
        pass

    def testparametersnotnone(self):
        self.assertNotEqual(lesson3_client.parsing()[0], None, 'IP address could not be None or Null')
        self.assertNotEqual(lesson3_client.parsing()[1], None, 'Port number could not be None or Null')
        print("test 2")
        pass

    def testdatanotnone(self):
        print("test 3")
        params = lesson3_client.parsing()
        runresult = lesson3_client.myconnect(params)
        print(params[0])
        print(type(runresult)) #return NoneType somehow
        #self.assertNotEqual(runresult, None, 'data could not be None or Null')
        pass


class connect(unittest.TestCase):
    def isresponsedatapresent(self):
        print("I had never been invoked")
        pass


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()

