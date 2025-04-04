# import smtplib

# email = "hussainiahmed222@gmail.com"
# password = "*****************"
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email, 
#         to_addrs="hussainiahmed444@gmail.com", 
#         msg="Subject:Hello \n\nThis is the body of my email"
#         )
    
# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()

# date_of_birth = dt.datetime(year=2001, month=3, day=19, hour=16, minute=39)
# print(date_of_birth)


# import smtplib
# import random
# import datetime as dt
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Get the current day of the week
# now = dt.datetime.now()
# day_of_the_week = now.weekday()

# # Read quotes from the file
# with open('./Day 32/quotes.txt', 'r', encoding='utf-8') as file:
#     quotes = file.readlines()
# quotes = [quote.strip() for quote in quotes]

# # Get a random quote
# random_quote = random.randint(0, len(quotes) - 1)

# # Email configuration
# email = "hussainiahmed222@gmail.com"
# password = "*************"
# to_email = "hussainiahmed444@gmail.com"

# # Send the email if it's Monday (day 0 in `weekday()` method)
# if day_of_the_week == 4:  # Monday
#     # Create the email message
#     msg = MIMEMultipart()
#     msg['From'] = email
#     msg['To'] = to_email
#     msg['Subject'] = "Motivational Quote"
    
#     # Attach the quote as the body of the email (use MIMEText for proper encoding)
#     body = quotes[random_quote]
#     msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
#     # Send the email
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=email, password=password)
#         connection.sendmail(from_addr=email, to_addrs=to_email, msg=msg.as_string())

#     print("Email sent successfully!")


import pandas as pd
import datetime as dt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Get the current date
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# Email credentials
email = "hussainiahmed222@gmail.com"
password = "*************"

# Read the CSV with birthdays
data = pd.read_csv("./Day 32/birthdays.csv")

# Read the letter template
with open('./Day 32/letter_templates/letter_1.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Strip newline characters and create a list of lines
lines = [line.strip() for line in lines]

# Loop through the rows in the DataFrame
for index, row in data.iterrows():
    name = row["name"]
    birth_year = row['year']
    birth_month = row["month"]
    birth_day = row["day"]

    # Check if today is the person's birthday
    if year == birth_year and month == birth_month and day == birth_day:
        print(f"Name: {name}, Year: {birth_year}, Month: {birth_month}, Day: {birth_day}")
        
        # Replace the [NAME] placeholder with the actual name
        lines[0] = lines[0].replace('[NAME]', name)
        
        # Prepare the email details
        to_email = row["email"]
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = "Happy Birthday"
        
        # Attach the body of the email with the modified lines
        body = "\n".join(lines)
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=to_email, msg=msg.as_string())
        
        print("Email sent successfully!")






