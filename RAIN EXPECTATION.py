import scipy.stats as stats

prob1 = stats.poisson.pmf(6,10)
print("THE PROBABILITY OF RAINING FOR EXACTLY FOR SIX DAYS", prob1)

prob2 = stats.poisson.pmf(12,10) + stats.poisson.pmf(13,10) + stats.poisson.pmf(14,10)
print("THE PROBABILITY FOR RAINING FOR EXACTLY 12-14 DAYS ",prob2)