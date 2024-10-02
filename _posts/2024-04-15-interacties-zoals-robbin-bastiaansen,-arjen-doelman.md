---
layout: post
title: "Interacties zoals Robbin Bastiaansen, Arjen Doelman"
date: 2024-04-15
---
<style>
.math-container {
    max-width: 100%; /* Set a maximum width to prevent it from expanding the page */
    overflow-x: auto; /* Enable horizontal scrolling */
    white-space: nowrap; /* Prevent the text from wrapping */
}
</style>
We introduce locations $$P_j(t)$$, where $$j=1,\dots,N$$, which introduces $$N$$ inner (boundary) layers with $$N+1$$ outer layers. Denote:
<div class="math-container">\[
\begin{aligned}
\xi_j = \frac1\epsilon (x-P_j(t)) = \frac1\epsilon\left( x-P_j(0)-\int_0^t \hat c_j(s) ds\right)
\end{aligned}
\]</div>
Check wat $$\hat c$$ moet zijn! We willen dat ie langzaam beweegt: dus dat we oplossingen van steady state kunnen gebruiken! Logisch dat het snelheid order $$\epsilon$$ word? want diffusie gaat zo snel.
Maar om vergelijkbaar met paper te krijgen, moet ik $$\epsilon^2$$ gebruiken, misschien is dat logisch omdat de reactie-term de boel bij elkaar houd?
Voorbeeld: $$\hat c = \epsilon^2 c$$. 
Note we get traveling wave solutions now:
<div class="math-container">\[\begin{aligned}
U_t &= U_{\xi_j}(\xi_j)_t = \frac1\epsilon U_{\xi_j}\hat c_j(t)= \epsilon  U_{\xi_j} c_j(t)\\
V_t &= V_{\xi_j}(\xi_j)_t = \frac1\epsilon V_{\xi_j}\hat c_j(t)= \epsilon V_{\xi_j} c_j(t)
\end{aligned}\]</div>
Inside these inner layers with coordinates $$\xi_j$$, we have the equations:
<div class="math-container">\[
\begin{aligned}
\epsilon U_{\xi_j} c_j(t) &=  U_{\xi_j\xi_j} + f(U,V)\\
\epsilon V_{\xi_j} c_j(t) &=  \frac{1}{\epsilon^2}V_{\xi_j\xi_j} - f(U,V)\\
\end{aligned}
\]</div>
To leading order, we get the same expressions as we find for the steady solutions, $$v$$ is to leading order constant, and $$u$$ is following a heteroclinic orbit. Expanding as $$U = u_0+\epsilon u_1$$, we get:
<div class="math-container">\[
\begin{aligned}
\epsilon (u_0+\epsilon u_1)_{\xi_j} c_j(t) &=  (u_0+\epsilon u_1)_{\xi_j\xi_j} + f((u_0+\epsilon u_1),(v_0+\epsilon v_1))\\
\epsilon^3 (v_0+\epsilon v_1)_{\xi_j} c_j(t) &=  (v_0+\epsilon v_1)_{\xi_j\xi_j} - \epsilon^2 f((u_0+\epsilon u_1),(v_0+\epsilon v_1))\\
\end{aligned}
\]</div>
Collecting terms of order $$\epsilon$$, we find:
<div class="math-container">\[
\begin{aligned}
 (u_0)_{\xi_j} c_j(t) &=   (u_1)_{\xi_j\xi_j} + f_u(u_0,v_0) u_1+f_v(u_0,v_0) v_1\\
0 &=  ( v_1)_{\xi_j\xi_j}-\epsilon^2 f_u(u_0,v_0) u_1-\epsilon^2 f_v(u_0,v_0) v_1
\end{aligned}
\]</div>
So we find that $$v_1$$ is also constant to leading order (which is unsurprising), and that we now have an expression that is similar to the expression for the linear stability of the steady front, but now with the speed incorporated into it.
Treating $$t$$ as a parameter, we can simply write:
<div class="math-container">\[
\begin{aligned}
(u_0)_{\xi_j} c_j(t)-f_v(u_0,v_0) v_1:=g(\xi_j;t) &=  (\partial_{\xi_j\xi_j}+f_u(\xi)) u_1\\
\end{aligned}
\]</div>
This is an inhomogeneous Sturm-Liouville problem with operator $$\mathcal L =   (\partial_{\xi_j\xi_j}+f_u(\xi))$$. This is the same operator as for the steady state problem! This already implies that the eigenvalues of the stability of the steady state problem will matter for the dynamics between the pulses.

