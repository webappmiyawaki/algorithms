from random import randint

# 3-1

# 1. True
# 2. ×
# 3. gihuはkansaiに含まれるか
# 4. a足すb 大なり60　かつ、　dayが3ならば
# 5. False

# 3-2

# 1. if initial == 'k':
# 2. if point >= 80 and point <= 256:
# 3. if bmi < 20 or bmi > 25:
# 4. if year % 4 == 0:
# 5. if day in (28,30,31):

day = 30
list = [28,30,31]
if day in list:
    print('True')


# 3-3

isError = False
n = randint(0,200)
if n % 2 == 0:
    isEven = True
else:
    isEven = False

if isError == False and n < 100:
    print(f'n={n} True isEven={isEven}')
else:
    print(f'n={n} False isEven={isEven}')

Greetings = input('あいさつを入力してください。 >>')
if Greetings == 'こんにちは':
    reply = 'ようこそ！'
elif Greetings == '景気は？':
    reply = 'ぼちぼちです'
elif Greetings == 'さようなら':
    reply = 'お元気で！'
else:
    reply = 'どうしました？'

print(reply)

# 3-4

# 1. 1,3,5,7,8,10,12
# 2. 2,3,6,9,11
# 3. 2月