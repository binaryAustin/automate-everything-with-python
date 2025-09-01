from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
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
    driver.get("https://automated.pythonanywhere.com/login/")

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
    print(temperature)

    driver.quit()


if __name__ == "__main__":
    main()
