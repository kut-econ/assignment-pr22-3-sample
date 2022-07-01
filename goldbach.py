# 4以上の偶数を２つの素数の和で表すプログラム
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
for i in range(4,101,2):
    print(i,end=' ')
    for j in range(2,i//2+1):
        # jとi-jが共に素数のときだけ印字する
        if j in primes and i-j in primes:
            print('=',j,'+',i-j,end=' ')
    print()
# %%
