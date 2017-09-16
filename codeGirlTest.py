#!/usr/bin/env python3

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib


while True:
    # set the url,
    url = "https://www.sympla.com.br/code-girl-5__185364"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    # if the number of times "Lote 3" occurs on the page is less than 1,
    if str(soup).find("Lote 3") == -1:
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue

    # but if "Lote 3" occurs any other number of times,
    else:
        email = 'tayspambot@gmail.com'
        # create an email message with just a subject line,
        msg = 'Subject: CODE GIRL LOTE 3 AAAAAAAAA'
        # set the 'from' address,
        fromaddr = email
        # set the 'to' addresses,
        toaddrs  = ['taynaran.n@gmail.com', 'taypih@gmail.com']

        try:
	        # setup the email server,
	        server = smtplib.SMTP('smtp.gmail.com', 587)
	        server.ehlo()
	        server.starttls()
	        with open('pw.txt') as f:
	            pw = f.read()
	        # add my account login name and password
	        server.login(email, pw)

	        # send the email
	        server.sendmail(fromaddr, toaddrs, msg)
	        # disconnect from the server
	        server.close()

	        # Print the email's contents
	        print('From: ' + fromaddr)
	        print('To: ' + str(toaddrs))
	        print('Message: ' + msg)
        except:
            print("failed to send mail")

        # exit loop
        break