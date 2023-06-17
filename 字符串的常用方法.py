str_1 = 'hello word it helloit'
# 根据下标索引去出特定位置的字符
stra = str_1[1]
print(f'下标为一的字符是：{stra}')

# 查找给定字符串第一个匹配项
str_2 = 'hello word it helloit'
strb = str_2.index('w')
print(f'第一个匹配项的下标是：{strb}')

# 将字符串内的全部字符串1，替换为字符串2；不会修改原字符串，而是得到一个新的字符串
str_3 = 'hello word it helloit'
strc = str_3.replace('hello', 'hi')
print(f'替换后的字符串内容为：{strc}')

# 按照给定字符串，对字符串进行分隔；不会对原字符串修改，而是得到一个新的列表
str_4 = 'hello word it helloit'
strd = str_4.split(' ')
print(f'字符串分隔后的列表为：{strd}')

# 移除首尾的空格字符或者换行符    语法：字符串.split; 字符串.split(字符串)
str_5 = "12hello word it helloit21"
stre = str_5.strip('12')  # 只要是1或者2都将被移除
print(f'移除前的字符串为：{str_5}; 移除后的字符串为：{stre}')

# 统计字符串内某数字的出现次数
str_6 = 'hello word it helloit'
strf = str_6.count('hello')
print(f'hello出现的次数为：{strf}')

# 统计字符串的个数
str_7 = 'hello word it helloit'
strg = len(str_7)
print(f'字符串的个数为{strg}')