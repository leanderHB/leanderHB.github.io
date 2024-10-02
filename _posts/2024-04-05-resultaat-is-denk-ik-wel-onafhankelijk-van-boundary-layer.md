---
layout: post
title: "Resultaat is denk ik wel onafhankelijk van boundary layer"
date: 2024-04-05
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

Now we found the integral of $$r_{\xi\xi}$$, which we match to the conditions found from the fast subsystem:
<div class="math-container">\[\begin{aligned}
\int_{I}r_{\xi\xi}d\xi &= \epsilon^2\int_{-\epsilon^{-\nu}}^{\epsilon^{-\nu}}[\lambda  + f_u(u_0,v_0)s_{inner}+f_v(u_0,v_0)]d\xi\\
&= -\epsilon \sqrt{\lambda +\frac{\lambda f_{v,right}}{\lambda-f_{u,right}}}-\epsilon \sqrt{\lambda +\frac{\lambda f_{v,left}}{\lambda-f_{u,left}}}
\end{aligned}\]</div>
we can evaluate the part with $$\lambda$$:
<div class="math-container">\[
\epsilon^2\int_{-\epsilon^{-\nu}}^{\epsilon^{-\nu}}\lambda d\xi=\frac{2}{\sqrt{\epsilon}}\lambda  = 2\epsilon^{2-\nu} \lambda
\]</div>
If $$\lambda=O(1)$$, this is a higher order term, compared to the RHS. Let's say $$\lambda=l\epsilon^{\alpha}$$. If $$\alpha=0$$, we can't match order to the RHS, and else:
<div class="math-container">\[
\sqrt{l\epsilon^{\alpha} +\frac{l\epsilon^{\alpha} f_{v,right}}{l\epsilon^{\alpha}-f_{u,right}}}=\epsilon^{\alpha/2}\sqrt{l +\frac{l f_{v,right}}{l\epsilon^{\alpha}-f_{u,right}}}
\]</div>
If $$\alpha<0$$ and $$\epsilon\to0$$, then this expression becomes:
<div class="math-container">\[
\epsilon^{\alpha/2}\sqrt l
\]</div>
If $$\alpha>0$$ and $$\epsilon\to 0$$, then it becomes $$\epsilon^{\alpha/2}\sqrt{l-l f_{v,right}/f_{u,right})}$$. In both cases, scaling as $$\epsilon^{\alpha/2}$$. Let's plug this scaling into our equation:
<div class="math-container">\[
2\epsilon^{2-\nu}l\epsilon^{\alpha}\sim-\epsilon \sqrt{l}\epsilon^{\alpha/2}
\]</div>
If the lamba term matters, it should be the same, or lower order than the RHS, so:
<div class="math-container">\[
2-\nu+\alpha<1+\alpha/2\implies \alpha<2(\nu -1)
\]</div>
Since $$\nu\in(0,1)$$, this is always negative, so we're dealing with asympotically large lambda's for which the order theoretically could match or be problematic. Then we get an equation for $$l$$:
<div class="math-container">\[
2l = -2\sqrt l
\]</div>
This has solution $$l=0$$, so this term is either higher order (irrelevant for leading order behaviour), or zero. 

[View Raw Markdown](/assets/md/Resultaat is denk ik wel onafhankelijk van boundary layer.md)
