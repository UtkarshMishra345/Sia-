try:
#libraries
    from click import command
    from gtts import gTTS
    import pyautogui
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import os
    import pyjokes
    import requests
    import webbrowser
    import time
    import wikipedia
    import operator
    from bs4 import BeautifulSoup
    from pywikihow import search_wikihow
    import psutil
    import pywhatkit as kit
    import sys  
    from tkinter import Tk
    from tkinter import Label
    from tkinter import Entry
    from tkinter import Button
    from tkinter import StringVar
    from pytube import YouTube
    import keyboard
    from keyboard import press
    from keyboard import press_and_release
    from keyboard import write 
    from time import sleep
    import wolframalpha

        
#audio
    def speak(audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        #print(voices[1].id)
        engine.setProperty('voice', voices[1].id)
        # engine.setProperty('rate', 120)
        engine.say(audio)
        print(audio)
        engine.runAndWait()

# To convert voice into text
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=100, phrase_time_limit=10)

        try:
            #print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Lucky Said: {query}")


        except Exception as e:
            # speak("Say that again please...")
            return 'none'
        query = query.lower()
        return query

# To wish
    def wish():
        hour = int(datetime.datetime.now().hour)
        if 5 <= hour < 12:
            speak("Good Morning!")
        elif 12 <= hour < 18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")
            # To translate the given word or sentence to English
            def translate(text):
                from googletrans import Translator
                translator = Translator(to_lang="en", from_lang="hi")
                translation = translator.translate(text)
                return translation
            
        speak("Hello sir I am Sia, Tell me how can I help you")

# for news updates
    def news():
        main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey={your_api_key}"

        main_page = requests.get(main_url).json()
        # print(main_page)
        articles = main_page["articles"]
        # print(articles)
        head = []
        day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
        for ar in articles:
            head.append(ar['title'])
        for i in range(len(day)):
            # print(f"today's {day[i]} news is: ", head[i])
            speak(f"today's {day[i]} news is: {head[i]}")

#google_search
    def googleit():
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")
        speak("Wait a Second, I am fetching Data")

#open apps
    def OpenApps():

        speak("Ok Sir , Wait A Second!")
            
        if 'code' in query:
            os.startfile(path)
            #give your path here

        elif 'telegram' in query:
            os.startfile("https://web.telegram.org/")
            #give your path here
            speak("Your Command Has Been Completed Sir!")
        elif 'chrome' in query:
            os.startfile("path")
            #give your path here
            speak("Your Command Has Been Completed Sir!")
        elif 'Whatsapp' in query:
            os.startfile("https://web.whatsapp.com/")
            #give your path here
            speak("Your Command Has Been Completed Sir!")
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
            #give your path here
            speak("Your Command Has Been Completed Sir!")
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')
            speak("Your Command Has Been Completed Sir!")
        elif 'open drive' in query:
            webbrowser.open('https://drive.google.com/')
            speak("Your Command Has Been Completed Sir!")
        elif 'map' in query:
            webbrowser.open('https://www.google.com/maps/')
            speak("Your Command Has Been Completed Sir!")
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')
            speak("Your Command Has Been Completed Sir!")

        speak("Your Command Has Been Completed Sir!")

#close apps
    def CloseAPPS():
        speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'map' in query:
            os.system("TASKKILL /F /im chrome.exe")

        speak("Your Command Has Been Succesfully Completed!")


#temprature
    def Temp():
        speak("Tell me place name sir ..")
        search = takecommand().lower()
        h = f"temperature in {search}"
        url = f"https://www.google.com/search?q={h}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_="BNeawe").text
        speak(f"The Temperature Outside Is {temperature}")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_="BNeawe").text
            speak(f"The Temperature in {name} is {temperature}")

