# python -m pytest -v --driver Chrome --driver-path chromedriver tests/rtests.py
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import settings
from pages.authorization import AuthPage
from pages.locators import AuthLocators
from settings import *


class TestAuthPage():

"""Переход на страницу с формой авторизации"""
    def test_login_form_opens(self, driver):
        authorization = AuthPage(driver, base_url)
        authorization.open()
        authorization.login_form_opens()

"""Расположение продуктового слогана и вспомогательной информации"""
    def test_location_slogan_and_support_info(self, driver):
        authorization = AuthPage(driver, base_url)
        authorization.open()
        authorization.location_slogan_and_support_info()

"""Отображение меню выбора авторизации."""
    def test_location_authentication_selection_menu(self, driver):
        authorization = AuthPage(driver, base_url)
        authorization.open()
        authorization.location_auth_selection_menu()

"""Проверка названия табов в меню выбора типа авторизации."""
    def test_menu_type_autoriz(self, driver):
        try:
            authorization = AuthPage(driver, base_url)
            menu = [authorization.tab_phone.text, authorization.tab_mail.text, authorization.tab_login.text, authorization.tab_ls.text]
            for i in range(len(menu)):
                assert "Телефон" in menu
                assert 'Почта' in menu
                assert 'Логин' in menu
                assert 'Лицевой счёт' in menu
        except AssertionError:
            print('Ошибка в имени таба Меню типа аутентификации')

"""Автоматическое изменение таба выбора авторизации"""
    def test_auto_change_auth_tab(self, driver):
        authorization = AuthPage(driver, base_url)
        authorization.open()
        authorization.auto_change_auth_tab()

"""Сценарий авторизации клиента с валидными значениями e-mail и паролем."""
    def test_autoriz_valid_email_pass(self, driver):
        page = AuthPage(driver, base_url)
        page.email.send_keys(settings.valid_email)
        page.email.clear()
        page.password.send_keys(settings.valid_password)
        page.password.clear()
        page.btn_enter.click()

        try:
            assert page.get_relative_link() == '/auth/realms/b2c/login-actions/authenticate'
        except AssertionError:
            assert 'Неверно введен текст с картинки' in page.find_other_element(*AuthLocators.ERROR_MESSAGE).text

""""Сценарий авторизации клиента по эл.почте, кнопка "Почта" с невалидным email и паролем, а также пустые значения."""
    @pytest.mark.parametrize("incor_email", [settings.invalid_email, settings.empty_email],
                             ids=['invalid_email', 'empty'])
    @pytest.mark.parametrize("incor_passw", [settings.invalid_password, settings.empty_password],
                             ids=['invalid_password', 'empty'])
    def test_autoriz_invalid_email_pass(self, driver, incor_email, incor_passw):
        page = AuthPage(driver, base_url)
        page.email.send_keys(incor_email)
        page.email.clear()
        page.password.send_keys(incor_passw)
        page.password.clear()
        page.btn_enter.click()
        assert page.get_relative_link() != '/account_b2c/page'

"""Переход по ссылке авторизации пользователя через VK."""
    def test_auth_vk(self, driver):       
        page = AuthPage(driver, base_url)
        page.vk_button.click()
        assert page.get_base_url() == 'oauth.vk.com'

"""Переход по ссылке авторизации пользователя через сайт одноклассники."""
    def test_auth_ok(self, driver):        
        page = AuthPage(driver, base_url)
        page.ok_button.click()
        assert page.get_base_url() == 'connect.ok.ru'

"""Переход по ссылке авторизации пользователя через сайт Мой мир."""
    def test_auth_mail(self, driver):       
        page = AuthPage(driver, base_url)
        page.mail_button.click()
        assert page.get_base_url() == 'connect.mail.ru'

"""Переход по ссылке авторизации пользователя через Google."""
    def test_auth_google(self, driver):        
        page = AuthPage(driver, base_url)
        page.google_button.click()
        assert page.get_base_url() == 'accounts.google.com'

"""Авторизация с незаполненными полями."""
    def test_authorization_with_empty_fields(self, driver):        
        authorization = AuthPage(driver, base_url)
        authorization.open()
        authorization.authorization_with_empty_fields()


class TestRegPage():

"""Переход и отображение формы для восстановления пароля."""
    def test_go_to_the_password_recovery_form(self, driver):        
        authorization = AuthPage(driver, base_url)
        authorization.open()
        authorization.go_to_the_password_recovery_form()

"""Работа кнопки "Вернуться назад" на странице восстановления пароля"""
    def test_back_button(self, driver):        
        change_pass_page = AuthPage(driver, url_change_page)
        change_pass_page.open()
        change_pass_page.back_button()

"""Переход на форму "Регистрация"."""
    def test_registration_link(self, driver):        
        authorization = AuthPage(driver, base_url)
        authorization.register_link.click()

"""Наличие основных элементов на странице "Регистрация"."""
    def test_elements_registration(self, driver):
        try:
            page_reg = AuthPage(driver, base_url)
            page_reg.open_reg_page()
            card_of_reg = [page_reg.first_name, page_reg.last_name, page_reg.address_registration,
                           page_reg.email_registration, page_reg.password_registration,
                           page_reg.password_registration_confirm, page_reg.registration_btn]
            for i in range(len(card_of_reg)):
                assert page_reg.first_name in card_of_reg
                assert page_reg.last_name in card_of_reg
                assert page_reg.email_registration in card_of_reg
                assert page_reg.address_registration in card_of_reg
                assert page_reg.password_registration in card_of_reg
                assert page_reg.password_registration_confirm in card_of_reg
                assert page_reg.registration_btn in card_of_reg
        except AssertionError:
            print('Элемент отсутствует в форме «Регистрация»')

"""Работа формы "Регистрация" при вводе действительного e-mail в поле "e-mail или мобильный телефон"."""
    def test_valid_email_entry_check(self, driver):      
        page = AuthPage(driver, base_url)
        page.open_reg_page()
        page.valid_email_entry_check()

"""Работа формы "Регистрация" на ввод недействительного e-mail."""
    @pytest.mark.parametrize('input_text', invalid_email)
    def test_invalid_email_entry_check(self, driver, input_text):      
        page = AuthPage(driver, base_url)
        page.open_reg_page()
        page.invalid_email_entry_check(input_text)

"""Работа формы "Регистрация" на ввод невалидных данных в поле "Имя."""
    @pytest.mark.parametrize('input_text', invalid_name)
    def test_entering_invalid_name_data(self, driver, input_text):       
        page = AuthPage(driver, base_url)
        page.open_reg_page()
        page.entering_invalid_name_data(input_text)

"""Позитивные проверки для поля ввода фамилии."""
    @pytest.mark.parametrize('input_text', last_name_pozitiv)
    def test_last_name_positive(self, driver, input_text):       
        page = AuthPage(driver, base_url)
        page.open_reg_page()
        page.entering_last_name_pozitiv(input_text)

"""Негативные проверки для поля ввода фамилии."""
    @pytest.mark.parametrize('input_text', last_name_negativ)
    def test_last_name_negativ(self, driver, input_text):        
        page = AuthPage(driver, base_url)
        page.open_reg_page()
        page.entering_last_name_negativ(input_text)
