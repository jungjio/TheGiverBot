#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


#THING TO CHANGE IN THIS BOT
# MAKE IT FASTER
# CHANGE THE WHILE LOOPS TO CHECK FOR RESPONSE = 200
# GUI BUILDING

import urllib3
import re
import webbrowser
import requests
import sys
# import cookielib
import timeit
import time
import Tkinter as tk
import os
import json
import codecs
import datetime
import multiprocessing
import tkMessageBox as messagebox
from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
from time import sleep
from time import sleep
from random import randint
import Cookie
from bs4 import BeautifulSoup
from collections import OrderedDict



utf1 = '%E2%9C%93' #how to send request to atc
commit1 = 'add to cart'
_UTMC = '74692624'
_GAT = '1'
__UTMT = '1'
__UTMA= '74692624.1540672019.1492808721.1493098767.1493149663.16'
__UTMZ='74692624.1492808721.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
SUPREMECART = 'http:www.supremenewyork.com/shop/cart'
SITEKEY = "6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz"
CAPTANSWER ='03AIezHSZ6y7GJ2AYcb1z031JlZOwNb7JEzqMdP5m6rF7Ty3ZjB96g8T0eqtOqeUxCkmVjbGE2xkKJ5IFqrEh28RXT7KWpeoK4ywKcAtosSqL2fcCBOBbcMiG-TGERpoNxZ-2nTFzJrvRclQWyRkocQqJv5V-SDEj00kk4--yJmk2UMw4K2TchZqF01mly0-FV91dFKGlis4QUwWZEM3xZZ42hPM3WIbbEyrVHj7GLgMRhWhsVdaOq4Ro_mEZ-hdkdh7MSLlWQlBqlqmoZ2o_qSWRWDneqSnaPbfD8DUPIWcygWmqg13d3nszG7TQvlplzLsJWFt_sQis1WHo8OEsVgw6DmvXI99uADKnLbRYQ61e5S1JPxxOIV0eLfPHPLFSmL510O-qRTRjwvlEeWw2qsV_QodxLxIIRI7dRNgFkdmFJ_2_NBywKu3A'
SUPREME = 'http://www.supremenewyork.com'
SUPREMEJACKETS = 'http://www.supremenewyork.com/shop/all/jackets'
SUPREMESHIRTS = 'http://www.supremenewyork.com/shop/all/shirts'
SUPREMESWEATERS = 'http://www.supremenewyork.com/shop/all/tops_sweaters'
SUPREMESWEATSHIRT = 'http://www.supremenewyork.com/shop/all/sweatshirts'
SUPREMEPANTS = 'http://www.supremenewyork.com/shop/all/pants'
SUPREMESHORTS= 'http://www.supremenewyork.com/shop/all/shorts'
SUPREMEHATS = 'http://www.supremenewyork.com/shop/all/hats'
SUPREMEACCESSORIES = 'http://www.supremenewyork.com/shop/all/accessories'
SUPREMETSHIRTS = 'http://www.supremenewyork.com/shop/all/t-shirts'
SUPREMECHECKOUT = 'https://www.supremenewyork.com/checkout.json'
SUPREMESHOES = 'http://www.supremenewyork.com/shop/all/shoes'
SUPREMEBAGS = 'http://www.supremenewyork.com/shop/bags'
SUPREMEEMAIL = 'https://www.supremenewyork.com/store_credits/verify?email='




def Categories(wyw): #category
    if wyw == "jackets":
        supreme = SUPREMEJACKETS
        return supreme
    if wyw == "shirts":
        supreme = SUPREMESHIRTS
        return supreme
    if wyw == "tshirts":
        supreme = SUPREMETSHIRTS
        return supreme
    if wyw == "sweaters":
        supreme = SUPREMESWEATERS
        return supreme
    if wyw == "sweatshirts":
        supreme = SUPREMESWEATSHIRT
        return supreme
    if wyw == "pants":
        supreme = SUPREMEPANTS
        return supreme
    if wyw == "shorts":
        supreme = SUPREMESHORTS
        return supreme
    if wyw == "hats":
        supreme = SUPREMEHATS
        return supreme
    if wyw == "accessories":
        supreme = SUPREMEACCESSORIES
        return supreme
    if wyw == "shoes":
        supreme = SUPREMESHOES
        return supreme
    if wyw == 'bags':
        supreme = SUPREMEBAGS
        return supreme

