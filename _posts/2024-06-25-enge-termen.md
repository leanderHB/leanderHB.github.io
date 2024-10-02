---
layout: post
title: "Enge termen"
date: 2024-06-25
---
#### note: ik heb hier een beetje zitten prutsen met de afgeleiden, en dit is afgeleid toen ik vrij op was al, dus check nog een keer!

We have the "scary term"
<div>\[
H=u_{1,\xi\xi}^*+f_u(u^*_0,K^*_0)u_1^*+f_v(u^*_0,K^*_0)(K_1^*-u_0^*)=0
\]</div>
This relation holds for all $$\xi$$, hence the $$dH/d\xi$$ is also zero.
<div>\[\begin{aligned}
dH/d\xi&=u_{1,\xi\xi\xi}^*+f_{uu}(u^*_0,K^*_0)u^*_{0,\xi}u_1^*+f_u(u^*_0,K^*_0)u_{1,\xi}^*\\&+f_{vu}(u^*_0,K^*_0)K_1^*u^*_{0,\xi}-f_{vu}(u^*_0,K^*_0)u_0^*u_{0,\xi}^*-f_{v}(u^*_0,K^*_0)u_{0,\xi}^*=0\\
&=u_{1,\xi\xi\xi}^*+f_u(u^*_0,K^*_0)u_{1,\xi}^*-f_{v}(u^*_0,K^*_0)u_{0,\xi}^*\\
&+(f_{uu}(u^*_0,K^*_0)u_1^*+f_{vu}(u^*_0,K^*_0)(K_1^*-u_0^*))u^*_{0,\xi}=0
\end{aligned}\]</div>
Great, we're a bit further, and can replace some terms in the integral:
<div>\[\begin{aligned}
I = -\int  [(\hat\lambda+f_{v}(u_0^*,K_0^*)) u_{0,\xi}^*-(u_{1,\xi\xi\xi}^*+f_u(u^*_0,K^*_0)u_{1,\xi}^*-f_{v}(u^*_0,K^*_0)u_{0,\xi}^*)]d\xi
\end{aligned}\]</div>
But again, the solutions become flat towards the ends, so we can drop the third derivative.

<div>\[
\begin{aligned}
I = -\int  [(\hat\lambda+f_{v}(u_0^*,K_0^*)) u_{0,\xi}^*-f_u(u^*_0,K^*_0)u_{1,\xi}^*+f_{v
}(u^*_0,K^*_0)u_{0,\xi}^*]d\xi
\end{aligned}
\]</div>
Not sure if this is better, but at least we don't have the second derivatives anymore!
