from selenium import webdriver
from locators import Locators
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Открыть главную страницу
driver.get("https://stellarburgers.nomoreparties.site/")
# Найти кнопку "Войти в аккаунт" и нажать на неё
driver.find_element(*Locators.INTO_ACCOUNT_BUTTON).click()
# Найти поле почта и добавить в него значение
driver.find_element(*Locators.LOGIN).send_keys("nikolay_voronov_10_001@yandex.ru")
# Найти поле пароль и добавить в него значение
driver.find_element(*Locators.PASSWORD).send_keys("123456")
# Нажать кнопку "Войти"
driver.find_element(*Locators.ENTER_BUTTON).click()
# Ждем три секунды
time.sleep(3)

# Проверить, что авторизация прошла успешно
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# Закрыть браузер
driver.quit()
