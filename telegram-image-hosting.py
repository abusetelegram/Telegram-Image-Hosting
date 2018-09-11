# -*- coding: utf-8 -*-
import urllib.request
import sys
import re

if len(sys.argv) <= 1 :
    print('Arg is missing, E.g: python3 telegram-image-hosting.py https://t.me/ButNothingHappened/2614')
    sys.exit(1)

r = urllib.request.urlopen(sys.argv[1]+'/?embed=1')

if r.getcode() == 404:
    print('Requested url does not exist, please check.')
    sys.exit(1)

result = re.findall(r'(https:\/\/)(cdn)(\w)(.telesco\.pe)([^"\']*)', r.read().decode('utf8'))

if result is not None:
    print(str(len(result)) + ' Resource(s) found: ')
    for i in result:
        print(''.join(str(e) for e in i))
else:
    print('No Resource found in this link')