#jokes 
    def jokes():


            url = "https://hindi-jokes-api.onrender.com/jokes?api_key=your_api_key"

            headers = {
                "accept": "application/json"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                joke = response.json()['jokeContent']
                print(joke)
                
                from googletrans import Translator
                from gtts import gTTS
                import os
                
                translator = Translator()
                from_lang = 'hi'
                to_lang = 'hi'
                print("Phase to be Translated :"+ joke)
                text_to_translate = translator.translate(joke, 
                                                        src= from_lang,
                                                        dest= to_lang)
                text = text_to_translate.text 
                speak = gTTS(text=text, lang=to_lang, slow= False)
                speak.save("captured_voice.mp3")	 
                os.system("start captured_voice.mp3")

            else:
                print("Error: Unable to fetch a joke.")

#location 
    def location():
        speak("Please Wait For A Moment...")


        import requests
        from bs4 import BeautifulSoup
        import json

        try:
                        
                        ipAdd = requests.get('https://api.ipify.org').text

                        print(ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        #print(geo_data)
                        city = geo_data['city']
                        state = geo_data['region']
                        country = geo_data['country']
                        lat = geo_data['latitude']
                        lon = geo_data['longitude']
                        #print(state)
                        speak(f"sir, we are in : {state} State , {city} city of country : {country} , Our latitude is : {lat} and longitude is : {lon}")

        except Exception as e:
                        speak("sorry sir,due to network issue i amnot able to find where we are.")
                        pass

        import requests

        def get_exact_location(latitude, longitude):
            # OpenStreetMap Nominatim API
            api_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
            
            response = requests.get(api_url)
            data = response.json()
            #print(data)
            
            if data:
                return data['address']['suburb']
            else:
                return None

        location = get_exact_location(lat, lon)
        speak(location)

#main function 
                    
    if __name__ == "__main__":
        
        print("Initiating system...")
        time.sleep(2)
        print("Starting up...")
        time.sleep(2)
        print("Loading resources...")
        time.sleep(2)
        print("Ready to go!")
        time.sleep(2)
        wish()
        while True:

            query = takecommand().lower()

# Logic building for tasks
            if "open notepad" in query:
                npath = 'path'
                #give your path here
                os.startfile(npath)
                speak("opening")

#Date
            elif "what is date today" in query:
                import datetime

                today = datetime.date.today()
                formatted_date = today.strftime("%Y-%m-%d")
                speak(f"Today date is : {formatted_date}")

#Time
            elif "what is current time" in query:
                import datetime

                now = datetime.datetime.now()
                formatted_time = now.strftime("%H:%M:%S")
                speak(f"Now Time is : {formatted_time}")



#play music
            elif 'play music' in query:

                music_dir = "path"

                #give your path here
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[128]))
                speak("playing music")

#Helping Bot
            elif 'alpha' in query:
                    speak("Alpha is Here")
                    # Python program to
                    # demonstrate creation of an
                    # assistant using wolf ram API
                    question = input('Question: ')
                    if "no" in question:
                        pass

                    else:
                        while True:


                            import wolframalpha

                            # Taking input from user


                            # App id obtained by the above steps
                            app_id = "your_app_id"

                            # Instance of wolf ram alpha
                            # client class
                            client = wolframalpha.Client(app_id)

                            # Stores the response from
                            # wolf ram alpha
                            res = client.query(question)

                            # Includes only text from the response
                            answer = next(res.results).text

                            print(answer)
                            speak(answer)

# To Close any application
            elif 'close notepad' in query:
                speak("okay sir, closing")
                os.system("taskkill /f /im notepad.exe")

# To find a joke
            elif "joke" in query:
                jokes()

#shutdown
            elif "shutdown" in query:
                os.system("shutdown /s /t 10")

#restart
            elif "restart" in query:
                os.system("shutdown /r /t 10")

#sleep
            elif "sleep" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

#switch window
            elif "switch the window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(10)
                pyautogui.keyUp("alt")

#Extract News
            elif "news" in query:
                speak("please wait sir, while fetching the news for you")
                news()

# to find my location using IPaddress
            elif "where i am" in query or "where we are" in query:
                location()

# to take screenshot
            elif "screenshot" in query:
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                #img.save(f"{name}.png")
                speak("i am done sir, screenshot is taken in our main folder")
            
# to hide files and folder
            elif "hide all files" in query or "hide this folder" in query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("sir, all files are now hidden")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir,all the files are now visible")

                elif "leave it" in condition:
                    speak("ok sir")

# how to do mode
            elif "how to" in query:
                #speak("how to do mode is activated")
                speak("Hold on I'm fetching details ...")
                query = query.replace("how to", "")
                try:
                        max_results = 1
                        how_to = search_wikihow(query, max_results)  # pip install pywikihow
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry, not able to find")

# to know battery percentage
            elif "battery" in query:
                import psutil

                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")
                if percentage >= 75:
                    speak("we have enough power, no need to charge")
                elif percentage >= 40 and percentage <= 75:
                    speak("we should connect our system to the charging point")
                elif percentage >= 15 and percentage <= 30:
                    speak("we don't have enough power,please connect to the charger")
                elif percentage <= 15:
                    speak("we ahve very low power , please connect to the charger")

