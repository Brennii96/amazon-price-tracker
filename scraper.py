import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/Anker-PowerCore-20100-20000mAh-Technology-Black/dp/B00VJSGT2A/ref=sr_1_7?keywords' \
      '=power+bank&qid=1564832822&s=gateway&sr=8-7 '

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 "
                  "Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    if converted_price < 30.99:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@gmail.com', 'randompassword')

    subject = "Hey the price has dropped the item you wanted!"
    body = 'Check the amazon link https://www.amazon.co.uk/Anker-PowerCore-20100-20000mAh-Technology-Black/dp' \
           '/B00VJSGT2A/ref=sr_1_7?keywords=power+bank&qid=1564832822&s=gateway&sr=8-7 '
    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        'from@gmail.com',
        'to@email.com',
        msg
    )

    print("Email has been Sent")
    server.quit()


while True:
    check_price()
    time.sleep(60 * 60 * 24)
