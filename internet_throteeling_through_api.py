from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import os
import requests
desired_caps = {
    "lt:options": {
        "app":"lt://APP10160591891685101090430535",
        "build": "Goseetravel",
        "console": "False",
        "deviceName": "Galaxy S21 5G",
        "isRealMobile": True,
        "name": "Date Range Picker issue",
        "platform": "android",
        "platformName": "android",
        "platformVersion": "12",
        "video": True,
        "visual": True,
        "w3c": True,
    },
}
def scroll_to_element(driver, element):
    # Perform scroll until the element is visible
    driver.scroll_to(element)
def startingTest():
    try:
        if os.environ.get("LT_USERNAME") is None:
            # Enter LT username here if environment variables have not been added
            username = "ritamg"
        else:
            username = os.environ.get("LT_USERNAME")
        if os.environ.get("LT_ACCESS_KEY") is None:
            # Enter LT accesskey here if environment variables have not been added
            accesskey = "e4vXxk64hYOIkG7gwld5Fsb5LpmhI8wq6J0LQ2KC9LSgJHc1N5"
        else:
            accesskey = os.environ.get("LT_ACCESS_KEY")
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                    username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")
        #Turning on the internet througt api
        url = f"https://mobile-api.lambdatest.com/mobile-automation/api/v1/sessions/{driver.session_id}/update_network"
        headers = {
            "Authorization": "Basic ZGVlcGFuc2h1bGFtYmRhdGVzdDpmOHhyOGVWN2hwSkppeE82c2JWbVBhekFINEM4Vm9BVWhFQU5QamlrYXlMVFhObEpLcw==",
            "Content-Type": "application/json"
        }
        body = {
            "mode": "offline"
        }
        response = requests.post(url, headers=headers, json=body)
        print(response.status_code)
        #Performing actions in app
        colorElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/color")))
        colorElement.click()
        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.lambdatest.proverbial:id/Text")))
        textElement.click()
        toastElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/toast")))
        toastElement.click()
        notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/notification")))
        notification.click()
        geolocation = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/geoLocation")))
        geolocation.click()
        time.sleep(5)
        driver.back()
        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
        home.click()
        speedTest = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/speedTest")))
        speedTest.click()
        time.sleep(5)
        driver.back()
        browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/webview")))
        browser.click()
        print("Offline")
        url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/url")))
        url.send_keys("https://www.lambdatest.com")
        find = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/find")))
        find.click()
        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
        home.click()
        #Turning on the internet connection through api
        url = f"https://mobile-api.lambdatest.com/mobile-automation/api/v1/sessions/{driver.session_id}/update_network"
        body = {
            "mode": "online"
        }
        response = requests.post(url, headers=headers, json=body)
        colorElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/color")))
        colorElement.click()
        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.lambdatest.proverbial:id/Text")))
        textElement.click()
        toastElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/toast")))
        toastElement.click()
        notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/notification")))
        notification.click()
        geolocation = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/geoLocation")))
        geolocation.click()
        time.sleep(5)
        driver.back()
        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
        home.click()
        speedTest = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/speedTest")))
        speedTest.click()
        time.sleep(5)
        driver.back()
        browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/webview")))
        browser.click()
        print("Online")
        driver.quit()
    except Exception as e:
        print("Error: ", str(e))
    driver.quit()
startingTest()
