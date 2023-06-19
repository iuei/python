# 对list进行切片，从1开始，4结束，步长1  #语法：序列[起始下标:结束下标:步长]起始下标，结束下标留空默认从开始到结束，步长留空默认为1
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4:1]
print(f'结果1:{result1}')

# 对tuple进行切片，从头开始，到最后结束，步长1
my_list = (0, 1, 2, 3, 4, 5, 6)
result2 = my_list[::1]  #
print(f'结果2：{result2}')

# 对str进行切片，从头开始，到最后结束，步长2
my_list = '1234567'
result3 = my_list[::2]
print(f'结果3：{result3}')

# 对str进行切片，从头开始，到最后结束，步长-1
my_list = '1234567'
result4 = my_list[::-1]
print(f'结果4：{result4}')

# 对列表进行切片，从3开始，到1结束，步长-1
my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(f'结果5：{result5}')

# 对元组进行切片，从头开始，到尾结束，步长-2
my_list = (0, 1, 2, 3, 4, 5, 6)
result6 = my_list[::-2]
print(f'结果6：{result6}')