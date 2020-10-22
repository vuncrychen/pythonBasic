# 猜一組四位數, 會收到 XAYB, X 代表猜的數字中, 位置以及數值皆正確的 數量, Y 代表猜的數字中. 位置不正確但數值正確的 數量

import random

answer = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

# print("Answer: " + str(answer))

input_guess = input("請猜出正確的四位數: ")

endgame = 0
chance = 10
message = 1

while endgame != 1:

    if chance == 0:
        message = 0
        break

    user_guess = [int(x) for x in input_guess]

    # print(type(user_guess))

    a = 0
    b = 0

# b

    for ges in user_guess:
        for ans in answer:
            if ges == ans:
                b += 1

# a

    for x in range(0, len(answer)):
        if user_guess[x] == answer[x]:
            a += 1

    b -= a

    if a == len(answer):
        endgame = 1
        continue

    print(str(a) + "A" + str(b) + "B")

    input_guess = input("猜錯啦! 剩餘 " + str(chance) + " 次機會: ")

    chance -= 1

if message:
    print("恭喜你! 你贏了~")
else:
    print("很抱歉! 你輸了~")
