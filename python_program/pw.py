#!/usr/bin/python
#pw-py - An insecure password locker program

passwords={'bjtumail': '010634',
           'paperfree':'zhaomiao1001',
           'baiduwenku':'5njjimaf',
           '5njjimaf':'xl3430',
           'zhixing':'wsk6234',
           'wsk6234':'wsk87412083wsk',
           'suning':'zhaomiao541045',
           'huaxin':'zhaomiao1001',
           'zsanshui':'zhaomiao1001'
           
        }

import sys,pyperclip
if len(sys.argv)<2:
    print('please enter account')
    sys.exit()
    
account=sys.argv[1]      #the first command line arg is account

if account in passwords:
    pyperclip.copy(passwords[account])
    print('password for '+account+' copied to clipboard.')
else:
    print('There is\'t account.')
