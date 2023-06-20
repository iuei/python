# 得到"黑马程序员"
str1 = "万过薪月，员序程马黑来，nohtyP学"
result = str1[::-1][9:14:1]
print(f'方法1：{result}')

# 方式2
str1 = "万过薪月，员序程马黑来，nohtyP学"
my_list = str1[5:10:1][::-1]
print(f'方法2：{my_list}')