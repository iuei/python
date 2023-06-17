# 使用while循环遍历元组
a1 = (9, 8, 7, 6, 5, 4, 3, 2, 1)
# 使用变量num控制循环语句
num = 0
b = 0  # 充当计数器
while num < len(a1):
    print(f"元组下标{b}的元素为：{a1[num]}")
    num += 1
    b += 1

print('')

# 使用for循环遍历元组
c = 0
a2 = ('hai', 'hi', 'word', 'you')

for c in a2:
    print(f"{c}")