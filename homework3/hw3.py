# $UWHPSC/codes/homework3/test_code.py 
# To include in newton.py

from numpy import *
# This algoritm works with varying succcess in differant regions. Implement a test for convergence to reduce the number of itterations once a solution has been found

def sqrt2(x):

	
	s=1.
	kmax=100
	tol = 1.0e-14
	for k in range(kmax):
		s0=s
		s=0.5*(s+ x/s)
		delta_s = s-s0
		print "s=%20.15f" % s
		if abs(delta_s/x) < tol: # N.b error relative to x 

		   break
	print "After %g iterations s= %20.15f" % (k+1,s)
