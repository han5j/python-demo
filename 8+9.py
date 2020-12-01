age = input('請輸入存活時間:')
age = int(age)
if age < 13:
    print('小猴')
elif age >= 13 and age < 18:
    print('8+9')
elif age >= 19 or age < 88:
    print('18+++')
else:
    print('be a man')