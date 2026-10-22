
iDnum = input("Enter your ID number: ")
totalSum = 0
# 1: length
if len(str(iDnum)) != 9: 
    print("Invalid ID length")
    raise SystemExit

# 2: *1
for i in range(0, 9, 2):
    digit = int(str(iDnum)[i])
    totalSum += digit

# 3: *
for i in range(1, 9, 2):
    digit = int(str(iDnum)[i])
    result = digit * 2

    if result >= 10: # 4: if the result is a two-digit number
        result = result // 10 + result % 10
    
    totalSum += result
print("Total Sum:", totalSum)

if totalSum % 10 == 0:
    print("Valid ID number")
else:
    print("Invalid ID number")

