import json

# # 写入json
# new_dict = {'ak_1':100, 'r':200}
# print(new_dict)
# print(type(new_dict))
# with open("akr.json", "w") as f:
#     json.dump(new_dict, f)
#     print("写入完成")
#
#
# # 读取json
# with open('akr.json', 'r') as f:
#     load_dic = json.load(f)
#     print(load_dic)
#     print(type(load_dic))
#     print("读取完成")
#
#
# def test(a, b=2):
#     print(a)
#
#
# test(2,3)

userstr = '0,1,2,3,4'
struserlist = userstr.split(',')
userlist = [int(struser) for struser in struserlist]
print(userlist)