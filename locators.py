from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
    INTO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    PRIVATE_CAB_BUTTON = (By.XPATH, ".//nav/a")  # Кнопка "Личный кабинет"
    SOUCE_BUTTON = (By.XPATH, ".//main/section[1]/div[1]/div[2]") # Кнопка "Соусы"
    STUFFING_BUTTON = (By.XPATH, ".//main/section[1]/div[1]/div[3]") # Кнопка "Начинки"
    AREA_BAKERY = (By.XPATH, ".//main/section[1]/div[1]/div[contains(@class,'2BEPc')]/span[text()='Булки']") # Раздел с булками
    AREA_SOUCE = (By.XPATH, ".//main/section[1]/div[1]/div[contains(@class,'2BEPc')]/span[text()='Соусы']") # Раздел с соусами
    AREA_STUFFING = (By.XPATH, ".//main/section[1]/div[1]/div[contains(@class,'2BEPc')]/span[text()='Начинки']") # Раздел с начинками
    # Страница с формой авторизации /login
    LOGIN = (By.XPATH, ".//input[contains(@type,'text')]")  # Поле "Почта"
    PASSWORD = (By.XPATH, ".//input[contains(@type,'password')]")  # Поле "Пароль"
    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти"
    # Страница с формой регистрации /register
    FIELD_NAME = (By.XPATH, ".//input")  # Поле "Имя"
    FIELD_EMAIL = (By.XPATH, ".//fieldset[2]/div/div/input")  # Поле "Почта"
    FIELD_PASSWORD = (By.XPATH, ".//fieldset[3]/div/div/input")  # Поле "Пароль"
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    INCORRECT_PASS_MESSAGE = (By.XPATH, ".//fieldset[3]/div/p")  # Сообщение "Некорректный пароль"
    ENTER_BUTTON_REG = (By.XPATH, "//p[text()='Уже зарегистрированы?']/a")  # Кнопка "Войти"
    # Страница с формой восстановления /forgot-password
    ENTER_BUTTON_REC = (By.XPATH, "//p[text()='Вспомнили пароль?']/a") # Поле "Войти"
    # Страница с личным кабинетом /account/profile
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//nav/ul/li[1]/a")  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class,'2D0X2')]/a") # Кнопка логотипа
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выход"