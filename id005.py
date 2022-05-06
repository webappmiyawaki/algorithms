print('N個の整数mod100の値を出力するプログラムです。')
n = int(input('個数を指定してください。 >>'))

num_list = []
[num_list.append(i) for i in range(1,n+1,1)]
    
print(f'total={sum(num_list)}')
print(f'total(mod100) = {sum(num_list)%100}')