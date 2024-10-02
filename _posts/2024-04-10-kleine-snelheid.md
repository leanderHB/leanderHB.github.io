---
layout: post
title: "Kleine snelheid"
date: 2024-04-10
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

# $$\alpha=2, \beta=1$$
### Outer equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}0&=f \\0&=-f + (V_0)_{xx} \end{aligned}\]</div>
First order: lies on the nullclines, at flux-balance? 

order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}0&=f_{U}U_1 + f_{V}V_1 \\0&=-f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} \end{aligned}\]</div>
Correction along the nullcline: $$V_1(x)=V_1$$, and $$U_1 = f_V/f_U V_1$$, which is perpendicular to the gradient: 
<div class="math-container">\[(U_1,V_1)\cdot \nabla f = f_UU_1+f_VV_1=0\]</div>
Here, $$V_1$$ is to be fixed by $$\eta$$ hopefully? 
### Inner equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}0&=f + (U_0)_{\xi \xi } \\0&=(V_0)_{\xi \xi } \end{aligned}\]</div>
Again $$V_0$$ is constant, and $$U_0$$ is given by the same Hamiltonian system as in the stationary stability analysis. 

order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}0&=-c(U_0)_\xi  + f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\0&=(V_1)_{\xi \xi } \end{aligned}\]</div>


[View Raw Markdown](/assets/md/Kleine snelheid.md)
