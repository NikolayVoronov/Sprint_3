from selenium import webdriver
from locators import Locators
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Открыть страницу с формой регистрации
driver.get("https://stellarburgers.nomoreparties.site/register")
# Найти поле имя и добавить в него значение
driver.find_element(*Locators.FIELD_NAME).send_keys("Жан Жак Тестировалль")
# Найти поле почта и добавить в него значение
driver.find_element(*Locators.FIELD_EMAIL).send_keys("nikolay_voronov_10_008@yandex.ru")
# Найти поле пароль и добавить в него значение
driver.find_element(*Locators.FIELD_PASSWORD).send_keys("123456")
# Нажать кнопку зарегистрироваться
driver.find_element(*Locators.REG_BUTTON).click()
# Ждем три секунды
time.sleep(3)

# Проверить успешность регистрации
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

# Закрыть браузер
driver.quit()
