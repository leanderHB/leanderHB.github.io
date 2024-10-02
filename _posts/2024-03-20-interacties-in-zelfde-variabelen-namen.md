---
layout: post
title: "Interacties in zelfde variabelen namen"
date: 2024-03-20
---
Here are the equations with the variable names changed as per your request:

We introduce locations $$P_j(t)$$, where $$j=1,\dots,N$$, which introduces $$N$$ inner (boundary) layers with $$N+1$$ outer layers. Denote:
<div>\[
\begin{aligned}
\xi_j = \frac1\epsilon (x-P_j(t)) = \frac1\epsilon\left( x-P_j(0)-\int_0^t \hat c_j(s) ds\right)
\end{aligned}
\]</div>
Check what $$\hat c$$ moet zijn! We willen dat ie langzaam beweegt: dus dat we oplossingen van steady state kunnen gebruiken! Logisch dat het snelheid order $$\epsilon$$ word? want diffusie gaat zo snel.
Maar om vergelijkbaar met paper te krijgen, moet ik $$\epsilon^2$$ gebruiken, misschien is dat logisch omdat de reactie-term de boel bij elkaar houd?
Voorbeeld: $$\hat c = \epsilon^2 c$$. 
Note we get traveling wave solutions now:
<div>\[\begin{aligned}
u_t &= u_{\xi_j}(\xi_j)_t = \frac1\epsilon u_{\xi_j}\hat c_j(t)= \epsilon u_{\xi_j} c_j(t)\\
v_t &= v_{\xi_j}(\xi_j)_t = \frac1\epsilon v_{\xi_j}\hat c_j(t)= \epsilon  v_{\xi_j} c_j(t)
\end{aligned}\]</div>
Inside these inner layers with coordinates $$\xi_j$$, we have the equations:
<div>\[
\begin{aligned}
\epsilon u_{\xi_j} c_j(t) &=  \frac{1}{\epsilon^2}u_{\xi_j\xi_j} - f(u,v)\\
\epsilon v_{\xi_j} c_j(t) &=  v_{\xi_j\xi_j} + f(u,v)
\end{aligned}
\]</div>
To leading order, we get the same expressions as we find for the steady solutions, $$u$$ is to leading order constant, and $$v$$ is following a heteroclinic orbit. Expanding as $$v = v_0+\epsilon v_1$$, we get:
<div>\[
\begin{aligned}
\epsilon^3 (u_0+\epsilon u_1)_{\xi_j} c_j(t) &=  (u_0+\epsilon u_1)_{\xi_j\xi_j} - \epsilon^2 f((u_0+\epsilon u_1),(v_0+\epsilon v_1))\\
\epsilon (v_0+\epsilon v_1)_{\xi_j} c_j(t) &=  (v_0+\epsilon v_1)_{\xi_j\xi_j} + f((u_0+\epsilon u_1),(v_0+\epsilon v_1))\\
\end{aligned}
\]</div>
Collecting terms of order $$\epsilon$$, we find:
<div>\[
\begin{aligned}
0 &=  \epsilon( u_1)_{\xi_j\xi_j}\\
 (v_0)_{\xi_j} c_j(t) &=   (v_1)_{\xi_j\xi_j} + f_v(u_0,v_0) v_1+f_u(u_0,v_0) u_1
\end{aligned}
\]</div>
So we find that $$u_1$$ is also constant (which is unsurprising), and that we now have an expression that is similar to the expression for the linear stability of the steady front, but now with the speed incorporated into it.
Treating $$t$$ as a parameter, we can simply write:
<div>\[
\begin{aligned}
(v_0)_{\xi_j} c_j(t)-f_u(u_0,v_0) u_1:=g(\xi_j;t) &=  (\partial_{\xi_j}+f_v(\xi)) v_1\\
\end{aligned}
\]</div>
This is an inhomogeneous Sturm-Liouville problem with operator $$\mathcal L =   (\partial_{\xi_j}+f_v(\xi))$$. This is the same operator as for the steady state problem! This already implies that the eigenvalues of the stability of the steady state problem will matter for the dynamics between the pulses.

This also implies that the kernel is non-empty! The translational eigenmode corresponds to a zero eigenvalue. This means that $$\mathcal L (v_0)_\xi=0$$. This means that for the equation to have a solution, the inhomogeneous part should at least be perpendicular to $$(v_0)_\xi$$:
<div>\[
\langle g(\xi;t),(v_0)_\xi \rangle=0
\]</div>
Or written as integral:
<div>\[
c_j(t)\int_{I_f} ((v_0)_{\xi_j})^2 d\xi=u_1\int_{I_f} f_u(u_0,v_0) \,(v_0)_{\xi_j}  d\xi
\]</div>
Note that the integral on the left is familiar:
<div>\[
((v_0)_{\xi_j})^2= \frac{1}{\epsilon^2}((v_0)_{x})^2= 2E-2 F(v)
\]</div>
The Hamiltonian we found in the steady state analysis!
We noted before that when we set the primitive correctly, we can set $$E=0$$. Then we get:
<div>\[
((v_0)_{x})^2= -2 \epsilon^2F(v) = 2\int_{v_-}^v\tilde f(v',\eta_0)dv'
\]</div>
Under the integral again:
<div>\[
2\int_{I_f}\int_{v_-}^{v_0(\xi)}\tilde f(v',\eta_0)dv'd\xi
\]</div>
This number can be calculated for a specific $$\tilde f$$, and is has the same magnitude for every front (by symmetry). The thing that differs is the sign, which follows from flipping the bounds of integration.

We integrate the RHS of the Fredholm condition by parts once and get:
<div>\[\begin{aligned}
&u_1\int_{I_f} f_u(\xi) \,(v_0)_{\xi_j}  d\xi \\
=&\,u_1\int_{I_f} f_u(\xi) \,(v_0)_{\xi_j}  d\xi 
\end{aligned}\]</div>

<div>\[
fg\Big|_a^b = \int_a^b f'g+\int_a^b fg'
\]</div>
take $$f=(v_0)_{\xi_j}$$ and $$g'=f_u(\xi)$$, then:
<div>\[
\int_{I_f} (v_0)_{\xi_j}f_u(\xi)=(v_0)_{\xi_j}F_u\Big|_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon} -\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}
\]</div>
