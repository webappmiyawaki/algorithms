from time_measurement import measurement
from math import sqrt

def input_num(n):
    num_list = [2]
    for i in range(3,n+1,1):
        for num in num_list:
            if i % num == 0:
                break
        else:
            num_list.append(i)
    num_list.insert(0,1)
    return num_list

N = int(input('input N >>'))
measurement(input_num(N))