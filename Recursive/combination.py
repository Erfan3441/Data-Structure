def combination(n, m):
    
    if m == 0 or m == n:
        return 1
    
    else:
        return combination(n - 1, m - 1) + combination(n - 1, m)
        

print(combination(5,3))
