data = [['春', '夏', '秋', '冬'], ['さくら', 'うみ', 'いちょう', 'こたつ']]

# 問1
print('q1')
[print(text,end=',') for ary in data for text in ary]
print()

# 問2
print('q2')
for ary in data:
    for i in range(len(ary)-1,-1,-1):
        print(f'\'{ary[i]}\'',end=',')
    print()

# 問3
print('q3')
for i in range(len(data)):
    data[i].reverse()

i = 0
j = 0
while i < len(data):
    while j < len(data[i]):
        print(f'\'{data[i][j]}\'',end=',')
        j += 1
    print()
    i += 1
    j = 0

[print(val,end=',')  for i in range(len(data)) for val in reversed(data[i])]