########       Old Item Finder          #########################################################################################################################################################################


def keywordhunter(cop, keyword, colorway): #finds keyword and color returns the final link
    final1 = str("")
    final2 = str("") #you need this for keyword searcher

    name_box = cop.find_all('p', attrs={'p': 'href'})  #this is used for all hrefs
    for lins in cop.find_all('a', {'class':'name-link'}):   #this forloop searches for classlink to sift all hrefs
        if keyword in lins.text:                            #uses keyword to find item
            matcher = lins["href"]
            for lines in cop.find_all("a", {'class':'name-link'}):
                if colorway in lines.text:                  #uses color to find the color
                    if matcher in lines["href"]:            # matches text
                        print (matcher)


########       Item Finder         #########################################################################################################################################################################


def wordscrambler(cop, keyword, colorway):
    for lins in cop.find_all('a', {'class':'name-link'}):
        # if "http://www.supremenewyork.com" in lins["href"]:
        #     results = requests.get(lins["href"])
        #     print (results.content)
        #     if keyword in results.title:
        #         if colorway in results.title:
        #             return (lins["href"])
        # else:
            link = "http://www.supremenewyork.com" + str(lins["href"])
            #print (link)
            results = requests.get(link)
            #print (results.content)
            while 'shop' not in str(results.content):
                print ("waiting still")
                sleep(0.1)
                results = requests.get(link)
            results = BeautifulSoup(results.text, "html.parser")
            result = results.encode('ascii', "ignore")
            #print (result)
            if keyword in str(results.find("title")):       #& colorway in str(results.find("title"))
                if colorway in str(results.find("title")):
                    print (lins["href"])
                    return (lins["href"])


########       Session Id        #########################################################################################################################################################################


def get_session_id(csrftoken): #look for session id
        csrf = "csrf-token"
        csrftok = csrftoken.find("meta",{'name':csrf})["content"]
        return csrftok


########       Size Code         #########################################################################################################################################################################


def Sizefinder(target, size): #simplified s = size

    final1 = ""
    captcha_page = requests.get(target)

    while 'Supreme' not in str(captcha_page.content):
        print ("waiting still")
        sleep(0.1)
        print (str(captcha_page.content))
        captcha_page = requests.get(target)
    print ("Entered Size")
    print (size)

    soup = BeautifulSoup(captcha_page.content, "html.parser")
    for action in soup.find_all('select'):
        for actions in action.find_all('option'):
            print(actions)
            if size in actions:
                size1 = actions['value']
                return size1
    if size == "Small":
        size = "Medium"
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                print(actions)
                if size in actions:
                    size1 = actions['value']
                    return size1
    elif size == "Medium":
        size = "Large"
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                print(actions)
                if size in actions:
                    size1 = actions['value']
                    return size1
    elif size == "Large":
        size = "XLarge"
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                print(actions)
                if size in actions:
                    size1 = actions['value']
                    return size1
    if size == "XLarge":
        size = "Small"
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                print(actions)
                if size in actions:
                    size1 = actions['value']
                    return size1

########       Style Code         #########################################################################################################################################################################

def Stylecode(link): #style code s = style
    final1 = ""
    swag = ""
    captcha_page = requests.get(link)
    while 'Supreme' not in str(captcha_page.content):
        print ("waiting still")
        sleep(0.1)
        print (str(captcha_page.content))
        captcha_page = requests.get(link)

    soup = BeautifulSoup(captcha_page.content, "html.parser")

    return soup.find(id="st")["value"]


