from Crypto.PublicKey import RSA
from models import DBfunc, User
import json


def rsa_init(n):
    DBfunc.drop_db()
    DBfunc.init_db()
    with open('db/n_all.json', 'w') as f:
        f.write(str(n))
    for i in range(0, n):
        # 生成密钥对代码如下：
        # 生成密钥对
        key = RSA.generate(2048)
        # 提取私钥并存入文件
        private_key = key.export_key()
        with open('db/pem/private_key' + '_U' + str(i) + '.pem', 'wb') as f:
            f.write(private_key)
        # 提取公钥存入文件
        public_key = key.publickey().export_key()
        with open('db/pem/public_key' + '_U' + str(i) + '.pem', 'wb') as f:
            f.write(public_key)
        # 写入数据库
        user = User(i, public_key, private_key)
        user.save()
        # 初始化关联标签
        new_dict = {'ak': 0, 'r': 0}
        with open("db/akr/akr" + str(i) + ".json", "w") as f:
            json.dump(new_dict, f)
    print("初始化完成")


if __name__ == "__main__":
    n = 5  # 假设n个用户
    rsa_init(n)