This also implies that the kernel is non-empty! The translational eigenmode corresponds to a zero eigenvalue. This means that $$\mathcal L (u_0)_\xi=0$$. But also $$\mathcal L (v_0)_\xi=0$$! 
## perpendicular to $$u_0$$
This means that for the equation to have a solution, the inhomogeneous part should at least be perpendicular to $$(u_0)_\xi$$:
<div class="math-container">\[
\langle g(\xi;t),(u_0)_\xi \rangle=0
\]</div>
Or written as integral:
<div class="math-container">\[
c_j(t)\int_{I_f} ((u_0)_{\xi_j})^2 d\xi=\int_{I_f} v_1 f_v(u_0,v_0) \,(u_0)_{\xi_j}  d\xi
\]</div>
Note that the integral on the left is familiar:
<div class="math-container">\[
((u_0)_{\xi_j})^2= \frac{1}{\epsilon^2}((u_0)_{x})^2= 2E-2 F(u)
\]</div>
The Hamiltonian we found in the steady state analysis!
We noted before that when we set the primitive correctly, we can set $$E=0$$. Then we get:
<div class="math-container">\[
((u_0)_{x})^2= -2 \epsilon^2F(u) = 2\int_{u_-}^u\tilde f(u',\eta_0)du'
\]</div>
Under the integral again:
<div class="math-container">\[
2\int_{I_f}\int_{u_-}^{u_0(\xi)}\tilde f(u',\eta_0)du'd\xi
\]</div>
This number can be calculated for a specific $$\tilde f$$, and is has the same magnitude for every front (by symmetry). The thing that differs is the sign, which follows from flipping the bounds of integration.

### gaat hopelijk wel goed

<div class="math-container">\[
c_j(t)\int_{I_f} ((u_0)_{\xi_j})^2 d\xi=\int_{I_f} v_1 f_v(u_0,v_0) \,(u_0)_{\xi_j}  d\xi
\]</div>
Integrating by parts twice, writing $$h' = f_v(u_0,v_0)(u_0)_{\xi_j}$$ and $$H' = h$$, we get:
<div class="math-container">\[
\int_{I_f} v_1 f_v(u_0,v_0) \,(u_0)_{\xi_j}  d\xi = h v_1\Big|_{I_f}-\int_{I_f}(v_1)_{\xi_j} hd\xi
\]</div>
we neglect the first part (why?)
<div class="math-container">\[
-\int_{I_f}(v_1)_{\xi_j}hd\xi = -(v_1)_{\xi_j} H\Big |_{I_f}+\int_{I_f}H (v_1)_{\xi_j\xi_j}d\xi_j
\]</div>
we neglect the second part (again, why?) and find:
<div class="math-container">\[
c_j(t)\int_{I_f} ((u_0)_{\xi_j})^2 d\xi=-(v_1)_{\xi_j} H\Big |_{I_f}
\]</div>
$$H$$ just depends on the reaction term, and not on any dynamics, and we're free to choose the constants of integration, so if we pick them wisely, we find that $$H=H_{1/\sqrt\epsilon}=-H_{-1/\sqrt\epsilon}=-H$$ and hence:
<div class="math-container">\[
c_j(t)=H ((v_1)_\xi(1/\sqrt{\epsilon})+(v_1)_\xi(-1/\sqrt{\epsilon}))
\]</div>


## Outer layer
in the outer layer, we'd like to match the derivatives of the fast $$v_1$$.  
We have the outer layer expressions, and since our wave travels at $$\epsilon^2$$ speed, we get:
<div class="math-container">\[
\begin{aligned}
\epsilon^2 U_{x_j} c_j(t)&=\epsilon^2U_{xx}+f(U,V)\\
\epsilon^2 V_{x_j} c_j(t)&=V_{xx}-f(U,V)
\end{aligned}
\]</div>
Taylor expanding this whole business, we get:
<div class="math-container">\[
\begin{aligned}
0&=\epsilon^2(u_0+\epsilon u_1)_{xx}+f(u_0+\epsilon u_1,v_0+\epsilon v_1)+O(\epsilon^2)\\
0&=(v_0+\epsilon v_1)_{xx}-f(u_0+\epsilon u_1,v_0+\epsilon v_1)+O(\epsilon^2)
\end{aligned}
\]</div>
Or in a bit more excruciating detail:
<div class="math-container">\[
\begin{aligned}
0&=\epsilon^2(u_0)_{xx}+\epsilon^3(\epsilon u_1)_{xx}+f(u_0,v_0)+\epsilon f_u(u_0,v_0)u_1+\epsilon f_v(u_0,v_0)v_1+O(\epsilon^2)\\
0&=(v_0)_{xx}+\epsilon (v_1)_{xx}-f(u_0,v_0)-\epsilon f_u(u_0,v_0)u_1-\epsilon f_v(u_0,v_0)v_1+O(\epsilon^2)
\end{aligned}
\]</div>
At order $$\epsilon^0=1$$, we get:
<div class="math-container">\[
\begin{aligned}
0&=f(u_0,v_0)\\
0&=(v_0)_{xx}-f(u_0,v_0)
\end{aligned}
\]</div>
Which results in $$u_0(x)=u_0$$, just constant, and thereby $$v_0(x)=v_0$$, also constant (assuming non-degenerate $$f$$).
Now at order $$\epsilon$$, we get:
<div class="math-container">\[
\begin{aligned}
0&=\epsilon f_u(u_0,v_0)u_1+\epsilon f_v(u_0,v_0)v_1\\
0&=(\epsilon v_1)_{xx}-\epsilon f_u(u_0,v_0)u_1-\epsilon f_v(u_0,v_0)v_1
\end{aligned}
\]</div>
this implies that also 


## Outer layer second try
in the outer layer, we'd like to match the derivatives of the fast $$v_1$$.  
We have the outer layer expressions, and since our wave travels at $$\epsilon^2$$ speed, we get:
<div class="math-container">\[
\begin{aligned}
\epsilon^2 U_{x} c_j(t)&=\epsilon^2U_{xx}+f(U,V)\\
\epsilon^2 V_{x} c_j(t)&=V_{xx}-f(U,V)
\end{aligned}
\]</div>
Taylor expanding this whole business, we get:
<div class="math-container">\[
\begin{aligned}
\epsilon^2 (\bar U+\delta u)_{x} c_j(t)&=\epsilon^2(\bar U+\delta u)_{xx}+f(\bar U+\delta u,\bar V+\delta v)+O(\delta^2)\\
\epsilon^2 (\bar V+\delta v)_{x} c_j(t)&=(\bar V+\delta v)_{xx}-f(\bar U+\delta u,\bar V+\delta v)+O(\delta^2)
\end{aligned}
\]</div>
Or in a bit more detail:
<div class="math-container">\[
\begin{aligned}
\epsilon^2 (\bar U+\delta u)_{x} c_j(t)&=\epsilon^2(\bar U+\delta u)_{xx}+f(\bar U,\bar V)+f_U(\bar U,\bar V)\delta u+f_V(\bar U,\bar V)\delta v+O(\delta^2)\\
\epsilon^2 (\bar V+\delta v)_{x} c_j(t)&=(\bar V+\delta v)_{xx}-f(\bar U,\bar V)-f_U(\bar U,\bar V)\delta u-f_V(\bar U,\bar V)\delta v+O(\delta^2)
\end{aligned}
\]</div>
At order $$\delta^0=1$$, we get:
<div class="math-container">\[
\begin{aligned}
\epsilon^2 \bar U_{x} c_j(t)&=\epsilon^2\bar U_{xx}+f(\bar U,\bar V)\\
\epsilon^2 \bar V_{x} c_j(t)&=\bar V_{xx}-f(\bar U,\bar V)
\end{aligned}
\]</div>
So we can assume that to leading order, $$\bar U,\bar V$$ satisfy the stationary equations.
Now at order $$\delta$$, we get:
<div class="math-container">\[
\begin{aligned}
0&=\epsilon^2(\bar U+\delta u)_{xx}+f(\bar U,\bar V)+f_U(\bar U,\bar V)\delta u+f_V(\bar U,\bar V)\delta v+O(\delta^2)\\
0&=(\bar V+\delta v)_{xx}-f(\bar U,\bar V)-f_U(\bar U,\bar V)\delta u-f_V(\bar U,\bar V)\delta v+O(\delta^2)
\end{aligned}
\]</div>
this implies that also 


### gaat nie goed

We integrate the RHS of the Fredholm condition by parts once and get:
<div class="math-container">\[\begin{aligned}
&v_1\int_{I_f} f_v(\xi) \,(u_0)_{\xi_j}  d\xi \\
=&\,v_1\int_{I_f} f_v(\xi) \,(u_0)_{\xi_j}  d\xi 
\end{aligned}\]</div>

<div class="math-container">\[
fg\Big|_a^b = \int_a^b f'g+\int_a^b fg'
\]</div>
take $$f=(u_0)_{\xi_j}$$ and $$g'=f_v(\xi)$$, then:
<div class="math-container">\[
\int_{I_f} (u_0)_{\xi_j}f_v(\xi)=(u_0)_{\xi_j}F_v\Big|_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon} -\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon} (u_0)_{\xi_j\xi_j}F_vd\xi
\]</div>
Where $$F_v$$ is a primitive of $$f_v(\xi)$$. Note that $$(u_0)_{\xi_j\xi_j} =f((u_0),(v_0)):=f(\xi)$$ to leading order. 
Note that $$u_0$$ becomes exponentially flat towards the slow region, and the primitive of $$f_v$$ doesn't become exponentially large, so the term that evaluates at the boundaries is zero to leading order.
<div class="math-container">\[
2c(t)\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}\int_{u_-}^{u_0(\xi)}\tilde f(u',\eta_0)du'd\xi=-v_1\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon} f(\xi)F_vd\xi
\]</div>
We can also write the integral differently:
<div class="math-container">\[
\int_{I_f} f_v(\xi) \,(u_0)_{\xi_j}  d\xi =
\]</div>

<div class="math-container">\[
fg\Big|_a^b = \int_a^b f'g+\int_a^b fg'
\]</div>
The only thing we haven't fixed is $$v_1$$, the rest all to leading order constant. 

<img src="/assets/images/Pasted image 20240320110210.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240320110210.png">
## Perpendicular to $$v_0$$
This means that for the equation to have a solution, the inhomogeneous part should at least be perpendicular to $$(u_0)_\xi$$:
<div class="math-container">\[
\langle g(\xi;t),(v_0)_\xi \rangle=0
\]</div>
Or written as integral:
<div class="math-container">\[
c_j(t)\int_{I_f} ((u_0)_{\xi_j})^2 d\xi=\int_{I_f} v_1 f_v(u_0,v_0) \,(u_0)_{\xi_j}  d\xi
\]</div>
