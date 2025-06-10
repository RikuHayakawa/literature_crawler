import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    print("Zenn人気記事ページにアクセスします...")
    driver.get("https://zenn.dev/topics/個人開発")
    time.sleep(20)

    # 各記事コンテナを取得
    elements = driver.find_elements(By.CLASS_NAME, "ArticleList_container__V4svj")

    print("\n--- Zenn 人気記事のURL一覧 ---")
    for i, elem in enumerate(elements[:10], 1):
        try:
            a_tag = elem.find_element(By.TAG_NAME, "a")
            url = a_tag.get_attribute("href")
            print(f"{i}. {url}")
        except Exception as e:
            print(f"{i}. <URL取得失敗> ({e})")

finally:
    driver.quit()
