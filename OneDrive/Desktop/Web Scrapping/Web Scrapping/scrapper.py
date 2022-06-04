# imports
import requests
from bs4 import BeautifulSoup
import time
import smtplib
url ='https://www.amazon.com/Apple-Wireless-Bluetooth-MMEF2AM-Refurbished/dp/B07731Y1CC/ref=sr_1_5?crid=3GONOK3DCHFID&keywords=airpods&qid=1654342664&sprefix=airpod%2Caps%2C452&sr=8-5'

# header
headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

# sleep
time.sleep(5)
page = requests.get(url, headers=headers)



soup = BeautifulSoup(page.content,'html.parser')
title = soup.find_all('h1',{'id':'title'})[0].find_all('span')[0].text.strip()
print(title)

price = soup.find_all('span',{'class':'a-price a-text-price a-size-medium'})[0].text.strip()
print(price)

availability = soup.find('div',{'id':'availability'}).find('span').text.strip()
print(availability)

title =soup.find('span',{'id':'productTitle'}).text

# email section
def my_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('olanipekunayo2012@gmail.com','password')

    

    subject = f'{title} is available!\n'
    body= f'\n{title} current price is {price} and the remaining stock is {availability}'

    message = subject + body


    server.sendmail('olanipekunayo2012@gmail.com','olanipekunayo2010@yahoo.com',message)

    server.quit()


my_email()
