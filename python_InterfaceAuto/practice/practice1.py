import unittest
import logging
class practic1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def setUp(self):
        print('setUp')

    def testCase001(self):
        print('testCase001')
        # log = Logger
        # self.assertLogs(logger=log, level=None)
        with self.assertLogs('foo', level='INFO') as cm:
            logging.getLogger('foo').info('first message')
            logging.getLogger('foo.bar').error('second message')
        self.assertEqual(cm.output, ['INFO:foo:first message',
                                     'ERROR:foo.bar:second message'])
        print(cm.output)
        print(cm.records)

    def testCase002(self):
        print('testCase002')
        # self.subTest(self.testCase003())
        # self.subTest(self.testCase001())

    def testCase003(self):
        print('testCase003')

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

# if __name__ == '__main__':
#     unittest.main()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(practic1('testCase001'))
    suite.addTest(practic1('testCase002'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())