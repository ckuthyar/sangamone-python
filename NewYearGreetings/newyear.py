import smtplib

names = []
emails = []
count1=0

f1=open('Customers - Sheet1.csv','r')
list1=f1.readlines() 
len1=len(list1)
for i in range(0,len1,1):
    list2=list1[i].replace("\n","").split(",")
    names.append(list2[0])
    emails.append(list2[1])

f1=open('config.txt','r')
list1=f1.readline().strip().split(',')
host=list1[0]
port=list1[1]
list1=f1.readline().strip().split(',')
username=list1[0]
password=list1[1]

f1=open('template_subject.txt','r')
subject=f1.read()

f1=open('template_body.txt','r')
template=f1.read()

server=smtplib.SMTP(host,port)
server.starttls()
server.login(username,password)

print("Total mails to be sent:",len1)


for i in range(0,len1,1):
    body=template.replace('<name>',names[i])
    msg=f"Subject: {subject}\n\n{body}"
    email=emails[i]
    server.sendmail(username,email,msg)
    count1=count1+1
print("Total mails sent:",count1)
server.close()


