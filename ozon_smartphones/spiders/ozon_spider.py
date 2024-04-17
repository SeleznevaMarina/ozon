import scrapy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy_selenium import SeleniumRequest
from ozon_smartphones.items import SmartphoneItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import pdb


class OzonSpider(scrapy.Spider):
    name = 'ozon'
    # driver = None
    
    def __init__(self):
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36"
            }
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # chrome_options.add_argument("--headless")
        
        # self.headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.0 Safari/537.36'
        # }
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        # cookies = [
        #     {'name': '__Secure-ETC', 'value': 'a4c0e7c47017cd84fdf201a82d4525cd', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': '__Secure-ab-group', 'value': '28', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': '__Secure-access-token', 'value': '4.0.5EDHzIVRTiiVeF_pZZ81qg.28.AeuF_Jhv72akJO7-CWS8jfGzqe0miY37ATilFZz8e9uqORTGXCky66P8vrtj6KRBZQ..20240417094506.V9GiwuNVAqt_zmB2WowixbAi2lOVMTI-kPqjN4hKuiI', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': '__Secure-ext_xcid', 'value': '1b97ac012841a10be159e225fa513b93', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': '__Secure-refresh-token', 'value': '4.0.5EDHzIVRTiiVeF_pZZ81qg.28.AeuF_Jhv72akJO7-CWS8jfGzqe0miY37ATilFZz8e9uqORTGXCky66P8vrtj6KRBZQ..20240417094506.eQkmeTn4Lj-iW40x4nHKq-LaxM9LsjDuDdFYBBZh3lc', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': '__Secure-user-id', 'value': '0', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': '__cf_bm', 'value': '9BVUrOjoLhyDxsi0a4fsT3KDwsRya_LT8pELWAmTggU-1713339917-1.0.1.1-c3kEBOX9.SVYTlVWBjEIsu19U1Ctfxr8VjHNN7pz.mDBoGtTl6Y.5hbQC4O4ojp78HPwEjikuXskhvm31gCkLw', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': 'abt_data', 'value': 'c436a87f881fe8c0a9817628bb335703:7cacdb9a2a3f36391909da93ba48b5fe2c0700b607ca7b4c99bec80a574dacca025853d429697492c1692db93c12c51ebf7b8c5a80cc0bcd3e145ac01e73a034c7d3d488c13451cf20c454a704323d892e3f0f5dfe8900a4194c019afc5c64e6db4a17189e56ba002f28eeeb946c53ff45d580f184df5feb2191a69ee647f809f00e58a5020ebd262921bce1a99ef4e93d92645a4e115b32a97d3034d6aae04303d80ea9f365ce113fd21eb52247b526153dc36bc867b39355ac456034cb2d802f206e71607be86021e77a254f3923066f37b7ba269a42d96ea2c1cf68f2df456bc0566694d2730caf3c7e7337758afa86a13e1ecd48e59fbc1f56f7c3f1435ca835dc8958841c9899529a719dc2f11d70d36f7ec0c6e4dfdb6701802624b48a9aa79c985244b4d01754472a83835ea422c77aa615551cfda24045bb3d3e67a57843e2119f11465098534e4919dcbb9a8437dea05a34f0bcc373d9533ab7de58ba8cc52ef908bd31837f43336246b91a1d44d16051888cc7ecf2e8117d9df045', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': 'cf_clearance', 'value': 'aDE_YaAsgn8R9SMhDrq7ywVJVZK2FSRgxhUmj6yh.Lw-1713339919-1.0.1.1-Mn1I5PTEkildd51P0v_9lj.f8Lu0Vl4OdL_haLWO7c7IWhjGoFZWWiZiwj.b7gFIMxQLB7AEN6mEplPPkUABJw', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': 'guest', 'value': 'true', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': 'is_cookies_accepted', 'value': '1', 'domain': '.ozon.ru', 'path': '/'},
        #     {'name': 'xcid', 'value': 'c874cd529fb85fc2eb6682807ad02e51', 'domain': '.ozon.ru', 'path': '/'}
        # ]

    def init_driver_cookies(self):
        cookies = [
            {'name': '__Secure-ETC', 'value': 'a4c0e7c47017cd84fdf201a82d4525cd', 'path': '/'},
            {'name': '__Secure-ab-group', 'value': '28', 'path': '/'},
            {'name': '__Secure-access-token', 'value': '4.0.5EDHzIVRTiiVeF_pZZ81qg.28.AeuF_Jhv72akJO7-CWS8jfGzqe0miY37ATilFZz8e9uqORTGXCky66P8vrtj6KRBZQ..20240417094506.V9GiwuNVAqt_zmB2WowixbAi2lOVMTI-kPqjN4hKuiI', 'path': '/'},
            {'name': '__Secure-ext_xcid', 'value': '1b97ac012841a10be159e225fa513b93', 'path': '/'},
            {'name': '__Secure-refresh-token', 'value': '4.0.5EDHzIVRTiiVeF_pZZ81qg.28.AeuF_Jhv72akJO7-CWS8jfGzqe0miY37ATilFZz8e9uqORTGXCky66P8vrtj6KRBZQ..20240417094506.eQkmeTn4Lj-iW40x4nHKq-LaxM9LsjDuDdFYBBZh3lc', 'path': '/'},
            {'name': '__Secure-user-id', 'value': '0', 'path': '/'},
            {'name': '__cf_bm', 'value': '9BVUrOjoLhyDxsi0a4fsT3KDwsRya_LT8pELWAmTggU-1713339917-1.0.1.1-c3kEBOX9.SVYTlVWBjEIsu19U1Ctfxr8VjHNN7pz.mDBoGtTl6Y.5hbQC4O4ojp78HPwEjikuXskhvm31gCkLw', 'path': '/'},
            {'name': 'abt_data', 'value': 'c436a87f881fe8c0a9817628bb335703:7cacdb9a2a3f36391909da93ba48b5fe2c0700b607ca7b4c99bec80a574dacca025853d429697492c1692db93c12c51ebf7b8c5a80cc0bcd3e145ac01e73a034c7d3d488c13451cf20c454a704323d892e3f0f5dfe8900a4194c019afc5c64e6db4a17189e56ba002f28eeeb946c53ff45d580f184df5feb2191a69ee647f809f00e58a5020ebd262921bce1a99ef4e93d92645a4e115b32a97d3034d6aae04303d80ea9f365ce113fd21eb52247b526153dc36bc867b39355ac456034cb2d802f206e71607be86021e77a254f3923066f37b7ba269a42d96ea2c1cf68f2df456bc0566694d2730caf3c7e7337758afa86a13e1ecd48e59fbc1f56f7c3f1435ca835dc8958841c9899529a719dc2f11d70d36f7ec0c6e4dfdb6701802624b48a9aa79c985244b4d01754472a83835ea422c77aa615551cfda24045bb3d3e67a57843e2119f11465098534e4919dcbb9a8437dea05a34f0bcc373d9533ab7de58ba8cc52ef908bd31837f43336246b91a1d44d16051888cc7ecf2e8117d9df045', 'path': '/'},
            {'name': 'cf_clearance', 'value': 'aDE_YaAsgn8R9SMhDrq7ywVJVZK2FSRgxhUmj6yh.Lw-1713339919-1.0.1.1-Mn1I5PTEkildd51P0v_9lj.f8Lu0Vl4OdL_haLWO7c7IWhjGoFZWWiZiwj.b7gFIMxQLB7AEN6mEplPPkUABJw', 'path': '/'},
            {'name': 'guest', 'value': 'true', 'path': '/'},
            {'name': 'is_cookies_accepted', 'value': '1', 'path': '/'},
            {'name': 'xcid', 'value': 'c874cd529fb85fc2eb6682807ad02e51', 'path': '/'}
            ]

        for cookie in cookies:
            self.driver.add_cookie(cookie)


    def start_requests(self):
        start_url = 'https://www.ozon.ru/category/smartfony-15502/?sorting=rating'
        self.driver.get(start_url)
        # self.init_driver_cookies()
        # self.driver.get(start_url)
        # self.handle_verification()

        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'a.tile-hover-target ui5 iu6')))
        pdb.set_trace()
        verification_element = self.driver.find_element(By.CLASS_NAME, 'captcha-prompt')
        time.sleep(20)
        verification_element.click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.tile-hover-target ui5 iu6')))
        
        smartphone_links = self.driver.find_elements_by_css_selector('a.tile-hover-target ui5 iu6')

        for link in smartphone_links[:100]:
            yield scrapy.Request(url=link.get_attribute('href'), callback=self.parse, headers=self.headers)
    
    def handle_verification(self):
        try:
            # Поиск элемента верификации
            verification_element = self.driver.find_element(By.CLASS_NAME, 'captcha-prompt')
            verification_element.click()  # Клик на элементе верификации
            time.sleep(3)
        except NoSuchElementException:
            pass


    def parse(self, response):
        item = SmartphoneItem()
        item['operating_system'] = response.css('dt:contains("Операционная система") + dd a::text').get()
        item['version'] = response.css(f'dt:contains("Версия {item["operating_system"]}") + dd a::text').get()
        yield item

    def closed(self, reason):
        if self.driver:
            self.driver.quit()
