from scipy.stats import binom

mu=0
sigma=1

y1=binom.cdf(0.5, mu, sigma)
y2=binom.cdf(-1.5, mu, sigma)

print(y1)
print(y2)