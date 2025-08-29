from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_presence(driver, by: By, locator: str, timeout: int = 10):
    """
    Espera até que o elemento esteja presente no DOM.
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator))
    )


def wait_for_visible(driver, by: By, locator: str, timeout: int = 10):
    """
    Espera até que o elemento esteja visível na página.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
    )


def wait_for_clickable(driver, by: By, locator: str, timeout: int = 10):
    """
    Espera até que o elemento esteja clicável.
    """
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator))
    )
