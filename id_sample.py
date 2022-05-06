# コピーして使う

from time_measurement import measurement

def input_num(n):
    num = 1
    for i in range(1,n+1,1):
        num *= i
    return num

N = int(input('input N >>'))
measurement(input_num(N))