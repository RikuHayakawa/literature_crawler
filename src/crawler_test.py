from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")  # Headlessモードで軽量実行
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Murasan IT Lab")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)
    print("Page title is:", driver.title)
finally:
    driver.quit()
