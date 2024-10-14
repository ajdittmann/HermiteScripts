from sympy import *
import sympy
import sys

n = 2	#number of points - 1
r = 1   #number of derivatives at each point

n_deriv_out = 2 # how many derivatives of the interpolant to take

sympy.var('x')
sympy.var('dt1')
sympy.var('dt2')
sympy.var('f')

def fact(n):
  if n <= 1: return 1
  else: return n*fact(n-1)

def pj(j):
  val = 1/((x - sympy.var('x'+str(j)))**(r+1))
  for i in range(n+1):
    val = val*(x - sympy.var('x'+str(i)))**(r+1)
  return val.subs(x0,0)

def gj(j):
  return 1/pj(j)

def dtgj(j,t):
  ret = gj(j)
  if t > 0:
    for i in range(0,t):
      ret = sympy.diff(ret, x)
  return ret.subs(x0,0)

def Ajk(j,k):
  val = gj(j).subs(x,sympy.var('x'+str(j)))
  for t in range(1,1+r-k):
    deriv = dtgj(j,t).subs(x,sympy.var('x'+str(j)))
    val = val + (deriv*(x-sympy.var('x'+str(j)))**t)/fact(t)
  ret = val*pj(j)*(x - sympy.var('x'+str(j)))**k/fact(k)
  return ret.subs(x0,0)		#set x0=0

for j in range(n+1):
 for k in range(r+1):
  print("k=%d, j=%d" %(k,j))

  out = sympy.simplify(Ajk(j,k))

  for N in range(n_deriv_out):
    out = simplify(diff(out, x))

  out = out.subs(x, x2) 	#evaluate the derivative of the interpolant at the final point in the quadrature,
				#in this case the third point x2.
				#if using n!=2, change this to xn.

  #out = simplify(out.subs(x1, dt1).subs(x2,dt2+dt1)) #

  out = simplify(out.subs(x1, dt2*f).subs(x2,dt2*(1+f))) # dt1 = f*dt2

  print(out)


