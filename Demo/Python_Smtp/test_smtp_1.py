import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Blog: https://blog.csdn.net/fengbingchun/article/details/89047574
# reference: http://www.runoob.com/python/python-email.html

# 第三方SMTP服务, 如163, qq, sina
mail_host = "smtp.163.com" # 设置服务器
mail_port = 25 # 端口号
mail_user = "fengbingchun" # 用户名
mail_pass = "xxxxx" # 163授权码

sender = "fengbingchun@163.com" # 发送方
receivers = ["fengbingchun@163.com"] # 接收方

def SendTextMessage(text):
	''' 发送纯文本邮件, text: 邮件内容 ''' 
	# 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
	message = MIMEText(text, 'plain', 'utf-8') # 邮件内容
	message['From'] = Header("菜鸟教程", 'utf-8') # 发送者
	message['To'] =  Header("测试", 'utf-8') # 接收者
	subject = 'Python SMTP 邮件测试: plain text' # 邮件主题
	message['Subject'] = Header(subject, 'utf-8')

	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, mail_port)
		smtpObj.login(mail_user, mail_pass) 
		smtpObj.sendmail(sender, receivers, message.as_string())
		print("邮件发送成功: plain text")
	except smtplib.SMTPException:
		print("Error: 无法发送邮件, plain text")

def SendHtmlMessage():
	''' 发送html格式邮件 '''
	mail_msg = """
	<p>Python 邮件发送测试: this is a html email</p>
	<p><a href="http://www.runoob.com">这是一个链接</a></p>
	"""

	message = MIMEText(mail_msg, 'html', 'utf-8')
	message['From'] = Header("菜鸟教程", 'utf-8')
	message['To'] =  Header("测试", 'utf-8')
	subject = 'Python SMTP 邮件测试: html'
	message['Subject'] = Header(subject, 'utf-8')
 
	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, mail_port)
		smtpObj.login(mail_user, mail_pass) 
		smtpObj.sendmail(sender, receivers, message.as_string())
		print("邮件发送成功: html")
	except smtplib.SMTPException:
		print("Error: 无法发送邮件, html")

def SendAttachmentMessage():
	''' 发送带附件的邮件 '''

	message = MIMEMultipart()
	message['From'] = Header("菜鸟教程", 'utf-8')
	message['To'] =  Header("测试", 'utf-8')
	subject = 'Python SMTP 邮件测试: attachment'
	message['Subject'] = Header(subject, 'utf-8')
 
	# 邮件正文内容
	message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试: attachment', 'plain', 'utf-8'))
 
	# 构造附件1，传送当前目录下的 test.txt 文件
	att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
	att1["Content-Type"] = 'application/octet-stream'
	# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
	att1["Content-Disposition"] = 'attachment; filename="test.txt"'
	message.attach(att1)
 
	# 构造附件2，传送当前目录下的 runoob.txt 文件
	att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
	att2["Content-Type"] = 'application/octet-stream'
	att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
	message.attach(att2)

	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, mail_port)
		smtpObj.login(mail_user, mail_pass) 
		smtpObj.sendmail(sender, receivers, message.as_string())
		print("邮件发送成功: attachment")
	except smtplib.SMTPException:
		print("Error: 无法发送邮件: attachment")

def SendHtmlImageMessage():
	''' 发送带html+image的邮件 '''
	msgRoot = MIMEMultipart('related')
	msgRoot['From'] = Header("菜鸟教程", 'utf-8')
	msgRoot['To'] =  Header("测试", 'utf-8')
	subject = 'Python SMTP 邮件测试: html+image'
	msgRoot['Subject'] = Header(subject, 'utf-8')

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	mail_msg = """
	<p>Python 邮件发送测试: html+image</p>
	<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
	<p>图片演示：</p>
	<p><img src="cid:image1"></p>
	"""
	msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

	# 指定图片为当前目录
	fp = open('test.png', 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()

	# 定义图片 ID，在 HTML 文本中引用
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)

	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, mail_port)
		smtpObj.login(mail_user, mail_pass) 
		smtpObj.sendmail(sender, receivers, msgRoot.as_string())
		print("邮件发送成功: html+image")
	except smtplib.SMTPException:
		print("Error: 无法发送邮件: html+image")

if __name__ == "__main__":
	SendTextMessage("Hello, Python 邮件发送测试: this is a plain text email!")
	SendHtmlMessage()
	SendAttachmentMessage()
	SendHtmlImageMessage()	
	print("finish")
