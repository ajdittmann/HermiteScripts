# Hermite scripts
Sympy scripts that can be used to carry out Hermite interpolation (e.g., [1](https://www.jstor.org/stable/2308924 )) and then take integrals or derivatives of the interpolants.

Each function $f(x)$ is approximated by an interpolant $\tilde{f}(x)$. The interpolant samples the function and its derivatives at points $x_j$ and is given by

$$ \tilde{f}(x) = \sum_{k=0}^r\sum_{j=0}^n c_{i,j}(x)  f^{(k)}(x_i),$$ where $$ f^{(k)} = \frac{d^k f}{dx^k}.$$

Note that integrals and derivatives of the interpolant will simply have different coefficients $c_{i,j}$. Each script prints a list of these coefficients for different applications.

* ``getInterpolant.py`` given values of $n$ and $r$, returns each function $c_{i,j}(x)$. By default assumes only that $x_0=0$.
* ``getIntegral.py`` given values of $n$ and $r$, returns the coeficients for the integral of $\tilde{f}$. Integration bounds are to be adjusted manually, and $x_0=0$ is assumed.
* ``getDerivative.py`` given values of $n$, $r$, and ``n_deriv_out`` returns the coeficients for the ``n_deriv_out``-th derivative of $\tilde{f}$. $x_0=0$ is assumed, and by default the derivatives are evaluated at $x_n$.

