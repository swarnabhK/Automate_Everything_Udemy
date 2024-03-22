from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
#Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver

def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")

print(main())

