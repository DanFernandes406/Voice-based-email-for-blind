import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import pytz 
from datetime import *
import pyautogui
import psutil
#import wolframaplpha
import speedtest
from GoogleNews import GoogleNews
import requests
import imaplib
import email
from email.header import decode_header
from selenium import webdriver



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def task():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('What should i search for')
            q1 = takeCommand().lower()
            kit.playonyt(q1)
            #webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google")

        elif 'search on google' in query:
            speak('what should i search')
            q1 = takeCommand().lower()
            driver = webdriver.Chrome()
            driver.get("https://google.co.in/search?q="+q1)


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Dan Fernandes\\Desktop\\voice\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'thanks a lot' in query or 'thank you' in query:
            speak("It's my pleasure, to assist you sir")

        elif 'sleep' in query or 'go offline' in query:
            break

        elif 'increase the volume' in query:
            pyautogui.press("volumeup")

        elif 'decrease the volume' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'terminate' in query:
            speak("Ok sir. Goodbye")
            sys.exit()

        elif 'tell me about yourself' in query:
            speak("I can help you in a lot of ways, just tell me")

        elif 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir your system has {percentage} percent power left")

        elif 'internet speed' in query or 'speed of my internet' in query:
            st = speedtest.Speedtest()
            o1 = st.download()
            o2 = st.upload()
            print(f"The download speed is {o1} and upload speed is {o2}")
            speak(f"The download speed is {o1} and upload speed is {o2}")

        elif 'show email inbox' in query or 'email inbox' in query:
            gmail = 'anonymous40621@gmail.com'
            passw = "#Mathew77"
            L1 = []
            q1 = 'y'
            C1 = 3
            w1 = 'no'
            Count = 0
            print(Count)
            H1 = 'yes'
            while H1 == 'yes':
                #if H1 == 'yes':
                L1= receive(gmail, passw, Count)
                print(L1[1])
                speak(f"From. {L1[1]}.")
                print(L1[0])
                speak (f"Subject. {L1[0]}")
                speak('would you like to view')
                q1 = takeCommand().lower()
                if 'yes' in q1:
                    print(L1[2])
                    speak(f"Body of mail. {L1[2]}")
                    C1 = 1
                elif 'next' in q1:
                    H1 = 'yes'
                    C1 = 0
                    Count = Count + 1
                elif 'close' in q1:
                    H1 = 'close'
                    speak("Ok sir")
                    break
                elif 'repeat' in q1:
                    H1 = 'yes'
                    C1 = 0
                else:
                    H1 = 'close'
                    speak("Ok sir")
                    break
                if C1 == 1:
                    speak("Should i proceed")
                    w1 = takeCommand().lower()
                    if 'yes' in w1:
                        H1 = 'yes'
                        Count = Count + 1
                    else:
                        H1 = 'no'
                print(H1)
                print(Count)

        elif "today's news" in query or "today's headlines" in query:
            speak("What topic would like to search")
            q1 = takeCommand().lower()
            secret = "2e328268597641a3b702c6c1e0a14c9c"
            url = 'https://newsapi.org/v2/everything?'
            parameters = {
                'q': q1, # query phrase
                'pageSize': 50, # maximum is 100
                'apiKey': secret # your own API key
                }
            response = requests.get(url,
                        params = parameters)
            response_json = response.json()


            for i in range(0,50,3):
                print(response_json['articles'][i]['title'])
                print(response_json['articles'][i]['description'])

                print(response_json['articles'][i+1]['title'])
                print(response_json['articles'][i+1]['description'])

                print(response_json['articles'][i+2]['title'])
                print(response_json['articles'][i+2]['description'])

                speak(f"{response_json['articles'][i]['title']}.")
                speak(f"{response_json['articles'][i]['description']}.")

                speak(f"Next news. {response_json['articles'][i+1]['title']}.")
                speak(f"{response_json['articles'][i+1]['description']}.")

                speak(f"Next news. {response_json['articles'][i+2]['title']}.")
                speak(f"{response_json['articles'][i+2]['description']}.")

                speak("Would you like to continue sir")
                t = takeCommand().lower()
                if t == 'no' or t == 'No':
                    break
                else:
                    continue


        elif 'send a whatsapp' in query:
            speak("Tell me the sender's phone number")
            q1 = takeCommand().lower()
            q1 = q1.replace(" ","")
            q1 = '+91' + q1
            speak("What message would you like to send")
            q2 = takeCommand().lower()
            print(q2)
            now_method = datetime.now()
            #datetime_INDIA = datetime.now(tz_INDIA) 
            p1 = now_method.strftime("%H:%M:%S")
            p6 = p1[:2]
            p2 = int(p6)
            p3 = p1[3:5]
            p3 = int(p3) + 1.10
            #p5 = str(p3)
            print(type(q1))
            print(type(q2))
            print(type(p2))
            print(type(p3))
            print(q1)
            print(q2)
            print(p2)
            print(p3)
            kit.sendwhatmsg(q1,q2,p2,p3)

        elif 'send an email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "8936.crce.ce@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sir, I am not able to send this email")    



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anonymous40621@gmail.com', '#Mathew77')
    server.sendmail('anonymous40621@gmail.com', to, content)
    server.close()

