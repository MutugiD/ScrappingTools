import time
import urllib
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import config


# Define path to Web Driver
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# Define the components of request
method = 'GET'
url = config.url
client_code = config.account_id + '@AMER.OAUTHAP'
account_id =  xxxxxxxxx
payload = {'response_type':'code', 'redirect_uri':config.url, 'client_id':client_code}

# Define Payload, MAKE SURE TO HAVE THE CORRECT REDIRECT URI
p = requests.Request(method, url, params=payload).prepare()
myurl = p.url
browser.visit(myurl)
payload = {'username': 'username',
           'password': 'password'}


# Fill Out the Form
username = browser.find_by_id("username").first.fill(payload['username'])
password = browser.find_by_id("password").first.fill(payload['password'])
submit   = browser.find_by_id("accept").first.click()
time.sleep(1)


# Get the Text Message Box
browser.find_by_text('Can\'t get the text message?').first.click()

# Get the Answer Box
browser.find_by_value("Answer a security question").first.click()

# Answer the Security Questions.
if browser.is_text_present('In what city was your high school?'):
    browser.find_by_id('secretquestion').first.fill('highschool')

elif browser.is_text_present('In what city was your father born?'):
    browser.find_by_id('secretquestion').first.fill('cityfather')

elif browser.is_text_present('In what city were you born?'):
    browser.find_by_id('secretquestion').first.fill('cityborn')

elif browser.is_text_present('What was the name of your junior high school?'):
    browser.find_by_id('secretquestion').first.fill('schoolname')

# Submit results
browser.find_by_id('accept').first.click()

# Sleep and click Accept Terms.
time.sleep(1)
browser.find_by_id('accept').first.click()

new_url = browser.url
parse_url = urllib.parse.unquote(new_url.split('code=')[1])