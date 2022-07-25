from bs4 import BeautifulSoup
import requests
import threading
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login('denemedoviz@gmail.com','deneme123')
msg = "online serverdan calistirildi (deneme mesaji) bundan sonraki mesajlar euro artmaya baslarsa gelecek"
s.sendmail("denemedoviz@gmail.com", "denemedoviz@gmail.com", msg)
deneme = [0]
def update():

    import time
    while True:
        url ="https://www.sozcu.com.tr/doviz-hesapla/euro/"
        istek = requests.get(url = url)
        html = istek.text
        soup = BeautifulSoup(html, 'html.parser')

        euro = soup.find_all("div",{"class": "_dh-result"})

        reeleuro = str(euro)
        reeleuro = reeleuro[26:32]

        euro2 = float(reeleuro)
        if(len(deneme) == 3):
            deneme[2] = euro2
        elif(len(deneme) == 2):
            deneme.append(euro2)
        elif(len(deneme) == 1):
            deneme.append(euro2)
        print euro2
        time.sleep(600)
        print("arrayici")
        for x in deneme:
            print(x)
        print ("arraydisi")

        if(len(deneme) == 3):
            if(deneme[1] > deneme[2]):
                msg2 = "son 10dkda euro " + str(deneme[2]-deneme[1]) + " kadar artti. Su anda 1 euro " + deneme[2] + " tl"
                s.sendmail("denemedoviz@gmail.com", "denemedoviz@gmail.com", msg2)

update()
