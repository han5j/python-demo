print('9527')
name = 'hans'
print("嗨,\
      你好", name, '992884')
cat = input("請輸入你的貓")
print(cat)
print('單引號包"雙引"號')

try:
    age = int(input('請輸入貓的年齡:'))
    print(format(age , '你可以投票' if age >= 20 else '去找媽媽'))
except ValueError:
    print('年齡一般都是阿拉伯數字')
# if age.isdigit():
#     pass
# age = int(age)
# try:
#    if age.isdigit()
# except:
#     print("Wrong input")
# if age >= 20:
#     print('你可以投票')
# else:
#     print('去找媽媽')

