from selenium.webdriver.common.by import By

class AuthLocators:
    BODY = (By.XPATH, "//body")
    AUTH_REGISTER_LINK = (By.XPATH, '//*[@id="kc-register"]')
    AUTH_HEADING = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    PAGE_RIGHT = (By.ID, 'page-right')
    PAGE_LEFT = (By.ID, 'page-left')
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_MAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TUB_LS = (By.ID, 't-btn-tab-ls')
    AUTH_LOGIN = (By.ID, "username")
    AUTH_MAIL = (By.ID, "username")
    AUTH_USERNAME_INPUT = (By.XPATH, "//input[@id='username']")
    AUTH_USERNAME_INPUT_EMAIL = (By.XPATH, "//span[contains(text(),'Электронная почта')]")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN_ENTER = (By.ID, "kc-login")
    FORGOT_PASS_LINK = (By.ID, "forgot_password")
    PLACEHOLDER_NAME = (By.XPATH, '//span[@class="rt-input__placeholder"]')
    PLACEHOLDER_MAIL = (By.XPATH, '//span[@class="rt-input__mask-start"]')
    CARD_OF_AUTH = (By.CLASS_NAME, 'card-container__wrapper')
    MENU_TAB = (By.XPATH, "//div[@class='rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs']")
    ACTIVE_TAB_PHONE = (By.XPATH, '//div[@id="t-btn-tab-phone" and @class="rt-tab rt-tab--small rt-tab--active"]')
    AUTH_LOGO = (By.XPATH, "//section[@id='page-left']/*/div[@class='what-is-container__logo-container']/*")
    AUTH_SLOGAN = (
    By.XPATH, "//section[@id='page-left']/*//p[contains(text(),'Персональный помощник в цифровом мире Ростелекома')]")
    AUTH_TAB_MENU = (By.XPATH, "//section[@id='page-right']/*//div[@id='t-btn-tab-phone' or @id='t-btn-tab-mail' or "
                "@id='t-btn-tab-login' or @id='t-btn-tab-ls']")
    AUTH_ERROR_ENTER_PHONE_NUMBER = (By.XPATH, "//span[contains(text(),'Введите номер телефона')]")
    ERROR_MESSAGE = (By.XPATH, '//span[@id="form-error-message"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@id='forgot_password']")
    CHANGE_PASSWORD = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    PASSWORD_GO_BACK_BUTTON = (By.XPATH, "//button[@id='reset-back']")
    VK_BUTTON = (By.ID, "oidc_vk")
    OK_BUTTON = (By.ID, 'oidc_ok')
    MAIL_BUTTON = (By.ID, 'oidc_mail')
    GOOGLE_BUTTON = (By.ID, 'oidc_google')
    YA_BUTTON = (By.ID, 'oidc_ya')
    YA_ENTER = (By.XPATH, "// button[ @ id = 'passp:sign-in']")
    MAIL_REGISTRATION = (By.CSS_SELECTOR, "input[id='address']")
    MAIL_REGISTRATION_VALUE = (By.XPATH, "//input[@type='hidden' and @name='address']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='lastName']")
    LAST_NAME_FIELD = (By.XPATH, '//input[@name="lastName"]')
    REGION_REGISTRATION = (By.XPATH, "//*[contains(text(),'Регион')]")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "input[id='password']")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input[id='password-confirm']")
    REG_BTN = (By.CSS_SELECTOR, "button[name='register']")
    REG_ERROR_INVALID_MAIL_PHONE_INPUT = (By.XPATH, "//span[contains(text(),"
                "'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")
    REG_FIRST_NAME_INPUT = (By.XPATH, "//span[contains(text(),'Имя')]/preceding-sibling::input")
    REG_LAST_NAME_INPUT = (By.XPATH, "//span[contains(text(),'Фамилия')]/preceding-sibling::input")
    REG_ERROR_FIRST_NAME_INPUT = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    REG_ERROR_LAST_NAME_INPUT = \
    (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")[1]
    WARNING_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')



    # REDIRECT_AUTH = (By.XPATH, '//button[text()="Войти"]')
    # CHANGE_PASS_BUTTON = (By.XPATH, "//button[@id='reset']")

