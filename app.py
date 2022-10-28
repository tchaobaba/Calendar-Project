"""
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
"""
from flask import *

app = Flask(__name__)

@app.route("/")
def root():
    #return render_template('maintenance.html')
    return render_template('index.html')

try:
    "/*"
    url = bad_url
except FileNotFoundError:
    print("404 ERROR")
except Exception:
    print('404 ERROR')
"""
@app.route("/solution")
def solution():
    return render_template('solution.html')


@app.route("/propos")
def about():
    return render_template('about.html')


@app.route("/ingeniere")
def ingeniere():
    return render_template('ingenierie.html')


@app.route("/formation", methods=['POST', 'GET'])
def formation():
    msg = " "
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        tel = request.form['tel']
        subject = request.form['subject']
        message = request.form['message']
        email_from = "contact@light-tg.com"  # Change to your own sending email
        email_to = "contact@light-tg.com"
        hostname = "mail.light-tg.com"
        login = "contact@light-tg.com"
        password = "LTD-contact2021"
        text = "Nom: " + str(name) + "\n" + "Téléphone: " + str(tel) + "\nEmail : " + str(email) + "\n" + str(message)
        smtp = SMTP_SSL(hostname)
        smtp.login(login, password)
        msg = MIMEText(text, "plain", "utf-8")
        msg["Subject"] = Header(str("Demande de Formation en : ") + subject, "utf-8")
        msg["from"] = email_from
        msg["to"] = email_to

        if name == name:
            smtp.sendmail(email_to, email_from, msg.as_string())
            msg = " 👉🏾👉 Votre message a été envoyé avec succès, LTG vous contactera bientôt"
        else:
            msg = "error"
    return render_template('formation.html', msg=msg)


@app.route("/travaux")
def travaux():
    return render_template('travaux.html')


@app.route("/devis", methods=['POST', 'GET'])
def devis():
    msg = " "
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        tel = request.form['tel']
        subject = request.form['subject']
        message = request.form['message']
        email_from = "contact@light-tg.com"  # Change to your own sending email
        email_to = "contact@light-tg.com"
        hostname = "mail.light-tg.com"
        login = "contact@light-tg.com"
        password = "LTD-contact2021"
        text = "Nom: " + str(name) + "\n" + "Téléphone: " + str(tel) + "\nEmail : " + str(email) + "\n" + str(message)
        smtp = SMTP_SSL(hostname)
        smtp.login(login, password)
        msg = MIMEText(text, "plain", "utf-8")
        msg["Subject"] = Header(str("choix du service : ") + subject, "utf-8")
        msg["from"] = email_from
        msg["to"] = email_to

        if name == name:
            smtp.sendmail(email_to, email_from, msg.as_string())
            msg = " 👉🏾👉 Votre message a été envoyé avec succès, LTG vous contactera bientôt"
        else:
            msg = "error"
    return render_template('devis.html', msg=msg)


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    msg = " "
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        tel = request.form['tel']
        subject = request.form['subject']
        message = request.form['message']
        email_from = "contact@light-tg.com"  # Change to your own sending email
        email_to = "contact@light-tg.com"
        hostname = "mail.light-tg.com"
        login = "contact@light-tg.com"
        password = "LTD-contact2021"
        text = "Nom: " + str(name) + "\n" + "Téléphone: " + str(tel) + "\nEmail : " + str(email) + "\n" + str(message)
        smtp = SMTP_SSL(hostname)
        smtp.login(login, password)
        msg = MIMEText(text, "plain", "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        msg["from"] = email_from
        msg["to"] = email_to

        if name == name:
            smtp.sendmail(email_to, email_from, msg.as_string())
            msg = " 👉🏾👉 Votre message a été envoyé avec succès, LTG vous contactera bientôt"
        else:
            msg = "error"
    return render_template('contact.html', msg=msg)
"""

if __name__ == '__main__':

    app.run(debug=True)





