$$
\begin{aligned}
u_t &= \delta\Delta u + f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
$$
Introduce $\xi= x+ct$, then $u_t = u_\xi \xi_t=cu_\xi$ and $u_x = u_\xi$. Filling this in (1D) yields:
$$
\begin{aligned}
cu_\xi &= \delta u_{\xi\xi} + f(u,v)\\
cv_\xi &=  v_{\xi\xi} - f(u,v)\\
\end{aligned}
$$
Adding the two equations yields:
$$
c(u_\xi+v_\xi) = \delta u_{\xi\xi}+v_{\xi\xi}
$$
We can integrate once to get:
$$
c(u+v) = \delta u_{\xi}+v_{\xi}+C = \frac{d(\delta u+v)}{d\xi}+C
$$
This should hold everywhere, in specific at $\xi\to\pm\infty$, where we assume the derivative to become zero for homoclinic/heteroclinic solutions, so 
$$
c(u_{\pm\infty}+v_{\pm\infty}) =C
$$
This dictates that $u_{\infty}+v_{\infty}=u_{-\infty}+v_{-\infty}$. This is also expected for non-moving fronts. 
Now we can use this solution:
$$
c(u-u_{\infty}+v-v_{\infty}) = \frac{d(\delta u+v)}{d\xi}
$$
Use perturbation theory:
$$
cu_0+c^2u_1 -cu_{\infty}+cv_0+c^2v_1+\dots-cv_{\infty}) = \frac{d(\delta u_0+cu_1+v_0+cv_1+\dots)}{d\xi}
$$
Collecting order of $c$ to second order:
$$\begin{aligned}
\delta (u_0)_\xi+ (v_0)_\xi = 0\\
\delta (u_1)_\xi+ (v_1)_\xi = u_0-u_\infty+v_0-v_\infty\\
\end{aligned}$$
The first equation trivially gives $\delta u_0+v_0=\eta$, for some constant of integration $\eta$. Filling this into the second equation yields a problem... :( 
$$
\delta (u_1)_\xi+ (v_1)_\xi = u_0-u_\infty+v_0-v_\infty\\
$$



Using integration trick:
$$
d\xi= \frac{d(\delta u+v)}{c(u+v) -C}
$$
If $c<<C$, then we get approximately (oh maar dat werkt niet...)
$$
K\xi (c(u+v) -C)= (\delta u+v)+\eta_0
$$
For $K\not=0$, this cannot stay bounded, since $c<< C$, so we must have $K=0$, and hence traveling wave solutions exist for small $c$, and also lie on 