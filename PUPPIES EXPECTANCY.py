import numpy as np

np.random.seed(42)

puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p = puppies.mean()

print("MEAN:",p)
print("STANDARD DEVIATION", puppies.std())
print("VARIENCE:",puppies.var())

np.random.choice(puppies,size = (1,5),replace = True)
np.random.choice(puppies,size=(1,5),replace=True).mean()

print("\nSAMPLE DISTRIBUTION WITH SIZE\n")

sample_props = []

for i in range (1000):
    sample = np.random.choice(puppies,5,replace=True)
    sample_props.append(sample.mean())
sample_props = np.array(sample_props)
sm = sample_props.mean()

print("MEAN", sample_props.mean)
print("DEVIATION",sample_props.std())
print("VARIENCE",sample_props.var)

twenty_sample_props = []

for i in range (1000):
    sample = np.random.choice(puppies,20,replace=True)
    twenty_sample_props = sample.mean()
    twenty_sample_props = np.array(twenty_sample_props)

print("NEW MEAN",twenty_sample_props.mean)
print("NEW DEVI",twenty_sample_props.std())
print("NEW VARIENCE", twenty_sample_props.var)

