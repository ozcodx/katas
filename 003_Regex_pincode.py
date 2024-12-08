'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
'''

import re
def validate_pin(pin):
    #$ validate end of line, so \n produces wrong behaviour
    regex = re.compile("^(\d{4}|\d{6})\Z")
    return bool(re.match(regex,pin))