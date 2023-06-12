from locators import Locators
from urls import Urls

class TestLoginProcess:
    def test_login_from_main_page_body(self, driver):
        """Авторизация в сервисе по кнопке «Войти в аккаунт» на главной"""
        driver.get(Urls.MAIN)
        driver.find_element(*Locators.INTO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN).send_keys("nikolay_voronov_10_001@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.implicitly_wait(3)
        assert driver.find_element(*Locators.PUSH_ORDER_BUTTON)

    def test_login_from_main_page_header(self, driver):
        """Авторизация в сервисе по кнопке «Личный кабинет» на главной"""
        driver.get(Urls.MAIN)
        driver.find_element(*Locators.PRIVATE_CAB_BUTTON).click()
        driver.find_element(*Locators.LOGIN).send_keys("nikolay_voronov_10_001@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.implicitly_wait(3)
        assert driver.find_element(*Locators.PUSH_ORDER_BUTTON)

    def test_login_from_reg_page(self, driver):
        """Авторизация в сервисе через кнопку в форме регистрации"""
        driver.get(Urls.REGISTRATION)
        driver.find_element(*Locators.ENTER_BUTTON_REG).click()
        driver.find_element(*Locators.LOGIN).send_keys("nikolay_voronov_10_001@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.implicitly_wait(3)
        assert driver.find_element(*Locators.PUSH_ORDER_BUTTON)

    def test_login_from_recovery_page(self, driver):
        """Авторизация в сервисе через кнопку в форме восстановления пароля"""
        driver.get(Urls.RECOVERY)
        driver.find_element(*Locators.ENTER_BUTTON_REC).click()
        driver.find_element(*Locators.LOGIN).send_keys("nikolay_voronov_10_001@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.implicitly_wait(3)
        assert driver.find_element(*Locators.PUSH_ORDER_BUTTON)
