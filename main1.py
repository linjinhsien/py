def check(**kwargs):
    print(kwargs)
    if 'alc' in kwargs:
        print('酒駕,酒精濃度:{}'.format(kwargs['alc']))
    if 'license' not in kwargs:
      print('無照')
check(name='Peter', alc='0.3',license='true')