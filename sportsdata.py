# importing the necessary libraries and packages
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

service = Service(executable_path="chromedriver.exe")
# let's initialize the driver
driver = webdriver.Chrome(service=service)

# the url for the target website
url = 'https://www.bbc.com/sport'
driver.get(url)
# navigating to the 'football' tab
football = driver.find_element(By.CSS_SELECTOR, "#product-navigation-menu > div.ssrcss-1h87eia-MenuListContainer.e14xdrat2 > ul > li:nth-child(2) > a > span")
time.sleep(2)
football.click()
# navigating to the 'top scorers' tab
top_scorers = driver.find_element(By.CSS_SELECTOR, "#header-content > div > nav > div.e19jy4800.ssrcss-19dj471-MenuContainer-SecondaryNavBarContainer.ebbwlb0 > div > div > ul > li:nth-child(6) > a > span")
top_scorers.click()
NameOfPlayer = []
GoalsScored = []
NameOfTeam = []
Assists = []
ShotAccuracy = []
names = driver.find_elements(By.XPATH,'//span[@class="gs-u-vh gs-u-display-inherit@l"]')
teams = driver.find_elements(By.XPATH,'//span[@class="gs-u-vh gs-u-display-inherit@m"]')
goal_analysis = driver.find_elements(By.XPATH,'//td[@class="gs-o-table__cell gs-o-table__cell--right"]')
accuracy_analysis = driver.find_elements(By.XPATH,'//td[@class="gs-o-table__cell gs-o-table__cell--right gs-u-display-none gs-u-display-table-cell@m"]')
for name in names:
    NameOfPlayer.append(name.text)
team_name = []
for team in teams:
    team_name.append(team.text)
for i in range(4,len(team_name)):
    NameOfTeam.append(team_name[i])
GoalAnalysis = []
for i in goal_analysis:
    GoalAnalysis.append(i.text)
# now let's extract data for goals scored
for g in range(0,len(GoalAnalysis),4):
    GoalsScored.append(GoalAnalysis[g])
# now let's extract assists
for a in range(1,len(GoalAnalysis),4):
    Assists.append(GoalAnalysis[a])

# now let's do the same for shot accuracy
AccuracyAnalysis = []
for k in accuracy_analysis:
    AccuracyAnalysis.append(k.text)

for s in range(2,len(AccuracyAnalysis),3):
    ShotAccuracy.append(AccuracyAnalysis[s])

df = pd.DataFrame({'Player':NameOfPlayer,'Team':NameOfTeam,'Goals':GoalsScored,'Assist':Assists,'Shot accuracy':ShotAccuracy})
df.to_csv('TopScorers.csv')



