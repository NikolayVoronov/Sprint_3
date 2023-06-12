from locators import Locators
from urls import Urls

class TestRegistrationProcess:
    def test_successful_reg(self, driver):
        """Проверяем успешность регистрации на валидных данных"""
        driver.get(Urls.REGISTRATION)
        driver.find_element(*Locators.FIELD_NAME).send_keys("Жан Жак Тестировалль")
        driver.find_element(*Locators.FIELD_EMAIL).send_keys("nikolay_voronov_10_023@yandex.ru")
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.implicitly_wait(3)
        assert driver.find_element(*Locators.FIELD_ENTER).text == 'Вход'

    def test_incorrect_pass(self, driver):
        """Проверяем сообщение об ошибке при указании некорректного пароля"""
        driver.get(Urls.REGISTRATION)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys("1234")
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.implicitly_wait(3)
        assert driver.find_element(*Locators.INCORRECT_PASS_MESSAGE).text == 'Некорректный пароль'
