import requests
from bs4 import BeautifulSoup
import smtplib
import time



URL='https://www.amazon.in/Mi-Mix-6Gb-128Gb-Black/dp/B0795MQGR2/ref=sr_1_1?crid=1RUJDWDNJA3U5&keywords=mi+mix2&qid=1580185485&sprefix=mi+mix%2Caps%2C553&sr=8-1'


headers={
    "Userver-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
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
    
    server.login('ptest7931@gmail.com','plyepyqnnvpyastg')
    
    subject='Hey the price fell down '
    body='check price \n https://www.amazon.in/Mi-Mix-6Gb-128Gb-Black/dp/B0795MQGR2/ref=sr_1_1?crid=1RUJDWDNJA3U5&keywords=mi+mix2&qid=1580185485&sprefix=mi+mix%2Caps%2C553&sr=8-1'

    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'ptest7931@gmail.com',
        'rajaga223@gmail.com',
        msg
    )
    print('Email has sent')
    server.quit()
    
while(True):

    check_price()
    time.sleep(60*60)