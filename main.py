# A set of classes and utils for reuse in other projects.
# Being collate here for reference, copy and paste to other projects.
# ---------------------------------------------------------------------------------------------------------------------
#
import re


class IPv4(object):
    """
    Base class for an IPv4 address
    """
    def __init__(self, ipv4addr=None, subnet=None, cidr=None):
        """
        ipv4addr is considered mandatory, subnet and cidr optional
        :param ipv4addr: IPv4 address value, eg 192.168.0.1.
        :param subnet: subnet of IPv4 address, eg 255.255.255.0
        :param cidr:
        """
        self.ipv4Addr = ipv4addr
        if not self.validate_ipv4():
            raise ValueError('Invalid IPv4 address supplied! {}'.format(self.ipv4Addr))
        else:
            self.ipv4_defang = "[.]".join(self.ipv4Addr.split("."))
            self.split_octet()

        if subnet:
            self.subnet = subnet
            if self.validate_subnet():
                self.cidr = (sum([bin(int(bits)).count("1") for bits in self.subnet.split(".")]))
            else:
                raise ValueError(' {} is not a valid subnet'.format(self.subnet))
        else:
            if cidr and not subnet:
                self.cidr = cidr

    def validate_ipv4(self):
        regex = '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
        return re.search(regex, self.ipv4Addr)

    def validate_subnet(self):
        regex = '^(255)\.(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)'
        return re.search(regex, self.subnet)

    def split_octet(self):
        self.octets = {}
        octet_list = self.ipv4Addr.split('.')
        count = 0
        for octet in octet_list:
            self.octets[("octet_" + str(count + 1))] = octet_list[count]
            count += 1
        return

class EmailAddress(object):
    """
    A base class for processing email addresses.
    """

    def __init__(self, email_addr):
        self.emailAddr = str(email_addr)
        self.emailAddr_valid = True

        if self.validate_emailaddress():
            self.emailAddrName = self.emailAddr.split("@")[0]
            self.emailAddrDomain = self.emailAddr.split("@")[1]
            self.emailAddr_defang = "[.]".join(self.emailAddr.split("."))
        else:
            self.emailAddr_valid = False

    def validate_emailaddress(self):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        return re.search(regex, self.emailAddr)

    def __str__(self):
        return self.emailAddr + "," + self.emailAddrName


def main():
    emailaddr = EmailAddress("peter.rabbit@microsoft.com")
    print(emailaddr.__dict__)
    ip = IPv4('192.168.0.1', subnet="255.255.255.0")
    print(ip.__dict__)
    return


if __name__ == '__main__':
    main()
