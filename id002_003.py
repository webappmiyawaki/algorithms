print('n個の整数を入力してください\n数字以外を入力したら入力終了です。\n')

num_list:int = []

while True:
    try:
        num_list.append(int(input('input num>>')))
    except ValueError:
        break

print(sum(num_list))