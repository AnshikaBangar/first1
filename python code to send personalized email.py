import smtplib,ssl
import pandas as pd
filepath=r"C:\Desktop\mail.csv"
df = pd.read_csv (filepath)
df
email_list = df["email"].tolist()
name_list=df["name"].tolist()
mydict = dict(zip(email_list, name_list))
port=587
smtp_server="smtp.gmail.com"
sender="testmail02082020@gmail.com"
pswd=input("Enter your password ")
for x,y in mydict.items():
    receiver=x
    name=y
    message="""Subject:test mail


this is a test mail from python for %s"""%name
    context=ssl.create_default_context()
    with smtplib.SMTP(smtp_server,port,) as server:
        server.starttls(context=context)
        server.ehlo
        server.login(sender,pswd)
        server.sendmail(sender,receiver,message)
