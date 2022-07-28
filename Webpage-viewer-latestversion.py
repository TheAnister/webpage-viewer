## IMPORT MODULES DON'T MESS WITH THIS PLEASE!!!!
import os
import webbrowser
import sys
from time import sleep
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import simpledialog


ROOT = tk.Tk()

ROOT.withdraw()
    
## webpage viewer 2.0

## Description: Combining all your favourite search engines into one, simple, easy-to-use tool. Set your default search engine,
## and search any query you like, or open up a website using prefixes: 'https', 'www'. You can even check your search history,
## or even re-create your webpage using text in python! You even have the option to input your querys into GUI or console!
## What's great is that it is open source!

## release notes: now has a default settings for either console-based input or gui-based input

## author: jaskaran (owner of https://jaskaranpython.glitch.me)

## license: 100% Open Source
print(" ")
print("webpage viewer beta, a project by jaskaran\n")
sleep(1)

print("Searching for default settings file...")
sleep(1)

## Search engine file


try:
    with open("C:\\Users\Public\webpage-viewer-settings.txt") as f:
        print("Found default settings file (C:\\Users\Public\webpage-viewer-settings.txt)")
        print("Reading contents...")
        sleep(0.5)
        xd = open("C:\\Users\Public\webpage-viewer-settings.txt")
        s = xd.read()
        print("\nYour default search engine is", s)
        xd.close()
except FileNotFoundError:
     print("No search engine file found, creating one now...\n")
     sleep(0.5)
     print("What is your default search engine? (Google, Bing, Yahoo, DuckDuckGo, Ecosia, Wikipedia, Baidu, Yandex, Ask, Webcrawler)")
     searchengine = input("> ")
     file = open("C:\\Users\Public\webpage-viewer-settings.txt", "w")
     file.write(str(searchengine))
     file.close()
     
## GUI Settings file
try:
    with open("C:\\Users\Public\webpage-viewer-settings-gui.txt") as f:
        print("Found default settings file (C:\\Users\Public\webpage-viewer-settings.txt)")
        print("Reading contents...")
        sleep(0.5)
        xd = open("C:\\Users\Public\webpage-viewer-settings-gui.txt")
        s = xd.read()
        print("\nYou are currently using", s)
        xd.close()
except FileNotFoundError:
     print("\nNo input file found, creating one now...\n")
     sleep(0.5)
     print("How would you like your input to display? (GUI, Console)")
     searchengine = input("> ")
     ttt = open("C:\\Users\Public\webpage-viewer-settings-gui.txt", "w")
     ttt.write(str(searchengine))
     ttt.close()
     
     


print("\njaskaran's webpage-viewer 2.0")

suii = open("C:\\Users\Public\webpage-viewer-settings-gui.txt")
mm = suii.read()

if mm == "gui" or "GUI":
    search = simpledialog.askstring(title="Search",
                                  prompt="Search for: (https/www for website, anything else for search query):")

elif mm == "console" or "Console":
    search = str(input("> "))


with open('C:\\Users\Public\webpage-viewer-search-history.txt','a+') as fileobj:
    fileobj.write("\n"+str(search))
    fileobj.close()
tree = open("C:\\Users\Public\webpage-viewer-settings.txt")
asd = search[:5]
qwe = search[:3]
file = tree.read()

if search == "searchHistory":
    a_file = open("C:\\Users\Public\webpage-viewer-search-history.txt")
    file_contents = a_file.read()
    print(file_contents)

elif search == "search history":
    a_file = open("C:\\Users\Public\webpage-viewer-search-history.txt")
    file_contents = a_file.read()
    print(file_contents)
    
elif str(asd) == "https":
    url = search
    webbrowser.open(url)

elif str(qwe) == "www":
    url = search
    webbrowser.open(url)
    
elif file == "Google" or file == "google":
    url = "https://www.google.com/search?q="+str(search)
    webbrowser.open(url, new=2)
        
    sleep(2)


                
    tree.close()
        
elif file == "Bing" or file == "bing":
    url = "https://www.bing.com/search?q="+str(search)
        
    webbrowser.open(url, new=2)
        
    sleep(2)

                     
    tree.close()
        
elif file == "Yahoo" or file == "yahoo":
    url = "https://uk.search.yahoo.com/search?p="+search
        
    webbrowser.open(url, new=2)
        
    sleep(2)

                    
    tree.close()
        
elif file == "DuckDuckGo" or file == "duckduckgo":
    url = "https://duckduckgo.com/?q="+search
        
    webbrowser.open(url, new=2)
        

                        
    tree.close()
        
elif file == "Ecosia" or file == "ecosia":
    url = "https://www.ecosia.org/search?method=index&q="+search
        
    webbrowser.open(url, new=2)
        
    sleep(2)

                    
    tree.close()
        
elif file == "Baidu" or file == "baidu":
    url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd="+search
        
    webbrowser.open(url, new=2)
        
    sleep(2)

                    
    tree.close()
        
elif file == "Yandex" or file == "yandex":
    url = "https://yandex.ru/search/?lr=21134&text="+search
        
    webbrowser.open(url, new=2)
        
    sleep(2)

                    
    tree.close()
        
elif file == "Ask" or file == "ask":
    url = "https://www.ask.com/web?q="+search
        
    webbrowser.open(url, new=2)
        
    sleep(2)

                        
    tree.close()
        
elif file == "Wikipedia" or file == "wikipedia":
    url = "https://en.wikipedia.org/wiki/"+search
        
    webbrowser.open(url, new=2)
        
    sleep(2)
                    
    tree.close()
        
elif file == "Webcrawler" or file == "webcrawler":
    url = "https://www.webcrawler.com/serp?q="+search
        
    webbrowser.open(url, new=2)
        
    sleep(2)

                
    tree.close()
        
else:
    print("Invalid: Please type a correct search engine. Replace your current search engine at (C:\\Users\Public\webpage-viewer-settings.txt)")
    sleep(2)
        
    tree.close()

# My attempt to convert the html to text (very laggy and buggy)



if not search == "searchHistory":
    if not search == "search history":
        print("Would you like to recreate the webpage using text? Note images won't be included and the program will time out before it can print all of the text.")
        yesno = input("> ")
        if yesno == "no":
            exit("Ok")
        print("Converting webpage to text..")

        req = requests.get(url)


        html = req.text


        PlainText = BeautifulSoup(html, 'lxml')

        text = PlainText.get_text()
        split = text.split('}')
        withoutCss = split[len(split) - 1]


        ## And now... Converting it line by line WITHOUT USING REGEX!

        text = withoutCss
        new_text = ''

        for i, letter in enumerate(text):
            if i and letter.isupper():
                new_text += '\n'

            new_text += letter
    
        print(new_text)


