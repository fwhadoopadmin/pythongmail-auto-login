import time
import selenium
from selenium import webdriver
import getpass


SENDER = "simeonewere@gmail.com"
GMAIL_USER = "simeonewere@gmail.com"
GMAIL_PASSWORD = getpass.getpass('Insert your password:')
MESSAGE = 'LOGIN SUCCESSFUL'

MESSAGE = 'I will get back to you soon. \n Thanks'



#driver = webdriver.Chrome()
s = r'C:\Users\customer\AppData\Local\Temp\Rar$EXa6940.47898\chromedriver.exe'
driver = webdriver.Chrome(s)
url = "https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver.get(url)
# driver.get("https://www.google.com")

driver.find_element_by_id("identifierId").send_keys(GMAIL_USER)

# click nect button
driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(5)

# find passwd
# //*[@id="password"]/div[1]/div/div[1]/input

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(GMAIL_PASSWORD)
# time.sleep(5)

# click NEXT to login
# //*[@id="passwordNext"]/content/span

driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
time.sleep(10)



