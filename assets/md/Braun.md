# gek

- local quasi-stable voelt gek? Want als je animatie bekijkt lijkt het vooral dat alles netjes op de lijn komt ipv de nullcline van de reactie. Die laatste wordt heel kort gevolgd tot die redelijk rap naar de 
# Afleidingen
$$
\begin{aligned}
u_t &= D_u\Delta u + f(u,v)\\
v_t &= D_v\Delta v - f(u,v)\\
\end{aligned}
$$
Clearly, $n = u + v$ is conserved globally by Stokes' theorem.
Well-mixed: the system reduces to
$$
\begin{aligned}
u_t &= f(u,v)\\
v_t &= -f(u,v)\\
\end{aligned}
$$
Since $n$ is fixed, the system is stable at the points $\vec{u}^*(n) = f(u^*,v^*) = 0$ and $u^* + v^* = n$. 
Note that we can write $v = n - u$, and therefore write:
$$
u_t = f(u, n - u)
$$
Which then captures all the dynamics. Then on the line $u + v = n$, we can find the stability by the sign of the derivative of $f$:
$$
\frac{d}{du}f(u, n - u) = f_u(u, n - u) - f_v(u, n - u)
$$
Then to first order, we can approximate $f$ around the reactive nullcline $u + v = n$:



## stationarity
Stationary equations:
$$
\begin{aligned}
0 &= D_u\Delta u + f(u,v)\\
0 &= D_v\Delta v - f(u,v)\\
\end{aligned}
$$
Adding these, gives:
$$
\begin{aligned}
D_u\Delta u &= -D_v\Delta v \\
\end{aligned}
$$
Integrating twice and using the boundary conditions:
$$
\frac{D_u}{D_v}u+v =\eta_0 
$$
Where $\eta_0$ is a constant of integration, fixed by the boundary terms. 
#### Higher Dim
We analogously get 
$$
\begin{aligned}
D_u\Delta u +D_v\Delta v&= 0 \\
D_u\int_X\Delta u(x)dx +D_v\int_X\Delta v(x)dx&= 0 \\
\end{aligned}
$$
Using Stokes' on the boundary, plus the no-flux boundary conditions (mass is conserved, so boundary term is zero) or the periodic boundary conditions (there is no boundary, so boundary term is zero), we get (weakly?):
$$
\begin{aligned}
D_u\nabla u +D_v\nabla v&= 0 \\
\frac{D_u}{D_v}\nabla u +\nabla v&= 0 \\
\end{aligned}
$$
Notably, in steady state, the flux is balanced in all directions. Integrating again gives the same result as earlier:
$$
\begin{aligned}
\int_X\frac{D_u}{D_v}\nabla u(x)dx +\int_X\nabla v(x)dx&= 0 \\
\int_{\partial X}\frac{D_u}{D_v}\nabla u(x)\cdot ds +\int_X\nabla v(x)dx&= 0 \\
\end{aligned}
$$
This yields again $\frac{D_u}{D_v} u+v=\delta u+v=\eta$, where $\eta$ is again a boundary term related to the total fluctuation of the effective flux over the domain.  
## Equation for $\eta_0$. 
Define $\eta:=v+\frac{D_u}{D_v}u=v+\delta u$, then define $\tilde f(u,\eta):=f(u, \eta-\delta u)=f(u,v)$. Then we can rewrite the stationarity equations:
$$
\begin{aligned}
0 &= D_u\Delta u + f(u,v)\\
0 &= D_v\Delta v - f(u,v)\\
\end{aligned}
$$
Into:
$$
\begin{aligned}
0 &= D_u\Delta u + \tilde f(u,\eta)\\
0 &= D_v\Delta v - f(u,\eta)+D_u\Delta u + f(u,\eta)\\
 &= D_v\left(\Delta v +\frac{D_u}{D_v}\Delta u \right)=D_v\eta\\
\end{aligned}
$$
The second again gives that $\eta$ is constant in steady state, so let's call it $\eta_0$. The second then tells us how to find that constant. The constant that satisfies the first equation, is the one we're after, and this constant tells us along which line in reactive phase-space our fields will exist. Note the power in this, stationary patterns cannot have other proportions than the one we're about to find. 
#### First approximation
Assume our domain is large enough to support plateaus, so there's bits where $\nabla u\approx0$ and $\Delta u\approx 0$. Then we can integrate over a line $\gamma:[0,1]\to X$, such that $\gamma(0)$ is at a flat spot on a low plateau, and $\gamma(1)$ is at a flat spot in the high plateau. Then our stationarity condition should still hold!
$$
0 =\int_0^1 D_u\Delta u(\gamma(t))dt + \int_0^1\tilde f(u(\gamma(t),\eta_0)dt
$$
Partially integrating and using the flat boundary, we find:
$$
0 =\int_0^1\tilde f(u(\gamma(t),\eta_0)dt
$$
We would of course like to make this an integral over $u$, since we'd like this analysis to be solution-independent. Therefore, we can multiply the stationarity condition by $\frac{du}{d\gamma}$ before this whole business. (doesn't this mess with the flatness?? Check ff). Then a reverse substitution of variables yields:
$$
0 = \int_{u_{-}}^{u_+}f(u,\eta_0)du
$$
If we assume that at the plateaus, the diffusion and reaction balance, we then get, via geometric construction, that we should use the intersection of the subspace parametrized by $\eta$ and the nullcline of the reaction to find $u_-$ and $u_+$. 
## $\eta_0$ approximation
As derived in the previous section, if the domain is large enough, we can approximate $\eta_0$ by solving
$$
0 = \int_{u_{-}}^{u_+}f(u,\eta)du
$$
Using fsolve to find the intersections with the line parametrized by $\eta$, and then numerically integrating using the trapezoid rule and going up/down using bissection, we find the line:
![[Pasted image 20240208151446.png]]]]

