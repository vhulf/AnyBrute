# LIBRARY FUNCTIONS FOR FORCING ANY IDENTIFIERS
# SHOULD BE USED BY OTHER SCRIPTS, NOT RAN ON ITS OWN

import random

# EX: generate(7) 
#           -> bcf4b14
#     generate(7, 'ascii_uppers_and_numbers) 
#           -> bcf4b14
def generate(length, charset='hex_upper'):
    gen = ""
    
    if charset == 'nums':
        charset = "1234567890"
    elif charset == 'hex_upper':
        charset = "ABCDEF1234567890"
    elif charset == 'hex_lower':
        charset = "abcdef1234567890"
    elif charset == 'ascii_upper':
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif charset == 'acii_lower':
        charset = "abcdefghijklmnopqrstuvwxyz"
    elif charset == 'ascii_upper_and_nums':
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    elif charset == 'ascii_lower_and_nums':
        charset = "abcdefghijklmnopqrstuvwxyz1234567890"
    elif charset == 'ascii_upper_lower_and_nums':
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    elif charset == 'ascii_all_printable':
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890<>?,./:;'{}|[]\"\\~`!@#$%^&*()-_=+ "
    else:
        charset = charset

    for _ in range(0, int(length)):
        rand = random.randint(0, len(charset) - 1)
        gen += charset[rand]
    return(gen)

# EX: generateFromForm("XXX-XXXXotherXXXX") 
#           -> f8d-7b3cother6195
#      generateFromForm("X-ClientID: ZZZZZ-ZZZZZZZZ-ZZZZZZZZZZZZ", control_char="Z") 
#           -> X-ClientID: 79ca5-415c331f-1108fb5925bb
def generateFromForm(form, control_char="X", charset='ascii_upper_and_nums'):
    template = form

    while template.count(control_char) != 0:
        newChar = generate(2, charset)
        template = template.replace(control_char, newChar[0], 1)
    
    return(template)


# TESTING STUFFS!
# print(generate(7, 'ascii_upper_and_nums'))
# print(generateFromForm("XXX-XXXXotherXXXX"))
# print(generateFromForm("X-ClientID: ZZZZZ-ZZZZZZZZ-ZZZZZZZZZZZZ", control_char="Z"))