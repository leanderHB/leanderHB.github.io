We introduce locations $P_j(t)$, where $j=1,\dots,N$, which introduces $N$ inner (boundary) layers with $N+1$ outer layers. Denote:
$$
\begin{aligned}
\xi_j = \frac1\epsilon (x-P_j(t)) = \frac1\epsilon\left( x-P_j(0)-\int_0^t \hat c_j(s) ds\right)
\end{aligned}
$$
Check wat $\hat c$ moet zijn! We willen dat ie langzaam beweegt: dus dat we oplossingen van steady state kunnen gebruiken! Logisch dat het snelheid order $\epsilon$ word? want diffusie gaat zo snel.
Maar om vergelijkbaar met paper te krijgen, moet ik $\epsilon^2$ gebruiken, misschien is dat logisch omdat de reactie-term de boel bij elkaar houd?
Voorbeeld: $\hat c = \epsilon^2 c$. 
Note we get traveling wave solutions now:
$$\begin{aligned}
U_t &= U_{\xi_j}(\xi_j)_t = \frac1\epsilon U_{\xi_j}\hat c_j(t)= \epsilon  U_{\xi_j} c_j(t)\\
_t &= V_{\xi_j}(\xi_j)_t = \frac1\epsilon V_{\xi_j}\hat c_j(t)= \epsilon V_{\xi_j} c_j(t)
\end{aligned}$$
Inside these inner layers with coordinates $\xi_j$, we have the equations:
$$
\begin{aligned}
\epsilon U_{\xi_j} c_j(t) &=  U_{\xi_j\xi_j} + f(U,V)\\
\epsilon V_{\xi_j} c_j(t) &=  \frac{1}{\epsilon^2}V_{\xi_j\xi_j} - f(U,V)\\
\end{aligned}
$$
To leading order, we get the same expressions as we find for the steady solutions, $v$ is to leading order constant, and $u$ is following a heteroclinic orbit. Expanding as $U = u_0+\epsilon s$, we get:
$$
\begin{aligned}
\epsilon (u_0+\epsilon s)_{\xi_j} c_j(t) &=  (u_0+\epsilon s)_{\xi_j\xi_j} + f((u_0+\epsilon s),(v_0+\epsilon r))\\
\epsilon^3 (v_0+\epsilon r)_{\xi_j} c_j(t) &=  (v_0+\epsilon r)_{\xi_j\xi_j} - \epsilon^2 f((u_0+\epsilon s),(v_0+\epsilon r))\\
\end{aligned}
$$
Collecting terms of order $\epsilon$, we find:
$$
\begin{aligned}
 (u_0)_{\xi_j} c_j(t) &=   (s)_{\xi_j\xi_j} + f_u(u_0,v_0) s+f_v(u_0,v_0) r\\
0 &=  ( r)_{\xi_j\xi_j}-\epsilon^2 f_u(u_0,v_0) s-\epsilon^2 f_v(u_0,v_0) r
\end{aligned}
$$
So we find that $r$ is also constant (which is unsurprising), and that we now have an expression that is similar to the expression for the linear stability of the steady front, but now with the speed incorporated into it.
Treating $t$ as a parameter, we can simply write:
$$
\begin{aligned}
(u_0)_{\xi_j} c_j(t)-f_v(u_0,v_0) r:=g(\xi_j;t) &=  (\partial_{\xi_j}+f_u(\xi)) s\\
\end{aligned}
$$
This is an inhomogeneous Sturm-Liouville problem with operator $\mathcal L =   (\partial_{\xi_j}+f_u(\xi))$. This is the same operator as for the steady state problem! This already implies that the eigenvalues of the stability of the steady state problem will matter for the dynamics between the pulses.

This also implies that the kernel is non-empty! The translational eigenmode corresponds to a zero eigenvalue. This means that $\mathcal L (u_0)_\xi=0$. This means that for the equation to have a solution, the inhomogeneous part should at least be perpendicular to $(u_0)_\xi$:
$$
\langle g(\xi;t),(u_0)_\xi \rangle=0
$$
Or written as integral:
$$
c_j(t)\int_{I_f} ((u_0)_{\xi_j})^2 d\xi=r\int_{I_f} f_v(u_0,v_0) \,(u_0)_{\xi_j}  d\xi
$$
Note that the integral on the left is familliar:
$$
((u_0)_{\xi_j})^2= \frac{1}{\epsilon^2}((u_0)_{x})^2= 2E-2 F(u)
$$
The hamiltonian we found in the steady state analysis!
We noted before that when we set the primitive correctly, we can set $E=0$. Then we get:
$$
((u_0)_{x})^2= -2 \epsilon^2F(u) = 2\int_{u_-}^u\tilde f(u',\eta_0)du'
$$
Under the integral again:
$$
2\int_{I_f}\int_{u_-}^{u_0(\xi)}\tilde f(u',\eta_0)du'd\xi
$$
This number can be calculated for a specific $\tilde f$, and is has the same magnitude for every front (by symmetry). The thing that differs is the sign, which follows from flipping the bounds of integration.

We integrate the RHS of the Fredholm condition by parts once and get:
$$\begin{aligned}
&r\int_{I_f} f_v(\xi) \,(u_0)_{\xi_j}  d\xi \\
=&\,r\int_{I_f} f_v(\xi) \,(u_0)_{\xi_j}  d\xi 
\end{aligned}$$

$$
fg\Big|_a^b = \int_a^b f'g+\int_a^b fg'
$$
take $f=(u_0)_{\xi_j}$ and $g'=f_v(\xi)$, then:
$$
\int_{I_f} (u_0)_{\xi_j}f_v(\xi)=(u_0)_{\xi_j}F_v\Big|_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon} -\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon} (u_0)_{\xi_j\xi_j}F_vd\xi
$$
Where $F_v$ is a primitive of $f_v(\xi)$. Note that $(u_0)_{\xi_j\xi_j} =f((u_0),(v_0)):=f(\xi)$ to leading order. 
Note that $u_0$ becomes exponentially flat towards the slow region, and the primitive of $f_v$ doesn't become exponentially large, so the term that evaluates at the boundaries is zero to leading order.
$$
2c(t)\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}\int_{u_-}^{u_0(\xi)}\tilde f(u',\eta_0)du'd\xi=-r\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon} f(\xi)F_vd\xi
$$
We can also write the integral differently:
$$
\int_{I_f} f_v(\xi) \,(u_0)_{\xi_j}  d\xi =
$$

$$
fg\Big|_a^b = \int_a^b f'g+\int_a^b fg'
$$
The only thing we haven't fixed is $r$, the rest all to leading order constant. 

![[Pasted image 20240320110210.png]]




