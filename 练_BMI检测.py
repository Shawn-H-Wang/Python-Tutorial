weight,height=eval(input("请输入体重(Kg)和身高(米)[逗号隔开]:"))

bmi = weight / pow(height,2)
#bmi = weight / (height * height)
print("BMI指数为:{}".format(bmi))

guoji,guonei="",""
if bmi < 18.5:
    guoji,guonei="偏瘦","偏瘦"
elif 18.5 <= bmi < 24:
    guoji,guonei="正常","正常"
elif 24 <= bmi < 25:
    guoji,guonei="正常","偏胖"
elif 25 <= bmi < 28:
    guoji,guonei="偏胖","偏胖"
elif 28 <= bmi < 30:
    guoji,guonei="偏胖","肥胖"
else:
    guoji,guonei="肥胖","肥胖"
print("国际BMI水平为{}，国内BMI水平为{}".format(guoji,guonei))
