# Inspired by work of Carlos Paris
# http://www.sievesofchaos.com

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.close()
N = 100
x = np.linspace(0,N,N^2)
plt.figure(figsize=(3*16,9));
for l in plt.gca().spines:
       plt.gca().spines[l].set_visible(False)

plt.tick_params(left='off',right='off')
plt.gca().set_axis_bgcolor('black')
for n in range(N):
          plt.plot((n,n),(0,N),'-',color="white",alpha=.5,linewidth=.25);

prime_ticks = [];
for p in Primes():
          if p < N:
              plt.plot(x,p*np.sqrt(np.abs(np.sin(pi/(p*1.0)*x))),'-',color="white",linewidth=0.75);
              plt.plot((p,p),(-N,0),'-',color="white",linewidth=.5)
              prime_ticks.append(p);
          else:
              break;
   
plt.yticks([])
plt.xticks(prime_ticks,color="white")
plt.ylim(-30,30)
plt.savefig("primes",facecolor="black") 