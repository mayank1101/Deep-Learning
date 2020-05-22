import numpy as np
import math
# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    ans = []
    np_L = np.array(L)
    np_exp_L = np.exp(np_L)
    for score in L:
        new_score = math.exp(score)/np_exp_L.sum()
        ans.append(new_score)
    return ans
    pass