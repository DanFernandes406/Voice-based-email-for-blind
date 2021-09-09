from django.shortcuts import render, HttpResponse
import smtplib 
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from gtts import gTTS
import re 
import datetime
global n1
global p1
class Node:
   def __init__(self, date=None, subject=None, rom=None, body=None, mp=None):
      self.date = date
      self.subject = subject
      self.rom = rom
      self.body = body
      self.mp = mp
      self.nextval = None

class SLinkedList:
    def __init__(self):
      self.headval = None
      self.tailval = None
    def AtEnd(self, date, subject, rom, body, mp):
      NewNode = Node(date, subject, rom, body, mp)
      if self.headval is None:
        self.headval = NewNode
        return
      laste = self.headval
      while(laste.nextval):
        laste = laste.nextval
      laste.nextval=NewNode
      self.tailval = laste.nextval
    def find(self, v1, name, password):
      count = 0
      if self.headval is None:
        return
      laste = self.headval
      while(v1 != count and laste.nextval):
        laste = laste.nextval 
        count = count + 1
      context = {
        'var1':laste.rom,
        'var2':laste.subject,
        'var3':laste.body,
        'var4':int(v1) + 1,
        #'var5':name,
        #'var6':password,
        'var7':laste.date,
        'var8':laste.mp
        
        }
      return context
list1 = SLinkedList()
def length(sing):
    count = 0
    curr = sing.headval
    while curr != None:
        count = count + 1
        curr = curr.nextval 
    return count
def rid1(v):
    f = v.find('+')
    c = v.find(',')
    e = v[:4]
    d = v[f::]
    v = v.replace(d, "")
    v = v.replace(e, "")    
    return v
def rid(v):
    v = v.replace("<style>","<")
    x = v.replace("""<style type="text/css">""", "<")
    y = x.replace("</style>", ">")
    v1 = re.sub("<[^>]+>", "", y)
    v2 = re.sub(r'&(#?)(.+?);', "", v1)
    return v2

def remove(string1): 
    string = str(string1)
    yu = string.replace(" ", "")
    yui = yu.replace("-","")
    tyu= yui.replace(":","")
    return tyu.replace(".","")
def speak(text):
    nou = datetime.datetime.now()
    now = remove(nou) 
    i=0
    while(i<1):
        try:
            #nuo = str(now)
            #uo = remove(nuo)
            tts = gTTS(text=text, lang="en")
            #filename = "voice1.mp3"
            file = "voice"
            name =".mp3"
            pu = "static/"
            pu = pu + file + now + name
            print(pu)
            filename = file+now+name
            tts.save(pu)
            #playsound.playsound(filename)
            i=1
        except:
            print("Processing")
    return pu
# Create your views here.
def check(add, password):
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    #add = decrypt(add)
    #password = decrypt(password)
    try:
        
        mailServer.starttls()
        print(mailServer.login(add, password))
        i=1
    except:
        i=0
    return i

def index(request):
    super = "static\Marjaani-Lovely.mp3"
    context ={
        'var':"hi",
        'var1':super
    }
    return render(request, 'index.html', context)
def first(request):
    return render(request, 'Login.html')
def choice(request):
    global n1
    global p1
    name = request.POST.get('username')
    n1 = request.POST.get('username')
    p1 = request.POST.get('password')
    #name = decrypt(name)
    n1 = n1.lower()
    #name = name + '@gmail.com' 
    print(n1.lower()) 
    password = request.POST.get('password')
    #password = decrypt(password)
    p1 = p1.lower()
    
    print(p1)
    action = request.POST.get('action')
    print(action)
    v1 = request.POST.get('hid')
    val = check(n1, p1)
    context ={
        'var1':name,
        'var2':password,
        'var3':action
    }
    if(val == 1 and action == "send"): #for send.
        return render(request, 'SendEmail.html', context)
    if(val == 1 and action == "inbox"): #for receive-
        context = receive1(n1, p1, v1, list1)

        return render(request, 'InboxEmail.html', context)
    if(val == 0):
        context ={
        'var1':name,
        'var2':password,
        'var3':action
     }

        return render(request, 'WrongEmail.html', context)
