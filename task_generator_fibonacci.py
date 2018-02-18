def fibonacci(number): 
    i = 0 
    k = 1 
    while i < number: 
        yield i 
        i, k = k, i + k 
 
for n in fibonacci(10): 
   print (n) 

