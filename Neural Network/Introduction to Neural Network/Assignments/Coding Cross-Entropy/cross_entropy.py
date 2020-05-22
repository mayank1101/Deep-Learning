import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    entropy_sum=0
    for y,p in zip(Y,P):
        entropy_sum += ((y * np.log(p)) + ((1 - y) * np.log((1 - p))))
    return (-entropy_sum)
    pass