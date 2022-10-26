# importing module
from email import message
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
  
driver = webdriver.Chrome(ChromeDriverManager().install())
  
# enter receiver user name
user = 'spikedoanz'
message_ = ("If you got this message then the script worked")
  
  
class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.message_url = 'https://www.instagram.com/direct/inbox/'
        self.bot = driver
        self.login()
        self.send(message)

    def login(self):
        self.bot.get(self.base_url)
  
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(10)
    
        # first pop-up
        self.bot.find_element(By.XPATH,
            '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/section/div/button').click()
        time.sleep(3)
        # second pop-up
        self.bot.find_element(By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(1)

        #click on the messaging button
        self.bot.find_element(By.XPATH,
            '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(3)

    def send(self,message):
            #click on create message button
            #//*[@id="mount_0_0_ea"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button
            self.bot.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(3)
            #type in name of user
            self.bot.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
            time.sleep(2)
            #select user
            self.bot.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button').click()
            time.sleep(2)
            #click next
            self.bot.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button').click()
            time.sleep(2)
            #enter text into box
            self.bot.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
            time.sleep(2)
            #click enter
            self.bot.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            #terminate browser
    

def init():
    bot_ = bot('tamagojin0000', 'qwe123QWE!@#', user, message_)
  
    # when our program ends it will show "done".
    message = input("please input a new message: ") 
    while(message != 'end'):
        bot.send(bot_, message = message)
        message = input("please input a new message: ") 
    input("DONE")
# calling the function

#format the message down here or something

init()