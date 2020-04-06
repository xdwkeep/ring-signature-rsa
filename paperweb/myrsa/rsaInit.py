from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_init(n):
    for i in range(0,n):
        # 生成密钥对代码如下：
        # 生成密钥对
        key = RSA.generate(2048)
        # 提取私钥并存入文件
        private_key = key.export_key()
        with open('db/pem/private_key'+'_U'+str(i)+'.pem', 'wb') as f:
            f.write(private_key)
        # 提取公钥存入文件
        public_key = key.publickey().export_key()
        with open('db/pem/public_key'+'_U'+str(i)+'.pem', 'wb') as f:
            f.write(public_key)
    print("初始化完成")

if __name__ == "__main__":
    n = 5 # 假设n个用户
    rsa_init(n)