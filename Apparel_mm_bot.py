from argparse import Action
from ast import Try
from cgi import print_directory
from dataclasses import replace
import email
from gettext import find
from lib2to3.pgen2.driver import Driver
from operator import concat, contains
from traceback import print_list
from unicodedata import name
from importlib.resources import path
from msilib.schema import File
from multiprocessing import Value
from re import I, search
import time
from tkinter.ttk import Style
from tokenize import Name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
from PIL import Image
from io import BytesIO
from os import listdir
from os.path import isfile, join
import pandas as pd
from win10toast import ToastNotifier
import requests


def get_profile_path(profile):
    FF_PROFILE_PATH = os.path.join(os.environ['APPDATA'],'Mozilla', 'Firefox', 'Profiles')

    try:
        profiles = os.listdir(FF_PROFILE_PATH)
    except WindowsError:
        print("Could not find profiles directory.")
        sys.exit(1)
    try:
        for folder in profiles:
            print(folder)
            if folder.endswith(profile):
                loc = folder
    except StopIteration:
        print("Firefox profile not found.")
        sys.exit(1)
    return os.path.join(FF_PROFILE_PATH, loc)

mime_types = "text/csv"
profile = webdriver.FirefoxProfile(get_profile_path('vvbb6a2w.default-release'))

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
Gecko_path = r"C:\Users\junai\OneDrive\Reporting\U2\gecko\geckodriver.exe"
driver = webdriver.Firefox(firefox_profile=profile ,executable_path= Gecko_path, options=options)
def ordering():
    appended_data = []
    wait = WebDriverWait(driver,20)
    url = 'https://atonce.nike.net/#/search'
    print(url)
    driver.get(url)
    try:
        Email = "estore@topsandbottomsusa.com"
        password = "TopBot.786#"
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"#okta-signin-username"))).click()
        driver.find_element(By.CSS_SELECTOR,"#okta-signin-username").send_keys(Keys.CONTROL+'a')
        driver.find_element(By.CSS_SELECTOR,"#okta-signin-username").send_keys(Email)

        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"#okta-signin-password"))).click()
        driver.find_element(By.CSS_SELECTOR,"#okta-signin-password").send_keys(Keys.CONTROL+'a')
        driver.find_element(By.CSS_SELECTOR,"#okta-signin-password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR,"#okta-signin-submit").click()
        time.sleep(30)
    except:
        print("No need to login again")
    url2 = "https://orders.nike.net/order-status/#/landing"
    driver.get(url2)
    time.sleep(10)
    from_date = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,'/html/body/div[7]/div/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div[2]/input[1]')))
    from_date.click()
    from_date.send_keys(Keys.CONTROL + "a")
    time.sleep(2)
    from_date.send_keys("12/08/2022")

    to_date = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,'/html/body/div[7]/div/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div[2]/input[2]')))
    time.sleep(1)
    to_date.click()
    to_date.send_keys(Keys.CONTROL + "a")
    time.sleep(2)
    to_date.send_keys("01/05/2023")
    time.sleep(2)
    cancel = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.CSS_SELECTOR,'button[class="btn-regular-darkgrey"]')))
    cancel.click()
    try:
        which_product_type = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.CSS_SELECTOR,'#selDIT_chzn > a:nth-child(1)')))
        which_product_type.click()
    except:
        print("trying different way")
        which_product_type = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,'/html/body/div[7]/div/div[2]/div[2]/div[2]/form/div[6]/div/a')))
        which_product_type.click()
    which_product_type.send_keys("Apparel",Keys.ENTER)
    time.sleep(1)
    what_type_of_order = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,'/html/body/div[7]/div/div[2]/div[2]/div[2]/form/div[7]/div[1]/div/a')))
    what_type_of_order.click()
    what_type_of_order.send_keys("Future",Keys.ENTER)
    time.sleep(1)
    all_order = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,'/html/body/div[7]/div/div[2]/div[2]/div[2]/form/div[8]/div/a')))
    all_order.click()
    all_order.send_keys("Rejected",Keys.ENTER)
    time.sleep(1)
    Search = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.CSS_SELECTOR,'button[id="advanced-search-submit-btn"]')))
    Search.click()
    time.sleep(3)
    for rejected_chart in range(1,50):
        time.sleep(5)
        try:
            print(rejected_chart)
            rejected_PO_locator = "/html/body/div[7]/div/div[1]/div[6]/table/tbody/tr[{}]/td[2]/div[1]/a".format(rejected_chart)
            rejected_po = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,rejected_PO_locator)))
            rejected_po.click()
        except:
            print("not clicked!")
            break
        time.sleep(2)
        i = 1
        while True:
            i=i+2
            if i >= 20:
                break
            else:
                try:
                    time.sleep(5)
                    name_locator = "/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[{}]/td[1]/div/div[1]/div[2]".format(i)
                    name = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,name_locator))).text
                    print(name)
                    image_locator = "/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[{}]/td[1]/div/div[1]/div[1]/img".format(i)
                    image = driver.find_element(By.XPATH,image_locator).get_attribute("src")
                    print(image)
                    requested_locator = '/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[{}]/td[1]/div/div[3]/div[2]/span[2]'.format(i)
                    request = WebDriverWait(driver,4).until(ec.presence_of_element_located((By.XPATH,requested_locator))).text
                    print(request)
                    confirmed_locator = '/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[{}]/td[1]/div/div[3]/div[2]/span[3]'.format(i)
                    confirmed  = WebDriverWait(driver,4).until(ec.presence_of_element_located((By.XPATH,confirmed_locator))).text
                    print(confirmed)
                    Rejected_locator='/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[{}]/td[1]/div/div[3]/div[2]/span[4]/span[2]'.format(i)
                    Rejected  = WebDriverWait(driver,4).until(ec.presence_of_element_located((By.XPATH,Rejected_locator))).text
                    print(Rejected)
                    po_number = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[7]/div/header/div/div[2]/div[2]/div[1]/div/div[2]"))).text
                    print(po_number)
                    order_number = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[7]/div/header/div/div[2]/div[2]/div[2]/div/div[2]"))).text
                    print(order_number)
                    product_data = pd.DataFrame({"image":[image],"PO Number":[po_number],"Order Number":[order_number],"Name":[name],"requested":[request],"Confirmed":[confirmed],"Rejected":[Rejected]})
                    appended_data.append(product_data)
                except:
                    print("PO data is scrapping")
        po_number = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[7]/div/header/div/div[2]/div[2]/div[1]/div/div[2]"))).text
        print(po_number)
        order_number = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[7]/div/header/div/div[2]/div[2]/div[2]/div/div[2]"))).text
        print(order_number)
        image = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[1]/td[1]/div[1]/div[1]/div[1]/img").get_attribute("src")
        print(image)
        name = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[1]/td[1]/div[1]/div[1]/div[2]"))).text
        print(name)
        request = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[1]/td[1]/div/div[3]/div[2]/span[2]"))).text
        print(request)
        confirmed = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[1]/td[1]/div/div[3]/div[2]/span[3]/span[2]"))).text
        print(confirmed)
        Rejected = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[7]/div/div[1]/div[5]/table/tbody/tr[1]/td[1]/div/div[3]/div[2]/span[4]/span[2]"))).text
        print(Rejected)
        product_data = pd.DataFrame({"image":[image],"PO Number":[po_number],"Order Number":[order_number],"Name":[name],"requested":[request],"Confirmed":[confirmed],"Rejected":[Rejected]})
        appended_data.append(product_data)
        result_button = driver.find_element(By.CSS_SELECTOR,'#nav-results > a')
        result_button.click()
    appended_data = pd.concat(appended_data)
    appended_data.to_csv("Apparel_mm.csv",index=False)
ordering()