########      Last Cart Link         #########################################################################################################################################################################


def atclink1(link,size5, style1, size): #final link to add to cart and simplified
    atclink = requests.get(link)
    #print (atclink.content)

    while 'Supreme' not in str(atclink.content):
        print ("waiting still")
        sleep(0.1)
        #print (str(atclink.content))
        atclink = requests.get(link)

    swag = ""
    soup = BeautifulSoup(atclink.content, "html.parser")
    for action in soup.find_all('form'):
        swag = action['action']
    return SUPREME + swag


def quit():
        category = var.get()
        size = var1.get()
        keyword = keyword1.get()
        colorwave = colorwave1.get()
        fullname = fullname1.get()
        email = email1.get()
        tele = tele1.get()
        address = address2.get()

        adres1 = (SecAddress.get())
        address1 = str(adres1)

        zipcode = zipcode1.get()
        city = city1.get()
        state = state1.get()
        creditcardtype = var2.get()
        creditcard = creditcard1.get()
        creditmonth = creditmonth1.get()
        credityear = credityear1.get()
        creditsec = creditsec1.get()
        captcharesp = captcharesp1.get()
        open('supremesave', 'w').close()

        f = open('supremesave', 'r+')
        array = [category, keyword, colorwave, size, fullname, email, tele, address,address1, zipcode, city, state, creditcardtype,creditcard, creditmonth, creditmonth, credityear, creditsec]

        f.write(category + '\n')
        f.write(keyword + '\n')
        f.write(colorwave + '\n')
        f.write(size + '\n')
        f.write(fullname + '\n')
        f.write(email + '\n')
        f.write(tele + '\n')
        f.write(address + '\n')
        f.write(address1 + '\n')
        f.write(zipcode + '\n')
        f.write(city + '\n')
        f.write(state + '\n')
        f.write(creditcardtype + '\n')
        f.write(creditcard + '\n')
        f.write(creditmonth + '\n')
        f.write(credityear + '\n')
        f.write(creditsec + '\n')
        f.write(captcharesp + '\n')


        master.destroy()

def change_dropdown(*args):
        print( tkvar.get() )

def clear_text():
    captcharesp1.delete(0, 'end')

def cop():

    timer1 = timer.get()
    start = time.time()
    lastidcookie = str(int(time.time()))
    category = var.get()
    size = var1.get()
    keyword = keyword1.get()
    colorwave = colorwave1.get()
    fullname = fullname1.get()
    email = email1.get()
    tele = tele1.get()
    address = address2.get()
    adres1 = (SecAddress.get())
    address1 = str(adres1)
    zipcode = zipcode1.get()
    city = city1.get()
    state = state1.get()
    creditcardtype = var2.get()
    creditcard = creditcard1.get()
    creditmonth = creditmonth1.get()
    credityear = credityear1.get()
    creditsec = creditsec1.get()
    captcharesp = captcharesp1.get()

    if "" not in timer1:
        sleep(int(timer1))

    supreme = Categories(category)
    supreme = requests.get(supreme)

    while 'Supreme' not in str(supreme.content):
        print ("waiting still")
        sleep(0.1)
        supreme = requests.get(link)

    cop = BeautifulSoup(supreme.content, "html.parser")

    # link = cop.find_all("article")

    print ("Benchmark1: Item Finder")
    target =  wordscrambler(cop,keyword, colorwave) #look for things link
    try:
        if "http://www.supremenewyork.com/" not in target:
            target = "http://www.supremenewyork.com" + target
        print (target)
    except:
        print ("out of stock")

    print ("Benchmark2: Size Finder")
    sizearray = ['Small', 'Medium', 'Large', 'XLarge']#this is for size swap if ur size is out of stock only things with these sizes


