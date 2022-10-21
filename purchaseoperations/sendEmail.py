import smtplib
import ssl
from email.message import EmailMessage
from purchaseoperations.admininfo import sender_email, sender_password
from dotenv import load_dotenv
_ = load_dotenv()

shop_name = "ROCKS SHOP"
cashier_name = "Eric Kyalo"
receipt_message = "Thank you for shopping with us"


def send_purchase_receipt(name, email, purchase_dictionary):
    EMAIL_ADDRESS = sender_email
    EMAIL_PASSWORD = sender_password
    recipient_email = "kyalokioko98@gmail.com"
    subject = ' Below is your receipt. Thank you for shopping with us!!'

    body = ''
    body += f'\t\tReceipt<br>'
    body += f'\t\t{shop_name.title()}<br>'
    body += '------------------------------------<br>'
    body += f'Customer: {name}<br>'
    body += '--------------------------------------<br>'
    body += f'Customer: {email}<br>'
    body += '--------------------------------------<br>'
    body += f'Cashier: {cashier_name}<br>'

    body += '---------------------------------------<br>'
    body += 'PURCHASE ITEMS<br>'
    body += "product_name | product_quantity | total_price<br>"
    for key, value in purchase_dictionary:
        print(key, value)
        body += f"{['product']} | {['quantity']} | {['price']}<br>"

    body += '------------------------------------------<br>'
    body += f"Net Total (paid)\t\t\t\t Kes {purchase_dictionary[-1]['to pay']:.2f}<br>"

    body += f"{receipt_message}<br>"
    body += ''

    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)
    headers = ["From: " + EMAIL_ADDRESS,
               "To: " + recipient_email,
               "Subject: " + subject,
               "Content-Type: text/html"]

    context = ssl.create_default_context()

    print("Email has been send successfully to" + recipient_email)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, recipient_email, "\r\n".join(headers) + "\r\n\r\n" + body)


