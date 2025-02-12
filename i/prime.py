number = int(input("Enter a number: "))
x=0
if number <= 1:
    print(f"{number} is not a prime number.",x)
else:
    flag = True
    for i in range(2, int(number**0.5) + 1):
        x+=1
        if number % i == 0:
            flag = False
            break

    if flag:
        print(f"{number} is a prime number.",x)
    else:
        print(f"{number} is not a prime number.",x)
