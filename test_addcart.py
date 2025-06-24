from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_checkout_process():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        print("🔄 Opened saucedemo.com")

        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        print("✅ Logged in")

        # Add product to cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()
        print("✅ Item added to cart")

        # Navigate to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("✅ Navigated to cart page")

        # Click checkout
        driver.find_element(By.ID, "checkout").click()
        print("✅ Checkout started")

        # Fill user info
        driver.find_element(By.ID, "first-name").send_keys("Jahnavi")
        driver.find_element(By.ID, "last-name").send_keys("QA")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        print("✅ Entered user info")

        # Wait for and click Finish
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()
        print("✅ Order completed")

        # Confirm success
        success_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text

        assert "THANK YOU" in success_text.upper()
        print("🎉 Order success confirmed")

        # Keep browser open for 10 seconds
        time.sleep(10)
        driver.quit()

    except Exception as e:
        print("❌ Test failed with exception:", e)

# Run the test
test_checkout_process()
    
    

    

    
