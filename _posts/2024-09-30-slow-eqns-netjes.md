---
layout: post
title: "Slow eqns netjes"
date: 2024-09-30
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

For the slow equations, we introduce $$X=\epsilon x$$. Then the (superslow) equations become:
<div class="math-container">\[
\begin{aligned}
\epsilon^2 \hat\lambda u & = \epsilon^4u_{XX}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)]u \\
& +[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)]v+\mathcal O(\epsilon^4) \\
\epsilon^2 \hat\lambda v & = \epsilon^2 v_{XX}+[-f_U^* -\epsilon^2f_{UU}^* U_1^*-\epsilon^2f_{UV}^* (K_1^*-U_0^*)]u \\
& +[-f_V^* -\epsilon^2f_{VU}^* U_1^*-\epsilon^2f_{VU}^* (K^*_1-U_0^*)]v+\mathcal O(\epsilon^4) \\
\end{aligned}
\]</div>
Everything is exponentially close to constant. Both equations give at leading order:
<div class="math-container">\[
u = -\frac{f_V^*}{f_U^*}v
\]</div>
Now we add the equations and find at the next order:
<div class="math-container">\[
\begin{aligned}
 \hat\lambda u+\hat\lambda v & =v_{XX}
\end{aligned}
\]</div>
Then:
<div class="math-container">\[
\begin{aligned}
\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} v & = v_{XX}
\end{aligned}
\]</div>
Then:
<div class="math-container">\[
v(X) = A\exp\left(\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }X\right)+B\exp\left(-\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }X\right)
\]</div>
in the fast coordinate $$\xi= X/\epsilon^2$$, we then get on the left:
<div class="math-container">\[
v(\xi) = A\exp\left(\epsilon^2\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }\xi \right)
\]</div>


[View Raw Markdown](/assets/md/Slow eqns netjes.md)
