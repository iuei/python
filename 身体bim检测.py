mass = float(input('请输入体重(kg):'))
height = float(input('请输入身高(m):'))
bmi = mass / height / height
if bmi < 18.5:
    body = '偏瘦'
elif 18.5 <= bmi and bmi < 24:
    body = '正常'
elif 24 <= bmi and bmi < 28:
    body = '超重'
elif bmi >= 28:
    body = '肥胖'
print('你的bmi是：{}'.format(bmi))
print(body)