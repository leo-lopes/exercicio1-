import numpy as np
import matplotlib.pyplot as plt
import os, sys
def func(a):
    u = np.zeros(int(L/dx))
    u[0] = 0.0
    u[1] = u[0] + a[0]*dx*(1./v1)
    for i in range (1,len(u)-1):
        if x[i] < L/2:
            u[i+1] = u[i-1] + 2.*a[i]*dx*(1./v1)
        else:
            u[i+1] = u[i-1] + 2.*a[i]*dx*(1./v2)
    return u
    
## exercicio 1
nsteps=2000
dt=0.01
dx=0.01
nplot=10
L=10.
v1=0.5
v2=0.5
x = np.linspace(0,L,int(L/dx))
u = np.zeros(int(L/dx))
s=np.zeros((3,int(L/dx)))
r=np.zeros((3,int(L/dx)))
n=10
k=2.*np.pi*n/(2.*L)
u[0]=0.0
u[1:] =np.sin(k*x[1:])
s[0,:]= v1*np.cos(k*x)
s[0,0] = 0.0
s[0,int(L/dx)-1] = 0.0
r[0,:] = -v1*np.cos(k*x)
r[1,:] = r[0,:]
v=np.zeros(int(L/dx))
v[:] = [v1 if x[j] < L/2 else v2 for j in range(int(L/dx))]
func(r[0,:])
c=0
d=0
for i in range (0,nsteps):
    c=c+1
    r[2,:] = 0.0
    s[2,:] = 0.0
    for j in range (1,len(u)-1):
        r[2,j] = r[0,j] +((s[1,j+1]-s[1,j-1])*v[j])
        s[2,j] = s[0,j] +((r[1,j+1]-r[1,j-1])*v[j])
    s[2,0] = 0.0
    s[2,int(L/dx)-1] =0.0
    r[2,0] = r[2,1]
    r[2,int(L/dx)-1] = r[2,int(L/dx)-2]
    u = func(r[2,:])
    r[0,:] = r[1,:]
    r[1,:] = r[2,:]
    s[0,:] = s[1,:]
    s[1,:] = s[2,:]
    if (c%nplot == 0):
        d=d+1
        plt.plot(x,u,linewidth=2)
        plt.plot(x,s[1,:],linewidth=2)
        plt.ylim([-0.7,0.7])
        filename = 'foo' + str(d).zfill(3) + '.jpg';
        plt.xlabel("x")
        plt.ylabel("u")
        plt.title("t = %2.2f"%(dt*(i+1)))
        plt.savefig(filename)
        plt.clf()
os.system("ffmpeg -r 5 -y -i 'foo%03d.jpg' test.m4v")
os.system("rm -f *.jpg")
