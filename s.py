#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:00:37 2017

@author: joshjung
"""
import urllib2
import re
import webbrowser
import requests
import sys
import cookielib
import timeit
import time
import Tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from lxml import html
from bs4 import BeautifulSoup
from urlparse import urlparse
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
SUPREMECHECKOUT = 'https://www.supremenewyork.com/checkout.js'
SUPREMESHOES = 'http://www.supremenewyork.com/shop/all/shoes'





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

def keywordhunter(cop, keyword, colorway): #finds keyword and color returns the final link
    final1 = str("")
    final2 = str("") #you need this for keyword searcher
    #link = cop.find_all("article")
    name_box = cop.find_all('p', attrs={'p': 'href'})
    for links in cop.find_all("h1"): # what the thingy
        if keyword in links.text:
            final1 = final1 + str(links)

    for links in cop.find_all("p"): # colour
        if colorwave in links.text:
            final2 = final2 + str(links)


    final1 = re.sub('<h1><a class="name-link" href="', " ", final1)
    final1 = re.sub('</a></h1>', " ", final1)
    final1 = re.sub(keyword, " ", final1)
    final1 = re.sub('>', " ", final1)
    final1 = re.sub('"', " ", final1)

    final2 = re.sub('<p><a class="name-link" href="', " ", final2)
    final2 = re.sub('</a></p>', " ", final2)
    final2 = re.sub('>', " ", final2)
    final2 = re.sub('"', " ", final2)
    fin1 = final1.split()
    fin2 = final2.split()


    fin3 = set(fin1).intersection(fin2)
    sfin3 = repr(fin3)
    sfin3 = re.sub('set', "", sfin3)
    sfin3 = sfin3.replace("[", "")
    sfin3 = sfin3.replace("]", "")
    sfin3 = sfin3.replace(")", "")
    sfin3 = sfin3.replace("(", "")
    sfin3 = sfin3.replace("'", "")
    return SUPREME + sfin3
def get_session_id(csrftoken): #look for session id
        csrf = "csrf-token"
        for link in csrftoken.find_all("meta"): # what the thingyl #change to meta content
             if csrf in str(link): #grab csrf token lmao
                 gotcha = str(link)
        csrf = gotcha
        gotcha = re.sub('<meta content="', "", gotcha)
        gotcha = re.sub('" name="csrf-token"/>', "", gotcha)

        return gotcha

def Sizefinder(link, size): #simplified
    final1 = ""
    captcha_page = requests.get(link)
    soup = BeautifulSoup(captcha_page.content)
    if size in "":
        return soup.find("input",{"name":"size"})["value"]
    else:
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                if size in actions:
                    return actions['value']


def Stylecode(link): #style code
    final1 = ""
    swag = ""
    captcha_page = requests.get(link)
    soup = BeautifulSoup(captcha_page.content)
    return soup.find("input",{"name":"style"})["value"]


def atclink1(link,size5, style1, size): #final link to add to cart and simplified
    atclink = requests.get(link)
    swag = ""
    soup = BeautifulSoup(atclink.content, "html.parser")
    for action in soup.find_all('form'):
        swag = action['action']
    return SUPREME + swag
def quit():
    global root
    root.quit()
def change_dropdown(*args):
        print( tkvar.get() )


if __name__ == '__main__':
    #copy link from UK version lol we scheming
    try:


#        category = raw_input("Category?(all lower case please):") #what you want
#        keyword = raw_input("You need a UNIQUE keyword for it to work Properly, something the other items names do not have keyword? (captialize first letter in each word) :")
#        colorwave = raw_input("color? (captialize first letter in each word) :")
#        size = raw_input("size? small -> xlarge:")
        category = ""
        keyword = ""
        colorwave = ""
        size = ""
        fullname= ""
        email = ""
        tele = ""
        address = ""
        address1 = ""
        zipcode = ""
        city = ""
        state = ""
        creditcardtype = ""
        creditcard = ""
        creditmonth = ""
        credityear = ""
        creditsec = ""


        master = tk.Tk()
        master.geometry("400x800+30+30")
        master.title("The Giver Bot")
        tk.Label(master, text="________category________").grid(row=0)
        tk.Label(master, text="keyword(First letter caps)").grid(row=1)
        tk.Label(master, text="colorwave(First letter caps)").grid(row=2)
        tk.Label(master, text="size(First letter caps)").grid(row=3)
        tk.Label(master, text="________Full name__________").grid(row=4)
        tk.Label(master, text="email").grid(row=5)
        tk.Label(master, text="tele").grid(row=6)
        tk.Label(master, text="address").grid(row=7)
        tk.Label(master, text="address1").grid(row=8)
        tk.Label(master, text="zipcode").grid(row=9)
        tk.Label(master, text="city").grid(row=10)
        tk.Label(master, text="state").grid(row=11)
        tk.Label(master, text="Credit card type ").grid(row=12)
        tk.Label(master, text="(Creditcard num)").grid(row=14)
        tk.Label(master, text="Credit month").grid(row=15)
        tk.Label(master, text="Credit year").grid(row=16)
        tk.Label(master, text="Credit SEC").grid(row=17)


        # category1 = tk.Listbox(master)
        # category1.pack()
        #
        # for item in ["jackets", "shirts", "tshirts", "sweaters", "sweatshirts", "pants", "shorts", "hats", "accessories", "shoes"]:
        #     category1.insert("end", item)

        var = tk.StringVar()
        category1 =tk.OptionMenu(master, var,"jackets", "shirts", "tshirts", "sweaters", "sweatshirts", "pants", "shorts", "hats", "accessories", "shoes")
        category1.config(width=10)
        category1.grid(row=0, column=1)



        keyword1 = tk.Entry(master, textvariable=keyword)
        colorwave1 = tk.Entry(master, textvariable=colorwave)



        var1 = tk.StringVar()
        size1 =tk.OptionMenu(master, var1,'Small', 'Medium', 'Large', 'XLarge')
        size1.config(width=8)
        size1.grid(row=3, column=1)



        fullname1 = tk.Entry(master, textvariable=fullname)
        email1 = tk.Entry(master, textvariable=email)
        tele1 = tk.Entry(master, textvariable=tele)
        address2 = tk.Entry(master, textvariable=address)
        SecAddress = tk.Entry(master, textvariable=address1)
        zipcode1 = tk.Entry(master, textvariable=zipcode)
        city1 = tk.Entry(master, textvariable = city)
        state1 = tk.Entry(master, textvariable = state)

        var2 = tk.StringVar()
        creditcardtype3 =tk.OptionMenu(master, var2,'visa', 'american_express', 'mastercard')
        creditcardtype3.config(width=8)

        creditcard1 = tk.Entry(master, textvariable = creditcard)
        creditmonth1 = tk.Entry(master, textvariable = creditmonth)
        credityear1 = tk.Entry(master, textvariable = credityear)
        creditsec1 = tk.Entry(master, textvariable = creditsec)

        print fullname1.get()

        end = tk.Button(master, text="Exit and cop", command=master.quit)
        end.pack()


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
        end.grid(row=18, column = 1)


        master.mainloop()

        category = var.get()
        size = var1.get()
        creditcardtype = var2.get()


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
        creditcard = creditcard1.get()
        creditmonth = creditmonth1.get()
        credityear = credityear1.get()
        creditsec = creditsec1.get()



        fullname = fullname.replace(" ","+" )
        print fullname
        address = address.replace(" ","+" )
        print address
        address1 = address1.replace(" ","+" )
        print address1
        city = city.replace(" ","+" )
        print city
        state = state.replace(" ","+" )
        print state
        email = email.replace("@","%40")
        print email
        addy = fullname + '%7C' + address + '%7C' + address1 + '%7C' + city + '%7C' + state + '%7C' + zipcode + '%7C' + 'USA' + '%7C' + email + '%7C' + tele
        print addy


        # Joshua+Jio%7C2+Buswell+St%7CApt+4%7CBoston%7CMA%7C02215%7CUSA%7Cjungjio%40yahoo.com%7C3106166650


        supreme = Categories(category)
        print supreme
        supreme = requests.get(supreme)
        cop = BeautifulSoup(supreme.content, "html.parser")
        link = cop.find_all("article")
        target =  keywordhunter(cop,keyword, colorwave) #look for things link

        print target
        size1 = Sizefinder(target,size) #look for things size finder
        print size1
        style1 = Stylecode(target)
        print style1
        destroy= requests.Session()
        destroyer = destroy.get(target) #starts the session
        csrftoken = BeautifulSoup(destroyer.content, "html.parser") #what he said ^
        token = get_session_id(csrftoken)
        print token
        #if size in "SmallMediumLargeXLarge":
        #atclink = atclink(target, size1,style1, size)
        #if size in "678910111213":
        #    atclink = atclink1(target, size1, style1, size)#for sneaker sizes
        destroy.cookies.get_dict()

        atclink = atclink1(target, size1,style1, size)

        print atclink
        {}
        headers1 = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
        data1 = {'utf8': '%E2%9C%93',
                   'style': style1, 'size': size1,
                   'commit':commit1,
                   }
        d1 = OrderedDict([('utf8', '%E2%9C%93'),
                        ('style', style1),
                        ('size', size1),
                        ('commit',commit1)])

        #X-CSRF-Token': token
        payload = {'type': 'submit', 'name': 'commit', 'value': 'add to cart', 'X-CSRF-Token': token}

        d = OrderedDict([('utf8', utf1),
        ('authenticity_token', token),
        ('order[billing_name', fullname),
        ('order[email]', email),
        ('order[tel]', tele),
        ('order[billing_address]', address),
        ('order[billing_address_2]', address1),
        ('order[billing_zip]', zipcode),
        ('order[billing_city]', city,),
        ('order[billing_state]', state),
        ('order[billing_country]', 'USA'),
        ('same_as_billing_address','1'),
        ('store_credit_id' , ''), #this is blank
        ('store_address', '1',),    #this is 1
        ('credit_card[type]',creditcardtype),
        ('credit_card[nlb]', creditcard),
        ('credit_card[month]',"03"),
        ('credit_card[year]',credityear),
        ('credit_card[rvv]',creditsec),
        ('order[terms]' ,'0'),
        ('order[terms]', '1') #delete ]) for captcha, //check box for terms
        ])

        #driver.findElement(By.name("userName")).sendKeys ("tutorial");
        cookies1 = {'_utmc' : _UTMC, '_gat' : _GAT, '__utmt': __UTMT }
        with requests.Session() as response:
            cookie = response.cookies.get_dict()
            {}
            get_data = response.get(atclink, data = d1)
            post_data = response.post(atclink, data=d1, headers = headers1)
            cookies1 = response.cookies

            for c in cookies1:
                if 'cart' in c.name:
                    cart = {'name':'cart', 'value': c.value,
                    'path': '/'}
                if '_supreme' in c.name:
                    sup_sesh = {'name':'_supreme_sess', 'value': c.value,
                    'path': '/'}
            print cart
            print sup_sesh
            addy1 = {'name' : 'address',
            'value': addy }




            driver = webdriver.Chrome('/Users/joshjung/Downloads/chromedriver')

            driver.get("http://www.supremenewyork.com/shop/cart")
            driver.add_cookie(sup_sesh)
            driver.add_cookie(cart)
            driver.add_cookie(addy1)

            driver.refresh()
            driver.refresh()

            link = driver.find_element_by_css_selector("a[href='https://www.supremenewyork.com/checkout']")
            link.click()
            driver.find_element_by_name("credit_card[type]").send_keys("Mastercard")
            driver.find_element_by_id("cnb").send_keys(creditcard)
            driver.find_element_by_id("credit_card_month").send_keys(creditmonth)
            driver.find_element_by_id("credit_card_year").send_keys(credityear)
            driver.find_element_by_id("vval").send_keys(creditsec)






            #
            # driver.find_element_by_css_('order_terms').click()
            #
            #
            #
            #
            #
            #
            # driver.find_element_by_name('order[terms]').click()
            # #driver.find_element_by_id("order_terms").click()
            # driver.find_element_by_id("order_terms").click()
            # swag =
            # swag.click()
            # driver.find_element_by_id("store_address").click()
            # driver.find_element_by_xpath("//*[@id='cart-cc']/fieldset/p[2]/label/div").click
            #
            #











            # post_data1get = response.post(SUPREMECHECKOUT, headers = headers1, params =d)
            # print "cunt"
            # #data= request.POST.get('data','')
            # print post_data1get.headers
            # #post_data1 = response.post(SUPREMECHECKOUT, data = payload1, headers = headers1, cookies = response.cookies)#checks out the item
            # print post_data1get.request.headers
            # print post_data1get.headers
            # print post_data1get.POST.get('data', '')
            #
            # print post_data1get.content


    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
          #you need this to throw the exception
