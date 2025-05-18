from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseSeleniumTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()


class MainPageFuncTest(BaseSeleniumTest):
    def test_search_location_form_can_be_seen(self):
        '''
        Тест: Пользователь видит поле ввода населенного пункта
        '''
        self.browser.get(self.live_server_url)
        try:
            self.browser.find_element(By.CSS_SELECTOR, 'form.location-search')
        except NoSuchElementException:
            self.fail('Нет поля ввода или неправильный селектор')