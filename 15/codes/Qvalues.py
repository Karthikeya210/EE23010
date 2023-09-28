import scipy.stats as stats


def F(x):
	if x < -1:
		return(stats.norm.cdf(x))
	else:
		return(stats.norm.cdf(x+1))

print(f"P(X <= -1)={F(-1)}")
print(f"P(X = -1)={F(-1)-F(-1-1e-10)}")
print(f"P(X < -1)={F(-1-1e-10)}")
print(f"P(X <= 0)={F(0)}")
