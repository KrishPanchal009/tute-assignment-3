def fac(num):
    factor = 1
    while num >= 1:
        factor *= num
        num -= 1
    return factor

num = int(input("Enter a number: "))
n = fac(num)
print(f"The factor of {num} is {fac(num)}")