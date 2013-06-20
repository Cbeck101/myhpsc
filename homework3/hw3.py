"""
Homework for solving newtons equation
"""


from numpy import *


def solve(x0):
      """
      Doc-string text
      """		
          	
      kmax=100
      tol = 1.0e-14
      
      for k in range(kmax):
              f,fp = target_func(x0)
              
              delta_x = f/fp    
              x0 = x0-delta_x
              print f,fp,x0,delta_x

              if abs(delta_x/x0) < tol:
                  break
#%22.15e.
def target_func(x):
    
     f = sin(x)-(1.-x**2)      
     fp = cos(x)+2.*x
      
     return f,fp




