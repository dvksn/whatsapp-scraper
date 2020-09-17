import argparse
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def get_contacts():
    # Return list of numbers
    return ["91XXXXXXXXXX", "919416046768"]


if __name__ == "__main__":
    print("Starting program")

    parser = argparse.ArgumentParser()
    parser.add_argument("--chrome_driver", required=True,
                        help="Specify the chrome driver path")
    parser.add_argument("--message", required=True,
                        help="Specify the message you want to send to your contacts")
    args = parser.parse_args()
    chrome_driver = args.chrome_driver
    message = args.message

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./newprofile")
    driver = webdriver.Chrome(chrome_driver, options=options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://web.whatsapp.com/")

    contacts = get_contacts()
    for contact in contacts:
        try:
            driver.get('https://web.whatsapp.com/send?phone={phone}'.format(phone=contact))
            driver.implicitly_wait(10)
            driver.find_element_by_xpath(
                '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]').send_keys(
                message + Keys.ENTER)
            time.sleep(5)
            print("Message sent to ", contact)
        except NoSuchElementException:
            print("Failed to send message. Please check if the contact has whatsapp id ")
            continue

    driver.quit()
