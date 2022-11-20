from googlesearch import search
from bs4 import BeautifulSoup
import requests
def profLookup(course):
    query = course + "rate my prof"
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
        #soup1 = doc.find('a', href_="#ratingsList")
        #soup1 = doc.find('div', class_="FeedbackItem__StyledFeedbackItem-uof32n-0 dTFbKx")
        #print(soup1)
        lastName = doc.find('span', class_="NameTitle__LastNameWrapper-dowf0z-2 glXOHH").text
        firstName = soup.span.text
        fullName = firstName + " " + lastName
        professorRating = doc.find('div', class_="RatingValue__Numerator-qw8sqy-2 liyUjw").text
        professorRating1 = str(professorRating)
        professorTakeAgain = doc.find('div', class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs").text
        professorTakeAgain1 = str(professorTakeAgain)
        profList.append(professorRating1)
        profList.append(professorTakeAgain1)
        profDictonary.update({fullName: profList})
        #professorDifficulty = doc.find('div', class_="FeedbackItem__StyledFeedbackItem-uof32n-0 dTFbKx").text
        #print(professorDifficulty)
    #<div class="FeedbackItem__StyledFeedbackItem-uof32n-0 dTFbKx">
    return profDictonary #[rating, would take again or not, difficulty]
