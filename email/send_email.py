import smtplib

server_host = "smtp.exmail.qq.com"
email_user = "tangxiaojun@checheweike.com"
email_pwd = "fire8848"
server = smtplib.SMTP(server_host)

#Next, log in to the server
server.login(email_user,email_pwd)

#Send the mail
to_user = "hawk418@qq.com"
msg = "test email from python"
res = server.sendmail(email_user, [to_user], msg)

print("send res:")
print(res)