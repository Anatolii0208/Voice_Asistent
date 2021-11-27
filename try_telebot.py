import telebot
from telebot import types
import speech_recognition as sr
import os
import sys
import webbrowser
import requests
import pywhatkit as kt
from bs4 import BeautifulSoup
import requests, lxml, os
import smtplib
import subprocess
import numpy as np
import pyautogui
import imutils
import cv2
from googletrans import Translator, LANGUAGES
from googleapiclient.discovery import build
import numpy as np
import face_recognition


def do():
    l = 0
    # show_new("dvdfdgf")
    """file = open('text.txt','r')
    code = ()
    code = int(input("Задайте код:"))
    answer = int(input("\nКакой код?"))
    while (code - answer > 1):
        answer = int(input("\nКод неверный!Попробуй снова!"))
        if code - answer == 0:
            break
    if code == answer:
        print ("\nДоступ разрешён!")
    if code == answer:
        print(file.read())
    else:
        print()


    exit(0)

    cap = cv2.VideoCapture(0)

    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(30):
        ret,frame = cap.read()

    # Делаем снимок
    ret, frame = cap.read()

    cap.release()

    img_to_com = frame
    img_to_com = cv2.cvtColor(img_to_com, cv2.COLOR_BGR2RGB)
    img_to_com_encode = face_recognition.face_encodings(img_to_com)[0]
    path = 'img_alow'
    img_to_check = []
    myList = os.listdir(path)
    for i in myList: img_to_check.append(face_recognition.face_encodings(cv2.cvtColor(face_recognition.load_image_file(f"img_alow/" + i), cv2.COLOR_BGR2RGB))[0])

    result = face_recognition.compare_faces(img_to_check, img_to_com_encode)

    if True in result:
        print("Hi, Boss")
    else:
        print("Sorry, but we can't give you a succes! Try again")"""
    """imgElon = face_recognition.load_image_file("img_basics/Elon Mask.jpeg")
    imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
    imgTest = face_recognition.load_image_file("img_basics/Ilon mask test.jpeg ")
    imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
    
    faceLoc = face_recognition.face_locations(imgElon)[0]
    encodeElon = face_recognition.face_encodings(imgElon)[0]
    cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)
    
    faceLocTest = face_recognition.face_locations(imgTest)[0]
    encodeTest = face_recognition.face_encodings(imgTest)[0]
    cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255), 2)
    
    result = face_recognition.compare_faces([encodeElon], encodeTest)
    faceDis = face_recognition.face_distance([encodeElon], encodeTest)
    print(result, faceDis)
    
    cv2.imshow('Elon Mask', imgElon)
    cv2.imshow('Ilon mask test', imgTest)
    cv2.waitKey(0)"""

    # password of gmail
    password = ''

    # name of my voice assistant
    name = ''

    # reading password from file
    with open("include/password.txt") as file:
        password = file.read()

    # my browser header
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }

    # function that send an email
    def send_email(host, subject, to_addr, from_addr, body_text):
        # message that will send
        BODY = "\r\n".join((
            "From: %s" % from_addr,
            "To: %s" % to_addr,
            "Subject: %s" % subject,
            "",
            body_text
        ))

        # start server
        server = smtplib.SMTP(host, 587)
        server.starttls()

        # login to my gmail
        server.login(from_addr, password)

        # send email
        server.sendmail(from_addr, [to_addr], BODY)

        # stop server
        server.quit()

    # function that talk what you want
    def talk(words):
        print(words)
        os.system("say " + words)

    # start my program
    talk("Hy, ask me something")

    # function that listen and return what you say
    def command():
        # creating an object
        r = sr.Recognizer()

        # listen for words
        with sr.Microphone() as source:
            print("Say:")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        # try understand what you say
        try:
            task = r.recognize_google(audio).lower()
            print("You say: " + task)
        except sr.UnknownValueError:
            talk("I dont understand you")
            task = command()

        # return what you say
        return task

    # function that return weather in city by index (not use)
    """def weather(s_city):
        talk("Хорошо, пожалуйста")
        appid = "7fc48d355390dd501686310d0604be52"
        print(s_city)
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print("conditions:", data['weather'][0]['description'])
            print("temp:", data['main']['temp'])
            print("temp_min:", data['main']['temp_min'])
            print("temp_max:", data['main']['temp_max'])
        except Exception as e:
            print("Exception (weather):", e)
            pass
        talk("Озвучить?")
        task_weather = command()
        if 'yes' in task_weather:
            #print("conditions" + str(data['weather'][0]['description']) + "temp" + str(data['main']['temp']) + "tempmin:" + str(data['main']['temp_min']) + "tempmax:" + str(data['main']['temp_max']))
            talk("кондишинс," + str(data['weather'][0]['description']) + "," + "температура," + str(data['main']['temp']) + "градусов" + "," + "температура, минимальная," + str(data['main']['temp_min']) + "градусов" + "," + "температура, максимальная,:" + str(data['main']['temp_max']) + "градусов")
        else:
            talk("хорошо не буду")"""

    # main function
    def makeSomething(task):
        # get name
        global name

        # check what you say
        # if you say stop
        if 'stop' in task:
            talk("Ok,no problem")
            l = 1
            return 0
            # sys.exit()

        # if you want get her name
        elif 'name' in task:
            if name != '':
                talk("My name is " + name)
            else:
                talk("Name me please ")
                name = command()
                talk("My name is " + name)

        # hard type of checking weather
        # elif ('weather' in task) and ('kharkiv' in task):
        # weather("Kharkiv, UA")
        # elif ('weather' in task) and ('kyiv' in task):
        # weather("Kyiv, UA")

        # if you want get weather
        elif 'weather' in task:
            # make a request
            html = requests.get(f"https://www.google.com/search?&q={task}", headers=headers).text

            # creating a soup object
            soup = BeautifulSoup(html, 'lxml')

            # print weather with parsing a first website
            print(f"{soup.find('span', class_='wob_t q8U8x').text} degrees\n"
                  f"Probability of precipitation:{soup.find('span', id='wob_pp').text}\n"
                  f"Humidity:{soup.find('span', id='wob_hm').text}\n"
                  f"Winter:{soup.find('span', id='wob_ws').text}\n")
            talk(
                f"{soup.find('span', class_='wob_t q8U8x').text} degrees, Probability of precipitation:{soup.find('span', id='wob_pp').text}, Humidity:{soup.find('span', id='wob_hm').text}, Winter:{soup.find('span', id='wob_ws').text[0:-6]}")
        # if you want search and open website
        elif ('search' in task) and ('open' in task):
            talk("What do you want me find and open")
            task = command()
            talk('I am opening')
            kt.search(task)

        # if you want send an email
        elif ('send' in task) and ('email' in task):
            # host
            host = "smtp.gmail.com"
            talk("You want to say or to write")
            what = command()
            if 'right' not in what:
                talk("Say a title of a letter:")
                subject = command()
                talk("Write who you want send:")
                to_addr = input()
                from_addr = "ashandybin1@gmail.com"
                talk("What do you want to send:")
                body_text = command()
            else:
                subject = input("Write a title of the letter: ")
                to_addr = input("Write who you want send: ")
                from_addr = "ashandybin1@gmail.com"
                body_text = input("What do you want to send: ")

            # send email
            send_email(host, subject, to_addr, from_addr, body_text)

            talk("I have sent")

        # shutdown
        elif ('shutdown' in task or 'turn off' in task) and ('computer' in task or 'mac' in task or 'notebook' in task):
            talk("I am turning off")
            subprocess.call(['osascript', '-e', 'tell app "loginwindow" to «event aevtrsdn»'])

        # screenshot
        elif 'screenshot' in task:
            talk("Say a name of the screenshot")
            pyautogui.screenshot(
                "/Users/anatolijsandybin/Documents/Anatolii/ttt/venv/include/img/" + str(command()) + '.png')
            talk("I have done a screenshot")

        # camera photo
        elif 'camera' in task or 'make photo' in task:
            talk("Say a name of the photo")
            # Включаем первую камеру
            cap = cv2.VideoCapture(0)

            # "Прогреваем" камеру, чтобы снимок не был тёмным
            for i in range(30):
                ret, frame = cap.read()

            # Делаем снимок
            ret, frame = cap.read()

            # Записываем в файл
            cv2.imwrite("/Users/anatolijsandybin/Documents/Anatolii/ttt/venv/include/photos/" + str(command()) + '.png',
                        frame)

            # Отключаем камеру
            cap.release()
            talk("I have done a photo")

        # translater
        elif 'translate' in task:
            talk("Say in english what do you want to translate")
            text_to_trans = command()
            talk("Write a languege to what do you want to translate")
            lang = input()
            translater = Translator()
            # print(translater.translate(text_to_trans,dest=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]).text)
            talk(translater.translate(text_to_trans,
                                      dest=list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]).text)
        elif 'close' in task:
            talk("I am closing")
            list_ap = list(task.split())
            list_ap = list_ap[1:]
            task = " ".join(list_ap).title()
            os.system("pkill " + task)
        elif 'open' in task:
            talk("I am opening")
            list_ap = list(task.split())
            list_ap = list_ap[1:]
            task = " ".join(list_ap).title()
            subprocess.call(
                ["/usr/bin/open", "-W", "-n", "-a", "/Applications/" + task + '.app']
            )
        elif 'time' in task:
            # make a request
            html = requests.get(f"https://www.google.com/search?&q={task}", headers=headers).text

            # creating a soup object
            soup = BeautifulSoup(html, 'lxml')

            # print
            print(soup.find('div', class_="gsrt vk_bk FzvWSb YwPhnf").text, soup.find('div', class_="vk_gy vk_sh").text)
            talk(soup.find('div', class_="gsrt vk_bk FzvWSb YwPhnf").text)
        elif 'what' in task or 'means' in task or 'mean' in task:
            my_api_key = "AIzaSyDfbp3ZPXKyWT5XYgo18uVLC9BOFlyy3F0"
            my_cse_id = "5e2ccab0206963d38"

            talk('What do you want to understand')

            search = command()

            def google_search(search_term, api_key, cse_id, **kwargs):
                service = build("customsearch", "v1", developerKey=api_key)
                res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
                if "items" in res.keys():
                    return res["items"]
                else:
                    return None

            results = google_search(
                search, my_api_key, my_cse_id, num=1)
            arr = list(BeautifulSoup(str(results[0]['htmlSnippet']), 'lxml').text)
            arr = arr[0:-4]
            if "." in arr:
                for i in arr[::-1]:
                    if i == ".":
                        break
                    else:
                        arr = arr[0:-1]
            talk("".join(arr))

    # while program not stop
    """    def loop():
        makeSomething(command())
        root.after(1, loop) # 1000 is equal to 1 second.

    root.after(1, loop)"""
    while True:
        if l == 1:
            break
        makeSomething(command())


