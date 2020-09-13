import smtplib,ssl
import pandas as pd
filepath=r"C:\Desktop\mail.csv"
df = pd.read_csv (filepath)
df
email_list = df["email"].tolist()
email_list
port=587
smtp_server="smtp.gmail.com"
sender="testmail02082020@gmail.com"
receiver=email_list
pswd=input("Enter your password ")
message="""Subject:test mail


hi  this is a test mail from python"""
context=ssl.create_default_context()
with smtplib.SMTP(smtp_server,port,) as server:
    server.starttls(context=context)
    server.ehlo
    server.login(sender,pswd)
    server.sendmail(sender,receiver,message)
