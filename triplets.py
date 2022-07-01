# 5000以下の三つ子素数を列挙するプログラム
# %%
# 5000以下の素数のリストprimesを作成
primes = []
for i in range(2,5000):
    for j in range(2,i//2+1):
        if i % j == 0:
            break
    else:
        primes.append(i)
# %%
# 三つ子素数の印字
for i in primes:
    if i+2 in primes and i+6 in primes:
        print(i,i+2,i+6)
    elif i+4 in primes and i+6 in primes:
        print(i,i+4,i+6)
# %%
