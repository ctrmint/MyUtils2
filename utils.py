# ---------------------------------------------------------------------------------------------------------------------
# A set of classes and utils for reuse in other projects.
# Being collate here for reference, copy and paste to other projects.
# ---------------------------------------------------------------------------------------------------------------------
#
import re


class DomainName(object):
    """
    Class for a domain name
    """
    def __init__(self, domainname):
        self.domainname = domainname
        self.domainname_defang = ''
        self.domain_list = []

        if not self.validate_domain():
            raise ValueError('Invalid Domain Name supplied'.format(self.domainname))
        else:
            self.domain_list = self.domainname.split('.')
            self.domainname_defang = "[.]".join(self.domainname.split("."))

    def validate_domain(self):
        regex = '^([a-z][a-z0-9+\-.]*)'
        return re.search(regex, self.domainname)

    def __str__(self):
        return self.domainname + ',' + str(self.domain_list)


class URL(object):
    """
    Base class for URL
    """
    def __init__(self, url):
        self.url = url
        self.url_scheme = self.url.split(":")[0]
        self.url_authority = re.findall("^http|https:///?([a-z][a-z0-9+\-.]:([0-9]+)", self.url)[1]
        self.url_domain = re.search("^http|https:///?([a-z][a-z0-9+\-.]*)", self.url)[1]
        if ":" in self.url_authority:
            self.port = self.url_authority.split(":")[1]


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
            self.emailAddrDomain = DomainName((self.emailAddr.split("@")[1]))
            self.emailAddr_defang = "[.]".join(self.emailAddr.split("."))
        else:
            raise ValueError('Invalid email address supplied'.format(self.emailAddr))

    def validate_emailaddress(self):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        return re.search(regex, self.emailAddr)

    def __str__(self):
        return self.emailAddr + "," + self.emailAddrName + str(self.emailAddrDomain2)


def main():
    emailaddr = EmailAddress("peter.rabbit@microsoft.com")
    print(emailaddr.__dict__)
    print(emailaddr.emailAddrDomain.__dict__)
    ip = IPv4('192.168.0.1', subnet="255.255.255.0")
    print(ip.__dict__)
    #url = URL("http://www.w3schools.com:443/python/python_regex.asp")
    #print(url.__dict__)
    return


if __name__ == '__main__':
    main()
