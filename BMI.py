def calculate_bmi(weight, height):
    """
    计算BMI指数
    :param weight: 体重（单位：千克）
    :param height: 身高（单位：米）
    :return: BMI指数
    """
    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    """
    根据BMI指数进行判定
    :param bmi: BMI指数
    :return: 判定结果
    """
    if bmi < 18.5:
        interpretation = "体重过轻"
    elif 18.5 <= bmi < 24.9:
        interpretation = "正常范围"
    elif 24.9 <= bmi < 29.9:
        interpretation = "超重"
    else:
        interpretation = "肥胖"
    return interpretation


weight = float(input("请输入体重（单位：千克）："))
height = float(input("请输入身高（单位：米）："))

bmi = calculate_bmi(weight, height)
interpretation = interpret_bmi(bmi)

print("您的BMI指数为：", bmi)
print("判定结果：", interpretation)
