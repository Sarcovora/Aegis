from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--start-maximized")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
option.add_experimental_option("excludeSwitches", ['enable-automation'])

browser = webdriver.Chrome(executable_path='./chromedriver.exe', options=option)
email = "your@emailaddress.com"
lastName = "Last Name"
firstName = "First Name"

# cyberpatriot form or robotics form (replace link with the correct one)
googleFormLink = "input form link here"
browser.get(googleFormLink)

# Use the following snippets to get elements by their class names
textboxes = browser.find_elements(By.CLASS_NAME, "quantumWizTextinputPaperinputInput")
radioNo = browser.find_elements(By.CLASS_NAME, "appsMaterialWizToggleRadiogroupOffRadio")
submitButton = browser.find_elements(By.CLASS_NAME, "appsMaterialWizButtonPaperbuttonContent")

textboxes[0].send_keys(email)
textboxes[1].send_keys(lastName)
textboxes[2].send_keys(firstName)

for i in range (len(radioNo)):
	radioNo[i].click()

submitButton[0].click()

#browser.close()
browser.quit()