## IMPORT MODULES DON'T MESS WITH THIS PLEASE!!!!
import os
import webbrowser
import sys
from time import sleep
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import simpledialog
import getpass
import asyncio

ROOT = tk.Tk()

ROOT.withdraw()
    
## webpage viewer 2.4

## Description: Combining all your favourite search engines into one, simple, easy-to-use tool. Set your default search engine,
## and search any query you like, or open up a website using prefixes: 'https', 'www'. You can even check your search history,
## or even re-create your webpage using text in python! You even have the option to input your querys into GUI or console!
## What's great is that it is open source!

## release notes: preview of website didn't really work this time, so it was removed (webpage-viewer browser will come out soon).
## Instead, we made the default search engine ask if you want to set it as default, or if you don't. Also, we added in a new
## search engine - Collins Dictionary

## author: jaskaran (owner of https://jaskaranpython.glitch.me)

## license: 100% Open Source
username = getpass.getuser()

print("\n")
print("Hello, "+username+", welcome to webpage viewer beta, a project by jaskaran\n")
sleep(1)

print("Searching for default settings file...")
sleep(1)



## Search engine file

try:

    with open("C://Users/"+username+"/AppData/webpage-viewer-settings.txt") as f:
        print("Found default settings file (C://Users/"+username+"/AppData/webpage-viewer-settings.txt)")
        print("Reading contents...")
        sleep(0.5)
        xd = open("C://Users/"+username+"/AppData/webpage-viewer-settings.txt")
        s = xd.read()
        print("\nYour default search engine is", s, "\n")
        xd.close()
except FileNotFoundError:
     print("\nNo search engine file found, would you like to create one now? (recommended)\n")
     oui = input("> ")
     if oui == "yes":
         sleep(0.5)
         print("What is your default search engine? (Google, Bing, Yahoo, DuckDuckGo, Ecosia, Wikipedia, Baidu, Yandex, Ask, Dictionary, Webcrawler)")
         searchengine = input("> ")
         file = open("C://Users/"+username+"/AppData/webpage-viewer-settings.txt", "w")
         file.write(str(searchengine))
         file.close()
     elif oui == "no":
         print("What would you like to set your temporary search engine to be? (Google, Bing, Yahoo, DuckDuckGo, Ecosia, Wikipedia, Baidu, Dictionary, Yandex, Ask, Webcrawler)")
         searchengine = input("> ")
     else:
         print("Error occured (unknown response). Please restart the program immediately!")
     
## GUI Settings file
try:
    with open("C://Users/"+username+"/AppData/webpage-viewer-settings-gui.txt") as f:
        print("Found default settings file (C://Users/"+username+"/AppData/webpage-viewer-settings-gui.txt)")
        print("Reading contents...")
        sleep(0.5)
        xd = open("C://Users/"+username+"/AppData/webpage-viewer-settings-gui.txt")
        s = xd.read()
        print("\nYou are currently using", s, "\n")
        xd.close()
except FileNotFoundError:
     print("\nNo input file found, creating one now...\n")
     sleep(0.5)
     print("How would you like your input to display? (GUI, Console)")
     searchengine = input("> ")
     ttt = open("C://Users/"+username+"/AppData/webpage-viewer-settings-gui.txt", "w")
     ttt.write(str(searchengine))
     ttt.close()


print("\njaskaran's webpage-viewer 2.4")

suii = open("C://Users/"+username+"/AppData/webpage-viewer-settings-gui.txt")
mm = suii.read()

if mm == "gui" or "GUI":
    search = simpledialog.askstring(title="Search",
                                  prompt="Search for: (https/www for website, anything else for search query):")

elif mm == "console" or "Console":
    search = str(input("> "))

## Opening Files
with open("C://Users/"+username+"/AppData/webpage-viewer-search-history.txt",'a+') as fileobj:
    fileobj.write("\n"+str(search))
    fileobj.close()

if oui == "yes":
    tree = open("C://Users/"+username+"/AppData/webpage-viewer-settings.txt")
    file = tree.read()
asd = search[:5]
qwe = search[:3]
wee = open("C://Users/"+username+"/AppData/webpage-viewer-settings-recreate.txt")
nope = wee.read()

if oui == "no":
    file = searchengine


if search == "searchHistory":
    a_file = open("C://Users/"+username+"/AppData/webpage-viewer-search-history.txt")
    file_contents = a_file.read()
    print(file_contents)

elif search == "search history":
    a_file = open("C://Users/"+username+"/AppData/webpage-viewer-search-history.txt")
    file_contents = a_file.read()
    print(file_contents)
    
## Opening Websites   
elif str(asd) == "https":
    url = search
 

elif str(qwe) == "www":
    url = search
 
## Opening search engines    
elif file == "Google" or file == "google":
    url = "https://www.google.com/search?q="+str(search)
     
    
        
    sleep(1)


                

elif file == "Dictionary" or file == "dictionary":
    url = "https://www.collinsdictionary.com/dictionary/english/"+str(search)
    
    sleep(1)
    
    
elif file == "Bing" or file == "bing":
    url = "https://www.bing.com/search?q="+str(search)
        

        
    sleep(1)

                     
        
elif file == "Yahoo" or file == "yahoo":
    url = "https://uk.search.yahoo.com/search?p="+search
        

        
    sleep(1)

                    
        
elif file == "DuckDuckGo" or file == "duckduckgo":
    url = "https://duckduckgo.com/?q="+search
        

    sleep(1)

                        
        
elif file == "Ecosia" or file == "ecosia":
    url = "https://www.ecosia.org/search?method=index&q="+search
        
        
    sleep(1)

                    
        
elif file == "Baidu" or file == "baidu":
    url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd="+search
        

        
    sleep(1)

                    
        
elif file == "Yandex" or file == "yandex":
    url = "https://yandex.ru/search/?lr=21134&text="+search
        

        
    sleep(1)

                    
        
elif file == "Ask" or file == "ask":
    url = "https://www.ask.com/web?q="+search
        

        
    sleep(1)

                        
        
elif file == "Wikipedia" or file == "wikipedia":
    url = "https://en.wikipedia.org/wiki/"+search

        
    sleep(1)
                    
        
elif file == "Webcrawler" or file == "webcrawler":
    url = "https://www.webcrawler.com/serp?q="+search
        

        
    sleep(1)

                
        
else:
    print("Invalid: Please type a correct search engine. Replace your current search engine at (C:\\Users\YourUsername\webpage-viewer-settings.txt)")
    sleep(1)
        

get_url= webbrowser.open(url)



