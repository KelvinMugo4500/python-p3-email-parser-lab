import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        
        pattern = r'[\w\.-]+@[\w\.-]+'
        addresses = re.findall(pattern, self.email_addresses)

        
        unique_addresses = sorted(set(addresses))

        return unique_addresses
