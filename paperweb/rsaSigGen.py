from Crypto.PublicKey import RSA
from Crypto.Random import random
from Crypto.Hash import SHA256
import base64
import gmpy2
import json


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


# d*a = 1 mod b, 返回d
def InvMod(a, b):
    t = gmpy2.invert(a, b)
    return t


# e = a*b mod c
def MulMod(a, b, c):
    return gmpy2.t_mod(a * b, c)


# 生成签名，n_all代表总用户数，k代表当前用户编号（0~n-1)
def sig_gen(n_all, k, userlist):

    # 读取Uk的私钥
    private_key = RSA.import_key(open('db/pem/private_key' + '_U' + str(k) + '.pem', "rb").read())
    d = private_key.d

    # 从文件中读取公钥
    Ln = []  # 公钥N
    Le = []  # 公钥e
    for i in userlist:
        public_key = RSA.import_key(open('db/pem/public_key' + '_U' + str(i) + '.pem').read())
        Ln.append(public_key.n)
        Le.append(public_key.e)
        if k == i:
            k = len(Ln) - 1
    n = len(userlist)  # 新的环的长度
    with open('db/n.json', 'w') as f:
        f.write(str(n))


    # 第一步计算关联标签e_
    phi_n = (private_key.p - 1) * (private_key.q - 1)
    ak = random.randrange(1, phi_n)
    while gmpy2.gcd(ak, phi_n) != 1:
        ak = random.randrange(1, phi_n)
    r = random.randrange(1, phi_n)
    while gmpy2.gcd(r, phi_n) != 1:
        r = random.randrange(1, phi_n)


    with open('db/flagakr.json', 'r') as f:
        flagakr = f.read()

    if flagakr == 'True':  # 生成相关的关联标签
        # 读取json
        with open("db/akr/akr" + str(k) + ".json", 'r') as f:
            load_dic = json.load(f)
        if load_dic['ak'] != 0:
            ak = load_dic['ak']
            r = load_dic['r']
        # 记录当前标签随机数
        with open('db/akr/akr' + str(k) + '.json', 'w') as f:
            new_dict = {'ak': int(ak), 'r': int(r)}
            json.dump(new_dict, f)
    else:  # 生成不相关的关联标签
        for i in range(n):
            # 初始化关联标签
            new_dict = {'ak': 0, 'r': 0}
            with open("db/akr/akr" + str(i) + ".json", "w") as f:
                json.dump(new_dict, f)
        # 记录当前标签随机数
        with open('db/akr/akr' + str(k) + '.json', 'w') as f:
            new_dict = {'ak': int(ak), 'r': int(r)}
            json.dump(new_dict, f)
    ak_1 = InvMod(ak, phi_n)
    e_ = MulMod(ak_1, r, phi_n)

    # 第二步计算c_(k+1)
    u = random.randrange(1, Ln[k])
    v = random.randrange(1, Ln[k])
    # 要签名的内容
    with open('db/message.txt', 'r') as f:
        m = f.read()
    # 公钥集合
    listL = Ln + Le
    strL = [str(i) for i in listL]
    L = '\n'.join(strL)
    with open('db/L.txt', 'w') as file_object:
        file_object.write(L)

    s = [0 for x in range(0, n)]
    s_ = [0 for x in range(0, n)]
    z = [0 for x in range(0, n)]
    z_ = [0 for x in range(0, n)]
    c = [0 for x in range(0, n + 1)]  # 0~n,包含边界
    c[k + 1] = hash_my(L, e_, m, u, v)  # 当前用户后一个
    z[k] = u
    z_[k] = v
    for i in range(k + 1, n):
        s[i] = random.randrange(1, Ln[i])
        s_[i] = random.randrange(1, Ln[i])
        z[i] = c[i] + gmpy2.powmod(s[i], Le[i], Ln[i])
        z_[i] = c[i] + gmpy2.powmod(s_[i], e_, Ln[i])
        c[i + 1] = hash_my(L, e_, m, z[i], z_[i])
        # c[i+1] = hash_my(L, e_, m, c[i]+gmpy2.powmod(s[i], Le[i], Ln[i]), c[i]+gmpy2.powmod(s_[i], e_, Ln[i]))
    c[0] = c[n]
    for i in range(0, k):
        s[i] = random.randrange(1, Ln[i])
        s_[i] = random.randrange(1, Ln[i])
        z[i] = c[i] + gmpy2.powmod(s[i], Le[i], Ln[i])
        z_[i] = c[i] + gmpy2.powmod(s_[i], e_, Ln[i])
        c[i + 1] = hash_my(L, e_, m, z[i], z_[i])
        # c[i+1] = hash_my(L, e_, m, c[i]+gmpy2.powmod(s[i], Le[i], Ln[i]), c[i]+gmpy2.powmod(s_[i], e_, Ln[i]))
    r_1 = InvMod(r, phi_n)
    s[k] = gmpy2.powmod(u - c[k], d, Ln[k])
    s_[k] = gmpy2.powmod(v - c[k], ak * r_1, Ln[k])

    # 合并生成签名
    sigma = []
    sigma = [c[0]] + s + s_ + [e_] + [r]
    str_sigma = [str(i) for i in sigma]  # 每个元素转化为字符串
    out_str_sigma = '\n'.join(str_sigma)
    # with open('sigma_U'+str(k)+'.txt', 'w') as file_object:
    with open('db/sigma.txt', 'w') as file_object:
        file_object.write(out_str_sigma)
        print('签名生成完成')


if __name__ == "__main__":
    userlist1 = [0,1,2,3,4]
    sig_gen(5, 0, userlist1)
