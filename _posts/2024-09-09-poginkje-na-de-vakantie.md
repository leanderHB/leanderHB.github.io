---
layout: post
title: "Poginkje na de vakantie"
date: 2024-09-09
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>


With the information that $$v_0=0$$, this becomes: 
<div class="math-container">\[
\begin{aligned}
 \hat\lambda u_0 &= u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+ v_1f_V^*\\
0&= ( v_1)_{\xi\xi}-f_U^*u_0
\end{aligned}
\]</div>
Okay that's workable, we find something interesting, when the equation for $$v_1$$ is added to the equation for $$u_0$$, we get:
<div class="math-container">\[
(u_0+v_1)_{\xi\xi}  =0\quad\implies \quad u_0=-v_1
\]</div>

Next we need one more order of $$v$$:
<div class="math-container">\[\begin{aligned}
0&= v_{2,\xi\xi}-f_U^* u_1+[ -f_{UU}^* U_1^*-f_{UV}^* (K_1^*-U_0^*)]u_0-f_V^*v_1
\end{aligned}
\]</div>
We do something similar to what we did earlier, and add this to the equation with $$u_1$$. Then we obtain:
<div class="math-container">\[
\hat \lambda u_0 = u_{1,\xi\xi}+v_{2,\xi\xi}
\]</div>
So where to leading order, the perturbation was just translation, we now find a nontrivial correction. We use $$u_0=-v_1$$ to rewrite:
<div class="math-container">\[
\begin{aligned}
\hat\lambda u_0 &= u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+ v_1f_V^*\\
\hat\lambda u_0 &= u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)- f_V^*]u_0\\
\end{aligned}
\]</div>
Fredholm solvability criterion then tells us that solutions should obey:
<div class="math-container">\[
\langle u_0, [f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)- f_V^*-\hat\lambda ]u_0\rangle = 0
\]</div>
or written differently:
<div class="math-container">\[
\langle (u_0)^2, f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)- f_V^* \rangle = \hat\lambda\|u_0\|^2_2
\]</div>


[View Raw Markdown](/assets/md/Poginkje na de vakantie.md)
