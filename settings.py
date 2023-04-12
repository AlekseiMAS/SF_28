from faker import Faker
import random

base_url = "https://b2c.passport.rt.ru/"

url_change_page = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"


def random_int():
    random_int = random.randint(1, 9999999999)
    return random_int

def generate_string(num):
    return "ю" * num

def rus_charset():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def special_chars():
    return '=+`~?"№;:[]{}_|\\/!@#$%^&*()-'

def valid_phone():
    random_valid_phone = random.randint(1111111111, 9999999999)
    return random_valid_phone

def valid_first_name():
    random_valid_first_name = Faker(['ru_RU']).first_name()
    return random_valid_first_name

def valid_last_name():
    random_valid_last_name = Faker(['ru_RU']).last_name()
    return random_valid_last_name

def first_name_en():
    random_first_name_en = Faker().first_name()
    return random_first_name_en

def first_name_last_name():
    random_first_name_last_name = Faker().name()
    return random_first_name_last_name

def without_name_email():
    return "@pyt.ru"

def without_at_email():
    return "pyt.ru"

def without_domain_email():
    return "ros@"


valid_email = 'sf_test123@mail.ru'  # Ввести валидный email
valid_password = 'rtkTest'  # Ввести валидный пароль
valid_email_reg = 'sf_test123@mail.ru'  # Ввести валидный email

invalid_name = [random_int()
    , generate_string(1)
    , generate_string(31)
    , first_name_en()
    , special_chars()
    , first_name_last_name()
                ]

invalid_email = [without_name_email()
    , without_at_email()
    , without_domain_email()
    , rus_charset()
    , special_chars()
                 ]

invalid_password = [random_int()
    , generate_string(10)
    , rus_charset()
    , special_chars()
    , first_name_en()
    , first_name_last_name()
                    ]

first_name = [valid_first_name()]

last_name = [valid_last_name()]

last_name_pozitiv = [generate_string(2)
    , generate_string(3)
    , generate_string(15)
    , generate_string(29)
    , generate_string(30)
    , "аа-аа"
                     ]

last_name_negativ = [generate_string(1)
    , generate_string(31)
    , "<script>alert('Поле input уязвимо!')</script>"  # XSS-инъекция
    , "SELECT*from NAMES"  # SQL-инъекция
    , "latin"
                     ]

menu_type_auth = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
placeholder_name = ['Мобильный телефон', 'Электронная почта', 'Логин', 'Лицевой счёт']

empty = ''
empty_email = ''
empty_password = ''

# Для использования данных методов в тестах необходимо убрать конкретные значения этих переменных
# def valid_email():
#    random_valid_email = Faker().email()
#    return random_valid_email


# def valid_password():
#     pwd = []
#     for i in range(3):
#         pwd.append(random.choice(string.ascii_lowercase))
#         pwd.append(random.choice(string.ascii_uppercase))
#         pwd.append(random.choice(string.digits))
#     return (''.join(pwd))

# valid_email_or_phone = [valid_email(), "54365672789", "2749567827405"]
# valid_password = [valid_password()]
