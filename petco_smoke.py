import unittest
import requests
from bs4 import BeautifulSoup as bs


class PetcoSmoke(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://petco.com"

    def tearDown(self):
        pass

    def test_petco_landing_equals_200(self):
        """ simple hook test assert  landing side response with 200"""
        r = requests.get(self.base_url)
        self.assertEqual(r.status_code, 200)

    def test_petco_local_is_us(self):
        """"Very Basic test to assert site is set to en-US"""
        r = requests.get(self.base_url)
        self.assertEqual(r.headers['Content-Language'], "en-US")

    def test_petco_cookie_is_issued(self):
        r = requests.get(self.base_url)
        self.assertIsNotNone(r.headers['Set-Cookie'])

    def test_petco_content_Encoding(self):
        r = requests.get(self.base_url)
        self.assertEqual(r.headers['Content-Encoding'], 'gzip')

    def test_petco_header_widget(self):
        r = requests.get(self.base_url)
        s = bs(r.text, 'html.parser')
        result = s.find(id='header')

        self.assertGreaterEqual(result.get_text(), 0)

    def test_petco_dog_training(self):
        r = requests.get(self.base_url+"/dog-training")
        self.assertEqual(r.status_code, 200)

    def test_petco_events(self):
        r = requests.get(self.base_url+"/events")
        self.assertEqual(r.status_code, 200)

    def test_petco_gitcards(self):
        r = requests.get(self.base_url+"/gift-cards")
        self.assertEqual(r.status_code, 200)

    def test_petco_grooming(self):
        r = requests.get(self.base_url+"/grooming")
        self.assertEqual(r.status_code, 200)

    def test_petco_help(self):
        r = requests.get(self.base_url+"/help")
        self.assertEqual(r.status_code, 200)

    def test_petco_kids(self):
        r = requests.get(self.base_url+"/kids")
        self.assertEqual(r.status_code, 200)

    def test_petco_pet_center(self):
        r = requests.get(self.base_url+"/new-pet-center")
        self.assertEqual(r.status_code, 200)

    def test_petco_newpet(self):
        r = requests.get(self.base_url+"/newpet")
        self.assertEqual(r.status_code, 200)

    def test_petco_gitcards(self):
        r = requests.get(self.base_url+"/gift-cards")
        self.assertEqual(r.status_code, 200)

    def test_petco_gitcards(self):
        r = requests.get(self.base_url+"/gift-cards")
        self.assertEqual(r.status_code, 200)

    def test_petco_nutrition(self):
        r = requests.get(self.base_url+"/nutrition")
        self.assertEqual(r.status_code, 200)

    def test_petco_order_status(self):
        r = requests.get(self.base_url+"/order-status")
        self.assertEqual(r.status_code, 200)

    def test_petco_pals_reward(self):
        r = requests.get(self.base_url+"/pals-rewards")
        self.assertEqual(r.status_code, 200)

    def test_petco_pet_care(self):
        r = requests.get(self.base_url+"/pet-care-resource-center")
        self.assertEqual(r.status_code, 200)

    def test_petco_pet_service(self):
        r = requests.get(self.base_url+"/pet-services")
        self.assertEqual(r.status_code, 200)

    def test_petco_promo_coupons(self):
        r = requests.get(self.base_url+"/petco-coupons-promos")
        self.assertEqual(r.status_code, 200)

    def test_petco_foundation(self):
        r = requests.get(self.base_url+"/petco-foundation")
        self.assertEqual(r.status_code, 200)

    def test_petco_pharmacy(self):
        r = requests.get(self.base_url+"/pharmacy")
        self.assertEqual(r.status_code, 200)

    def test_petco_private_policy(self):
        r = requests.get(self.base_url+"/privacy-policy")
        self.assertEqual(r.status_code, 200)

    def test_petco_product_guides(self):
        r = requests.get(self.base_url+"/product-guides")
        self.assertEqual(r.status_code, 200)

    def test_petco_repeat_delivery(self):
        r = requests.get(self.base_url+"/repeat-delivery")
        self.assertEqual(r.status_code, 200)

    def test_petco_returns(self):
        r = requests.get(self.base_url+"/returns")
        self.assertEqual(r.status_code, 200)

    def test_petco_shipping(self):
        r = requests.get(self.base_url+"/shipping")
        self.assertEqual(r.status_code, 200)

    def test_petco_shop_for_dog(self):
        r = requests.get(self.base_url + "/shop/en/petcostore/category/dog")
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
