from datetime import datetime, timedelta, time
import os

LOG_FILE_PATH = r'logs/email_log.txt'


def create_log_file_if_not_exist(log_file_path: str):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    if not os.path.isfile(log_file_path):
        with open(log_file_path, 'w+') as file:
            file.write('')


def count_send_email_per_day() -> int:
    create_log_file_if_not_exist(LOG_FILE_PATH)

    with open(LOG_FILE_PATH, 'r', encoding='utf-8') as email_log_file:
        email_log = email_log_file.readlines()

        now_datetime = datetime.now()
        datetime_format = "%Y-%m-%d %H:%M:%S.%f"
        count_emails = 0

        for log in email_log[::-1]:
            log = log[:-2]  # delete \n symbol

            if (now_datetime - datetime.strptime(log, datetime_format)).days < 1:
                count_emails += 1
            else:
                break

    return count_emails


def write_log_time_send_email() -> None:
    create_log_file_if_not_exist(LOG_FILE_PATH)

    with open(LOG_FILE_PATH, 'r+', encoding='utf-8') as email_log_file:
        email_log_file.readlines()
        email_log_file.write(f'{datetime.now()}\n')


if __name__ == '__main__':
    print(count_send_email_per_day())
    write_log_time_send_email()
