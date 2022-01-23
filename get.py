#!/usr/bin/env python3

import requests as req
from CASClient import CASClient
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#-----------------------------------------------------------------------
# app.secret_key = b'\xcdt\x8dn\xe1\xbdW\x9d[}yJ\xfc\xa3~/'
#-----------------------------------------------------------------------
username = CASClient().authenticate()
resp = req.get("https://tigerbook.herokuapp.com/api/v1/getkey/tigertickets")
print(resp.text)
