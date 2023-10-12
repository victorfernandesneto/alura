import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def validate_url(self):
        if not self.url:
            raise ValueError("URL is empty.")
        pattern = '(http(s)?://)?(www.)?boxrec.com/en/search'
        base = re.compile(pattern)
        if not base.match(self.url):
            raise ValueError("URL is not valid.")
        
    
    def get_url_base(self):
        qm_index = self.url.find('?')
        return self.url[:qm_index]
    
    def get_url_parameters(self):
        qm_index = self.url.find('?')
        return self.url[qm_index+1:]
    
    def get_value_parameter(self, parameter):
        parameter_index = self.url.find(parameter)
        value_index = parameter_index + len(parameter) + 4
        ec_index = self.url.find('&', value_index)
        if ec_index == -1:
            value = self.url[value_index:]
        else:
            value = self.url[value_index:ec_index]
        return value
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url
    
abner = ExtratorURL('https://boxrec.com/en/search?p%5Bfirst_name%5D=abner&p%5Blast_name%5D=&p%5Brole%5D=box-am&p%5Bstatus%5D=')
print(abner.get_url_base())
print(abner.get_url_parameters())
print(abner.get_value_parameter('first_name'))
print(abner.get_value_parameter('last_name'))
print(abner.get_value_parameter('role'))