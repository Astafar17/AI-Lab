def mathematics(n1,n2):
    sum=n1+n2
    diff=n1-n2
    mul=n1*n2
    if n2 != 0:
     quotient=n1/n2

    else:
     quotient="undefined"

    return sum,diff,mul,quotient


num1=float(input("enter the first number:-"))
num2=float(input("enter the second number:-"))


sum,diff,mul,quotient=mathematics(num1,num2)

print(f"sum:{sum}")
print(f"difference:{diff}")
print(f"multiplication:{mul}")
print(f"quotient:{quotient}")