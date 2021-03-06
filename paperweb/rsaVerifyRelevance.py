from Crypto.PublicKey import RSA
from Crypto.Random import random
from Crypto.Hash import SHA256
import base64
import gmpy2


# 两个要验证关联性的编号
def relevace_verify():
    # 读取输入的数据
    with open('db/vr_sigma_u0.txt', 'r') as f:
        sigma = f.read()
        # 读取sigma中的数组
        listSigma = sigma.split('\n')
        e_a = int(listSigma[-2])
        ra = int(listSigma[-1])
    with open('db/vr_sigma_u1.txt', 'r') as f:
        sigma = f.read()
        # 读取sigma中的数组
        listSigma = sigma.split('\n')
        e_b = int(listSigma[-2])
        rb = int(listSigma[-1])

    if e_a == e_b and ra == rb:
        print('true')
        print('关联性验证完成')
        return True
    else:
        print('false')
        return False


if __name__ == "__main__":
    relevace_verify()
