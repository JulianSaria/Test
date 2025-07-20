import numpy as np
import matplotlib.pyplot as plt
from Nachbau_ati_sauber.Element import Element

Emin = 1.1
Emax = 30

x_ele = Element(Element="Pb", step=0.01, Emax=Emax, Emin=Emin)
x, y = x_ele.Massenabsorptionskoeffizient_array()

K = np.array([x_ele.TauK(xi) for xi in x])
L1 = np.array([x_ele.TauL1(xi) for xi in x])
L2 = np.array([x_ele.TauL2(xi) for xi in x])
L3 = np.array([x_ele.TauL3(xi) for xi in x])

colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple"]

plt.figure(figsize=(8, 5))
plt.plot(x, y,      color=colors[0], label="Tau (gesamt)")
plt.plot(x, L1,     color=colors[2], label="TauK")
plt.plot(x, L2,     color=colors[3], label="TauL")
plt.plot(x, L3,     color=colors[4], label="TauM")

plt.ylim(0, 4000)
plt.xlabel("Energie (keV)")
plt.ylabel("Tau")
plt.title("Pb Massenabsorptionskoeffizient")

plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("Pb_Massenabsorptionskoeffizient.png", dpi=600, bbox_inches='tight')
plt.show()
