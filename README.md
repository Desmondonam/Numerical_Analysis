# Numerical_Analysis

# Jacobi Iteration
## Problem Statement:
A large linear system can easily be represented with matrices in the form “Ax=b”, where “A” represents a square matrix that contains the ordered coefficients of our linear system of equations, “x” holds all of our different variables, and “b” represents the constants that each linear equation is equal to. We wish to solve for our unknown x-values, and we can do so through the use of Jacobi Iteration.


## Conclusion 
That’s really all there is to Jacobi Iteration. We take a system of equations, rearrange it a bit, test for convergence, run a bit of code, and then we are done.

# Gauss-Seidel 
Let us take Jacobi’s Method one step further. Where the true solution is x = (x1, x2, … , xn), if x1(k+1) is a better approximation to the true value of x1 than x1(k) is, then it would make sense that once we have found the new value x1(k+1) to use it (rather than the old value x1(k)) in finding x2(k+1), … , xn(k+1). So x1(k+1) is found as in Jacobi's Method, but in finding x2(k+1), instead of using the old value of x1(k) and the old values x3(k), … , xn(k), we now use the new value x1(k+1) and the old values x3(k), … , xn(k), and similarly for finding x3(k+1), … , xn(k+1). This technique is called the Gauss-Seidel Method -- even though, as noted by Gil Strang in his Introduction to Applied Mathematics, Gauss didn’t know about it and Seidel didn’t recommend it.

 In numerical linear algebra, the Gauss–Seidel method, 
        also known as the Liebmann method or the method of successive displacement,
        is an iterative method used to solve a system of linear equations.
        It is named after the German mathematicians Carl Friedrich Gauss
        and Philipp Ludwig von Seidel, and is similar to the Jacobi method.
        Gauss Seidel for 4 Variable 
        Gauss_Seidel_4() 
        Also can pass number of Itration to Perform By default :=> 6
        call this function to get Your Values 