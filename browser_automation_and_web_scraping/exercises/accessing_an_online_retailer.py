import os
import csv
import time
from datetime import datetime, timezone
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://sicomp.vn/nguon-may-tinh-asus-prime-750w-gold-ap-750g-80-plus-gold-mau-trang-/"
filepath = "exercises/asus_prime_750w_gold_price_tracking.csv"

options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("start-maximized")
options.add_argument("disable-dev-shm-usage")
options.add_argument("no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option(
    "prefs",
    {
        "credentials_enable_service": False,  # Disable "Save Password"
        "profile.password_manager_leak_detection": False,  # Disable password leak detection pop-up
        "profile.default_content_setting_values.notifications": 2,  # Block notifications
        "profile.default_content_setting_values.geolocation": 2,  # Block geolocation requests
    },
)
options.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

try:
    while True:
        driver.get(url)

        try:

            cart_links = driver.find_elements(
                by=By.CSS_SELECTOR,
                value="a[data-href*='817'][data-type='cart'][data-action='add']",
            )
            is_available = len(cart_links) > 0

            price_el = driver.find_element(
                by=By.CSS_SELECTOR, value=".detail-n-price > span:first-child"
            )
            price = int(price_el.text.strip().replace("đ", "").strip().replace(".", ""))

            exists = os.path.exists(filepath)
            with open(filepath, mode="a", encoding="utf-8") as fw:
                csv_writer = csv.writer(fw)
                if not exists:
                    csv_writer.writerow(["recorded_at", "price"])
                recorded_at = (
                    datetime.now(timezone.utc)
                    .isoformat(timespec="seconds")
                    .replace("+00:00", "Z")
                )
                csv_writer.writerow([recorded_at, price])

        except Exception as e:
            # TODO: Output error to the logging file then notify the admin # [fixme]
            print("Error: " + e)
            break

        time.sleep(60.0)

except KeyboardInterrupt:
    print("Program is stopped by user")
finally:
    driver.quit()
