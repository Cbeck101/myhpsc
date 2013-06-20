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

def target_func(x):
    
     f = x**2-x      
     fp = 2.*x
      
     return f,fp




