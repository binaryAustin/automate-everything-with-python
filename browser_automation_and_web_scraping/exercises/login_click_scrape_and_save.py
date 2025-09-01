import os
import csv
import time
from datetime import datetime, timezone
from selenium import webdriver
from selenium.webdriver.common.by import By

filepath = "exercises/temperatures.csv"

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
        driver.get("https://automated.pythonanywhere.com/login/")

        try:
            username_input = driver.find_element(by=By.ID, value="id_username")
            password_input = driver.find_element(by=By.ID, value="id_password")
            sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
            username_input.send_keys("automated")
            password_input.send_keys("automatedautomated")
            sign_in_button.click()

            driver.implicitly_wait(10.0)

            home_link = driver.find_element(by=By.XPATH, value="/html/body/nav/div/a")
            home_link.click()

            div = driver.find_element(
                by=By.XPATH, value="//h1[@id='displaytimer']/div[@class='text-success']"
            )
            temperature = float(div.text.split(":")[1].strip())

            exists = os.path.exists(filepath)
            with open(filepath, mode="a", encoding="utf-8") as fw:
                csv_writer = csv.writer(fw)
                if not exists:
                    csv_writer.writerow(["recorded_at", "temperature"])
                recorded_at = (
                    datetime.now(timezone.utc)
                    .isoformat(timespec="seconds")
                    .replace("+00:00", "Z")
                )
                csv_writer.writerow([recorded_at, temperature])

        except Exception as e:
            print("Error: " + e)
            break

        time.sleep(30.0)

except KeyboardInterrupt:
    print("Program is stopped by user")
finally:
    driver.quit()
