# ユークリッドの互除法を使った最大公約数の求め方

def gcd(n_list):
    i = 2
    r_list = []
    max_num = max(n_list)
    while True:
        if max_num > i:
            j = 0
            for j in range(len(n_list)):
                if n_list[j] % i == 0:
                    print(f'n_list[{j}] ok')
                else:
                    print('break')
                    break
                n_list /= j
                j += 1
            else:
                print('-- Finish inner loop without BREAK')

                r_list.append(i)
                j = 0
                i += 1
        else:
            break
    return r_list


str_list = input('A1,...,An >>')

A_list = list(map(int, str_list.split()))
print(A_list)
print(gcd(A_list))