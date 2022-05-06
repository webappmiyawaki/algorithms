print('N以下の整数でXの倍数またはYの倍数であるものの個数を表示させるプログラム\n')

N = int(input('Nを入力してください。'))
X = int(input('Xを入力してください。'))
Y = int(input('Yを入力してください。'))

def calc_num_list(max_num:int, num01:int, num02:int) -> list:
    result_list:list = []
    for i in range(1, max_num+1, 1):
        if i % num01 == 0:
            result_list.append(i)
        elif i % num02 == 0:
            result_list.append(i)
        else:
            continue
    return result_list

r_list = calc_num_list(N, X, Y)
print(r_list)