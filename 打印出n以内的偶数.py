# 从键盘上获取一个值
num = int(input('请输入一个数:'))
# 判断是否满足循环条件，不满足则跳出
while num > 0:
    if num % 2 == 0:
        print(num)

    num -= 1
