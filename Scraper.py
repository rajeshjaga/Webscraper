import requests
from bs4 import BeautifulSoup
import smtplib
import time



URL='Add ur product Url'


headers={
    "User-Agent":'Ur user agent header'
    }

def check_price():

    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    convertedp=float(price[1:4])
    if(convertedp<20.0):
        send_mail()
        send_mail()
        print(title.strip())
        print(f'price right now is {convertedp}')
    


def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('hosts @gmail.com','App password ')
    
    subject='Hey the price fell down '
    body='check price \n Add the Link'

    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'From addres @gmail.com',
        'To address @gmail.com',
        msg
    )
    print('Email has sent')
    server.quit()
    
while(True):

    check_price()
    time.sleep(60*60)