# to play video and audio on yt
            elif "play songs on youtube" in query:
                try:
                    speak("tell me the song name")
                    name = takecommand().lower()
                    kit.playonyt(name)
                    speak("Hold on I'm Playing music...")
                except Exception as e:
                    speak("sorry sir i am unable to search")

# SHUT UP
            elif "sleep" in query:
                speak("Ok Sir, Call me when you need me..")
                sys.exit()

#web search
            elif "google" in query:
                speak("what should i search")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")
                speak("opening")
            
#wikipedia search
            elif "wikipedia" in query:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)

# ip address
            elif "ip address" in query:
                from requests import get
                ip = get("https://api.ipify.org").text
                speak(f"your IP address is {ip}")

# to download video
            elif 'download youtube video' in query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                speak("Enter Video Url Here !")
                Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
                link = StringVar()
                Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
                Entry(root,width = 70,textvariable = link).place(x=32,y=90)

                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.first()
                    video.download()
                    Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

                Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

                root.mainloop()
                speak("Video Downloaded")

#keyboard automation
            elif 'stop' in query:
                keyboard.press('k')

            elif 'start' in query:
                keyboard.press('k')

            elif 'restart' in query:
                keyboard.press('0')

            elif 'mute' in query:
                keyboard.press('m')

            elif 'volume up' in query:
                keyboard.press('Fn + F8')

            elif 'volume down' in query:
                keyboard.press('fn + f7')

            elif 'skip' in query:
                keyboard.press('l')

            elif 'back' in query:
                keyboard.press('j')

            elif 'full screen' in query:
                keyboard.press('f')

            elif 'film mode' in query:
                keyboard.press('t')

            elif 'close tab' in query:
                keyboard.press_and_release('ctrl + w')
                
            elif 'new tab' in query:
                keyboard.press_and_release('ctrl + t')

            elif 'new window' in query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in query: 
                keyboard.press_and_release('ctrl +h')

            elif 'home screen' in query:

                keyboard.press_and_release('windows + m')

            elif 'minimise window' in query:

                keyboard.press_and_release('windows + m')

            elif 'show start' in query:

                keyboard.press('windows')

            elif 'open setting' in query:

                keyboard.press_and_release('windows + i')

            elif 'open search' in query:

                keyboard.press_and_release('windows + s')

            elif 'screen shot' in query:

                keyboard.press_and_release('windows + SHIFT + s')

            elif 'restore windows' in  query:

                keyboard.press_and_release('Windows + Shift + M')

            elif 'increase' in query:

                keyboard.press_and_release('SHIFT + .')

            elif 'decrease' in query:

                keyboard.press_and_release('SHIFT + ,')

            elif 'previous' in query:

                keyboard.press_and_release('SHIFT + p')

            elif 'next' in query:

                keyboard.press_and_release('SHIFT + n')
        
            elif 'mute' in query:

                keyboard.press('m')

            elif 'unmute' in query:

                keyboard.press('m')
 
# open apps
            elif 'open facebook' in query:
                OpenApps()

            elif 'open instagram' in query:
                OpenApps()

            elif 'open map' in query:
                OpenApps()

            elif 'open drive' in query:
                OpenApps()

            elif 'open code' in query:
                OpenApps()

            elif 'open youtube' in query:
                OpenApps()
                
            elif 'open telegram' in query:
                OpenApps()

            elif 'open chrome' in query:
                OpenApps()

#close apps
            elif 'close chrome' in query:
                CloseAPPS()

            elif 'Code' in query:
                CloseAPPS()

            elif 'close telegram' in query:
                CloseAPPS()

            elif 'close instagram' in query:
                CloseAPPS()

            elif 'close facebook' in query:
                CloseAPPS()

            elif 'close map' in query:
                CloseAPPS()

#temprature
            elif 'temperature' in query:
                Temp()
        
