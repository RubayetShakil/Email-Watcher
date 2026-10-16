from dotenv import load_dotenv
import os
import time
import imaplib
import email
import subprocess


load_dotenv()

EMAIL_KEYWORD = os.getenv("EMAIL_KEYWORD", "").lower()

email_addr=os.getenv("EMAIL")
password=os.getenv("APP_PASSWORD")

mail=imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(email_addr, password)
mail.select("INBOX")

while True:

    status, email_id=mail.search(None, 'Unseen')
    email_id=email_id[0].split()


    for i in email_id:

       status, data=mail.fetch(i, "(RFC822)")
       message=email.message_from_bytes(data[0][1])
    
       if EMAIL_KEYWORD in message["From"].lower() or EMAIL_KEYWORD in message["Subject"].lower():
        
           for part in message.walk():

               if part.get_content_type()=="text/plain":
                  payload=part.get_payload(decode=True)
                  decoded_payload=payload.decode()
                  print(decoded_payload)
    time.sleep(60)
     
