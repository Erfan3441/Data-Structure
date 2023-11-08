def power(n,m):
    if m==1:
        return n
    else:
        return n*power(n,m-1)
    
n=int(input("Enter your first number : "))
m=int(input("Enter your second number : "))

print(power(n,m))
