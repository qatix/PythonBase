
#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

# me == my email address
# you == recipient's email address
me = "dev@mail.com"
you = "target1@qq.com,target2@qq.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link2"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
# msg.attach(part2)

filename = "attachment.xlsx"
part = MIMEBase('application', "octet-stream")
part.set_payload(open('../'+filename, "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="' +filename + '"')

msg.attach(part)

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.exmail.qq.com')

email_user = "dev@mailserver.com"
email_pwd = "password"
s.login(email_user,email_pwd)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()

print("send ok")