########       Multiprocess Size and Style         #########################################################################################################################################################################


    try:
        style1 = Stylecode(target)
        size1 = Sizefinder(target,size)
    except:
        print("Style and Size are gone")




    print(" ")
    print("---------------       SIZE AND STYLE CODE       ---------------------------------------------------------------------------------------------------------")
    print(" ")
    print ("Style Code: ", str(style1))
    print ("Size Code: ", str(size1))
    print(" ")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" ")






    driver.switch_to_window(main_window)
    driver.get(target)

    try:
        select = Select(driver.find_element_by_id("s"))
        select.select_by_value(size1)
    except:
        print "size DNE"



    driver.find_element_by_css_selector("#add-remove-buttons > input").click()
    time.sleep(.75)
    driver.get("https://www.supremenewyork.com/checkout")


    #driver.add_cookie({'name':'address', 'value': addy, 'path': '/'})

    driver.find_element_by_id("order_billing_name").send_keys(fullname)
    driver.find_element_by_id("order_email").send_keys(email)
    driver.find_element_by_id("order_tel").send_keys(tele)
    driver.find_element_by_name("order[billing_address]").send_keys(address)
    driver.find_element_by_name("order[billing_address_2]").send_keys(address1)
    driver.find_element_by_id("order_billing_zip").send_keys(zipcode)
    driver.find_element_by_id("order_billing_city").send_keys(city)
    driver.find_element_by_id("order_billing_state").send_keys(state)

    driver.find_element_by_name("credit_card[nlb]").send_keys(creditcard)

    select = Select(driver.find_element_by_id("credit_card_month"))
    select.select_by_value(creditmonth)

    select = Select(driver.find_element_by_id("credit_card_year"))
    select.select_by_value(credityear)

    driver.find_element_by_name("credit_card[rvv]").send_keys(creditsec)




    driver.find_element_by_id("cnb").send_keys(creditcard)
    driver.find_element_by_name("credit_card[cnb]").send_keys(creditcard)
    driver.find_element_by_id("credit_card_month").send_keys(creditmonth)
    driver.find_element_by_name("credit_card[month]").send_keys(creditmonth)
    driver.find_element_by_id("credit_card_year").send_keys(credityear)
    driver.find_element_by_name("credit_card[year]").send_keys(credityear)
    driver.find_element_by_name("credit_card[rvv]").send_keys(creditsec)
    driver.find_element_by_id("credit_card_rvv").send_keys(creditsec)

    browser.find_element_by_id("order_terms").click()
    checkboxes = driver.find_elements_by_xpath('//*[@id="order_terms"]')
    checkboxes.click()

    element = driver.find_elements_by_xpath('//*[@id="order_terms"]')
    element.click();


    payment = driver.find_elements_by_xpath('//*[@id="pay"]/input')
    payment.click()





    browser.find_element_by_css_selector('#pay > input')




    return()





    end = time.time()

    elapsed = end - start
    print (elapsed)

