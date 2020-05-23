from Crypto.PublicKey import RSA
import gmpy2
import json


# e = a*b mod c
def MulMod(a, b, c):
    return gmpy2.t_mod(a * b, c)


# d*a = 1 mod b, 返回d
def InvMod(a, b):
    t = gmpy2.invert(a, b)
    return t


def sig_convert(k):
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

    # 读取Uk的私钥
    private_key = RSA.import_key(open('db/pem/private_key' + '_U' + str(k) + '.pem', "rb").read())
    d = private_key.d

    # 读取json
    with open("db/akr/akr" + str(k) + ".json", 'r') as f:
        load_dic = json.load(f)
    if load_dic['ak'] != 0:
        ak = load_dic['ak']
        r = load_dic['r']

    phi_n = (private_key.p - 1) * (private_key.q - 1)
    ak_1 = InvMod(ak, phi_n)
    e_2 = MulMod(ak_1, r, phi_n)
    if e_ == e_2:
        print('True')
        return True
    else:
        print('False')
        return False


if __name__ == "__main__":
    sig_convert(1)