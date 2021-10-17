# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep

caps = {}
caps["deviceName"] = "SM-G960F"
caps["udid"] = "22a45084fd0d7ece"
caps["autoAcceptAlerts"] = True
caps["automationName"] = "UiAutomator2"
caps["appPackage"] = "com.android.settings"
caps["platformName"] = "Android"
caps["appActivity"] = "com.android.settings.Settings"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("https://dev-au-mel-1.headspin.io:7021/v0/a60f716ef7a04fb8b06a70201aa7ed86/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("Search settings")
el1.click()
sleep(5)

driver.quit()
