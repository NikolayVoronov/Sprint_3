from selenium import webdriver
from locators import Locators
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Открыть страницу с формой регистрации
driver.get("https://stellarburgers.nomoreparties.site/register")
# Найти поле пароль и добавить в него значение
driver.find_element(*Locators.FIELD_PASSWORD).send_keys("1234")
# Нажать кнопку зарегистрироваться
driver.find_element(*Locators.REG_BUTTON).click()
# Ждем три секунды
time.sleep(3)

# Проверить сообщение об ошибке
assert driver.find_element(*Locators.INCORRECT_PASS_MESSAGE).text == 'Некорректный пароль'

# Закрыть браузер
driver.quit()
