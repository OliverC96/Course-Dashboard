from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def getProfessor(courseName):
    dictonary = {}
    for x in range (1, 4):
        list = []
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://google.ca")
        link = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        link.send_keys(courseName + " rate my prof")
        link.send_keys(Keys.ENTER)
        link1 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[{}]/div/div/div[1]/div/a/h3'.format(x))
        link1.click()
        link = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/button')
        link.click()
        professorRating = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.cCBygY > div.TeacherRatingsPage__TeacherBlock-sc-1gyr13u-1.jMpSNb > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(1) > div.RatingValue__AvgRating-qw8sqy-1.gIgExh > div > div.RatingValue__Numerator-qw8sqy-2.liyUjw').text
        professorDifficulty = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.cCBygY > div.TeacherRatingsPage__TeacherBlock-sc-1gyr13u-1.jMpSNb > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div.TeacherFeedback__StyledTeacherFeedback-gzhlj7-0.cxVUGc > div:nth-child(2) > div.FeedbackItem__FeedbackNumber-uof32n-1.kkESWs').text
        professorName = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.cCBygY > div.TeacherRatingsPage__TeacherBlock-sc-1gyr13u-1.jMpSNb > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(2) > div.NameTitle__Name-dowf0z-0.cfjPUG').text
        professorRating1 = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.cCBygY > div.TeacherRatingsPage__TeacherBlock-sc-1gyr13u-1.jMpSNb > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(1) > div.RatingValue__NumRatings-qw8sqy-0.jMkisx > div > a').text
        strName = str(professorName)
        strRating = str(professorRating)
        strRating1 = str(professorRating1)
        strDifficulty = str(professorDifficulty)
        list.append(strRating)
        list.append(strRating1)
        list.append(strDifficulty)
        dictonary.update({strName : list})
    return dictonary
getProfessor("cs 1027")
print(dictonary)
