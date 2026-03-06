count = 0

number = int(input("Please enter a positive integer greater than 9: "))



while number > 9 :
    print(number," -> ",end="")
    digitSum = 0
    tempNum = number
    while tempNum > 0:
        digitSum += tempNum%10
        tempNum //= 10
    number = digitSum
    count += 1
print(number)

print("Final value: ", number)
print("Total steps: ", count)

number = int(input("Enter a number: "))

a = ""

while number < 10 or number > 100:
    number = int(input("Enter a number: "))

for i in range(1,number+1):
    a = ""
    if i % 7 == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        a += "FizzBuzz"
    elif i % 3 == 0:
        a += "Fizz"
    elif i % 5 == 0:
        a += "Buzz"
    else:
        print(i)
        continue
    print(a)

number = int(input("Enter a number: "))

while number > 9 or number < 3:
    number = int(input("Enter a number: "))

for i in range(1,(number*2)):
    k = number - abs(number-i)
    for j in range(1,k+1):
        print(j,end=" ")
    print()
