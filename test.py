import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email_logger import count_send_email_per_day, write_log_time_send_email
from email_data.conf import LOGIN, PASSWORD


def send_email(recipient_email: str | list, header_text: str, msg_text: str):
    if isinstance(recipient_email, list) and len(recipient_email) > 35:
        print('Количество получателей не должно превышать 35 за одну рассылку')
        return
    _cnt = count_send_email_per_day()
    if _cnt + len(recipient_email) > 3:
        print(f'Лимит на отправку писем в сутки превышен!')
        return

    login = LOGIN
    password = PASSWORD

    s = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)

    try:
        s.ehlo()
        s.starttls()
        s.login(login, password)
        s.sendmail(login, ', '.join(recipient_email), msg.as_string())
        for _ in range(len(recipient_email)):
            write_log_time_send_email()
        print(f'Сообщение было успешно отправлено! Сегодня еще можно отправить {3 - _cnt - 1} писем.')
    except Exception as _ex:
        print(_ex)
    finally:
        s.quit()


def main():
    emails = ['pythonscriptovich@yandex.ru']
    header = 'Заголовок 2'
    message = 'Тестовое тело сообщения 2'
    send_email(emails, header, message)
    emails = ['pythonscriptovich@yandex.ru']
    header = 'Заголовок 2'
    message = 'Тестовое тело сообщения 2'
    send_email(emails, header, message)


if __name__ == '__main__':
    main()
