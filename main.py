import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/mail": {"origins": "http://127.0.0.1:8080"}}, max_age=0)

sender_email = "jobavanika481@gmail.com"
sender_password = "yrxz rkcf yvvr lpmp"

receiver_email = "nika.jobava.1@btu.edu.ge"

def sendMail(subject: str, email, tel, messageText):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    body = f"email: {email}\ntel: {tel}\nmessage: {messageText}"
    message.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
        return "Email sent successfully!"
    except Exception as e:
        print(f"Error sending email: {e}")
        return f"Error sending email: {e}"

@app.route('/mail', methods=['POST'])
def process_mail():
    user_mail = request.form.get('userMail')
    tel = request.form.get('tel')
    msg = request.form.get('msg')
    subj = request.form.get('userSubject')

    print(f"User Mail: {user_mail}, Tel: {tel}, Message: {msg}")

    return sendMail(subj, user_mail, tel, msg)

if __name__ == '__main__':
    app.run(debug=True, threaded=False, port=5000)
