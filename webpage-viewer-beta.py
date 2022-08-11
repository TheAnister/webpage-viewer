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
    
## webpage viewer 2.3beta

## Description: Combining all your favourite search engines into one, simple, easy-to-use tool. Set your default search engine,
## and search any query you like, or open up a website using prefixes: 'https', 'www'. You can even check your search history,
## or even re-create your webpage using text in python! You even have the option to input your querys into GUI or console!
## What's great is that it is open source!

## release notes: now uses a GUI to create a screenshot of the website, which it opens for you to view it. this system is far too
## complex, so in 2.3 i may just switch back to a more simple screeenshot-based preview system.

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
     print("\nNo search engine file found, creating one now...\n")
     sleep(0.5)
     print("What is your default search engine? (Google, Bing, Yahoo, DuckDuckGo, Ecosia, Wikipedia, Baidu, Yandex, Ask, Webcrawler)")
     searchengine = input("> ")
     file = open("C://Users/"+username+"/AppData/webpage-viewer-settings.txt", "w")
     file.write(str(searchengine))
     file.close()
     
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

try:
    with open("C://Users/"+username+"/AppData\webpage-viewer-settings-recreate.txt") as f:
        print("Found default settings file (C://Users/"+username+"/AppData/webpage-viewer-settings-recreate.txt)")
        print("Reading contents...")
        sleep(0.5)
        xd = open("C://Users/"+username+"/AppData/webpage-viewer-settings-recreate.txt")
        s = xd.read()
        if s == "yes":
            print("\nYou are currently recreating the website.")
        elif s == "no":
            print("\nYou are currently not recreating the website.")
        else:
            print("An unknown error occured whilst reading the default settings file. Retrying, this time, please use a lowercase letter at the start.")
            sleep(2)
            print("Would you like to automatically re-create the website before it opens? Note this will take longer to open the url")
            recreate = input("> ")
            ttt = open("C://Users/"+username+"/AppData/webpage-viewer-settings-recreate.txt", "w")
            ttt.write(str(recreate))
            ttt.close()
     
        xd.close()
except FileNotFoundError:
     print("\nNo input file found, creating one now...\n")
     sleep(0.5)
     print("Would you like to automatically re-create the website before it opens? Note this will take longer to open the url")
     recreate = input("> ")
     ttt = open("C://Users/"+username+"/AppData/webpage-viewer-settings-recreate.txt", "w")
     ttt.write(str(recreate))

     


print("\njaskaran's webpage-viewer 2.0")

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
tree = open("C://Users/"+username+"/AppData/webpage-viewer-settings.txt")
asd = search[:5]
qwe = search[:3]
file = tree.read()
wee = open("C://Users/"+username+"/AppData/webpage-viewer-settings-recreate.txt")
nope = wee.read()

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
 
        
    sleep(2)


                
    tree.close()
        
elif file == "Bing" or file == "bing":
    url = "https://www.bing.com/search?q="+str(search)
        

        
    sleep(2)

                     
    tree.close()
        
elif file == "Yahoo" or file == "yahoo":
    url = "https://uk.search.yahoo.com/search?p="+search
        

        
    sleep(2)

                    
    tree.close()
        
elif file == "DuckDuckGo" or file == "duckduckgo":
    url = "https://duckduckgo.com/?q="+search
        

        

                        
    tree.close()
        
elif file == "Ecosia" or file == "ecosia":
    url = "https://www.ecosia.org/search?method=index&q="+search
        
        
    sleep(2)

                    
    tree.close()
        
elif file == "Baidu" or file == "baidu":
    url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd="+search
        

        
    sleep(2)

                    
    tree.close()
        
elif file == "Yandex" or file == "yandex":
    url = "https://yandex.ru/search/?lr=21134&text="+search
        

        
    sleep(2)

                    
    tree.close()
        
elif file == "Ask" or file == "ask":
    url = "https://www.ask.com/web?q="+search
        

        
    sleep(2)

                        
    tree.close()
        
