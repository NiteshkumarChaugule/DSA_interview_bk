"""
Assuming that we have some email addresses in the "username@companyname.com" format, please write program that;

•	Print the “username” of a given email address.
•	Prints the “companyname” of a given email address
"""


def parse_email(email_id):
    at_index = email_id.rfind("@")
    print(f"username = {email_id[:at_index]}")
    print(f"domain = {email_id[at_index + 1:email_id.rfind('.')]}")


if __name__ == '__main__':
    parse_email("username@companyname.com")
