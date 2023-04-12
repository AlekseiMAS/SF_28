from telnetlib import EC
from .locators import AuthLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from urllib.parse import urlparse


class BasePage():

    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        driver.maximize_window()
        self.url = url
        self.driver.implicitly_wait(timeout)

    # метод поиска и возврата одного элемента
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_base_url(self):
        url = urlparse(self.driver.current_url)
        return url.hostname

    def scroll_down(self, offset=0):
        if offset:
            self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        if offset:
            self.driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    # метод открытия нужной страницы в браузере, используя метод get()
    def open(self):
        self.driver.get(self.url)

    # метод открытия формы регистрации в браузере, используя метод get()
    def open_reg_page(self):
        self.driver.get(self.url)
        self.find_element(AuthLocators.AUTH_REGISTER_LINK).click()

    # метод перехвата исключения, используется для проверки присутствия элемента на странице
    def is_element_present(self, what):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((what)))
        except (NoSuchElementException):
            return False
        return True

    # метод проверки отсутствия элемента на странице
    def is_not_element_present(self, what):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((what)))
        except (TimeoutException):
            return True
        return False

    def screenshot(self, file_name='screenshot.png'):
        self.driver.save_screenshot(file_name)
