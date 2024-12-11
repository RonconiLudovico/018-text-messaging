import unittest

from main import main

class Test01(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the main function
        '''
        data = 'Hello, World!'
        result = main(data)
        self.assertEqual('4433555555666110966677755531111', result)


class Test02(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the main function
        '''
        data = 'ciao questo e un test'
        result = main(data)
        self.assertEqual('222444266607788337777866603308866083377778', result)


class Test03(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the main function
        '''
        data = 'abcdefghijklmnopqrstuvwxyz.,?!: '
        result = main(data)
        self.assertEqual('222222333333444444555555666666777777777788888899999999991111111111111110', result)
