import unittest
import requests



class PetcoSmoke(unittest.TestCase):

    def setUp(sel):
        pass

    def tearDown(arg):
        pass

    def test_petco_landing_equals_200(self):
        """assert to landing side response with 200"""
        r = requests.get('http://www.petco.com')
        self.assertEqual(r.status_code, 200)

    def test_petco_local_is_us(self):
        """"Very Basic test to assert site is set to en-US"""
        r = requests.get('http://www.petco.com')
        self.assertEqual(r.headers['Content-Language'],"en-US")

    def test_petco_cookie_is_issued(self):
        r = requests.get('http://www.petco.com')
        self.assertIsNotNone(r.headers['Set-Cookie'])

    def test_petco_content_Encoding(self):
        r = requests.get('http://www.petco.com')
        self.assertEqual(r.headers['Content-Encoding'],'gzip')




if __name__ == '__main__':
    unittest.main()