# from tkinter import *
# from tkinter import messagebox
mybot = telebot.TeleBot('2129496128:AAHL25Cx4KjNY3ThJho7EwgGekp6CIYhuVw')


@mybot.message_handler(commands=['start', 'help'])
def get_command(message):
    if message.text == '/start':
        cap = cv2.VideoCapture(0)

        # "Прогреваем" камеру, чтобы снимок не был тёмным
        for i in range(30):
            ret, frame = cap.read()
        path = 'include/img_alow'
        # Делаем снимок
        ret, frame = cap.read()

        cap.release()

        img_to_com = frame
        img_to_com = cv2.cvtColor(img_to_com, cv2.COLOR_BGR2RGB)
        #cv2.imshow('image',img_to_com)
        #cv2.waitKey(0)
        img_to_com_encode = face_recognition.face_encodings(img_to_com)[0]
        img_to_check = []
        myList = os.listdir(path)
        for i in myList: img_to_check.append(face_recognition.face_encodings(
            cv2.cvtColor(face_recognition.load_image_file(f"img_alow/" + i), cv2.COLOR_BGR2RGB))[0])
        result = face_recognition.compare_faces(img_to_check, img_to_com_encode)
        if True in result:
            # show_new("dvdfdgf")
            """file = open('text.txt','r')
            code = ()
            code = int(input("Задайте код:"))
            answer = int(input("\nКакой код?"))
            while (code - answer > 1):
                answer = int(input("\nКод неверный!Попробуй снова!"))
                if code - answer == 0:
                    break
            if code == answer:
                print ("\nДоступ разрешён!")
            if code == answer:
                print(file.read())
            else:
                print()
        
        
            exit(0)
        
            cap = cv2.VideoCapture(0)
        
            # "Прогреваем" камеру, чтобы снимок не был тёмным
            for i in range(30):
                ret,frame = cap.read()
        
            # Делаем снимок
            ret, frame = cap.read()
        
            cap.release()
        
            img_to_com = frame
            img_to_com = cv2.cvtColor(img_to_com, cv2.COLOR_BGR2RGB)
            img_to_com_encode = face_recognition.face_encodings(img_to_com)[0]
            path = 'img_alow'
            img_to_check = []
            myList = os.listdir(path)
            for i in myList: img_to_check.append(face_recognition.face_encodings(cv2.cvtColor(face_recognition.load_image_file(f"img_alow/" + i), cv2.COLOR_BGR2RGB))[0])
        
            result = face_recognition.compare_faces(img_to_check, img_to_com_encode)
        
            if True in result:
                print("Hi, Boss")
            else:
                print("Sorry, but we can't give you a succes! Try again")"""
            """imgElon = face_recognition.load_image_file("img_basics/Elon Mask.jpeg")
            imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
            imgTest = face_recognition.load_image_file("img_basics/Ilon mask test.jpeg ")
            imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
            
            faceLoc = face_recognition.face_locations(imgElon)[0]
            encodeElon = face_recognition.face_encodings(imgElon)[0]
            cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)
            
            faceLocTest = face_recognition.face_locations(imgTest)[0]
            encodeTest = face_recognition.face_encodings(imgTest)[0]
            cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255), 2)
            
            result = face_recognition.compare_faces([encodeElon], encodeTest)
            faceDis = face_recognition.face_distance([encodeElon], encodeTest)
            print(result, faceDis)
            
            cv2.imshow('Elon Mask', imgElon)
            cv2.imshow('Ilon mask test', imgTest)
            cv2.waitKey(0)"""

            # password of gmail
            password = ''

            # name of my voice assistant
            name = ''

            # reading password from file
            with open("include/password.txt") as file:
                password = file.read()

            # my browser header
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
            }

            # function that send an email
            def send_email(host, subject, to_addr, from_addr, body_text):
                # message that will send
                BODY = "\r\n".join((
                    "From: %s" % from_addr,
                    "To: %s" % to_addr,
                    "Subject: %s" % subject,
                    "",
                    body_text
                ))

                # start server
                server = smtplib.SMTP(host, 587)
                server.starttls()

                # login to my gmail
                server.login(from_addr, password)

                # send email
                server.sendmail(from_addr, [to_addr], BODY)

                # stop server
                server.quit()

            # function that talk what you want
            def talk(words):
                # print(words)
                mybot.send_message(message.chat.id, words)
                os.system("say " + words)

            # start my program
            talk("Hy, ask me something")

            # function that listen and return what you say
            def command():
                # creating an object
                r = sr.Recognizer()

                # listen for words
                with sr.Microphone() as source:
                    # print("Say:")
                    mybot.send_message(message.chat.id, "Say:")
                    r.pause_threshold = 1
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)

                # try understand what you say
                try:
                    task = r.recognize_google(audio).lower()
                    # print("You say: " + task)
                    mybot.send_message(message.chat.id, "You say: " + task)
                except sr.UnknownValueError:
                    talk("I dont understand you")
                    task = command()

                # return what you say
                return task

            # function that return weather in city by index (not use)
            """def weather(s_city):
                talk("Хорошо, пожалуйста")
                appid = "7fc48d355390dd501686310d0604be52"
                print(s_city)
                try:
                    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                    data = res.json()
                    print("conditions:", data['weather'][0]['description'])
                    print("temp:", data['main']['temp'])
                    print("temp_min:", data['main']['temp_min'])
                    print("temp_max:", data['main']['temp_max'])
                except Exception as e:
                    print("Exception (weather):", e)
                    pass
                talk("Озвучить?")
                task_weather = command()
                if 'yes' in task_weather:
                    #print("conditions" + str(data['weather'][0]['description']) + "temp" + str(data['main']['temp']) + "tempmin:" + str(data['main']['temp_min']) + "tempmax:" + str(data['main']['temp_max']))
                    talk("кондишинс," + str(data['weather'][0]['description']) + "," + "температура," + str(data['main']['temp']) + "градусов" + "," + "температура, минимальная," + str(data['main']['temp_min']) + "градусов" + "," + "температура, максимальная,:" + str(data['main']['temp_max']) + "градусов")
                else:
                    talk("хорошо не буду")"""

            # main function
            def makeSomething(task):
                # get name
                global name

                # check what you say
                # if you say stop
                if 'stop' in task:
                    talk("Ok,no problem")
                    exit(0)
                    # sys.exit()

                # if you want get her name
                elif 'name' in task:
                    if name != '':
                        talk("My name is " + name)
                    else:
                        talk("Name me please ")
                        name = command()
                        talk("My name is " + name)

                # hard type of checking weather
                # elif ('weather' in task) and ('kharkiv' in task):
                # weather("Kharkiv, UA")
                # elif ('weather' in task) and ('kyiv' in task):
                # weather("Kyiv, UA")

                # if you want get weather
                elif 'weather' in task:
                    # make a request
                    html = requests.get(f"https://www.google.com/search?&q={task}", headers=headers).text

                    # creating a soup object
                    soup = BeautifulSoup(html, 'lxml')

                    # print weather with parsing a first website
                    # print(f"{soup.find('span',class_='wob_t q8U8x').text} degrees\n"
                    #     f"Probability of precipitation:{soup.find('span',id='wob_pp').text}\n"
                    #    f"Humidity:{soup.find('span',id='wob_hm').text}\n"
                    #   f"Winter:{soup.find('span',id='wob_ws').text}\n")
                    mybot.send_message(message.chat.id, f"{soup.find('span', class_='wob_t q8U8x').text} degrees\nProbability of precipitation:{soup.find('span', id='wob_pp').text}\nHumidity:{soup.find('span', id='wob_hm').text}\nWinter:{soup.find('span', id='wob_ws').text}\n")
                    talk(
                        f"{soup.find('span', class_='wob_t q8U8x').text} degrees, Probability of precipitation:{soup.find('span', id='wob_pp').text}, Humidity:{soup.find('span', id='wob_hm').text}, Winter:{soup.find('span', id='wob_ws').text[0:-6]}")
                # if you want search and open website
                elif ('search' in task) and ('open' in task):
                    talk("What do you want me find and open")
                    task = command()
                    talk('I am opening')
                    kt.search(task)

                # if you want send an email
                elif ('send' in task) and ('email' in task):
                    # host
                    host = "smtp.gmail.com"
                    talk("You want to say or to write")
                    what = command()
                    if 'right' not in what:
                        talk("Say a title of a letter:")
                        subject = command()
                        talk("Write who you want send:")
                        to_addr = input()
                        from_addr = "ashandybin1@gmail.com"
                        talk("What do you want to send:")
                        body_text = command()
                    else:
                        subject = input("Write a title of the letter: ")
                        to_addr = input("Write who you want send: ")
                        from_addr = "ashandybin1@gmail.com"
                        body_text = input("What do you want to send: ")

                    # send email
                    send_email(host, subject, to_addr, from_addr, body_text)

                    talk("I have sent")

                # shutdown
                elif ('shutdown' in task or 'turn off' in task) and (
                        'computer' in task or 'mac' in task or 'notebook' in task):
                    talk("I am turning off")
                    subprocess.call(['osascript', '-e', 'tell app "loginwindow" to «event aevtrsdn»'])

                # screenshot
                elif 'screenshot' in task:
                    talk("Say a name of the screenshot")
                    pyautogui.screenshot(
                        "/Users/anatolijsandybin/Documents/Anatolii/ttt/venv/include/img/" + str(command()) + '.png')
                    talk("I have done a screenshot")

                # camera photo
                elif 'camera' in task or 'make photo' in task:
                    talk("Say a name of the photo")
                    # Включаем первую камеру
                    cap = cv2.VideoCapture(0)

                    # "Прогреваем" камеру, чтобы снимок не был тёмным
                    for i in range(30):
                        ret, frame = cap.read()

                    # Делаем снимок
                    ret, frame = cap.read()

                    # Записываем в файл
                    cv2.imwrite(
                        str(command()) + '.png',
                        frame)

                    # Отключаем камеру
                    cap.release()
                    talk("I have done a photo")

                # translater
                elif 'translate' in task:
                    talk("Say in english what do you want to translate")
                    text_to_trans = command()
                    talk("Write a languege to what do you want to translate")
                    lang = input()
                    translater = Translator()
                    # print(translater.translate(text_to_trans,dest=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]).text)
                    talk(translater.translate(text_to_trans,
                                              dest=list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]).text)
                elif 'close' in task:
                    talk("I am closing")
                    list_ap = list(task.split())
                    list_ap = list_ap[1:]
                    task = " ".join(list_ap).title()
                    os.system("pkill " + task)
                elif 'open' in task:
                    talk("I am opening")
                    list_ap = list(task.split())
                    list_ap = list_ap[1:]
                    task = " ".join(list_ap).title()
                    subprocess.call(
                        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/" + task + '.app']
                    )
                elif 'time' in task:
                    # make a request
                    html = requests.get(f"https://www.google.com/search?&q={task}", headers=headers).text

                    # creating a soup object
                    soup = BeautifulSoup(html, 'lxml')

                    # print
                    #print(soup.find('div', class_="gsrt vk_bk FzvWSb YwPhnf").text,
                    #      soup.find('div', class_="vk_gy vk_sh").text)
                    mybot.send_message(message.chat.id, soup.find('div', class_="gsrt vk_bk FzvWSb YwPhnf").text+soup.find('div', class_="vk_gy vk_sh").text)
                    talk(soup.find('div', class_="gsrt vk_bk FzvWSb YwPhnf").text)
                elif 'what' in task or 'means' in task or 'mean' in task:
                    my_api_key = "AIzaSyDfbp3ZPXKyWT5XYgo18uVLC9BOFlyy3F0"
                    my_cse_id = "5e2ccab0206963d38"

                    talk('What do you want to understand')

                    search = command()

                    def google_search(search_term, api_key, cse_id, **kwargs):
                        service = build("customsearch", "v1", developerKey=api_key)
                        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
                        if "items" in res.keys():
                            return res["items"]
                        else:
                            return None

                    results = google_search(
                        search, my_api_key, my_cse_id, num=1)
                    arr = list(BeautifulSoup(str(results[0]['htmlSnippet']), 'lxml').text)
                    arr = arr[0:-4]
                    if "." in arr:
                        for i in arr[::-1]:
                            if i == ".":
                                break
                            else:
                                arr = arr[0:-1]
                    talk("".join(arr))

            # while program not stop
            """    def loop():
                makeSomething(command())
                root.after(1, loop) # 1000 is equal to 1 second.
        
            root.after(1, loop)"""
            while True:
                makeSomething(command())
        else:
            exit(0)
    elif message.text == '/help':
        mybot.send_message(message.chat.id, """1. /start - приветствие
    2. /help - список доступных команд""")


