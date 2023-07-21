import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from tqdm import tqdm


# Get the values from the parsed arguments
leetcode_session_token = input("leetcode-session-token: ")
listname = input("listname: ")
add = input("action ( Add / Remove ): ")

# read text.txt
f = open("text.txt", "r")
text = f.read()
f.close()

# find urls
url_pattern = re.compile(
    r"https://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)
urls = url_pattern.findall(text)

# Create a new instance of the Google Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# iterate over each url
for i, url in enumerate(tqdm(urls, "working hard!!!")):
    # parts = url.split("/")
    # url = "/".join(parts[:5])

    # navigate to the page
    driver.get(url)

    if i == 0:
        # set cookie
        driver.add_cookie({"name": "LEETCODE_SESSION", "value": leetcode_session_token})

        # refresh the page
        driver.refresh()

    # wait until the page is ready
    time.sleep(1)

    try:
        # find star button and click
        star_button = driver.find_element(
            By.XPATH, "//div[contains(@id, 'headlessui-popover-button')]/div/div"
        )
        star_button.click()
    except StaleElementReferenceException:
        # find star button and click
        star_button = driver.find_element(
            By.XPATH, "//div[contains(@id, 'headlessui-popover-button')]/div/div"
        )
        star_button.click()

    # wait until the popover is ready
    time.sleep(0.8)
    # find add button
    add_button = driver.find_element(
        By.XPATH, f"//span[contains(text(), '{listname}')]/../../..//div[2]"
    )
    if add_button.text == add:
        add_button.click()

print("Done!")
# quit the driver
driver.quit()