if __name__ == '__main__':

    try:


        driver = webdriver.Chrome('/Users/'+ 'jiojung' +'/Downloads/chromedriver')
        driver.get('https://www.google.com/search?q=google.com+recaptcha+demo+google')
        first_result = ui.WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_class_name('rc'))
        first_link = first_result.find_element_by_tag_name('a')

        # Save the window opener (current window, do not mistaken with tab... not the same)
        main_window = driver.current_window_handle


        # Open the link in a new tab by sending key strokes on the elementd
        # Use: Keys.COMMAND + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
        first_link.send_keys(Keys.COMMAND + Keys.RETURN)

        # Switch tab to the new tab, which we will assume is the next one on the right
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)
        driver.get('https://www.google.com')

        # Put focus on current window which will, in fact, put focus on the current visible tab
        driver.switch_to_window(main_window)
        # driver.get('https://www.google.com/recaptcha/api2/demo')
        # do whatever you have to do on this page, we will just got to sleep for now
        sleep(2)

        # Close current tab
        # Put focus on current window which will be the window opener
        driver.switch_to_window(main_window)




        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = os.environ.get(name)
            if user:
                username = (user)

        f = open('supremesave', 'r+')

        category = f.readline()
        category = category.replace('\n', "")

        keyword = f.readline()
        keyword = keyword.replace('\n', "")

        colorwave = f.readline()
        colorwave = colorwave.replace('\n', "")

        size = f.readline()
        size = size.replace('\n', "")

        fullname= f.readline()
        fullname = fullname.replace('\n', "")

        email = f.readline()
        email = email.replace('\n', "")

        tele = f.readline()
        tele = tele.replace('\n', "")

        address = f.readline()
        address = address.replace('\n', "")

        address1 = f.readline()
        address1 = address1.replace('\n', "")

        zipcode = f.readline()
        zipcode = zipcode.replace('\n', "")

        city = f.readline()
        city = city.replace('\n', "")

        state = f.readline()
        state = state.replace('\n', "")

        creditcardtype = f.readline()
        creditcardtype = creditcardtype.replace('\n', "")

        creditcard = f.readline()
        creditcard = creditcard.replace('\n', "")

        creditmonth = f.readline()
        creditmonth = creditmonth.replace('\n', "")

        credityear = f.readline()
        credityear = credityear.replace('\n', "")

        creditsec = f.readline()
        creditsec = creditsec.replace('\n', "")

        captcharesp = f.readline()
        captcharesp = captcharesp.replace('\n', "")





####### FIRST COLUMN GUI ###########################################################################################
        master = tk.Tk()
        COLOR = "snow2"
        pad = 10
        master.configure(background=COLOR)
        master.geometry("325x600+30+30")
        master.title("The Supper Bot")
        tk.Label(master, text="Category", bg=COLOR).grid(row=0, sticky = "W", ipadx=pad)
        tk.Label(master, text="Keyword", bg=COLOR).grid(row=1, sticky = "W", ipadx=pad)
        tk.Label(master, text="Colorwave", bg=COLOR).grid(row=2, sticky = "W", ipadx=pad)
        tk.Label(master, text="Size", bg=COLOR).grid(row=3, sticky = "W", ipadx=pad)
        tk.Label(master, text="Full Name", bg=COLOR).grid(row=4,  sticky = "W", ipadx=pad)
        tk.Label(master, text="Email", bg=COLOR).grid(row=5, sticky = "W", ipadx=pad)
        tk.Label(master, text="Tele", bg=COLOR).grid(row=6, sticky = "W", ipadx=pad)
        tk.Label(master, text="Address", bg=COLOR).grid(row=7, sticky = "W", ipadx=pad)
        tk.Label(master, text="Address 1", bg=COLOR).grid(row=8, sticky = "W", ipadx=pad)
        tk.Label(master, text="Zipcode", bg=COLOR).grid(row=9, sticky = "W", ipadx=pad)
        tk.Label(master, text="City", bg=COLOR).grid(row=10, sticky = "W", ipadx=pad)
        tk.Label(master, text="State", bg=COLOR).grid(row=11, sticky = "W", ipadx=pad)
        tk.Label(master, text="Card Type ", bg=COLOR).grid(row=12, sticky = "W", ipadx=pad)
        tk.Label(master, text="Credit Card #", bg=COLOR).grid(row=14, sticky = "W", ipadx=pad)
        tk.Label(master, text="Credit Month", bg=COLOR).grid(row=15, sticky = "W", ipadx=pad)
        tk.Label(master, text="Credit Year", bg=COLOR).grid(row=16, sticky = "W", ipadx=pad)
        tk.Label(master, text="Credit SEC", bg=COLOR).grid(row=17, sticky = "W", ipadx=pad)
        tk.Label(master, text="Timer", bg=COLOR).grid(row=18, sticky = "W", ipadx=pad)
        tk.Label(master, text="Captcha Code", bg=COLOR).grid(row=20, sticky = "W", ipadx=pad)


