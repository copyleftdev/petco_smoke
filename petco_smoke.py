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

    def test_petco_affilate(self):
        r = requests.get(self.base_url+"/affiliate")
        self.assertEqual(r.status_code, 200)

    def test_petco_caresheet(self):
        r = requests.get(self.base_url+"/caresheet")
        self.assertEqual(r.status_code, 200)

    def test_petco_contact_us(self):
        r = requests.get(self.base_url+"/contact-us")
        self.assertEqual(r.status_code, 200)

    def test_petco_coe(self):
        r = requests.get(self.base_url+"/content/petco/PetcoStore/en_US/pet-services/corporate/code-of-ethics.html")
        self.assertEqual(r.status_code, 200)

    def test_petco_sponser(self):
        r = requests.get(self.base_url+"/content/petco/PetcoStore/en_US/pet-services/corporate/event-sponsorship.html")
        self.assertEqual(r.status_code, 200)

    def test_petco_venders(self):
        r = requests.get(self.base_url+"/content/petco/PetcoStore/en_US/pet-services/corporate/vendors.html")
        self.assertEqual(r.status_code, 200)

    def test_petco_sitemap(self):
        r = requests.get(self.base_url+"/shop/Sitemap?catalogId=10051&langId=-1&storeId=10151")
        self.assertEqual(r.status_code, 200)

    def test_petco_landing2(self):
        r = requests.get(self.base_url+"/shop/en/petcostore")
        self.assertEqual(r.status_code, 200)

    def test_petco_carefresh(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/brand/carefresh")
        self.assertEqual(r.status_code, 200)

    def test_petco_starwars(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/brand/star-wars")
        self.assertEqual(r.status_code, 200)

    def test_petco_trolls(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/brand/trolls")
        self.assertEqual(r.status_code, 200)

    def test_petco_birds(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_bath(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-bath")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_cages(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-cages-and-accessories")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_ordor(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-cleanup-and-odor-control")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_treats(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-food-and-treats")
        self.assertEqual(r.status_code, 200)

    def test_petco_(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-food-storage-supplies")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_grooming(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-grooming-and-bathing")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_welness(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-health-and-wellness")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_house(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-houses")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_nest(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-nests-and-accessories")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_perches(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/bird-perches")
        self.assertEqual(r.status_code, 200)

    def test_petco_chickens(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/chicken-supplies")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_gifts(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/gifts-for-bird-lovers")
        self.assertEqual(r.status_code, 200)

    def test_petco_live_birds(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/live-birds")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_outdoors(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/outdoor-bird-supplies")
        self.assertEqual(r.status_code, 200)

    def test_petco_bird_playground(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/bird/playgrounds-and-playstands")
        self.assertEqual(r.status_code, 200)

    def test_petco_cats(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat")
        self.assertEqual(r.status_code, 200)

    def test_petco_cats_flea_tick(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-and-kitten-flea-and-tick")
        self.assertEqual(r.status_code, 200)

    def test_petco_(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-apparel")
        self.assertEqual(r.status_code, 200)

    def test_petco_cats_beds(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-beds-and-bedding")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_odor_control(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-cleanup-and-odor-control")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_collars(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-collars-leashes-and-harnesses")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_id_tags(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-collars-leashes-and-harnesses/cat-id-tags")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_containment(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-containment")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_feeding_supplies(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-feeding-supplies")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_fleat_tick(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-flea-and-tick")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_food(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-food")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_furniture(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-furniture-and-scratchers")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_furniture_protection(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-furniture-protection")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_gifts(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-gifts-for-pet-lovers")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_grooming(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-grooming-and-bathing")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_health_welness(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-health-and-wellness")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_1(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-litter-boxes-and-accessories")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_2(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-steps-and-ramps")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_3(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-toys")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_4(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-training")
        self.assertEqual(r.status_code, 200)

    def test_petco_cat_5(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/cat/cat-treats")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_1(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_2(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-and-puppy-flea-and-tick")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_3(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-apparel")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_4(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-beds-and-bedding")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_5(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-cleanup-and-odor-control")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_6(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-collars-leashes-and-harnesses")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_7(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-collars-leashes-and-harnesses/dog-collar-id-tags")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_8(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-containment")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_9(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-feeding-supplies")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_10(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-food")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_11(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-food/natural-dog-food")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_12(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-furniture-protection")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_13(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-gifts-for-pet-lovers")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_14(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-grooming-and-bathing")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_15(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-health-and-wellness")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_16(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-lawn-care")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_17(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-steps-and-ramps")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_18(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-toys")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_19(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-trackers-and-locators")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_20(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-training")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_21(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-treats-and-chews")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_22(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/dog-vehicle-accessories")
        self.assertEqual(r.status_code, 200)

    def test_petco_dog_23(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/dog/waste-disposal")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_1(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_2(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/feeding-accessories")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_3(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-aquariums-kits")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_4(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-food")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_5(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-health-wellness")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_6(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-co2-accessories")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_7(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-decor")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_8(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-filtration")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_9(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-heaters-chillers")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_10(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-hoods-lighting")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_11(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-maintenance")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_12(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-protein-skimmers")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_13(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-pumps-and-powerheads")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_14(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-reverse-osmosis")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_15(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-sand-gravel-substrate")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_16(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-stands-canopies")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_17(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-tank-uv-sterilizers")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_18(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/fish-water-care")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_19(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/live-fish")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_20(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/fish/pond-supplies")
        self.assertEqual(r.status_code, 200)

    def test_petco_halloween(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/halloween-shop")
        self.assertEqual(r.status_code, 200)

    def test_petco_holiday(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/holiday-shop")
        self.assertEqual(r.status_code, 200)

    def test_petco_stocking(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/holiday-shop/holiday-stockings-and-decor")
        self.assertEqual(r.status_code, 200)

    def test_petco_home_collection(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/home-collections")
        self.assertEqual(r.status_code, 200)

    def test_petco_pet_tech(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/pet-technology")
        self.assertEqual(r.status_code, 200)

    def test_petco_fedders(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/pet-technology/automatic-feeders-and-waterers")
        self.assertEqual(r.status_code, 200)

    def test_petco_pet_cams(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/pet-technology/pet-cameras")
        self.assertEqual(r.status_code, 200)

    def test_petco_gps(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/pet-technology/pet-gps-and-activity-trackers")
        self.assertEqual(r.status_code, 200)

    def test_petco_pool_alarm(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/pet-technology/pet-pool-alarms")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_1(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_2(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/gifts-for-reptile-lovers")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_3(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/live-reptiles")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_4(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-cleanup-and-odor-control")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_5(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-collars-leashes-and-harnesses")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_6(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-food")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_7(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-growth-shells")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_8(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-habitat-accessories")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_9(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-habitat-decor")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_10(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-habitat-hoods-and-lighting")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_11(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-habitat-stands-and-canopies")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_12(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-habitats-and-enclosures")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile_welness(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-health-and-wellness")
        self.assertEqual(r.status_code, 200)

    def test_petco_reptile(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/reptile/reptile-treats")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_small_an(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_small_an(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/gifts-for-small-animal-lovers")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_hitches(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/hutches")
        self.assertEqual(r.status_code, 200)

    def test_petco_(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/live-small-animals")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_1(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-bedding-litter")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_2(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-cages-habitats")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_3(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-carriers")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_4(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-cleanup-odor-control")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_5(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-collars-leashes-harnesses")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_6(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-feeding-supplies")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_treats(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-food-treats")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_grooming(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-grooming-bathing")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_wellness(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-health-wellness")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_sleepter(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-sleepers-hideaways")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_toys(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/category/small-animal/small-animal-toys-habitat-accessories")
        self.assertEqual(r.status_code, 200)

    def test_petco_current_offer(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/current-offer-details")
        self.assertEqual(r.status_code, 200)

    def test_petco_events(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/events")
        self.assertEqual(r.status_code, 200)

    def test_petco_fish_resouces_events(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/fish-resources-and-events")
        self.assertEqual(r.status_code, 200)

    def test_petco_sale_and_offer(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/sale-and-offers")
        self.assertEqual(r.status_code, 200)

    def test_petco_small_animal_cages(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/small-animal/small-animal-cages-habitats")
        self.assertEqual(r.status_code, 200)

    def test_petco_travel(self):
        r = requests.get(self.base_url+"/shop/en/petcostore/specialty/travel-and-adventure-shop")
        self.assertEqual(r.status_code, 200)

    def test_petco_starwars(self):
        r = requests.get(self.base_url+"/star-wars")
        self.assertEqual(r.status_code, 200)

    def test_petco_adoption(self):
        r = requests.get(self.base_url+"/think-adoption-first")
        self.assertEqual(r.status_code, 200)

    def test_petco_pet_services(self):
        r = requests.get(self.base_url+"/veterinary-services")
        self.assertEqual(r.status_code, 200)





if __name__ == '__main__':
    unittest.main()
