from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'r')
    try:
        yield f
    finally:
        f.close()


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
                  'recruitment-task-backend-internship-main/emails/last-email-pack.csv') as email_pack_5:
    email_pack_list = [email_pack_1, email_pack_2, email_pack_3, email_pack_4, email_pack_5]
    for email_pack in email_pack_list:
        for email in email_pack.readlines():
            print(email)


class EmailCollector:
    def __init__(self):
        self.all_email = []


            # for email_pack in email_pack_list:
            #     for email in email_pack.readlines():
            #
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
                          'recruitment-task-backend-internship-main/emails/last-email-pack.csv') as email_pack_5:
                self.email_pack_list = [email_pack_1, email_pack_2, email_pack_3, email_pack_4, email_pack_5]

        return self.email_pack_list


    def clear_files(self):
        for line in self.file.readlines():
            line = line.strip('\n')

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
