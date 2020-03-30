import requests
import os
import sys
import logging
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/opt/google/chrome/chrome"    #chrome binary location specified here
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument('--window-size=1420,1080')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
service_log_path = "{}/chromedriver.log".format('/home/kriss')
#service_args = ['--verbose']
service_args = ['--enable-logging --v=1']
#print(service_log_path)

#logging module
myapp=sys.argv[0].split('.')[0]
#print(myapp)
#print(os.getcwd() + '/' + myapp + '.log')
logger = logging.getLogger(myapp)
hdlr = logging.FileHandler(os.getcwd() + '/' + myapp + '.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

print('Starting of the script ' + sys.argv[0])
logger.info('Starting of the script ' + sys.argv[0])


driver = webdriver.Chrome(options=options, executable_path=r'/usr/local/share/chromedriver', service_args=service_args,
       service_log_path=service_log_path)
driver.get('https://www.atg.party/')

#HTTP Response Code
r = requests.get("https://www.atg.party/")
logger.info('Status code after invoke the URL ' + str(r.status_code))
print('Status code after invoke the URL ' + str(r.status_code))

#Response Time
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")
response_time = domComplete - responseStart
print("Response Time: %s" % response_time)
logger.info("Response Time: %s" % response_time)

#Login process
element= driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/ul/li[2]/a")
element.click()
time.sleep(3)
email=driver.find_element_by_id("email")
email.send_keys("wiz_saurabh@rediffmail.com")
password=driver.find_element_by_id("password")
password.send_keys("Pass@123")
time.sleep(3)
button=driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button")
button.click()
time.sleep(3)

print("Navigating to Article Page: https://www.atg.party/article")
logger.info("Navigating to Article Page: https://www.atg.party/article")
driver.get("https://www.atg.party/article")
time.sleep(2)
#title=driver.title
#print(title)

#publishing Article
title=driver.find_element_by_id("title")
title.send_keys("Selenium Driven Title")
desc=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/div/form/div[2]/div/div[3]/div")
desc.send_keys(" Sample Description from Selenium - Python Script")
#print("Added Description")

image=driver.find_element_by_id("article_pic")
image.send_keys("/home/kriss/python_examples/download.png")
#print("Image Uploaded")

button=driver.find_element_by_id("featurebutton")
button.click()
time.sleep(2)
#title=driver.title
#print(title)

print("current URL: " + driver.current_url)
logger.info("current URL: " +  driver.current_url)
logger.info('End of the script' + sys.argv[0]+ " \n")

driver.quit()
