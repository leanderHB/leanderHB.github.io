connected to [[Arjen Notes (my interpretation)]]
Take the stationary equation for $u$:
$$
u_{\xi\xi}+f(u,K-\epsilon^2u)=0
$$
Let's assume there exists a $K=K^*$ such that this equation has a heteroclinic orbit. 
Then expand $u$ and $K$:
$$
\begin{aligned}
u^* = u^*_0+\epsilon^2u^*_1+\dots\\
K^* = K^*_0+\epsilon^2K^*_1+\dots\\
\end{aligned}
$$
Inserting this into the equation, we find at order $1$:
$$
u_{0,\xi\xi}^* +f(u^*_0,K^*_0)=0
$$
and at order $\epsilon^2$:
$$
u_{1,\xi\xi}^*+f_u(u^*_0,K^*_0)u_1^*+f_v(u^*_0,K^*_0)(K_1^*-u_0^*)
$$
Here we recognize the SL operator that we keep getting, and therefore note that to have a solution, we require:
$$
\int_\mathbb R u_0^*(\xi)u_{0,\xi}^*(\xi)f_v(u_0^*(\xi),K_0^*)d\xi = K_1^*\int_\mathbb R u_{0,\xi}^*f_v(u_0^*(\xi),K_0^*)d\xi
$$
So we have:
$$
K_1^*=\frac{\int_\mathbb R u_0^*(\xi)u_{0,\xi}^*(\xi)f_v(u_0^*(\xi),K_0^*)d\xi}{\int_\mathbb R u_{0,\xi}^*f_v(u_0^*(\xi),K_0^*)d\xi} 
$$



# Stability next order
We set $\lambda = \epsilon^2 \hat\lambda$ 
$$
\begin{aligned}
u = u^*+\delta \hat u\exp(\lambda t)\\
v = v^*+\delta v\exp(\lambda t) 
\end{aligned}
$$
$$\begin{aligned}
\epsilon^2 \hat\lambda \hat u&=\hat u_{\xi\xi}+f_u(u^*,v^*)\hat u+f_v(u^*,v^*)\hat v\\
\epsilon^4\hat\lambda \hat v&=\hat v_{\xi\xi}-\epsilon^2f_u(u^*,v^*)\hat u-\epsilon^2f_v(u^*,v^*)\hat v
\end{aligned}$$
Using our expansions: 
$$\begin{aligned}
u^*&=u^*_0+\epsilon^2u_1^* \\ 
v^*&=K^*-\epsilon^2 u^* = K_0^*+\epsilon^2 (K_1^* -u^*_0)\\
\hat u&=\hat u_0+\epsilon^2\hat u_1\\
\hat v&=\epsilon^2\hat{\hat v}_0+\epsilon^4\hat{\hat v}_1
\end{aligned}$$
Here we use $\hat{\hat v}$ as otherwise, we get no solutions, see [[Problem]]
we get:
$$
\begin{aligned}
0&=\hat u_{0,\xi\xi}+f_u(u^*_0,v^*_0)\hat u_0\\
0&=\hat{\hat v}_{0,\xi\xi}-f_u(u^*,v^*)\hat u_0
\end{aligned}
$$
at leading order.
Note the implications, like you might expect, at leading order, the perturbations have to be mass conserving, this is reassuring (and actually the first thing I said to Arjen haha). This is described by a similar relation as before: 
$$
\hat {\hat v}_0+\hat u_0=C
$$
I feel like $C$ should be zero, but that's again my intuition about massless perturbations. 

