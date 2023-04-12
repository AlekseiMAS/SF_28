import pytest
from selenium import webdriver
import time
from datetime import datetime

@pytest.fixture(scope="function")
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Chrome('chromedriver')
    driver.maximize_window()

    yield driver

    print("\nquit driver..")
    driver.quit()

    # Перехват и определение провалившегося теста и его скриншот
@pytest.hookimpl(tryfirst=True, hookwrapper=True)  # tryfirst определяет объект перехвата
def pytest_runtest_makereport(item, call):   # функция репорта состояний
    outcome = yield   # перехват всех yield
    rep = outcome.get_result()  # получаем результат
    setattr(item, "rep_" + rep.when, rep)   # определение атрибута результата

@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request): # функция обработки падения
    yield
    if request.node.rep_setup.failed:
        print("test is failed", request.node.nodeid)
    elif request.node.rep_setup.passed:   # возможно прошёл, но неудачно
        if request.node.rep_call.failed:  # засчитываем неудачный
            driver = request.node.funcargs["driver"]  # уровень падения driver
            save_screenshot(driver, request.node.nodeid)
            print("executing is failed", request.node.nodeid)

def save_screenshot(driver, nodeid):  # функция для скриншота
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M:%S")}.png'.replace('/', '_').replace('::', '__')
    driver.save_screenshot(file_name)
