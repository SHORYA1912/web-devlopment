import scipy.stats as stats

prob1 = stats.poisson.pmf(12,10)
print("THE PROBABILITY OF RAIN FOR EXACTLY 12 DAYS",prob1)

prob2 = stats.poisson.pmf(12,10) + stats.poisson.pmf(18,10) + stats.poisson.pmf(14,10) + stats.poisson.pmf(15,10) + stats.poisson.pmf(16,10) + stats.poisson.pmf(17,10) + stats.poisson.pmf(18,10)
print("THE PROBABILITY OF RAINNING FOR 12 TO 18 DAYS",prob2)