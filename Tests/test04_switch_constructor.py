from locators import Locators
from urls import Urls

class TestSwitchConstructor:
    def test_switch_to_bakery(self, driver):
        """Проверяем, что открыт раздел с булками"""
        driver.get(Urls.MAIN)
        assert driver.find_element(*Locators.AREA_BAKERY)

    def test_switch_to_souce(self, driver):
        """Переходим в раздел с соусами и проверяем, что открыт именно он"""
        driver.get(Urls.MAIN)
        driver.find_element(*Locators.SOUCE_BUTTON).click()
        assert driver.find_element(*Locators.AREA_SOUCE)

    def test_switch_to_stuffing(self, driver):
        """Переходим в раздел с начинками и проверяем, что открыт именно он"""
        driver.get(Urls.MAIN)
        driver.find_element(*Locators.STUFFING_BUTTON).click()
        assert driver.find_element(*Locators.AREA_STUFFING)