######## FIRST COLUMN GUI ###########################################################################################


######## SECOND COLUMN GUI  ###########################################################################################

        var = tk.StringVar()

        category1 =tk.OptionMenu(master, var,"jackets", "shirts", "tshirts", "sweaters", "sweatshirts", "pants", "shorts", "hats", "accessories", "shoes", "bags")
        var.set(category)
        category1.config(width=20, bg=COLOR)
        category1.grid(row=0, column=1)

        keyword1 = tk.Entry(master)
        keyword1.insert(0,keyword)
        keyword1.config(highlightbackground= COLOR)

        colorwave1 = tk.Entry(master, textvariable=colorwave)
        colorwave1.insert(0,colorwave)
        colorwave1.config(highlightbackground= COLOR)

        var1 = tk.StringVar()
        size1 =tk.OptionMenu(master, var1,'' ,'S/M','L/XL','Small', 'Medium', 'Large', 'XLarge')
        var1.set(size)
        size1.config(width=20,bg=COLOR)
        size1.grid(row=3, column=1)

        fullname1 = tk.Entry(master, textvariable=fullname)
        fullname1.config(highlightbackground= COLOR)
        fullname1.insert(0,fullname)

        email1 = tk.Entry(master, textvariable=email)
        email1.config(highlightbackground= COLOR)
        email1.insert(0,email)

        tele1 = tk.Entry(master, textvariable=tele)
        tele1.config(highlightbackground= COLOR)
        tele1.insert(0,tele)

        address2 = tk.Entry(master, textvariable=address)
        address2.config(highlightbackground= COLOR)
        address2.insert(0,address)

        SecAddress = tk.Entry(master, textvariable=address1)
        SecAddress.config(highlightbackground= COLOR)
        SecAddress.insert(0,address1)

        zipcode1 = tk.Entry(master, textvariable=zipcode)
        zipcode1.config(highlightbackground= COLOR)
        zipcode1.insert(0,zipcode)

        city1 = tk.Entry(master, textvariable = city)
        city1.config(highlightbackground= COLOR)
        city1.insert(0,city)

        state1 = tk.Entry(master, textvariable = state)
        state1.config(highlightbackground= COLOR)
        state1.insert(0,state)

        var2 = tk.StringVar()
        creditcardtype3 =tk.OptionMenu(master, var2,'visa', 'american_express', 'mastercard')
        creditcardtype3.config(width=20,bg=COLOR)
        var2.set(creditcardtype)

        creditcard1 = tk.Entry(master, textvariable = creditcard)
        creditcard1.config(highlightbackground= COLOR)
        creditcard1.insert(0,creditcard)

        creditmonth1 = tk.Entry(master, textvariable = creditmonth)
        creditmonth1.config(highlightbackground= COLOR)
        creditmonth1.insert(0,creditmonth)

        credityear1 = tk.Entry(master, textvariable = credityear)
        credityear1.config(highlightbackground= COLOR)
        credityear1.insert(0,credityear)

        creditsec1 = tk.Entry(master, textvariable = creditsec)
        creditsec1.config(highlightbackground= COLOR)
        creditsec1.insert(0,creditsec)

        captcharesp1 = tk.Entry(master, textvariable = captcharesp)
        captcharesp1.config(highlightbackground= COLOR)
        captcharesp1.insert(0,captcharesp)

        end = tk.Button(master, text="Exit", highlightbackground = COLOR, command = quit)
        end.config(width = 10)

        buy = tk.Button(master, text="Buy", highlightbackground = COLOR, command = cop) # this is to cop, create the function
        buy.config(width = 10)

        timer = tk.Entry(master)
        timer.config(highlightbackground= COLOR)

        captchaclearnbutton = tk.Button(master, text="Clear Captcha",highlightbackground = COLOR, command=clear_text)
        captchaclearnbutton.config(width = 10)



        category1.grid(row=0, column=1)
        keyword1.grid(row=1, column=1)
        colorwave1.grid(row=2, column=1)
        size1.grid(row=3, column=1)
        fullname1.grid(row=4, column=1)
        email1.grid(row=5, column=1)
        tele1.grid(row=6, column=1)
        address2.grid(row=7, column=1)
        SecAddress.grid(row=8, column=1)
        zipcode1.grid(row=9, column=1)
        city1.grid(row=10, column=1)
        state1.grid(row=11, column=1)
        creditcardtype3.grid(row=12, column=1)
        creditcard1.grid(row=14, column=1)
        creditmonth1.grid(row=15, column=1)
        credityear1.grid(row=16, column=1)
        creditsec1.grid(row=17, column=1)
        timer.grid(row=18, column=1)
        captcharesp1.grid(row=20, column = 1)
        captchaclearnbutton.grid(row=21, column = 1)
        end.grid(row=22, column = 1)
        buy.grid(row=21, column = 0)


