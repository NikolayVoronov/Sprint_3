from selenium import webdriver
from locators import Locators
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Открыть страницу с авторизацией
driver.get("https://stellarburgers.nomoreparties.site/login")
# Найти поле почта и добавить в него значение
driver.find_element(*Locators.LOGIN).send_keys("nikolay_voronov_10_001@yandex.ru")
# Найти поле пароль и добавить в него значение
driver.find_element(*Locators.PASSWORD).send_keys("123456")
# Нажать кнопку "Войти"
driver.find_element(*Locators.ENTER_BUTTON).click()
# Ждем три секунды
time.sleep(3)
# Нажать кнопку "Личный кабинет"
driver.find_element(*Locators.PRIVATE_CAB_BUTTON).click()
# Ждем три секунды
time.sleep(3)

# Проверить, что открылась страница личного кабинета
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

# Закрыть браузер
driver.quit()
