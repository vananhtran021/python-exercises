import random

# 3-digit code: each number is between 0 and 9
code_3 = ""

for i in range(3):
    code_3 += str(random.randint(0, 9))

# 4-digit code: each number is between 1 and 6
code_4 = ""

for i in range(4):
    code_4 += str(random.randint(1, 6))

print("3-digit code:", code_3)
print("4-digit code:", code_4)