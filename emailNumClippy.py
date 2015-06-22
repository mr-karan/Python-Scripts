import phonenumbers
import pyperclip
import re

text = str(pyperclip.paste())
matches=[]

emailRegex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

for groups in emailRegex.findall(text):
       matches.append(groups[0])    #groups[0] is email address ; groups[1] is '.com'

for match in phonenumbers.PhoneNumberMatcher(text, "IN"):
    matches.append(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))      #A new Line character is added to every list element
    print('\n'.join(matches))
else:
    print('No Matches Found.')



