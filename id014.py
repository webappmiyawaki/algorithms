# 自然数Nを素因数分解するプログラム

N = int(input('input N >>'))

i = 2
num_list = []
while True:
    if N > i:
        if N % i == 0:
            num_list.append(i)
            N = int(N / i)
            print(f'N={N}')
        else:
            i+=1
    else:
        num_list.append(N)
        break

print(num_list)