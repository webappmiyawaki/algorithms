N = int(input('input N>>'))
S = int(input('input S>>'))

# 上限Sまで
counter = 0
for i in range(1, N+1, 1):
    for j in range(1, S+1, 1):
        if i+j <=S:
            counter += 1
            # print(f'i:{i} j:{j} i + j = {i+j}')

print()
print(f'{counter}通り')
