import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='minakatokatori@gmail.com',
    to_emails='caohoanganh2000@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)