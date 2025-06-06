
# Alert functions: alarm and emergency email


# import packages
from playsound import playsound
import smtplib
import ssl


def sound_alarm():
    """The function plays an alarm sound"""
    playsound("../Data/alarm.wav")


def send_email(username, contact_name, contact_email):
    """
    The function sends an email to an emergency contact, letting him know the driver is asleep
    Note:
    In order to send an email using this Google account, we had to enable "less secure app access".
    This needs to be done once in a while, since Google automatically turns this setting off if it is not being used.
    """
    sender_email = "kathisirichandanakathyayani@gmail.com"
    sender_password = "bogv zhec pytw uwuc"
    message = open("../Data/email_message.txt").read().replace("CONTACT_NAME", contact_name).replace("DRIVER_NAME", username)  # read the message and paste contact and driver names
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(sender_email, sender_password)  # log into sender account
        server.sendmail(sender_email, contact_email, message)  # send the email to emergency contact