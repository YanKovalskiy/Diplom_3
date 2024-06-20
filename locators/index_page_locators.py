from selenium.webdriver.common.by import By


class IndexPageLocators:
    LIST_OF_INGREDIENTS = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    NAME_INGREDIENT_IN_DETAILS_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]/div/div/p"
    BUTTON_CROSS_IN_DETAILS_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button"

    TAB_BUNS = By.XPATH, "//span[text()='Булки']/parent::div"
    TAB_SAUCES = By.XPATH, "//span[text()='Соусы']/parent::div"
    TAB_FILLINGS = By.XPATH, "//span[text()='Начинки']/parent::div"
