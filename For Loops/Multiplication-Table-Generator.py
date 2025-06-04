#Multiplication Table Generator
num = int(input("Enter number: "))
print()
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    #if u don use int() with input , it will consider given number as string
