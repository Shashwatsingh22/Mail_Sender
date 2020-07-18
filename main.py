import smtplib
import getpass
import imghdr
from pyfiglet import Figlet
import os

def render(text,style):
    f=Figlet(font=style)
    print('\n'*2)
    print(f.renderText(text))
    print("\t"*5)

#________________________________Function For The Normal Text Message__________________________________
def mail_text(Email_Address, Email_Password, Reciver_Mail, Subject, Body):
    msg=EmailMessage()
    msg["Subject"]=Subject
    msg["From"]=Email_Address
    msg["To"]=Reciver_Mail
    msg.set_content(Body)

    with smtplib.SMTP_SSL(Mail_Server,465) as smtp:
         # Given Port No.=>465 Becoz we are using SMPT_SSL
        smtp.login(Email_Address,Email_Password)

        smtp.send_message(msg)
#-------------------------------------------------------------------------------------------------------

#_________________________________Function For The Add_Attachement_Images_______________________________

def mail_add_attachment_images(Email_Address, Email_Password, Reciver_Mail,Attachement,Subject, Body):
    msg = EmailMessage()
    msg["Subject"] = Subject
    msg["From"] = Email_Address
    msg["To"] = Reciver_Mail
    msg.set_content(Body)

    for names in Attachement:
        # rb is the mode to read ==>Read Byte
        with open(names, "rb") as file:
            file_data = file.read()
            file_name= file.name
            # Now we are going to find the ext of the image like jpg or png ...
            file_type = imghdr.what(file.name)
            msg.add_attachment(file_data,
                               maintype="image",
                               subtype=file_type,
                               file_name=file_name)

    with smtplib.SMTP_SSL(Mail_Server, 465) as smtp:
        # Given Port No.=>465 Becoz we are using SMPT_SSL
        smtp.login(Email_Address, Email_Password)

        smtp.send_message(msg)
#--------------------------------------------------------------------------------------------------------

#___________________ Function For the Add Atachemnt For The Other Files (like-pdf,docx etc..)_____________

def mail_add_other_attachement(Email_Address, Email_Password, Reciver_Mail,Attachement,Subject, Body):
    msg=EmailMessage()
    msg["Subject"]=Subject
    msg["From"]=Email_Address
    msg["To"]=Reciver_Mail
    msg.set_content(Body)

    for names in Attachement:
        #rb is the mode to read ==>Read Byte
        with open(names,"rb") as file:
            file_data=file.read()
            #Now we are going to find the ext of the image like pdf ,docx... ...

            msg.add_attachment(file_data,
                               maintype="application",
                               subtype="octet_stream",
                               )

    with smtplib.SMTP_SSL(Mail_Server,465) as smtp:
        smtp.login(Email_Address,Email_Password)

        smtp.send_message(msg)
#---------------------------------------------------------------------------------------------------------

#______________________________________________MAIN FUNCTION______________________________________________
while True:
    os.system("clear")
    os.system("tput setaf 1")
    render('Mail Sender','5lineoblique')
    os.system("tput setaf 2")
    render("\tby Shashwat Singh", 'digital')
    os.system("tput setaf 5")

    Confiromation="Mail Sent"

    Email_Address = input("Enter Your E-mail Address:   ")
    Email_Password = getpass.getpass("Enter Password:   ")
    Mail_Server=input("Enter Mail Server:   ")
    num = int(input("Enter The Number Reciever Emails:   "))
    Reciver_Mails = []
    for i in range(num):
        Reciver_Mail = input("Enter The Reciver E-mail ID:   ")
        Reciver_Mails.append(Reciver_Mail)
    Subject = input("Enter The Subject For Your Mail:   ")
    Body = input("Write The Message Content:   ")

    os.system("clear")
    os.system("tput setaf 1")
    render('Mail Sender','5lineoblique')
    os.system("tput setaf 2")
    render('\t*10 by Shashwat Singh', 'digital')
    os.system("tput setaf 4")
    print("___________________________________MAIN MENU_________________________________________")
    os.system("tput setaf 3")

    print("""
		Press 1: To Directly Mail An Text Mail Only.
		Press 2: To Mail With Attachement (image).
		Press 3: To Mail With Attachement (for Others Documents Type).
		Press 4: Exit
		""")
    print("Enter Your Choice:  ",end=" ")
    os.system("tput setaf 7")
    
    ch=input()

 #_______________________________________________1_______________________________________   
    if int(ch)==1:
        
        os.system("clear")
        os.system("tput setaf 1")
        render('Mail Sender','5lineoblique')
        os.system("tput setaf 2")
        render('\t by Shashwat Singh', 'digital')
        os.system("tput setaf 4")
        print("_____________________Sending Normal Text Mail______________________________\n\n\n\n")
        os.system("tput setaf 3")


        from email.message import EmailMessage

        mail_text(Email_Address, Email_Password, Reciver_Mails, Subject, Body)
        print(Confiromation)

#_______________________________________________2__________________________________________
    if int(ch)==2:

        os.system("clear")
        os.system("tput setaf 1")
        render('Mail Sender','5lineoblique')
        os.system("tput setaf 2")
        render('\t by Shashwat Singh', 'digital')
        os.system("tput setaf 4")
        print("_____________________Menu For Attachement Mail______________________________\n\n\n\n")
        os.system("tput setaf 3")


        Attachement = []
        n = int(input("Enter The Numbers Of the Images:   "))
        for i in range(n):
            file_name = input("Enter The File Name With Correct Extension:   ")
            Attachement.append(file_name)

        from email.message import EmailMessage

        mail_add_attachment_images(Email_Address, Email_Password, Reciver_Mail,Attachement,Subject, Body)
        print(Confiromation)

#______________________________________________3___________________________________________________
    if int(ch)==3:
        
        os.system("clear")
        os.system("tput setaf 1")
        render('Mail Sender','5lineoblique')
        os.system("tput setaf 2")
        render('\t by Shashwat Singh', 'digital')
        os.system("tput setaf 4")
        print("_____________________Menu For Attachement Mail______________________________\n\n\n\n")
        os.system("tput setaf 3")
        
        
        Attachement = []
        n = int(input("Enter The Numbers Of the Files:   "))
        for i in range(n):
            file_name = input("Enter The File Name With Correct Extension:   ")
            Attachement.append(file_name)
        
        mail_add_other_attachement(Email_Address, Email_Password, Reciver_Mail,Attachement,Subject, Body)
        print(Confiromation)

#----------------------------------------------------------------------------------------------------------