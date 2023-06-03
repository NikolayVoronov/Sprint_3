from selenium import webdriver
from locators import Locators
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Открыть главную страницу
driver.get("https://stellarburgers.nomoreparties.site/")
# Нажать кнопку "Начинки"
driver.find_element(*Locators.STUFFING_BUTTON).click()
# Ждем три секунды
time.sleep(3)

# Проверить, что на экране открылся раздел с соусами
assert driver.find_element(*Locators.AREA_STUFFING)

# Закрыть браузер
driver.quit()
