n = eval(input('请输入一个数字：'))
if type(n) == type(123):
    print("请输入的数字是整数。")
elif type(n) == type(11.3):
    print("输入的数字是浮点数。")
else:
    print("无法判断输入类型。")
        