def receive(mail, passw, v1):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    C1 = 0
    L1 = []
    gmailaddress = mail
    gmailpassword = passw
    imap.login(gmailaddress, gmailpassword)
    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 1
    # total number of emails
    messages = int(messages[0])
    for i in range(messages, messages-N, -1):    
        # fetch the email message by ID      
        #v1 = int(v1)  
        i = i - v1
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):           
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):                      
                    # if it's a bytes, decode to str
                    subject = subject.decode()
                date = decode_header(msg["Date"])[0][0]
                if isinstance(date, bytes):
                # if it's a bytes, decode to str
                    date = date.decode()
                # decode email sender
                print("Date:", date)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                #speak(subject)
                D=str(N)
                #print("TSubject:", subject)
                lk = "Subject"
                L1.append(subject) 
                #speak(D,lk,subject)
            
                #print("From:", From)
                kl = "From"
                L1.append(From)
                #speak(D,lk,subject)
                #speak(D,kl,From)
                # if the email message is multipart
                if msg.is_multipart():                    
                    # iterate over email parts
                    for part in msg.walk():                       
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:     
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                        
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            
                       
                            # print text/plain emails and skip attachments
                            #print("hi rick boy",body)
                            jk = "body"
                            L1.append(body)
                            #speak(D,jk,body)
                        elif "attachment" in content_disposition:
                            
                        
                            # download attachment
                            filename = part.get_filename()
                            if filename:
                                
                            
                                if not os.path.isdir(subject):
                                    
                                
                                    # make a folder for this email (named after the subject)
                                    os.mkdir(subject)
                                filepath = os.path.join(subject, filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))
                else:                    
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "C:/Users/Dan Fernandes/Desktop/voice":                                            
                        # print only text email parts
                        print(body)
                if content_type == "C:/Users/Dan Fernandes/Desktop/voice/html":                                  
                    # if it's HTML, create a new HTML file and open it in browser
                    if not os.path.isdir(subject):                    
                        # make a folder for this email (named after the subject)
                        os.mkdir(subject)
                    filename = f"{subject[:50]}.html"
                    filepath = os.path.join(subject, filename)
                    # write the file
                    open(filepath, "w").write(body)
                    # open in the default browser
                    webbrowser.open(filepath)
                print("="*100)
                # close the connection and logout
    imap.close()
    imap.logout()
    return L1

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if "wake up" in query or "come online" in query:
            task()
        elif "goodbye" in query or "terminate" in query:
            sys.exit()

        # Logic for executing tasks based on query
        