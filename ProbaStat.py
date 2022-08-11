"""for i in range(4000000000000):
    j=10**i
    print(j)
    if j>10000: break"""
from matplotlib import pyplot as plt

"""str = "abcdef"
print(str[:3])
print(str[3:])
print(str[3:5])
print(str[-2])"""

"""import numpy as np

size=123
k=5
liste=np.random.randint(0,10,size=size)
size_tranche=size//k
tranches=[]

for i in range(k):
    tranches.append(liste[i*size_tranche: (i+1)*size_tranche])

print("liste :", liste[:10])
print("tranches :", tranches[:3])"""


"""a=["bonjour", "baba", "rhum", "comment", "dodo", "allez"]
a.sort(key=lambda elem:elem[-1])
print(a)"""

"""import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1,100)
for alpha in [0,1,2,3]:
    plt.plot(x,x**alpha,label=fr"$\alpha=${alpha}")
plt.legend()
plt.title(r"f:$[0,1]\to[0,1]$, $x\mapsto x^\alpha$")
plt.show()"""

import sklearn.datasets
X, y = sklearn.datasets.make_moons(n_samples=5000, noise=0.30,random_state=42)

fig,(ax0,ax1)=plt.subplots(1,2,figsize=(10,5) ,sharey=True)

ax0.scatter(
    X[:500,0] ,#abscisses
    X[:500,1] ,#ordonnees
    c=y[:500] ,#couleurs
    edgecolor="w" , #couleur du tour
    cmap="jet" #color-map
)
ax0.set_title("beaucoup de données")
ax0.set_aspect("equal")

ax1.scatter(
    X[: ,0] ,#abscisses
    X[: ,1] ,#ordonnees
    c=y[:] ,#couleurs
    marker="." , #petits points
    alpha=0.3,
    linewidths=0, #pas d'entourage
    cmap="jet" #color-map
)
ax1.set_title("encore plus de données")
ax1.set_aspect("equal")
plt.show()