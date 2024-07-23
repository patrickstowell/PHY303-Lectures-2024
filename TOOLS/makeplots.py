import matplotlib.pyplot as plt
import pandas as pd
plt.xkcd(randomness=1)

vals = pd.read_csv("data1.csv",names=["x","y"])

plt.plot(vals.x, vals.y, c='gray',zorder=-1)
plt.scatter(vals.x, vals.y, s=15, c='red',zorder=2)
plt.yscale('log')
plt.ylabel("Relative Abundance")
plt.xlabel("Mass Number (A)")
plt.show()

vals = pd.read_csv("data2.csv",names=["x","y"])

plt.scatter(vals.x, vals.y, s=15, c='red',zorder=2)
plt.ylabel("Binding Energy Last Neutron (MeV)")
plt.xlabel("Neutron Number (N)")
plt.show()


vals2 = pd.read_csv("data3.csv",names=["x","y"])
vals3 = pd.read_csv("data4.csv",names=["x","y"])
#plt.plot(vals2.x, vals2.y, c='gray',zorder=-1)
plt.scatter(vals3.x, vals3.y, s=20, c='red',zorder=2)
plt.ylabel("Neutron Capture Cross-section (mb)")
plt.xlabel("Neutron Number (N)")
plt.yscale('log')
plt.show()

vals3 = pd.read_csv("data5.csv",names=["x","y"])
#vals2 = pd.read_csv("data6.csv",names=["x","y"])
#plt.plot(vals2.x, vals2.y, c='gray',zorder=-1)
plt.scatter(vals3.x, vals3.y, s=40, c='red',zorder=2)
plt.ylabel("Reduced Quadrupole Moment (eb)")
plt.xlabel("Neutron Number (A)")
plt.xlim(0,160)
plt.ylim(-0.1,0.4)
plt.show()