#translate
            elif 'translate' in query:

                # Importing necessary modules required
                from googletrans import Translator
                from gtts import gTTS
                import os
                # Initializing the translator object
                # Translator method for translation
                translator = Translator()
                    
                # short form of english in which 
                # you will speak
                from_lang = 'en'
                
                # In which we want to convert, short 
                # form of hindi
                to_lang = 'hi'
                    
                print("Speak a stentence...")
                get_sentence  = takecommand().lower()

                        # Using try and except block to improve
                        # its efficiency.
                
                            
                    # Printing Speech which need to 
                    # be translated.
                print("Phase to be Translated :"+ get_sentence)

                    # Using translate() method which requires 
                    # three arguments, 1st the sentence which
                    # needs to be translated 2nd source language
                    # and 3rd to which we need to translate in 
                text_to_translate = translator.translate(get_sentence, 
                                                        src= from_lang,
                                                        dest= to_lang)
                
                # Storing the translated text in text 
                # variable 
                text = text_to_translate.text 

                # Using Google-Text-to-Speech ie, gTTS() method
                # to speak the translated text into the 
                # destination language which is stored in to_lang.
                # Also, we have given 3rd argument as False because
                # by default it speaks very slowly
                speak = gTTS(text=text, lang=to_lang, slow= False)



                # Using save() method to save the translated 
                # speech in capture_voice.mp3
                speak.save("captured_voice.mp3")	 
                
                # Using OS module to run the translated voice.
                os.system("start captured_voice.mp3")

#weather 
            elif "weather" in query:
                    import requests
                    import json

                    print("Wait Sir Fetching Details...")

                    ipAdd = requests.get('https://api.ipify.org').text

                    print("Your Ip Add: " + ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    #print(geo_data)
                    city = geo_data['city']

                    api_key = "your_api_key" # replace with your API key
                    city_name = city # replace with your desired city
                    complete_api_link = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

                    api_link = requests.get(complete_api_link)
                    api_data = api_link.json()

                    if api_data['cod'] == '404':
                        print("Invalid city. Please check your city name.")
                    else:
                        main = api_data['main']
                        temperature = main['temp'] - 273.15 # converting from Kelvin to Celsius
                        humidity = main['humidity']
                        pressure = main['pressure']
                        weather_desc = api_data['weather'][0]['description']

                        speak("Here are the details")
                        time.sleep(0.2)
                        speak(f"Temperature: {temperature} degree Celsius")
                        time.sleep(0.2)
                        speak(f"Humidity: {humidity}%")
                        time.sleep(0.2)
                        speak(f"Pressure: {pressure} hPa")
                        time.sleep(0.2)
                        speak(f"Weather Description: {weather_desc}")
        
#claculator
            elif "calculator" in query:

                speak("Tell me the Operation...")
                oper = takecommand().lower()
                speak(eval(oper))

#whatsapp
            elif "whatsapp" in query:
                import pickle 
                from selenium import webdriver
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver import *
                from selenium.webdriver.common.by import By
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC
                import unittest, time, re

                options = webdriver.ChromeOptions()
                options.add_experimental_option("detach", True)
                options.add_argument(r'--user-data-dir=C://Users//91930//AppData//Local//Google//Chrome//Application//Default') 
                path = "C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
                driver=webdriver.Chrome(path, options = options)

                driver.get("https://web.whatsapp.com/")

                wait = WebDriverWait(driver, 100)
                
#message
            elif "message" in query:             
                        try:

                            import pickle 
                            from selenium import webdriver
                            from selenium.webdriver.common.keys import Keys
                            from selenium.webdriver.common.by import By
                            from selenium.webdriver.support.ui import WebDriverWait
                            from selenium.webdriver.support import expected_conditions as EC
                            import unittest, time, re

                            speak("To whom I have to send message? ")
                            person = input("Enter User Name: ")
                            speak("Enter message to send")
                            string = takecommand().lower()
                            

                            options = webdriver.ChromeOptions()
                            options.add_experimental_option("detach", True)
                            options.add_argument(r'--user-data-dir=C://Users//91930//AppData//Local//Google//Chrome//Application//Default') 
                            path = "C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
                            driver=webdriver.Chrome(path, options = options)

                            driver.get("https://web.whatsapp.com/")

                            wait = WebDriverWait(driver, 100)
                            speak("Wait,I'm sending message...")


                            search_user_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'

                            search = wait.until(EC.presence_of_element_located(
                                    (By.XPATH, search_user_path)))

                            search.send_keys(person, Keys.ENTER)

                            message_box_path =  '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
                            message_box = wait.until(EC.presence_of_element_located(
                                    (By.XPATH, message_box_path)))

                            message_box.send_keys(string, Keys.ENTER)
                            speak('Message sent!')
                            driver.quit()
                        except Exception as e:
                            print(e)

            else:
                if query:
                    url = f"https://www.google.com/search?q={query}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    res = data.find("div", class_="BNeawe").text
                    print(res)
                else:
                    # Do nothing or print a message indicating that no query was provided
                    pass
       
except Exception as e:
    print(e)
    print("An error occurred while processing your request.\nPlease try again later or report the issue")
