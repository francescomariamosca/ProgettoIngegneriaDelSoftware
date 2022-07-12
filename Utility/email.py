import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class email():
    def __init__(self):
        self.context = ssl.create_default_context()
        self.senderEmail = "centrosportivounivpm@gmail.com"
        self.password = "kdptimxzwhafawsn"
        pass

    def emailScadenzaAbbonamento(self, email, nome, cognome):
        recEmail = email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Prenotazione avvenuta con successo"
        message["From"] = self.senderEmail
        message["To"] = recEmail

        text = f"""\
           Caro {nome} {cognome},
           Il suo abbonamento sta per scadere, si ricordi di rinnovarlo!
           """
        part = MIMEText(text, "plain")
        message.attach(part)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as server:
            server.login(self.senderEmail, self.password)
            server.sendmail(self.senderEmail, recEmail, message.as_string())

    def emailPrenotazioneAvvenuta(self, email, nome, cognome, data, ora, campo):
        recEmail = email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Prenotazione avvenuta con successo"
        message["From"] = self.senderEmail
        message["To"] = recEmail

        text = f"""\
Caro {nome} {cognome},
La sua prenotazione per il campo: {campo} in data: {data} alle ore: {ora} è avvenuta 
con successo!
Buona giornata da tutto lo staff del Centro Sportivo!
                """
        part = MIMEText(text, "plain")
        message.attach(part)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as server:
            server.login(self.senderEmail, self.password)
            server.sendmail(self.senderEmail, recEmail, message.as_string())




    def emailPrenotazioneCancellata(self, email, nome, cognome, data, ora, campo):
        recEmail = email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Prenotazione eliminata con successo"
        message["From"] = self.senderEmail
        message["To"] = recEmail

        text = f"""\
Caro {nome} {cognome},
La sua prenotazione per il campo: {campo} in data: {data} 
alle ore: {ora} è stata cancellata.
Buona giornata da tutto lo staff del Centro Sportivo!
                """
        part = MIMEText(text, "plain")
        message.attach(part)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as server:
            server.login(self.senderEmail, self.password)
            server.sendmail(self.senderEmail, recEmail, message.as_string())