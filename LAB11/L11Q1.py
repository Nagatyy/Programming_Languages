import re

def numberCheck(number):
    phone_re = re.compile('(\(?\d{3}\)?(\s|-)|0)((50|55|56)|[234679])-\d{7}')
    matcher = phone_re.fullmatch(number)

    print(matcher.string + " is a valid phone number" if matcher is not None else
          number + " is not a valid phone number")

numberCheck("(971) 50-5672722")
numberCheck("971-55-6713432")
numberCheck("971-6-5150000")
numberCheck("056-8887272")
numberCheck("051-8887272")




