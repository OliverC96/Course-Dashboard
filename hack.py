from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import requests
from bs4 import BeautifulSoup

year_1 = []
year_2 = []
year_3 = []
year_4 = []

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.westerncalendar.uwo.ca/Modules.cfm"
driver.get(url)

program = "Computer Science"  # For testing purposes
module = "Honours Specialization"  # For testing purposes
st = module + " in " + program
st = st.upper()

# Find the search bar and clicks on it
search_bar = driver.find_element(By.CSS_SELECTOR, "input[type='search'][class='form-control input-sm']")
search_bar.send_keys(program)

# Click on the module
driver.find_element(By.CLASS_NAME, "moduleDeptName").click()

# Finds the collapse interative thing to open the lists of courses:
driver.find_element(By.CSS_SELECTOR, "a[role='button'][data-toggle='collapse']").click()

# Click on the specific module on the collapse window 
dir_mod = driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div/a")
for s in dir_mod:
  print(s.text)
  if s.text == st:
    s.click()


# Click on the course:
# dir_course = driver.find_elements(By.XPATH, "//*[@id='AdmissionRequirements']/div/span/a")

# for s in dir_course:
#   print(s.text)
