import numpy as np

AREA_SIZE = 1000
SPEED = 50
SIGMA = (SPEED * 1000. / 24. / AREA_SIZE) / (3. * np.sqrt(2))
UNSEEN = 0
DONE = 1
SOCIAL_DISTANCE = 0.0000007
BETA1 = 1  # amylase rate
BETA2 = 1  # glucose to lactate rate
BETA3 = 0.3  # lactate to electron rate

FRAME_RATE = 1  # Refresh graphics very FRAME_RATE hours
# DENSITY = 100
starch_density = 1000
ecoli_density = 1000
so_density = 1000
e_density = 0
l_density = 0
g_density = 0
duration = .5
