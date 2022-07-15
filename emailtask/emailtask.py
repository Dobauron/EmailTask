import csv
from contextlib import contextmanager
import typer


@contextmanager
def open_file(name):
    f = open(name, 'r')
    try:
        yield f
    finally:
        f.close()

class EmailCollector:
    def __init__(self):
        self.all_email = []
        self.incorrect_email_list = []
        self.correct_email_list = []
        self.data_from_logs_file = []
        self.open_files_read_email()
        self.clear_files_from_whitespace()
        self.validate_email()


    def open_files_read_email(self):
        with open_file('/home/dob/PycharmProjects/emailtask - dobromir matuszak/'
                       'recruitment-task-backend-internship-main/'
                       'emails/email-pack-1.txt') as email_pack_1, \
                open_file('/home/dob/PycharmProjects/emailtask - dobromir matuszak/'
                          'recruitment-task-backend-internship-main/emails/emails-pack-2.txt') as email_pack_2, \
                open_file('/home/dob/PycharmProjects/emailtask - dobromir matuszak/'
                          'recruitment-task-backend-internship-main/emails/emails3.txt') as email_pack_3, \
                open_file('/home/dob/PycharmProjects/emailtask - dobromir matuszak/'
                          'recruitment-task-backend-internship-main/emails/other-emails4.txt') as email_pack_4, \
                open_file('/home/dob/PycharmProjects/emailtask - dobromir matuszak/'
                          'recruitment-task-backend-internship-main'
                          '/emails/last-email-pack.csv') as email_pack_5_CSV, \
                open_file('/home/dob/PycharmProjects/emailtask - dobromir matuszak/'
                          'recruitment-task-backend-internship-main/email-sent.logs') as email_pack_6_logs:

            email_pack_list = [email_pack_1,
                               email_pack_2,
                               self.clear_email_from_csv_file(email_pack_5_CSV),
                               email_pack_4,
                               email_pack_3,
                               ]

            for email_pack in email_pack_list:
                for email in email_pack:
                    self.all_email.append(email)

            for logs_email in email_pack_6_logs:
                self.data_from_logs_file.append(logs_email)



    def clear_files_from_whitespace(self):
        temporary_list = []
        for line in self.all_email:
            line = line.strip('\n')
            temporary_list.append(line)
        self.all_email = temporary_list

    def clear_email_from_csv_file(self, csv_file):
        reader = csv.reader(csv_file, delimiter=';')
        temporary_list = []
        header = 'email'
        for row in reader:
            if row[1] == header:
                continue
            temporary_list.append(row[1])

        return temporary_list

    def validate_email(self):
        for email in self.all_email:
            if email.count('@') != 1 \
                    or email.find('@') < 1 \
                    or email.find('@.') > -1 \
                    or email.find('.@') > -1 \
                    or email.rfind('.') < 1 \
                    or email.rfind('.') > 4 \
                    and email[email.rfind('.'):].isalnum():
                self.incorrect_email_list.append(email)
            else:
                self.correct_email_list.append(email)

    def search_value(self, phrase):
        for email in self.all_email:
            if phrase in email:
                print(phrase)
                print(email)

    def sort_by_domain(self):
        domain_dict = {}
        for email in self.correct_email_list:
            domain = email.split('@')[1]
            if domain in domain_dict:
                domain_dict[domain].append(email)
            else:
                domain_dict[domain] = [email]

        for item, value in sorted(domain_dict.items()):
            ListToStr = '\n\t'.join(map(str, sorted(value)))
            print(f'Domain {item} ({len(value)}):\n\t{ListToStr}')

    def clear_data_logsfile_to_obtain_email(self, file):
        logs_email_list = []
        for line in file:

            email = line.split('\'')
            logs_email_list.append(email[1])


        return logs_email_list

    def is_exist_logsemail_in_all_email(self):
        message_not_send_to_email_list = []
        logs_email = self.clear_data_logsfile_to_obtain_email(self.data_from_logs_file)
        for email in self.correct_email_list:

            if email not in logs_email:
                message_not_send_to_email_list.append(email)

        return sorted(message_not_send_to_email_list)
E = EmailCollector()
import sys


if __name__ == '__main__':
    print(E.is_exist_logsemail_in_all_email())

# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# # parser.add_argument('--incorrect-email', '-ic', required=False)
# # parser.add_argument('--search', '-s', type =str)
# # parser.add_argument('--group-by-domain', '-gbd')
# # parser.add_argument('--find-emails-not-in-logs', '-feil')
#
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
# args = parser.parse_args()
# print(args)
# parser = argparse.ArgumentParser()
#
# parser.add_argument("filename", help="path to a file to process")
# parser.add_argument(
#     "-s", "--search",
# )
# app = typer.Typer()

# def main(incorrect_email: bool = typer.Option(...), search: str = typer.Option(...)):
#     if search:
#         print(E.search_value(search))
#     if incorrect_email is True:
#         for email in E.incorrect_email_list:
#             print(email)
#
# @app.command('gbd')
# def gbd_email():
#     E.sort_by_domain()
#
# @app.command('ic')
# def email():
#     for email in E.incorrect_email_list:
#         print(email)
#
#
# @app.command('s')
# def email(
#         search: str = typer.Option(...)
# ):
#     print(E.search_value(search))
#
# @app.command('feil')
# def email_logsfile():
#     for email in E.is_exist_logsemail_in_all_email():
#         print(email)
# if __name__ == "__main__":
#     app()

# class File:
#     def __init__(self, file_name, method):
#         self.file_obj = open(file_name, method)
#
#     def __enter__(self):
#         return self.file_obj
#
#     def __exit__(self, type, value, traceback):
#         self.file_obj.close()
#

# class EmailReader:
#     def __init__(self):
#         self.all_email_list = []
#         self.incorrect_email_list = []
#         with File(
#                 '/home/dob/PycharmProjects/emailtask - dobromir matuszak/recruitment-task-backend-internship-main/'
#                 'emails/email-pack-1.txt',
#                 'r') as emails_pack_1:
#                 for email in emails_pack_1.readlines():
#                     email = email.strip('\n')
#                     self.all_email_list.append(email)
#
#     def show_incorrect_email(self):
#
#         for email in self.all_email_list:
#             if email.count('@') != 1:
#                 self.incorrect_email_list.append(email)
#             if email.find('@') < 1:
#                 self.incorrect_email_list.append(email)
#             inproper_dot_at_conf = ['@.', '.@']
#             if email.find('@.') > -1 or email.find('.@') > -1:
#                 self.incorrect_email_list.append(email)
#             if email.rfind('.') < 1 or email.rfind('.') > 4:
#                 if email[email.rindex('.'):].isalnum():
#                     self.incorrect_email_list.append(email)
#
#
# o = EmailReader()
#
# o.show_incorrect_email()
# for email in o.incorrect_email_list:
#     print(email)

# import typer
# from typing import Optional
#
# app = typer.Typer()
#

# @app.command()
# def incorrect_email():
#     print('number of incorrect email = ', len(E.incorrect_email_list))
#     for email in E.incorrect_email_list:
#         print(email)
#
# @app.command()
# def ic():
#     print('uha')
# if __name__ == "__main__":
#     app()
#
# @app.command("ic")
# def ic( username:str,
#          incorrect_email: bool = True,
#          ):
#     for email in E.incorrect_email_list:
#         print(email)

# @app.command()
# def ic(
#         username:str):
#     for email in E.incorrect_email_list:
#         print(email)
