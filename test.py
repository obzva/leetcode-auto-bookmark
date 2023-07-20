import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import os
from dotenv import load_dotenv
import time

# get the value of your key
load_dotenv()
leetcode_session_token = os.getenv("LEETCODE_SESSION")

# Create a new instance of the Google Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# navigate to the page
driver.get("https://leetcode.com/problems/generate-parentheses/")

# set cookie
driver.add_cookie({"name": "LEETCODE_SESSION", "value": leetcode_session_token})

# refresh the page
driver.refresh()

time.sleep(1.5)

divs_with_id = driver.find_elements(
    By.XPATH, "//div[contains(@id, 'headlessui-popover-button')]/div/div"
)

time.sleep(3)
for div in divs_with_id:
    div.click()
    time.sleep(1)
    try:
        span_with_text = driver.find_element(
            By.XPATH, "//span[contains(text(), 'PIRATE_KING: STRING')]"
        )
        print(f"yes {url}")
    except NoSuchElementException:
        pass
    time.sleep(1)

time.sleep(30)
