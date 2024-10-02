Maybe this:
$$
H=u_{1,\xi\xi}^*+f_u(u^*_0,K^*_0)u_1^*+f_v(u^*_0,K^*_0)(K_1^*-u_0^*)=0
$$
Take functional derivative wrt to $u_0^*$:
$$
\int u_{1,\xi\xi}^*+f_u((u^*_0+\delta w),K^*_0)u_1^*+f_v((u^*_0+\delta w),K^*_0)(K_1^*-(u_0^*+\delta w))d\xi
$$
Expanding $f$:
$$\begin{aligned}
\int u_{1,\xi\xi}^*+f_u(u^*_0,K^*_0)u_1^*+\delta wf_{uu}(u^*_0,K^*_0)u_1^*+f_v(u^*_0,K^*_0)(K_1^*-u_0^*)\\+f_{vu}(u^*_0,K^*_0)K_1^*\delta w+f_v(u^*_0,K^*_0)\delta wd\xi+O((\delta w)^2)
\end{aligned}$$
The linear terms in $\delta w$ are:
$$
\begin{aligned}
\frac{d H}{d u_0^*}=f_{uu}(u^*_0,K^*_0)u_1^*+f_{vu}(u^*_0,K^*_0)K_1^*+f_v(u^*_0,K^*_0)
\end{aligned}
$$