######## SECOND COLUMN GUI  ###########################################################################################


######## Main loop logic  ###########################################################################################
        # master.attributes("-topmost", True)
        master.lift()
        master.attributes('-topmost',True)
        master.after_idle(master.attributes,'-topmost',False)

        master.mainloop()

        category = var.get()
        size = var1.get()
        keyword = keyword1.get()
        colorwave = colorwave1.get()
        fullname = fullname1.get()
        email = email1.get()
        tele = tele1.get()
        address = address2.get()

        adres1 = (SecAddress.get())
        address1 = str(adres1)

        zipcode = zipcode1.get()
        city = city1.get()
        state = state1.get()
        creditcardtype = var2.get()
        creditcard = creditcard1.get()
        creditmonth = creditmonth1.get()
        credityear = credityear1.get()
        creditsec = creditsec1.get()
        open('supremesave', 'w').close()


        f = open('supremesave', 'r+')
        array = [category, keyword, colorwave, size, fullname, email, tele, address,address1, zipcode, city, state, creditcardtype,creditcard, creditmonth, creditmonth, credityear, creditsec]

        f.write(category + '\n')
        f.write(keyword + '\n')
        f.write(colorwave + '\n')
        f.write(size + '\n')
        f.write(fullname + '\n')
        f.write(email + '\n')
        f.write(tele + '\n')
        f.write(address + '\n')
        f.write(address1 + '\n')
        f.write(zipcode + '\n')
        f.write(city + '\n')
        f.write(state + '\n')
        f.write(creditcardtype + '\n')
        f.write(creditcard + '\n')
        f.write(creditmonth + '\n')
        f.write(credityear + '\n')
        f.write(creditsec + '\n')





######## Data Organization  #################################################################################################################################################################################################################################################################################


        #     # driver.find_element_by_css_('order_terms').click()
        #     #
        #     #
        #     #
        #     #
        #     #
        #     #
        #     # driver.find_element_by_name('order[terms]').click()
        #     # #driver.find_element_by_id("order_terms").click()
        #     # driver.find_element_by_id("order_terms").click()
        #     # swag =
        #     # swag.click()
        #     # driver.find_element_by_id("store_address").click()
        #     # driver.find_element_by_xpath("//*[@id='cart-cc']/fieldset/p[2]/label/div").click
        #     #
        #     #
        #t
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #     # post_data1get = response.post(SUPREMECHECKOUT, headers = headers1, params =d)
        #     # print "cunt"
        #     # #data= request.POST.get('data','')
        #     # print post_data1get.headers
        #     # #post_data1 = response.post(SUPREMECHECKOUT, data = payload1, headers = headers1, cookies = response.cookies)#checks out the item
        #     # print post_data1get.request.headers
        #     # print post_data1get.headers
        #     # print post_data1get.POST.get('data', '')
        #     #
        #     # print post_data1get.content
        #

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
          #you need this to throw the exception
