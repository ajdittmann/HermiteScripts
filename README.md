# HermiteScripts
Sympy scripts that can be used to carry out Hermite interpolation (e.g. [1](https://www.jstor.org/stable/2308924 ))and then take integrals or derivatives of the interpolants. 

Each function $f(x)$ is approximated by an interpolant $\tilde{f}(x)$. The interpolant samples the function and its derivatives at points $x_i$ and is given by

$$ \tilde{f}(x) = \sum_{j=0}^r\sum_{i=0}^n c_{i,j}  f^{(j)}(x_i),$$ where $$ f^{(j)} = \frac{d^j f}{dx^j}.$$

Note that integrals and derivatives of the interpolant will simply have different coefficients $c_{i,j}$. Each script prints a list of these coefficients for different applications.


