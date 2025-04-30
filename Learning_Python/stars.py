num = int(input("Enter the number: "))

for i in range(num+1):
    print(" " * (num-i), end="")
    print("*" * ((2*i)-1), end="")
    print("")