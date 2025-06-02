from scipy.stats import binom, norm
import numpy as np

n = 4
p = 0.35

print("Q1:")

print("P(X = 0):", binom.pmf(0, n, p))
print("P(X = 1):", binom.pmf(1, n, p))
print("P(X = 2):", binom.pmf(2, n, p))
print("P(X = 3):", binom.pmf(3, n, p))
print("P(X = 4):", binom.pmf(4, n, p))

print("P(X ≤ 2):", binom.cdf(2, n, p))
print("P(X ≤ 3):", binom.cdf(3, n, p))

print("P(X ≥ 2):", 1 - binom.cdf(1, n, p))
print("P(X ≥ 3):", 1 - binom.cdf(2, n, p))

E_X = n * p
V_X = n * p * (1 - p)
S_X = np.sqrt(V_X)
print("E(X):", E_X)
print("V(X):", V_X)
print("S(X):", S_X)

print("\nQ2:")
print("P(Z < 0.67):", norm.cdf(0.67))
print("P(Z < 1.96):", norm.cdf(1.96))
print("P(-1.23 < Z < 2.30):", norm.cdf(2.30) - norm.cdf(-1.23))

mu = 12
sigma = 4

print("\nQ3:")
print("P(X > 9):", 1 - norm.cdf(9, mu, sigma))
print("P(X < 10):", norm.cdf(10, mu, sigma))
print("P(8 < X < 14):", norm.cdf(14, mu, sigma) - norm.cdf(8, mu, sigma))
