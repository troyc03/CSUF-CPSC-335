"""
Algorithm: Taylor Expansion Problem
Find: The Taylor expansion of a function P(x) and its k^th derivative
Input: A function f(x) and its derivatives d^(k)/dx
Output: The sum of all Taylor polynomials (or the partial sum of the Taylor series)
"""

def taylor_polynomial(tol, N, x0, D, X):
    k = 0
    sum_Taylor = D[0]  # Initialize sum with the first term D(0)
    prod = 1  # Initialize product for factorial computation
    
    if X == x0:
        close = 0
    else:
        close = tol  # Start with a value above tolerance to enter the loop

    while close >= tol and k < N:
        k += 1
        prod *= (X - x0) / k  # Compute (x - x0)^k / k!
        term = D[k] * prod  # Compute the k-th term

        if term != 0:
            close = abs(term)  # Update close value to check convergence
        
        sum_Taylor += term  # Add term to summation

        if close < tol and k < N:
            print("The sum of the Taylor polynomial is:", sum_Taylor)
            return sum_Taylor
        else:
            print("The current partial sum is", sum_Taylor)
            print("Convergence has not been achieved")

    return sum_Taylor  # Return the final computed sum

# Example execution
tol = 0.0001  # Tolerance value
N = 5  # Maximum degree of the Taylor polynomial
x0 = 0  # Expansion point
D = [1, 1, 1, 1, 1, 1]  # Precomputed derivatives for e^x at x0 = 0
X = 1  # Evaluation point

result = taylor_polynomial(tol, N, x0, D, X)
print("Final computed sum:", result)
