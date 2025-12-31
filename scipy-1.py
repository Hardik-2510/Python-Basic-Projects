import numpy as np

# OPTIMIZATION (Minimization)
from scipy.optimize import minimize

f = lambda x: x**2 + 5
opt_result = minimize(f, x0=2)

print("Optimization Result:")
print("Minimum at x =", opt_result.x)
print("Minimum value =", opt_result.fun)
print("-" * 40)


#  LINEAR ALGEBRA (Solve equations)
from scipy.linalg import solve

A = [[3, 1], [1, 2]]
B = [9, 8]
solution = solve(A, B)

print("Linear Algebra Result:")
print("Solution of Ax = B:", solution)
print("-" * 40)


#  INTEGRATION
from scipy.integrate import quad

area, _ = quad(lambda x: x**2, 0, 1)

print("Integration Result:")
print("Area under x^2 from 0 to 1 =", area)
print("-" * 40)


#  INTERPOLATION
from scipy.interpolate import interp1d

x = [0, 1, 2]
y = [0, 1, 4]
interp_func = interp1d(x, y)

print("Interpolation Result:")
print("Value at x = 1.5:", interp_func(1.5))
print("-" * 40)


#  STATISTICS
from scipy import stats

data = [10, 20, 30, 40, 50]

print("Statistics Result:")
print("Mean:", stats.gmean(data))
print("Standard Deviation:", stats.tstd(data))
print("-" * 40)


#  SIGNAL PROCESSING
from scipy.signal import find_peaks

signal = [1, 2, 3, 2, 1, 2, 3, 2]
peaks, _ = find_peaks(signal)

print("Signal Processing Result:")
print("Peaks at index:", peaks)
print("-" * 40)


#  SPECIAL FUNCTION
from scipy.special import gamma

print("Special Function Result:")
print("Gamma(5) =", gamma(5))
print("-" * 40)
