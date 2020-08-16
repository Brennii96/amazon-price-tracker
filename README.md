# Amazon Price Tracker

You will of course need the latest Python installed and run the following command to get the required packages.
```python3 -m pip install requests bs4```

Go into `scraper.py` and change the URL:6 headers:9 search what's my ua on google [What's My UA](https://www.google.com/search?ei=zX9FXbbODonzgQbK8LiYCA&q=whats+my+ua&oq=whats+my+ua&gs_l=psy-ab.3..0i10l3j0i22i10i30l3j0i22i30l4.3238.5916..6168...0.0..0.108.1123.13j1......0....1..gws-wiz.......0i71j35i39j0i131j0i67j0j0i131i67j0i20i263j0i10i67..11%3A1j12%3A13j13%3A0.2M1aSxOEwK0&ved=0ahUKEwj26OXK2-bjAhWJecAKHUo4DoMQ4dUDCAo&uact=5)

Go to `server = smtplib.SMTP`:28 and enter your smtp server.
Go to `server.login()`:33 and enter your username and password. Google may require an app password if you have 2fa enabled.
Change the body to whatever you would like the email to say and the subject.
Go to `server.sendmail`:40 and enter from email, to email then the msg you would like to send.

`time.sleep`:52 will specify how long you would like it to check in seconds. Currently set to every 24 hours.
