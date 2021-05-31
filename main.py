# A set of classes and utils for reuse in other projects.
# Being collate here for reference, copy and paste to other projects.

class EmailAddres(object):
    """
    A class for processing email addresses
    """
    def __init__(self, emailAddr):
        self.emailAddr = str(emailAddr)

        self.emailAddrName = self.emailAddr.split("@")[0]
        self.emailAddrDomain = self.emailAddr.split("@")[1]

    def __str__(self):
        return self.emailAddr + "," +self.emailAddrName


def main():
    emailaddr = EmailAddres("peter.rabbit@microsoft.com")
    print(emailaddr.__dict__)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
