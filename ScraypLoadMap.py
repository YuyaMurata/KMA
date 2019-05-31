import sys
import json
import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

import codecs

#IE11
ie_path = 'ie/IEDriverServer.exe'

# Selenium settings
driver = webdriver.Ie(executable_path=ie_path)

def login():
    # get a Top page
    driver.get('https://gg-komtrax.komatsu.co.jp/komtrax/web/POBSlogon.asp')

    # Certificate
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        print('accept fail')

    # Login
    driver.find_element_by_name('submit1').click()

def targetMachine(kisy, typ, kiban):
    #Main page
    driver.switch_to.frame("menu_frame")
    driver.execute_script("OnClickMachine()")
    driver.switch_to.default_content()

    #車両ID
    driver.switch_to.frame("work_frame")
    driver.find_element_by_name('Kind').send_keys(kisy)
    driver.find_element_by_name('Type').send_keys(typ)
    driver.find_element_by_name('Number').send_keys(kiban)
    driver.execute_script("OnClickCid()")

    #driver.find_element_by_name("pobs1_frame")
    try:
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'pobs1_frame')))
    except:
        print("not found")
    driver.switch_to.frame("pobs1_frame")
    driver.execute_script("OnClickFTP()")
    driver.switch_to.default_content()

def remoteDataAccess():
    #test
    print()

if __name__ == '__main__':
    login()

    targetMachine("PC200","10","450635")

    html = driver.page_source.encode('sjis')  # more sophisticated methods may be available
    # parse the response
    soup = BeautifulSoup(html, "lxml")
    print(soup.prettify())

#driver.close()
