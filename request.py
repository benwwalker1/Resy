import requests
import json
import smtplib
from email.mime.text import MIMEText
import constants

def send_email(content):
    username = constants.SMTP_Username
    password = constants.SMTP_Password

    fake_from = "noreply@resy.com"
    fake_name = "Resy Reservation Bot"

    to_email = constants.SMTP_To
    to_name = "Person"

    subject = "Reservation Available"

    # build the complete email message from all variables
    message = f"From: {fake_name} <{fake_from}>\nTo: {to_name} <{to_email}>\nSubject: {subject}\n\n{content}"

    # show the email message for debuging
    #print(message)

    # set the email Server and Network Port here it is gmail 
    server = smtplib.SMTP("smtp.gmail.com", 587)

    # set secure sending 
    server.starttls()

    # login into the email server
    server.login(username, password)

    # send the message
    server.sendmail(username, to_email, message )

    # close mail server connection 
    server.close()

s = requests.Session()

s.headers.update(constants.my_header)

r = s.get(
    "https://api.resy.com/4/find",
    params={
        "lat": "0",
        "long": "0",
        "day": "2023-05-10",
        "party_size": "2",
        "venue_id": "958",
    },
    headers={"Sec-Fetch-Mode": "no-cors"},
)
res_dict = json.loads(r.text)
slots = res_dict['results']['venues'][0]['slots']
if slots != []:
    send_email(slots)
    print("Reservation Available!")
else:
    print("Reservation Not Available")
