from selenium import webdriver
from locators import Locators
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Открыть главную страницу
driver.get("https://stellarburgers.nomoreparties.site/")
# Нажать кнопку "Соусы"
driver.find_element(*Locators.SOUCE_BUTTON).click()
# Ждем три секунды
time.sleep(3)

# Проверить, что на экране открылся раздел с соусами
assert driver.find_element(*Locators.AREA_SOUCE)

# Закрыть браузер
driver.quit()
