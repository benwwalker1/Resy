# Resy Reservation Checker

## Description

A really simple way to use the Resy API to constantly check whether a given reservation is available on a given day. Future work can easily check for individual times by parsing the JSON response, but I don't have a need for it. Future work can also improve the data sent in the email to the user.

## Usage

Run the script periodically on your local machine via `crontab`, or run it periodically on Lambda using `EventBridge (CloudWatchEvents)`.

## Dependencies

* requests
* json
* smtplib
* email

This script uses only python standard libraries, however, `requests` is not a standard library on AWS, therefore this layer should be added. I recommend using [Klayers](https://github.com/keithrozario/Klayers#list-of-arns), and if you're using Python 3.9 on `us-east-1` you can use this ARN: `arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p39-requests:11`.

## Constants

One should replace the constants seen in `request.py` with their own values. I recommend generating the header by using inspect element on your browser, obtaining the HAR file of your request, and using [har2requests](https://pypi.org/project/har2requests/).

Below is an example `constants.py` file:

`SMTP_Password = "Password123"`

`SMTP_Username = "my-email@gmail.com"`

`SMTP_To = "my-other-email@gmail.com"`

`my_header = {API: "api_key", User-Agent: "my_computer"}`

## Notes

The venue_id used in the GET request can also be obtained from your HAR file, in order to find the specific restaurant you wish to check for reservations.