The rest of the mess:
$$
\begin{aligned}
\epsilon^2 \hat\lambda (\hat u_0+\epsilon^2\hat u_1)&=(\hat u_0+\epsilon^2\hat u_1)_{\xi\xi}+f_u(u^*,v^*)(\hat u_0+\epsilon^2\hat u_1)+f_v(u^*,v^*)\epsilon^2\hat{\hat v}\\
\epsilon^4\hat\lambda (\hat{\hat v}_0+\epsilon^2\hat{\hat v}_1)&=(\hat{\hat v}_0+\epsilon^2\hat{\hat v}_1)_{\xi\xi}-f_u(u^*,v^*)(\hat u_0+\epsilon^2\hat u_1)-\epsilon^2f_v(u^*,v^*)(\hat{\hat v}_0+\epsilon^2\hat{\hat v}_1)
\end{aligned}
$$
expanding $f$ too and tossing terms of order $4$:
$$
\begin{aligned}
\epsilon^2 \hat\lambda \hat u_0&=(\hat u_0+\epsilon^2\hat u_1)_{\xi\xi}+(f_{u}(u_0^*,K_0^*)+\epsilon^2(f_{uu}(u_0^*,K_0^*)u_1^* \\&+f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0)))(\hat u_0+\epsilon^2\hat u_1)+(f_{v}(u_0^*,K_0^*)+\epsilon^2(f_{vu}(u_0^*,K_0^*)u_1^* \\&+f_{vv}(u_0^*,K_0^*)(K_1^* -u^*_0)))\epsilon^2\hat{\hat v}_0\\
0&=\epsilon^2\hat{\hat v}_{1,\xi\xi}-f_u(u^*,v^*)\epsilon^2\hat u_1-\epsilon^2f_v(u^*,v^*)\hat{\hat v}_0
\end{aligned}
$$
At order 2 we get:
$$
\begin{aligned}
\hat\lambda \hat u_0&=\hat u_{1,\xi\xi}+f_{u}(u_0^*,K_0^*)\hat u_1+(f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0\\&+f_{v}(u_0^*,K_0^*)\hat{\hat v}_0 \\
0&=\epsilon^2\hat{\hat v}_{1,\xi\xi}-f_u(u^*,v^*)\epsilon^2\hat u_1-\epsilon^2f_v(u^*,v^*)\hat{\hat v}_0
\end{aligned}
$$
The top term is again an inhomogeneous SL problem:
$$
g(\xi)=\hat u_{1,\xi\xi}+f_{u}(u_0^*,K_0^*)\hat u_1
$$
Where $g$ captures the horror that $\nu=2$ created...

### Fast jump
$$
\int \hat{\hat v}_{\xi\xi} = \int \hat{\hat v}_{0,\xi\xi}+\epsilon^2 \hat{\hat v}_{1,\xi\xi}d\xi
$$
The first integral is zero:
$$
\int \hat{\hat v}_{0,\xi\xi}d\xi = -\int \hat u_{0,\xi\xi}d\xi = 0
$$
As $\hat u_0=u^*_0$, therefore is heteroclinic, and has flat ends. So our fast jump is:
$$
\Delta_{fast} \hat{\hat v}_{\xi} = \epsilon^2\int_\mathbb R f_u(u^*,v^*)\hat u_1+f_v(u^*,v^*)\hat{\hat v}_0 d\xi
$$
The good news is that both integrals now converge (i think?) It's also almost the same expression as before, except the fact that the functions here are a lot harder to find explicitly. 
### Enge dingen
We've got our fast jump:
$$
\Delta_{fast} \hat{\hat v}_{\xi} = \epsilon^2\int_\mathbb R f_u(u^*,v^*)\hat u_1+f_v(u^*,v^*)\hat{\hat v}_0 d\xi
$$
Using the order $2$ equations for $\hat u$, we get:
$$
f_{u}(u_0^*,K_0^*)\hat u_1+f_{v}(u_0^*,K_0^*)\hat{\hat v}_0= \hat\lambda \hat u_0-(f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0-\hat u_{1,\xi\xi}
$$
Substituting in our integral we get a bit of a mess:
$$
\Delta_{fast} \hat{\hat v}_{\xi}  = \int [\hat\lambda \hat u_0-\hat u_{1,\xi\xi}-(f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0]d\xi
$$
The slow region is a linear, constant coefficient problem, so $\hat u_1$ will be a decaying function on both ends, hence the integral over the curvature of $\hat u_1$ is zero. 
$$
\Delta_{fast} \hat{\hat v}_{\xi}  = \int  [(\hat\lambda+f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0]d\xi
$$
Good news: integral indeed converges. Bad news, I have no clue what to do with this (:

in enge termen schrijf ik dit om naar een integraal over alleen maar eerste afgeleiden van $f$, maar nu wel een $\hat u_{1,\xi}$ term... [[Enge termen]]
$$
\begin{aligned}
\Delta_{fast} \hat{\hat v}_{\xi}  = -\int  [(\hat\lambda-f_u(u^*_0,K^*_0)u_{1,\xi}^*+f_{v}(u^*_0,K^*_0)u_{0,\xi}^*]d\xi
\end{aligned}
$$

[[oude versie fast jump]]

### afgeleide langs functie
$$
f_\xi(u^*,v^*) = f_u(u^*,v^*)u^*_\xi+f_v(u^*,v^*)v^*_\xi = f_u(u^*,v^*)u^*_\xi-\epsilon^2 f_v(u^*,v^*)u_\xi^*
$$
inserting $u^*$ expansion:
$$
f_\xi(u^*,v^*) = f_u(u^*,v^*)(u^*_{0,\xi}+\epsilon^2u^*_{1,\xi})-\epsilon^2 f_v(u^*,v^*)u^*_{0,\xi}+O(\epsilon^4)
$$
Integrating over the entire line, we find:
$$
0=\int_\mathbb R f_\xi(u^*,v^*)d\xi = \int_\mathbb R f_u(u^*,v^*)(u^*_{0,\xi}+\epsilon^2u^*_{1,\xi})-\epsilon^2 f_v(u^*,v^*)u^*_{0,\xi}d\xi +O(\epsilon^4)
$$
So:
$$
\int_\mathbb R f_u(u^*,v^*)u^*_{1,\xi}- f_v(u^*,v^*)u^*_{0,\xi}d\xi= \frac{1}{\epsilon^2}\int_\mathbb R f_u(u^*,v^*)u^*_{0,\xi}d\xi +O(\epsilon^2) 
$$