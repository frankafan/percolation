from pylab import *
from scipy.ndimage import measurements

nsamp = 2000
L = 200
p = 0.58
allarea = array([])
for i in range(nsamp):
    z = rand(L)
m = z < p
lw, num = measurements.label(m)
labelList = arange(lw.max() + 1)
area = measurements.sum(m, lw, labelList)
allarea = append(allarea, area)
n, sbins = histogram(allarea, bins=int(max(allarea)))
s = 0.5 * (sbins[1:] + sbins[:-1])
nsp = n / (L * nsamp)
i = nonzero(n)
subplot(2, 1, 1)
plot(s[i], nsp[i],'o')
xlabel('$s$')
ylabel('$n(s, p)$')
subplot(2, 1, 2)
loglog(s[i], nsp[i],'o')
xlabel('$s$')
ylabel('$n(s, p)$')
show()
