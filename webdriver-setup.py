import time
import selenium
from selenium import webdriver


def web_testing():

    # driver = webdriver.Chrome('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"' )
    s = r'C:\Users\customer\AppData\Local\Temp\Rar$EXa6940.47898\chromedriver.exe'
    driver = webdriver.Chrome(s)
    driver.get('http://www.google.com/xhtml');
    time.sleep(5)
    
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5) # Let the user actually see something!
    driver.quit()

if __name__ == "__main__":
    web_testing()
