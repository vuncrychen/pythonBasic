f = open("text.txt", "r")

# words = f.read()

# count = 0

# for i in words:
#     print(count, end="")
#     print(": " + i)
#     count += 1

line1 = f.readline()
line2 = f.readline(2)

print(line2)

f.close()

