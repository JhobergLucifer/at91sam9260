# Control PID rootlocus in python
# by Jhoberg Quevedo Ruiz
# Engineer


#           u    +         +---+      +------+y
#          ------>(+)----->| Gs |----->| Gp |--------+------->
#                  ^ -     +---+      +------+       |
#                  |                                 |
#                  +---------------------------------+



from control.matlab import *
import control
from sympy import symbols, simplify, poly , limit, solve, Eq, Function, integrate, fraction, expand
import matplotlib.pyplot as plt
import math as math1
import numpy as np
import sympy as sym

S = symbols('S')
s= symbols('s')
Kp = symbols('Kp')
Ki= symbols('Ki')
Kd = symbols('Kd')
t = symbols('t')



Kpow=49.5
Gpts=sym.exp(-t/14.940)+19
Gpts=Kpow*Gpts+19
print(Gpts)
Gptf1=sym.integrate(Gpts*sym.exp(-s*t), (t, 0, sym.oo)).args
#print(Gptf1)
#sym.init_printing(use_unicode=False, wrap_line=True)
x=str(Gptf1)

ver1=fraction(Gptf1)
print(ver1)
#Gptf1=Gptf1.coeffs()

Gptf=(15074.46*s + 959.5)/(s*(14.94*s + 1))
Gptf=simplify(Gptf)
print(Gptf)
nump1, denp1 = Gptf.as_numer_denom()
Gnum1=poly(nump1)
Gden1=poly(denp1)
num1=Gnum1.coeffs()
den1=Gden1.coeffs()
print("GP: ",Gptf,num1,den1)

#num=np.array([102339,1900])
#den=np.array([1494,100,0])
Gps=control.tf(num,den)

plt.clf()
t,y=control.step_response(Gps)
plt.plot(t,y)
plt.show()


#num=np.array([1])
#GP=poly(Gptf1)
#GP.coeffs()
#print(GP)

print(Gps)
rootsGps=control.pzmap(Gps)
print(rootsGps)
plt.show()




#%%%%%%%%%%%%%%%Control PID

#%error state stable rampa unitaria <=0,001
#%sobrepaso max<=10%
#%tiempo levantamiento tr<=0,005 seg
#%tiempo asentamiento ts <=0,007 seg

#calculo ovreshot <= 0.1
pi=3.1416
E = symbols('E')
overshot=pow(-pi*E/(1-E*E),0.5)-0.1
E=solve(overshot,E)
E=0.9102
print(overshot,E)

#error stabl state unit rampa <= 0,01
#limiterror = limit(Gp, S, 0) 
#print(limiterror)

#%%%%%
#%3) calculo Tiempo retardo tr 
#% aproxlinea recta , fr=1/(L*C)^0.5=316.22 , tr>>10*1/fr
wn=symbols('wn')
tr=(0.8+2.5*E)/(wn)-0.001
wn=solve(tr,wn)
print(wn)
wn=3075.4

#%5)caculo PID , ecuacion caracteristica Close Loop Gcl
#%divisor orden 2 , S*S+2*E+wn+wn*wn


sd1=-E*wn+1j*wn*(1-E*E)**0.5
sd2=-E*wn-1j*wn*(1-E*E)**0.5
print(sd1)


#Calculo punto PD en Gs
#sum(Z)-sum(P)=-180
# (teta1-teta4)-(teta2-teta3)=-180

teta4=math1.atan(1273.9/(2799.2-0))
teta3=180-math1.atan(1273.9/(2799.2-0.01856))
teta2=180-math1.atan(1273.9/(2799.2-0.066934))
     #teta1=atan(182.73/(a-134.68))
#     solve(atan(42/(a-40))-(179.26+179.18)=-180,a)
     #teta1=atan(1766/a-3075.7)
#sum(tetaZ)-sum(tetaP)=-180
a=1273.9/math1.tan(-0.43)+2799.2
a=21.525
print(a)

######Calculo K en PD
K = 0.014498
Gc=0.014498*(S+21.525)*(S+0.1)/S
Gc=expand(Gc)
print(Gc)     
Kd1=0.01691
Kp1=0.3657
Ki1=0.036399

#PID form PD 
#%Kd*X=0.0638
#     %X=0.3657/0.016910
Kp=21.626
Ki=2.1525
Kd=0.014498

numPID=np.array([Kd,Kp,Ki])
denPID=np.array([1,0])

Gc1=control.tf(numPID,denPID)
Gcl1=Gc1*Gps/(1+Gc1*Gps)

plt.clf()
t,y=control.step_response(Gcl1,T=0.3)
plt.plot(t,y)
plt.title('Control PID Temperature')
plt.ylabel('Unit Temperature')
plt.xlabel('Time')
plt.show()
