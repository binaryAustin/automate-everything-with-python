from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[1]")
    print(element.text)
    driver.quit()


if __name__ == "__main__":
    main()
