import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("lum_data.csv", delimiter=",")
data2 = np.loadtxt("lum_data_withsource.csv", delimiter=",")

data /= data[0]
data2 /= data2[0]
print(data2, data)
data = data2/data
print(data.shape)

print((2592,1952), 1280*720)
#plt.plot(data)
#plt.show()

xxi = np.linspace(0,1280,1280)
yyi = np.linspace(0,720,720)


xx,yy = np.meshgrid(xxi,yyi)
xxr = xx.ravel()
yyr = yy.ravel()


rebin=1

xxii = np.linspace(0,1280,int(1280/rebin))
yyii = np.linspace(0,720,int(720/rebin))

plt.hist2d(xxr,yyr,weights=(data), bins=(xxii, yyii))
plt.colorbar()

plt.show()

