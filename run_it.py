import unittest
import xmlrunner

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_isequal(self):
	self.assertEqual('foo'.upper(), 'FAIL')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

def runner(output='python_tests_xml'):
	return xmlrunner.XMLTestRunner(output=output)

#def find_tests():
	#return unittest.main()
	#return unittest.TestLoader().discover('JenkinsTest')

if __name__ == '__main__':
    	#unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
	runner().run(suite)
	#runner().run(find_tests())
	
