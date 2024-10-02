$$\begin{aligned}
U_t &=\epsilon^2 U_{xx}+f(U,V)\\
V_t &= V_{xx}-f(U,V)
\end{aligned}$$
Do the $\epsilon^2 U+V=K$ trick, and define:
$$
(U_{het},V_{het})
$$
as the heteroclinic solution to the planar Hamiltonian system (parameterized by K) that arises:
$$
(U_{het})_{xx}+f(U_{het},K-\epsilon^2 U_{het})=0
$$
Define the fast subsystem as:
$$\begin{aligned}
\tilde U_t=\tilde U_{xx}+f(\tilde U,\tilde V)\\
\epsilon^2\tilde V_t=\tilde V_{xx}-\epsilon^2f(\tilde U,\tilde V)
\end{aligned}$$
We find: $\tilde V=\tilde V_0+\epsilon^2 \tilde V_2+O(\epsilon^3)$, hence:
$$
\tilde U_t=\tilde U_{xx}+f(\tilde U,\tilde V_0+\epsilon^2 \tilde V_2)\\
$$
We'd like to paste things together, so we pick $\tilde V_0=K$? voelt niet helemaal legaal dit.
$$
\tilde U_t=\tilde U_{xx}+f(\tilde U,\tilde V_0+\epsilon^2 \tilde V_2)\\
$$

