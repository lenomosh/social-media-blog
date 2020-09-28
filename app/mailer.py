from werkzeug.exceptions import InternalServerError
from threading import Thread
from app import mail,create_app
from flask_mail import Message
from flask import render_template,current_app


def send_async_email(msg):
    with create_app().app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")


def send_email(subject, sender, recipient, name):
    msg = Message(subject, sender=sender, recipients=[recipient])
    msg.body = render_template('email/welcome_user.txt', name=name)
    msg.html = render_template('email/welcome_user.html', name=name)
    Thread(target=send_async_email, args=(msg,)).start()
