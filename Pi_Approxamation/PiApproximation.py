#PiApproxmation.py

Pi = 3.14159265358979

Pi_approx = 0

x = 3

y = 1

error_tolerance = float(input("Input error tolerance:"))

error = abs(Pi - Pi_approx)

while error_tolerance < error :
   
    x = (4) * ((-1) ** (y + 1))
    Pi_end = x / ((2 * y) - 1)
    Pi_approx += Pi_end
 
    error = abs(Pi - Pi_approx)
    print(y, end ="")
    print("\t",Pi_approx)
    y += 1
else:
 
    print(f"\nAfter {y} terms, pi is approximataly {Pi_approx}.\nOur error is {error} which is less than or equal to {error_tolerance}")
    