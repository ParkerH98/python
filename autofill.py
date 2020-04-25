import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

fileName = '/Users/Parker/Desktop/test.txt'

with open(fileName) as file:
    data = file.read().replace('\n', 'j')

lines = data.split('j')

firstName = lines[0]
middleName = lines[1]
lastName = lines[2]
dob = lines[3]
state = lines[4]
heightFt = lines[5]
heightIn = lines[6]
weight = lines[7]
eyeColor = lines[8]
hairColor = lines[9]
gender = lines[10]
address = lines[11]
city = lines[12]
zip = lines[13]

firstName = firstName[11:]
middleName = middleName[12:]
lastName = lastName[10:]
dob = dob[14:]
state = state[6:]
heightFt = heightFt[12:]
heightIn = heightIn[14:]
weight = weight[7:]
eyeColor = eyeColor[10:]
hairColor = hairColor[11:]
gender = gender[7:]
address = address[8:]
city = city[5:]
zip = zip[4:]

driver = webdriver.Chrome('/Users/Parker/chromedriver')

url = 'https://www.idtop.ph/order/'
driver.get(url)

emailBox = driver.find_element_by_name('name')
emailBox.send_keys('thefamilycalender18230@gmail.com')

passwordBox = driver.find_element_by_name('pwd')
passwordBox.send_keys('Ph4058220384' + Keys.TAB)

time.sleep(5)

passwordBox = driver.find_element_by_name('yzm')
passwordBox.send_keys('\n')

time.sleep(5)

actions = ActionChains(driver)
actions.send_keys(Keys.TAB * 20)
actions.perform()

driver.switch_to.active_element.send_keys(firstName + Keys.TAB)
driver.switch_to.active_element.send_keys(middleName + Keys.TAB)
driver.switch_to.active_element.send_keys(lastName + Keys.TAB)
driver.switch_to.active_element.send_keys(dob + Keys.TAB)
driver.switch_to.active_element.send_keys(state + Keys.TAB)
driver.switch_to.active_element.send_keys(heightFt + Keys.TAB)
driver.switch_to.active_element.send_keys(heightIn + Keys.TAB)
driver.switch_to.active_element.send_keys(weight + Keys.TAB)
driver.switch_to.active_element.send_keys(eyeColor + Keys.TAB)
driver.switch_to.active_element.send_keys(hairColor + Keys.TAB)
driver.switch_to.active_element.send_keys(gender + Keys.TAB)
driver.switch_to.active_element.send_keys(address + Keys.TAB)
driver.switch_to.active_element.send_keys(city + Keys.TAB)
driver.switch_to.active_element.send_keys(zip + Keys.TAB * 3)
