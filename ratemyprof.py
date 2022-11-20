from googlesearch import search
from bs4 import BeautifulSoup
import requests


def profLookup(course):
    query = course + " rate my prof"
    websiteList = []
    for x in search(query, tld="com", num=3, stop=3, pause=2):
        websiteList.append(x)
    profDictonary = {}
    for x in range (len(websiteList)):
        profList = []
        url = websiteList[x]
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        soup = doc.find('div', class_="NameTitle__Name-dowf0z-0 cfjPUG")
        soup1 = doc.find('div', class_="RatingValue__NumRatings-qw8sqy-0 jMkisx")
        soup2 = doc.find('div', class_="TeacherFeedback__StyledTeacherFeedback-gzhlj7-0 cxVUGc")
        rating = (soup1.a.text)
        rating1 = int(rating.replace("ratings" , ""))
        lastName = doc.find('span', class_="NameTitle__LastNameWrapper-dowf0z-2 glXOHH").text
        firstName = soup.span.text
        fullName = firstName + " " + lastName
        professorRating = doc.find('div', class_="RatingValue__Numerator-qw8sqy-2 liyUjw").text
        professorRating1 = str(professorRating)
        professorTakeAgain = doc.find('div', class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs").text
        professorTakeAgain1 = str(professorTakeAgain)
        profList.append(professorRating1)
        profList.append(professorTakeAgain1)
        profList.append(rating1)
        profDictonary.update({fullName: profList})
    return profDictonary


print(profLookup("Computer Science 1026A/B"))
