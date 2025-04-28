from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    time.sleep(2)

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, ".inventory_item button")
    add_to_cart_button.click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    if cart_badge.text == '1':
        print("Produto adicionado ao carrinho com sucesso!")
    else:
        print("Falha ao adicionar produto ao carrinho.")

finally:
    time.sleep(5)
    driver.quit()