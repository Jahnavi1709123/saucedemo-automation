from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_checkout_process():
    # Step 1: Setup browser and login
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("✅ Logged in")

    # Step 2: Add item to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    print("🛒 Item added to cart")

    # Step 3: Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    print("🧭 Navigated to cart page")

    # Step 4: Start checkout
    driver.find_element(By.ID, "checkout").click()
    print("📝 Checkout started")

    # ✅ Wait for checkout form to load
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    # Step 5: Enter user info
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    print("📋 Entered user info")

    # Step 6: Finish checkout
    driver.find_element(By.ID, "finish").click()
    print("💳 Finished order")

    # Step 7: Confirm success
    confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in confirmation
    print("✅ Order placed successfully")

    # Step 8: Close browser
    driver.quit()

if __name__ == "__main__":
    test_checkout_process()