##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime
import random

email = "jeremy.life0107@gmail.com"
password = "pgmsaalgjzlfvngh"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
# today_format = (today.month, today.day)
# print(today_format)
data = pandas.read_csv("birthdays.csv")
names = data[(data.month == today.month) & (data.day == today.day)].name
if len(names) > 0:
    for name in names:
        letterNum = random.randint(1,3)
        fileName = f"./letter_templates/letter_{letterNum}.txt"
        file = open(fileName, 'r')
        content = file.read()
        content = content.replace("[NAME]", name)
        targetEmail = data[data.name == name].email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # secure connection
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=targetEmail,
                                msg=f"subject:Happy Birthday!\n\n{content}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




