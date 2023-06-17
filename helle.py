# BMI = 体重 / (身高 ** 2)
tizhong = float(input("请输入体重（kg）"))
shenggao = float(input("请输入身高（m）"))
bmi = tizhong / (shenggao ** 2)
print("BMI="+str(bmi))

if bmi <= 18.5:
    input("体重过轻")
elif 18.5 < bmi < 23.9:
    input("体重正常")
elif 24 < bmi < 27.9:
    input("体重偏重")
else: input("超重")

input("Press Any Key")