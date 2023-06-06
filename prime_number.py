num = int(input("Enter a number: "))

if num == 1:
    print(num,"is not a prime number")
elif num > 1:
    for i in range (2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"X",num//i,"=",num)
            break
    else:
            print(num,"is a prime number")
else: # i < 1, negative, 0.1,0.2
    print(num,"is not a prime number")                 
