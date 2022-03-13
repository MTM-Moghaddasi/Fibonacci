def fibo(number):
    if number == 0 or number == 1:
        return number
    else:
        return fibo(number - 1) + fibo(number - 2)

number = int(input("Enter Your Number : "))
for i in range(0, number):
    print(fibo(i))