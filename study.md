# study

p.37
床関数、天井関数、ガウス記号

p.53
math.log(x, y)はyを底としたxの対数を返す。

p.63
2重for文で、内ループをbreak以外で終了した場合の処理

```Python
for i in l1:
    print('Start outer loop')

    for j in l2:
        print('--', i, j)
        if i == 2 and j == 20:
            print('-- BREAK inner loop')
            break
    else:
        print('-- Finish inner loop without BREAK')
        continue

    print('BREAK outer loop')
    break
```
