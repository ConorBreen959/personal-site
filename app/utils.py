from flask import current_app
from flask_mail import Message

import app


def send_email(name, email, message):
    subject = "Personal Site Query Submission"
    body = f"""A query form submission has been made on your personal site.
    
    {name} sends the following message:
    
    {message}
    
    They can be contacted at the following email address:
    
    {email}
    """
    env = current_app.config["FLASK_ENV"]
    if env != "prod":
        subject = f"{env.upper()} {subject}"
    message = Message(
        subject,
        recipients=[
            "conor.breen32@gmail.com"
        ],
        cc=[],
        body=body,
    )
    app.mail.send(message)