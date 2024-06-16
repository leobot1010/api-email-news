import smtplib, ssl


def send_email(titles_and_descriptions):
    host = "smtp.gmail.com"
    port = 465

    username = "leobot1010@gmail.com"
    password = 'vuihokpyyfphutnc'

    receiver = 'kieran303@hotmail.com'
    # receiver = 'leobot1010@gmail.com'

    context = ssl.create_default_context()
#     message = f"""\
# Subject: Tesla daily news\n
# {titles_and_descriptions}
# """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, titles_and_descriptions)
