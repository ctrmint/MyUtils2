# A set of classes and utils for reuse in other projects.
# Being collate here for reference, copy and paste to other projects.
import re


class EmailAddress(object):
    """
    A class for processing email addresses
    """

    def __init__(self, email_addr):
        self.emailAddr = str(email_addr)
        self.emailAddr_valid = True

        if self.validate_emailaddr(self.emailAddr):
            self.emailAddrName = self.emailAddr.split("@")[0]
            self.emailAddrDomain = self.emailAddr.split("@")[1]
        else:
            self.emailAddr_valid = False

    @staticmethod
    def validate_emailaddr(emailaddr):
        """
        Check's the email address supplied is valid.
        :param emailaddr:
        :return:
        """
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(regex, emailaddr):
            return True
        return False

    def __str__(self):
        return self.emailAddr + "," + self.emailAddrName


def main():
    emailaddr = EmailAddress("peter.rabbit@microsoft.com")
    print(emailaddr.__dict__)
    return


if __name__ == '__main__':
    main()
