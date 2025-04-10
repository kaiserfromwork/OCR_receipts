import os
from dotenv import load_dotenv

import imaplib

# load .env
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# CONNECT IMAP
imap_login = imaplib.IMAP4_SSL("imap.gmail.com") # Port 993
imap_login.login(EMAIL, PASSWORD)

