# -*- coding: utf-8 -*-
"""
KKU Internet Autologin

Apache License 2.0

พัฒนาโดย นาย วรรณพงษ์ ภัททิยไพบูลย์
สาขาวิทยาการคอมพิวเตอร์และสารสนเทศ
คณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์
มหาวิทยาลัยขอนแก่น วิทยาเขตหนองคาย

wannaphong@kkumail.com
"""
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
def is_connected()->bool:
 try:
  r = requests.get("https://www.google.com", allow_redirects=False)
  if r.status_code!=200:
      return False
  return True
 except:
  return False
def login(user:str,password:str)->bool:
    try:
        browser.get('https://login.kku.ac.th/')
        time.sleep(0)
        browser.find_element_by_id('username').send_keys(user)
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/form/div[4]/div/button").click()
        return True
    except Exception as E:
        print(E)
        return False

def login_cli(user:str,pas:str)->None:
    while True:
        if is_connected()==False:
            print("Not login!!!")
            login(user,pas)