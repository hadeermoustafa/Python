def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
        
    if n % 2 == 0 or n % 3 == 0:
            return False
    
    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    
    return True
    
x = list(range(100,152,1))
total = 0
for i in x:
    if is_prime(i):
        total += 1
    i += 1
  
print(total)
print(is_prime(351))
