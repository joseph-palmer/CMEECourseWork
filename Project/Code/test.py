import numpy as np
from sumexp import *

seed_val = 13
np.random.seed(seed_val)


rts = [0.75, 1.18]
psi = [0.49, 0.51]

sample_sumexp(rts, psi, 10)

rts = [1.18, 0.75]
psi = [0.51, 0.49]
print("\n")
sample_sumexp(rts, psi, 10)