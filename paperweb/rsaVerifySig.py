from Crypto.PublicKey import RSA
from Crypto.Random import random
from Crypto.Hash import SHA256
import base64
import gmpy2


# 生成哈希摘要
def hash_my(L, e, m, u, v):
    L = str(L)
    e = str(e)
    m = str(m)
    u = str(u)
    v = str(v)
    data = L + e + m + u + v
    hash_object = SHA256.new(data.encode())
    return int(hash_object.hexdigest(), 16)


def sig_verify():
    # 读取输入的数据
    with open('db/n.json', 'r') as f:
        n = int(f.read())
    with open('db/message.txt', 'r') as f:
        m = f.read()
    with open('db/sigma.txt', 'r') as f:
        sigma = f.read()
        # 读取sigma中的数组
        listSigma = sigma.split('\n')
        c = [0 for x in range(0, n)]
        s = [0 for x in range(0, n)]
        s_ = [0 for x in range(0, n)]
        c[0] = int(listSigma[0])
        for i in range(n):
            s[i] = int(listSigma[1 + i])
        for i in range(n):
            s_[i] = int(listSigma[1 + n + i])
        e_ = int(listSigma[-2])
        r = int(listSigma[-1])
    with open('db/L.txt', 'r') as f:
        L = f.read()
        Le = [0 for x in range(0, n)]
        Ln = [0 for x in range(0, n)]
        listL = L.split('\n')
        for i in range(n):
            Ln[i] = int(listL[i])
        for i in range(n):
            Le[i] = int(listL[n + i])

    # 开始验证
    z = [0 for x in range(0, n)]
    z_ = [0 for x in range(0, n)]
    for i in range(n):
        z[i] = c[i] + gmpy2.powmod(s[i], Le[i], Ln[i])
        z_[i] = c[i] + gmpy2.powmod(s_[i], e_, Ln[i])
        if i != n - 1:
            c[i + 1] = hash_my(L, e_, m, z[i], z_[i])

    answer = hash_my(L, e_, m, z[n - 1], z_[n - 1])
    if c[0] == answer:
        print('true')
        print('签名验证完成')
        return True
    else:
        print('false')
        return False


if __name__ == "__main__":
    sig_verify()
