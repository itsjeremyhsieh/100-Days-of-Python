import smtplib
import datetime as dt
import random
email = "jeremy.life0107@gmail.com"
password = "pgmsaalgjzlfvngh"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quoteToday = random.choice(all_quotes)
    # print(quoteToday)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure connection
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="paulazaq35789@gmail.com",
                            msg=f"subject:Quote of the day\n\n{quoteToday}")
