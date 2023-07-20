import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import os
from dotenv import load_dotenv
from tqdm import tqdm
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description="Add or remove problems to a list.")
parser.add_argument(
    "--listname", type=str, help="List name where you want to add problems into"
)
parser.add_argument(
    "--add",
    dest="action",
    action="store_const",
    const="Add",
    help="Add problems to the list",
)
parser.add_argument(
    "--remove",
    dest="action",
    action="store_const",
    const="Remove",
    help="Remove problems from the list",
)

# Parse the arguments
args = parser.parse_args()


# Get the values from the parsed arguments
listname = args.listname
add = args.action

# read text.txt
f = open("text.txt", "r")
text = f.read()
f.close()

# find urls
url_pattern = re.compile(
    r"https://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)
urls = url_pattern.findall(text)


# get the value of your key
load_dotenv()
leetcode_session_token = os.getenv("LEETCODE_SESSION")

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
