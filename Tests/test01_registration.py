from locators import Locators
import time

class TestRegistrationProcess:
    def test_successful_reg(self, driver):
        driver.find_element(*Locators.FIELD_NAME).send_keys("Жан Жак Тестировалль")
        driver.find_element(*Locators.FIELD_EMAIL).send_keys("nikolay_voronov_10_010@yandex.ru")
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.REG_BUTTON).click()
        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_incorrect_pass(self, driver):
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys("1234")
        driver.find_element(*Locators.REG_BUTTON).click()
        time.sleep(3)
        assert driver.find_element(*Locators.INCORRECT_PASS_MESSAGE).text == 'Некорректный пароль'