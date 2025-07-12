import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# parameters
a1 = 1 / 4
a2 = 3 / 4
b1 = np.sqrt(1 - a1**2)
b2 = np.sqrt(1 - a2**2)

def F0(v1, v2):
    return (((a1 * b2)**2 + (a2 * b1)**2) - (b1**2 + b2**2) * (v1 + v2)**2 / 4 - (a1**2 + a2**2) * (v1 - v2)**2 / 4) / (2 * a1 * a2 * b1 * b2)

def F1(v1, v2):
    return 1 - (v1 + v2)**2 / (4 * a1**2) - (v1 - v2)**2 / (4 * b1**2)
def F2(v1, v2):
    return 1 - (v1 + v2)**2 / (4 * a2**2) - (v1 - v2)**2 / (4 * b2**2)

def mask(v1, v2):
    return (F1(v1, v2) >= 0) & (F2(v1, v2) >= 0)

def fp(v1, v2):
    m = mask(v1, v2)
    result = np.zeros_like(v1, dtype=float)
    result[~m] = 0
    result[m] = (F0(v1, v2)[m] + np.sqrt(F1(v1, v2)[m] * F2(v1, v2)[m])) / (2 * np.pi**2 * (1 - v1[m]**2) * (1 - v2[m]**2) * np.sqrt(F1(v1, v2)[m] * F2(v1, v2)[m]))
    return result
def fm(v1, v2):
    m = mask(v1, v2)
    result = np.zeros_like(v1, dtype=float)
    result[~m] = 0
    result[m] = (F0(v1, v2)[m] - np.sqrt(F1(v1, v2)[m] * F2(v1, v2)[m])) / (2 * np.pi**2 * (1 - v1[m]**2) * (1 - v2[m]**2) * np.sqrt(F1(v1, v2)[m] * F2(v1, v2)[m]))
    return result

mgn = 0.1

v1 = np.linspace(-1, 1, 201)
v2 = np.linspace(-1, 1, 201)
v1, v2 = np.meshgrid(v1, v2)

fplus = fp(v1, v2)
fminus = fm(v1, v2)

fig = plt.figure(figsize=(10, 10))
plt.subplots_adjust(wspace=0.3)

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(v1, v2, fplus, edgecolor='royalblue', lw=0.2, alpha=0.3)
ax1.set(zlim=(0, 1))
ax1.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
ax1.set_title(r"(a) 3D Plot of $f_+(v_1, v_2)$")

ax2 = fig.add_subplot(222)
heatmap = ax2.pcolormesh(v1, v2, fplus, vmin=0, vmax=1, cmap='RdBu_r')
cbar2 = fig.colorbar(heatmap, ax=ax2)
ax2.axis("equal")
ax2.set(xlim=(-1.0 - mgn, 1.0 + mgn), ylim=(-1.0 - mgn, 1.0 + mgn))
ax2.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
ax2.set_title(r"(b) Heatmap of $f_+(v_1, v_2)$")

ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(v1, v2, fminus, edgecolor='royalblue', lw=0.2, alpha=0.3)
ax3.set(zlim=(0, 1))
ax3.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
ax3.set_title(r"(c) 3D Plot of $f_-(v_1, v_2)$")

ax4 = fig.add_subplot(224)
heatmap = ax4.pcolormesh(v1, v2, fminus, vmin=0, vmax=1, cmap='RdBu_r')
cbar4 = fig.colorbar(heatmap, ax=ax4)
ax4.axis("equal")
ax4.set(xlim=(-1.0 - mgn, 1.0 + mgn), ylim=(-1.0 - mgn, 1.0 + mgn))
ax4.set(xlabel=r"$v_1$", ylabel=r"$v_2$")
ax4.set_title(r"(d) Heatmap of $f_-(v_1, v_2)$")

fig.savefig("plot_fpm.pdf")