def gf(request):
    action = request.POST.get('action')
    #name = request.POST.get('ga')
    #password = request.POST.get('gp')
    v1 = request.POST.get('hid')
    if (int(v1) < length(list1) and action == "-"):
        print("o")
        print(v1)
        ty = int(v1) - 2
        print(ty)
        context = list1.find(ty,n1,p1)
        return render(request, 'InboxEmail.html', context)
    elif (int(v1) < length(list1) and action == "next"):
        print("o")
        print(v1)
        ty = int(v1) 
        print(ty)
        context = list1.find(ty,n1,p1)
        return render(request, 'InboxEmail.html', context)
    elif(int(v1) >= length(list1) and action == "previous"):
        print("o")
        print(v1)
        ty = int(v1) - 2
        print(ty)
        context = list1.find(ty,n1,p1)
        return render(request, 'InboxEmail.html', context)
    elif(action == "previous"):
        v1 = int(v1) - 2
        context = receive1(n1, p1, v1, list1)
        return render(request, 'InboxEmail.html', context)
    elif(action == "next"):
        context = receive1(n1, p1, v1, list1)
        return render(request, 'InboxEmail.html', context)
    elif(action == "home"):
        return render(request, 'Login.html')

    '''if(action == "previous"): #-
        v1 = int(v1) - 2
        context = receive1(name, password, v1)
        return render(request, 'InboxEmail.html', context)

    elif(action == "next"): #.
        context = receive1(name, password, v1)
        return render(request, 'InboxEmail.html', context)
    elif(action == "home"): #..
        return render(request, 'Login.html')'''

def send(request):
    name1 = request.POST.get('username')
    password = request.POST.get('password')
    name2 = request.POST.get('username2')
    msg = request.POST.get('msg')
    #name1 = decrypt(name1)
    #password = decrypt(password)
    ##name2 = decrypt(name2)
    ##msg = decrypt(msg)
    #name1 = name1.lower()
    #password = password.lower()
    name2 = name2.lower()
    #name2 = name2 + '@gmail.com'
    msg = msg.lower()
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(name1, password)
        mailServer.sendmail(name1, name2 , msg)
        mailServer.quit()
        context ={
            'var1':name1,
            'var2':password,
        
        }
        return render(request, 'SuccessSent.html', context)
    except:
        context={
            'var1':name1,
            'var2':password
        }
        return render(request,'WrongEmail.html', context)
def receive1(add, password, v1, list):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    gmailaddress = add
    gmailpassword = password
    imap.login(gmailaddress, gmailpassword)
    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 1
    # total number of emails
    messages = int(messages[0])
    for i in range(messages, messages-N, -1):    
        # fetch the email message by ID      
        v1 = int(v1)  
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
                print("TSubject:", subject)
                lk = "Subject"
                #speak(D,lk,subject)
            
                print("From:", From)
                kl = "From"
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
                            print("hi rick boy",body)
                            jk = "body"
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
    date = rid1(date)
    body = rid(body)
    Final = "Date. "+date + ". " + "From. "+ From + ". " + "Subject "+ subject + ". " +"Body. " + body
    f1 = speak(Final)
    index = v1 + 1
    context = {
        'var1':From,
        'var2':subject,
        'var3':body,
        'var4':index,
        #'var5':gmailaddress,
        #'var6':gmailpassword,
        'var7':date,
        'var8':f1
        
    }
    sin = Node(date,subject,From,body,f1)
    
    print(sin)
    if v1 == 0:
        list1.headval = sin
        list1.tailval = sin
        print(list1.headval.date)
    if v1 != 0:
        list1.AtEnd(date,subject,From,body,f1)
        print("fg")
        print(list1.tailval.date)
    print("wtf")
    print(index)
    return context
    #print("wtf")
    imap.close()
    imap.logout()
def receive(request):
    return render(request, 'Login.html')

def about(request):
    #print("Current date and time: ")
    i =0
    bid = "The size attribute specifies the visible width, in characters, of an <input> element. Note: The size attribute works with the following input types: text, search, tel, url, email, and password. Tip: To specify the maximum number of characters allowed in the <input> element, use the maxlength attribute"
    while(i<1):
        try:
            fro="From: dansan.jon@gmail.com"
            dot=". "
            subject= "Subject: Schitt's creek information for testing"
            body="hi"
            
            text= fro + dot + subject + dot + body
            tts = gTTS(text=text, lang="en")
            #filename = "voice1.mp3"
            filename = "static/jumanji.mp3"
            tts.save(filename)
            #playsound.playsound(filename)
            i=1
        except:
            print("Processing")
    context ={
        'var1':filename,
        'var2':text,
        'var3':bid
        
    }
    
    return render(request, 'test.html', context)