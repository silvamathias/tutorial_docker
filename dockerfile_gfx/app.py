# %%
import numpy as np
import matplotlib.pyplot as mp 


# %%
a = np.linspace(0,4*np.pi,400)

# %%
y1 = np.sin(a)

# %%
y2 = np.cos(a)

# %%
mp.plot(a,y1)
mp.plot(a,y2)
mp.show()

# %%
fig, gx = mp.subplots(2,1)
gx[0].plot(a,y1)
gx[1].plot(a,y2)
mp.show()

print(a)