mybot.polling()

"""img_to_check = [-7.52607286e-02,  2.20126286e-02,  4.03227359e-02, -6.14114814e-02,
   -1.77022904e-01, -4.28239256e-03,  7.58015364e-03, -1.06954969e-01,
   1.85455889e-01, -6.90499321e-02,  2.87694484e-01,  4.02675532e-02,
   -2.52020210e-01, -5.59287556e-02,  3.57387215e-02,  1.36532307e-01,
   -6.48785532e-02, -2.08441257e-01, -5.28483354e-02, -1.48275644e-02,
   1.24655105e-02,  2.13176310e-02,  9.12080705e-03,  1.94761008e-02,
   -2.15828031e-01, -3.14095974e-01, -6.03724457e-02, -7.91951418e-02,
   -3.86605226e-02, -6.59403354e-02,  4.46452647e-02,  1.51318714e-01,
   -1.64653510e-01,  1.37418509e-04,  5.30223548e-02,  1.56241000e-01,
   -1.45847514e-01, -4.96960729e-02,  1.85073897e-01,  2.46588234e-02,
   -2.55584389e-01,  5.79553694e-02,  9.94140655e-03,  2.68053889e-01,
   1.88102737e-01,  2.19990164e-02,  7.34422281e-02, -7.30394721e-02,
   5.17048240e-02, -3.17092866e-01,  9.52117592e-02,  1.09801605e-01,
   7.86983892e-02,  4.59281802e-02,  5.83186299e-02, -1.51291862e-01,
   9.20528173e-03,  1.10880792e-01, -2.63189852e-01,  4.67356704e-02,
   6.08061850e-02, -9.89864543e-02, -4.03406508e-02, -1.15290679e-01,
   2.47624218e-01,  1.39309525e-01, -1.34417534e-01, -8.59393775e-02,
   1.98094577e-01, -1.85264811e-01, -1.35011137e-01,  1.53019384e-01,
   -1.28567070e-01, -2.11992279e-01, -2.83449233e-01,  1.98134482e-02,
   4.71151710e-01,  1.05632901e-01, -1.76239461e-01, -1.11280456e-02,
   -1.87365636e-02,  1.66448951e-03,  2.85993516e-03,  4.28961962e-02,
   8.52260366e-03, -8.04313347e-02, -1.30076528e-01, -2.66344249e-02,
   3.05524796e-01, -3.55816334e-02, -4.29738462e-02,  2.53967047e-01,
   7.44155124e-02,  4.89668548e-03,  4.48570698e-02,  7.04195797e-02,
   1.43103749e-02, -4.87669297e-02, -1.16164394e-01, -4.67319414e-02,
   -7.51335248e-02, -1.04066610e-01, -4.28512394e-02,  9.23231915e-02,
   -1.88334689e-01,  2.44781703e-01,  7.47159123e-03, -4.93696518e-03,
   -1.80157423e-02,  1.19667351e-02, -5.13635352e-02, -3.36854756e-02,
   1.41424596e-01, -3.42191517e-01,  2.06903070e-01,  1.69640854e-01,
   9.17313248e-02,  1.38419211e-01, -1.16333291e-02,  3.64993438e-02,
   -5.04209995e-02, -6.14963397e-02, -2.01094776e-01, -1.05207913e-01,
   3.91972810e-03, -5.17886654e-02,  4.91201133e-02,  1.11219302e-01]
"""

"""textt = 30
def show_message():
    messagebox.showinfo("пример ввода\вывода", message.get())
    message.set("")
def show_new(what):
    global textt
    canvas.create_text(30,textt,text=what)
    textt+=50
root = Tk()
root['bg'] = "#fafafa"
root.title("Voice assistant")
root.geometry("300x500")
btn = Button(root,fg="blue", text="start",command=do)
btn.pack()
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
canvas = Canvas(root,width=300,height=300,yscrollcommand=scrollbar.set)
canvas.pack()
scrollbar.config(command=canvas.yview)
show_new("dsfsdfsdf")
message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.75, anchor="c")
message_button = Button(text="Submit", command=show_message)
message_button.place(relx=.5, rely=.83, anchor="c")"""
"""

text = Text(width=25, height=10, bg="grey",
            fg='white', wrap=WORD)

text.pack()

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)
s = text.get(0.0, END)"""

# root.mainloop()
