def even_sum(n):
    total = 0  # Initialize the total sum
    fib1, fib2 = 1, 1  # The first two Fibonacci numbers
    
    # Loop until the second Fibonacci number exceeds n
    while fib2 <= n:
        # If the current Fibonacci number is even, add it to the total
        if fib2 % 2 == 0:
            total += fib2
        # Update the Fibonacci numbers: calculate the next Fibonacci number
        fib1, fib2 = fib2, fib1 + fib2  
    return total 
