import streamlit as st
import smtplib
#Simple Mail Transfer Protocol Library
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(sender_email, subject, body):
    # Replace these values with your email and app password
    #This is used so that the server can send you emails 
    gmail_user = 'enter your personal email address'
    gmail_app_password = 'enter your email password'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = gmail_user
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.sendmail(sender_email, gmail_user, msg.as_string())
        st.success('Email sent successfully!')
    except Exception as e:
        st.error(f'Error sending email: {str(e)}')

# Streamlit form
form = st.form('my_form')
fullname = form.text_input(label='Full Name', value='')
user_email = form.text_input(label='Your Email', value='')
phone = form.text_input(label='Your Phone Number', value='')
message = form.text_area(label="Your Message", value='', height=100, key='message')
submit = form.form_submit_button(label='Send Message')
# Handle form submission
if submit:
    send_email(user_email, 'New Message from Streamlit Form', f"Name: {fullname}\nPhone: {phone}\n\nMessage:\n{message}")




""" If your email account has two-factor authentication (2FA), you can't use your regular email password directly in your script. Instead, you should generate an "App Password" or use OAuth for secure authentication.

Using App Password (Gmail example):
Go to your Google Account settings: https://myaccount.google.com/
Under "Security," select "App passwords."
In the "Select app" dropdown, choose "Mail" and in the "Select device" dropdown, choose "Other (Custom name)."
Give your app password a name (e.g., "StreamlitApp") and click "Generate."
Copy the generated app password.
Replace 'your_app_password' with the generated app password in the script. """