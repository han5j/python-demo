import random
r = random.randint(1, 50)
# print(r)
count = 0
while True:
    print(r)
    count += 1
    num = input('幸運數字幾多?')
    num = int(num)
    if num == r:
        print('優丟ㄚ')
        break
    elif num > r:
        print('禿畢ㄍ')
    elif num < r:
        print('禿死帽')
    print('try and Error：',count,)