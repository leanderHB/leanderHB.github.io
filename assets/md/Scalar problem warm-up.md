Take the scalar problem:
$$
U_t = U_{xx}+f(U)
$$
and assume the conditions are such that there's a heteroclinic steady-state solution $U(x)$. Then to find its stability, we expand around this solution:
$$
U^* = U+\delta u(x)\exp(\lambda t)
$$
with $\delta\ll1$. Then we obtain:
$$
\lambda u=u_{xx}+f_U(U^*)u
$$
We now define $\mathcal L=\partial_{xx}+f_U(U^*)$. This is a Sturm-Liouville operator, hence solutions can be enumerated: $\lambda_0>\lambda_1>\dots$ with $u_{\lambda_0},u_{\lambda_1},\dots$ the solutions, with $0,1,\dots$ zeros. Now consider the following:
$$
U^*_{xxx}+f_U(U^*)U^*_x = (U^*_{xx}+f(U^*))_x = (0)_x =0
$$
Hence $U^*_x$ is a solution with eigenvalue $0$. Then lastly, since $U^*$ is monotonic, $U^*_x$ has no zeros. Hence we found the solution with the largest eigenvalue, and all other solutions to the stability problem must have strictly smaller eigenvalues. 