elif file == "Wikipedia" or file == "wikipedia":
    url = "https://en.wikipedia.org/wiki/"+search

        
    sleep(2)
                    
    tree.close()
        
elif file == "Webcrawler" or file == "webcrawler":
    url = "https://www.webcrawler.com/serp?q="+search
        

        
    sleep(2)

                
    tree.close()
        
else:
    print("Invalid: Please type a correct search engine. Replace your current search engine at (C:\\Users\YourUsername\webpage-viewer-settings.txt)")
    sleep(2)
        
    tree.close()

get_url= webbrowser.open(url)


# My attempt to display HTML (v2) by taking a screenshot then displaying it




if nope == "yes":
    if not search == "search history":
        if not search == "searchHistory":
            print("Loading..")
            from cefpython3 import cefpython as cef
            import os
            import platform
            import subprocess
            import sys
            
            try:
                from PIL import Image
            except ImportError:
                print("[screenshot.py] Error: PIL module not available. To install"
                      " type: pip install Pillow")
                sys.exit(1)
            
            
            # Config
            # URL = "https://github.com/cztomczak/cefpython"
            
            
            def main(url, w, h):
                global VIEWPORT_SIZE, URL, SCREENSHOT_PATH
            
                # URL = "https://www.apple.com/it/iphone/"
                URL = url
                VIEWPORT_SIZE = (w, h)
                SCREENSHOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                               "screenshot.png")
                check_versions()
                sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
                if os.path.exists(SCREENSHOT_PATH):
                    print("[screenshot.py] Remove old screenshot")
                    os.remove(SCREENSHOT_PATH)
                command_line_arguments()
                # Off-screen-rendering requires setting "windowless_rendering_enabled"
                # option.
                settings = {
                    "windowless_rendering_enabled": True,
                }
                switches = {
                    # GPU acceleration is not supported in OSR mode, so must disable
                    # it using these Chromium switches (Issue #240 and #463)
                    "disable-gpu": "",
                    "disable-gpu-compositing": "",
                    # Tweaking OSR performance by setting the same Chromium flags
                    # as in upstream cefclient (Issue #240).
                    "enable-begin-frame-scheduling": "",
                    "disable-surfaces": "",  # This is required for PDF ext to work
                }
                browser_settings = {
                    # Tweaking OSR performance (Issue #240)
                    "windowless_frame_rate": 30,  # Default frame rate in CEF is 30
                }
                cef.Initialize(settings=settings, switches=switches)
                create_browser(browser_settings)
                cef.MessageLoop()
                cef.Shutdown()
                print("[screenshot.py] Opening screenshot with default application")
                open_with_default_application(SCREENSHOT_PATH)
            
            
            def check_versions():
                ver = cef.GetVersion()
                print("[screenshot.py] CEF Python {ver}".format(ver=ver["version"]))
                print("[screenshot.py] Chromium {ver}".format(ver=ver["chrome_version"]))
                print("[screenshot.py] CEF {ver}".format(ver=ver["cef_version"]))
                print("[screenshot.py] Python {ver} {arch}".format(
                       ver=platform.python_version(),
                       arch=platform.architecture()[0]))
                print("[screenshot.py] Pillow")
                assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"
            
            
            def command_line_arguments():
                if len(sys.argv) == 4:
                    url = sys.argv[1]
                    width = int(sys.argv[2])
                    height = int(sys.argv[3])
                    if url.startswith("http://") or url.startswith("https://"):
                        global URL
                        URL = url
                    else:
                        print("[screenshot.py] Error: Invalid url argument")
                        sys.exit(1)
                    if width > 0 and height > 0:
                        global VIEWPORT_SIZE
                        VIEWPORT_SIZE = (width, height)
                    else:
                        print("[screenshot.py] Error: Invalid width and height")
                        sys.exit(1)
            
                elif len(sys.argv) > 1:
                    print("[screenshot.py] Error: Expected arguments: url width height")
                    sys.exit(1)
            
            
            def create_browser(settings):
                # Create browser in off-screen-rendering mode (windowless mode)
                # by calling SetAsOffscreen method. In such mode parent window
                # handle can be NULL (0).
                global VIEWPORT_SIZE, URL
                parent_window_handle = 0
                window_info = cef.WindowInfo()
                window_info.SetAsOffscreen(parent_window_handle)
                print("[screenshot.py] Viewport size: {size}"
                      .format(size=str(VIEWPORT_SIZE)))
                print("[screenshot.py] Loading url: {url}"
                      .format(url=URL))
                browser = cef.CreateBrowserSync(window_info=window_info,
                                                settings=settings,
                                                url=URL)
                browser.SetClientHandler(LoadHandler())
                browser.SetClientHandler(RenderHandler())
                browser.SendFocusEvent(True)
                # You must call WasResized at least once to let know CEF that
                # viewport size is available and that OnPaint may be called.
                browser.WasResized()
            
            
            def save_screenshot(browser):
                global SCREENSHOT_PATH
                # Browser object provides GetUserData/SetUserData methods
                # for storing custom data associated with browser. The
                # "OnPaint.buffer_string" data is set in RenderHandler.OnPaint.
                buffer_string = browser.GetUserData("OnPaint.buffer_string")
                if not buffer_string:
                    raise Exception("buffer_string is empty, OnPaint never called?")
                image = Image.frombytes("RGBA", VIEWPORT_SIZE, buffer_string,
                                        "raw", "RGBA", 0, 1)
                image.save(SCREENSHOT_PATH, "PNG")
                print("[screenshot.py] Saved image: {path}".format(path=SCREENSHOT_PATH))
            
            
            def open_with_default_application(path):
                if sys.platform.startswith("darwin"):
                    subprocess.call(("open", path))
                elif os.name == "nt":
                    # noinspection PyUnresolvedReferences
                    os.startfile(path)
                elif os.name == "posix":
                    subprocess.call(("xdg-open", path))
            
            
            def exit_app(browser):
                # Important note:
                #   Do not close browser nor exit app from OnLoadingStateChange
                #   OnLoadError or OnPaint events. Closing browser during these
                #   events may result in unexpected behavior. Use cef.PostTask
                #   function to call exit_app from these events.
                print("[screenshot.py] Close browser and exit app")
                browser.CloseBrowser()
                cef.QuitMessageLoop()
            
            
            class LoadHandler(object):
                def OnLoadingStateChange(self, browser, is_loading, **_):
                    """Called when the loading state has changed."""
                    if not is_loading:
                        # Loading is complete
                        sys.stdout.write(os.linesep)
                        print("[screenshot.py] Web page loading is complete")
                        save_screenshot(browser)
                        # See comments in exit_app() why PostTask must be used
                        cef.PostTask(cef.TID_UI, exit_app, browser)
            
                def OnLoadError(self, browser, frame, error_code, failed_url, **_):
                    """Called when the resource load for a navigation fails
                    or is canceled."""
                    if not frame.IsMain():
                        # We are interested only in loading main url.
                        # Ignore any errors during loading of other frames.
                        return
                    print("[screenshot.py] ERROR: Failed to load url: {url}"
                          .format(url=failed_url))
                    print("[screenshot.py] Error code: {code}"
                          .format(code=error_code))
                    # See comments in exit_app() why PostTask must be used
                    cef.PostTask(cef.TID_UI, exit_app, browser)
            
            
            class RenderHandler(object):
                def __init__(self):
                    self.OnPaint_called = False
            
                def GetViewRect(self, rect_out, **_):
                    """Called to retrieve the view rectangle which is relative
                    to screen coordinates. Return True if the rectangle was
                    provided."""
                    # rect_out --> [x, y, width, height]
                    rect_out.extend([0, 0, VIEWPORT_SIZE[0], VIEWPORT_SIZE[1]])
                    return True
            
                def OnPaint(self, browser, element_type, paint_buffer, **_):
                    """Called when an element should be painted."""
                    if self.OnPaint_called:
                        sys.stdout.write(".")
                        sys.stdout.flush()
                    else:
                        sys.stdout.write("[screenshot.py] OnPaint")
                        self.OnPaint_called = True
                    if element_type == cef.PET_VIEW:
                        # Buffer string is a huge string, so for performance
                        # reasons it would be better not to copy this string.
                        # I think that Python makes a copy of that string when
                        # passing it to SetUserData.
                        buffer_string = paint_buffer.GetBytes(mode="rgba",
                                                              origin="top-left")
                        # Browser object provides GetUserData/SetUserData methods
                        # for storing custom data associated with browser.
                        browser.SetUserData("OnPaint.buffer_string", buffer_string)
                    else:
                        raise Exception("Unsupported element_type in OnPaint")
            
            import tkinter as tk
            
            root = tk.Tk()
            root.geometry("400x200")
            class Widgets:
                def __init__(self, labtext, set_variable):
                    self.lab = tk.Label(root, text=labtext)
                    self.lab.pack()
                    self.v = tk.StringVar()
                    self.entry = tk.Entry(root, textvariable=self.v)
                    self.entry.pack()
                    self.v.set(set_variable)
            
            
            a = Widgets("File Name", url)
            b = Widgets("Width", "1024")
            c = Widgets("Height", "5000")
            root.bind("<Return>", lambda x: main(a.v.get(), int(b.v.get()), int(c.v.get())))
            lab2 = tk.Label(root, text="PRESS ENTER TO CREATE THE SCREENSHOT")
            lab3 = tk.Label(root, text="Thanks to https://pythonprogramming.altervista.org/ for helping to create this feature")
            lab3.pack()
            lab2.pack()
            
            root.mainloop()
            1
            2
            3
            4
            5
            6
            7
            8
            9
            10
            11
            12
            13
            14
            15
            16
            17
            18
            19
            20
            21
            22
            23
            24
            25
            26
            27
            28
            29
            30
            31
            32
            33
            34
            35
            36
            37
            38
            39
            40
            41
            42
            43
            44
            45
            46
            47
            48
            49
            50
            51
            52
            53
            54
            55
            56
            57
            58
            59
            60
            61
            62
            63
            64
            65
            66
            67
            68
            69
            70
            71
            72
            73
            74
            75
            76
            77
            78
            79
            80
            81
            82
            83
            84
            85
            86
            87
            88
            89
            90
            91
            92
            93
            94
            95
            96
            97
            98
            99
            100
            101
            102
            103
            104
            105
            106
            107
            108
            109
            110
            111
            112
            113
            114
            115
            116
            117
            118
            119
            120
            121
            122
            123
            124
            125
            126
            127
            128
            129
            130
            131
            132
            133
            134
            135
            136
            137
            138
            139
            140
            141
            142
            143
            144
            145
            146
            147
            148
            149
            150
            151
            152
            153
            154
            155
            156
            157
            158
            159
            160
            161
            162
            163
            164
            165
            166
            167
            168
            169
            170
            171
            172
            173
            174
            175
            176
            177
            178
            179
            180
            181
            182
            183
            184
            185
            186
            187
            188
            189
            190
            191
            192
            193
            194
            195
            196
            197
            198
            199
            200
            201
            202
            203
            204
            205
            206
            207
            208
            209
            210
            211
            212
            213
            214
            215
            216
            217
            218
            219
            220
            221
            222
            223
            224
            225
            226
            227
            228
            229
            230
            231
            232
            233
            from cefpython3 import cefpython as cef
            import os
            import platform
            import subprocess
            import sys
             
            try:
                from PIL import Image
            except ImportError:
                print("[screenshot.py] Error: PIL module not available. To install"
                      " type: pip install Pillow")
                sys.exit(1)
             
             
            # Config
            # URL = "https://github.com/cztomczak/cefpython"
             
             
            def main(url, w, h):
                global VIEWPORT_SIZE, URL, SCREENSHOT_PATH
             
                # URL = "https://www.apple.com/it/iphone/"
                URL = url
                VIEWPORT_SIZE = (w, h)
                SCREENSHOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                               "screenshot.png")
                check_versions()
                sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
                if os.path.exists(SCREENSHOT_PATH):
                    print("[screenshot.py] Remove old screenshot")
                    os.remove(SCREENSHOT_PATH)
                command_line_arguments()
                # Off-screen-rendering requires setting "windowless_rendering_enabled"
                # option.
                settings = {
                    "windowless_rendering_enabled": True,
                }
                switches = {
                    # GPU acceleration is not supported in OSR mode, so must disable
                    # it using these Chromium switches (Issue #240 and #463)
                    "disable-gpu": "",
                    "disable-gpu-compositing": "",
                    # Tweaking OSR performance by setting the same Chromium flags
                    # as in upstream cefclient (Issue #240).
                    "enable-begin-frame-scheduling": "",
                    "disable-surfaces": "",  # This is required for PDF ext to work
                }
                browser_settings = {
                    # Tweaking OSR performance (Issue #240)
                    "windowless_frame_rate": 30,  # Default frame rate in CEF is 30
                }
                cef.Initialize(settings=settings, switches=switches)
                create_browser(browser_settings)
                cef.MessageLoop()
                cef.Shutdown()
                print("[screenshot.py] Opening screenshot with default application")
                open_with_default_application(SCREENSHOT_PATH)
             
             
            def check_versions():
                ver = cef.GetVersion()
                print("[screenshot.py] CEF Python {ver}".format(ver=ver["version"]))
                print("[screenshot.py] Chromium {ver}".format(ver=ver["chrome_version"]))
                print("[screenshot.py] CEF {ver}".format(ver=ver["cef_version"]))
                print("[screenshot.py] Python {ver} {arch}".format(
                       ver=platform.python_version(),
                       arch=platform.architecture()[0]))
                print("[screenshot.py] Pillow")
                assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"
             
             
            def command_line_arguments():
                if len(sys.argv) == 4:
                    url = sys.argv[1]
                    width = int(sys.argv[2])
                    height = int(sys.argv[3])
                    if url.startswith("http://") or url.startswith("https://"):
                        global URL
                        URL = url
                    else:
                        print("[screenshot.py] Error: Invalid url argument")
                        sys.exit(1)
                    if width > 0 and height > 0:
                        global VIEWPORT_SIZE
                        VIEWPORT_SIZE = (width, height)
                    else:
                        print("[screenshot.py] Error: Invalid width and height")
                        sys.exit(1)
             
                elif len(sys.argv) > 1:
                    print("[screenshot.py] Error: Expected arguments: url width height")
                    sys.exit(1)
             
             
            def create_browser(settings):
                # Create browser in off-screen-rendering mode (windowless mode)
                # by calling SetAsOffscreen method. In such mode parent window
                # handle can be NULL (0).
                global VIEWPORT_SIZE, URL
                parent_window_handle = 0
                window_info = cef.WindowInfo()
                window_info.SetAsOffscreen(parent_window_handle)
                print("[screenshot.py] Viewport size: {size}"
                      .format(size=str(VIEWPORT_SIZE)))
                print("[screenshot.py] Loading url: {url}"
                      .format(url=URL))
                browser = cef.CreateBrowserSync(window_info=window_info,
                                                settings=settings,
                                                url=URL)
                browser.SetClientHandler(LoadHandler())
                browser.SetClientHandler(RenderHandler())
                browser.SendFocusEvent(True)
                # You must call WasResized at least once to let know CEF that
                # viewport size is available and that OnPaint may be called.
                browser.WasResized()
             
             
            def save_screenshot(browser):
                global SCREENSHOT_PATH
                # Browser object provides GetUserData/SetUserData methods
                # for storing custom data associated with browser. The
                # "OnPaint.buffer_string" data is set in RenderHandler.OnPaint.
                buffer_string = browser.GetUserData("OnPaint.buffer_string")
                if not buffer_string:
                    raise Exception("buffer_string is empty, OnPaint never called?")
                image = Image.frombytes("RGBA", VIEWPORT_SIZE, buffer_string,
                                        "raw", "RGBA", 0, 1)
                image.save(SCREENSHOT_PATH, "PNG")
                print("[screenshot.py] Saved image: {path}".format(path=SCREENSHOT_PATH))
             
             
            def open_with_default_application(path):
                if sys.platform.startswith("darwin"):
                    subprocess.call(("open", path))
                elif os.name == "nt":
                    # noinspection PyUnresolvedReferences
                    os.startfile(path)
                elif os.name == "posix":
                    subprocess.call(("xdg-open", path))
             
             
            def exit_app(browser):
                # Important note:
                #   Do not close browser nor exit app from OnLoadingStateChange
                #   OnLoadError or OnPaint events. Closing browser during these
                #   events may result in unexpected behavior. Use cef.PostTask
                #   function to call exit_app from these events.
                print("[screenshot.py] Close browser and exit app")
                browser.CloseBrowser()
                cef.QuitMessageLoop()
             
             
            class LoadHandler(object):
                def OnLoadingStateChange(self, browser, is_loading, **_):
                    """Called when the loading state has changed."""
                    if not is_loading:
                        # Loading is complete
                        sys.stdout.write(os.linesep)
                        print("[screenshot.py] Web page loading is complete")
                        save_screenshot(browser)
                        # See comments in exit_app() why PostTask must be used
                        cef.PostTask(cef.TID_UI, exit_app, browser)
             
                def OnLoadError(self, browser, frame, error_code, failed_url, **_):
                    """Called when the resource load for a navigation fails
                    or is canceled."""
                    if not frame.IsMain():
                        # We are interested only in loading main url.
                        # Ignore any errors during loading of other frames.
                        return
                    print("[screenshot.py] ERROR: Failed to load url: {url}"
                          .format(url=failed_url))
                    print("[screenshot.py] Error code: {code}"
                          .format(code=error_code))
                    # See comments in exit_app() why PostTask must be used
                    cef.PostTask(cef.TID_UI, exit_app, browser)
             
             
            class RenderHandler(object):
                def __init__(self):
                    self.OnPaint_called = False
             
                def GetViewRect(self, rect_out, **_):
                    """Called to retrieve the view rectangle which is relative
                    to screen coordinates. Return True if the rectangle was
                    provided."""
                    # rect_out --> [x, y, width, height]
                    rect_out.extend([0, 0, VIEWPORT_SIZE[0], VIEWPORT_SIZE[1]])
                    return True
             
                def OnPaint(self, browser, element_type, paint_buffer, **_):
                    """Called when an element should be painted."""
                    if self.OnPaint_called:
                        sys.stdout.write(".")
                        sys.stdout.flush()
                    else:
                        sys.stdout.write("[screenshot.py] OnPaint")
                        self.OnPaint_called = True
                    if element_type == cef.PET_VIEW:
                        # Buffer string is a huge string, so for performance
                        # reasons it would be better not to copy this string.
                        # I think that Python makes a copy of that string when
                        # passing it to SetUserData.
                        buffer_string = paint_buffer.GetBytes(mode="rgba",
                                                              origin="top-left")
                        # Browser object provides GetUserData/SetUserData methods
                        # for storing custom data associated with browser.
                        browser.SetUserData("OnPaint.buffer_string", buffer_string)
                    else:
                        raise Exception("Unsupported element_type in OnPaint")
             
            import tkinter as tk
             
            root = tk.Tk()
            root.geometry("400x900")
            class Widgets:
                def __init__(self, labtext, set_variable):
                    self.lab = tk.Label(root, text=labtext)
                    self.lab.pack()
                    self.v = tk.StringVar()
                    self.entry = tk.Entry(root, textvariable=self.v)
                    self.entry.pack()
                    self.v.set(set_variable)
             
             
            a = Widgets("Site name", url)
            b = Widgets("Width", "2000")
            c = Widgets("Height", "5000")
            root.bind("<Return>", lambda x: main(a.v.get(), int(b.v.get()), int(c.v.get())))
            lab2 = tk.Label(root, text="PRESS ENTER TO CREATE THE SCREENSHOT")
            lab2.pack()
            root.destroy()
            root.mainloop()    
                        
       
        


