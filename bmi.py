# bmi -> 體重除以身高(m)平方

# bmi < 18.5 = 過輕
# 24 > bmi > 18.5 = 適中
# bmi >= 24 = 過重

def height_converter(h):
    return h/100

def make_bmi(h, w):
    return w/(h*h)

height = input("身高(cm): ")

# print(height)
# print(type(tall))

weight = input("體重(kg): ")

# print(weight)
# print(type(weight))

new_height = height_converter(int(height))

# print(new_height)

bmi = make_bmi(new_height, int(weight))

min_bmi = 18.5
max_bmi = 24

if bmi < min_bmi:
    print("過輕!", end="")
    print(" (bmi: " + str('%.1f' % bmi) + ")")

elif bmi < max_bmi:
    print("健康!", end="")
    print(" (bmi: " + str('%.1f' % bmi) + ")")

else:
    print("過重!", end="")
    print(" (bmi: " + str('%.1f' % bmi) + ")")

