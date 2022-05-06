from typing import List, Union

def cal_multi(n_list:list) -> int:
    base_num = 1
    print(n_list)
    for num in n_list:
        base_num *= num
    return base_num

print('n個の整数を入力してください\n数字以外を入力したら入力終了です。\n')

num_list:int = []

while True:
    try:
        num_list.append(int(input('input num>>')))
    except ValueError:
        break

print(cal_multi(num_list))