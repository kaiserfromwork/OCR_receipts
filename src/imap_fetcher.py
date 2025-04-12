import os
from dotenv import load_dotenv

import imaplib

# load .env
load_dotenv()

# retrieving variables from .env file
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# CONNECT IMAP
imap_login = imaplib.IMAP4_SSL("imap.gmail.com")  # Port 993
status, _ = imap_login.login(EMAIL, PASSWORD)  # Storing login status

print("Status: ", {status})
