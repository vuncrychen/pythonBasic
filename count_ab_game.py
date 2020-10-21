import random

answer = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

# print(answer)

endgame = 0

while endgame != 1:

    input_guess = input("請猜出正確的四位數: ")

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

print("you won!")
