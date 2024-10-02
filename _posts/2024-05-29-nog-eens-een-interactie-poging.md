---
layout: post
title: "Nog eens een interactie poging"
date: 2024-05-29
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

We expand as follows: $$U= \bar U+\epsilon^2 u$$. Besides that, we choose wave coordinates and get $$U_t= cU_x$$ Then we obtain:
<div class="math-container">\[
\begin{aligned}
\hat c\bar U_x =\epsilon^2 \bar U_{xx}+\epsilon^4 u_{xx}+f(\bar U, \bar V)+\epsilon^2f_Uu+\epsilon^2f_V v\\
\hat c\bar V_x = \bar V_{xx}+\epsilon^2 v_{xx}-f(\bar U, \bar V)-\epsilon^2f_Uu-\epsilon^2f_V v
\end{aligned}
\]</div>
anticipating that $$c\ll 1$$, we get the steady state solutions at leading order and are left with:
<div class="math-container">\[
\begin{aligned}
\hat c\bar U_x =\epsilon^2 \bar U_{xx}+\epsilon^2f_Uu+\epsilon^2f_V v\\
\hat c\bar V_x = \epsilon^2 v_{xx}-\epsilon^2f_Uu-\epsilon^2f_V v
\end{aligned}
\]</div>
To match orders, we relabel $$\hat c=\epsilon^2 c$$ and find:
<div class="math-container">\[
\begin{aligned}
c\bar U_x &= \bar U_{xx}+f_Uu+f_V v\\
c\bar V_x &= v_{xx}-f_Uu-f_V v
\end{aligned}
\]</div>
Now we can add these two equations to obtain:
<div class="math-container">\[
c(\bar U_x+\bar V_x)=v_{xx}+\bar U_{xx}
\]</div>

We integrate once and find:
<div class="math-container">\[
v^{+}_x-v_x^- = c\int_-^+ \bar U_x+\bar V_xdx +\bar U_{x}^+-\bar U_{x}^-
\]</div>
<div class="math-container">\[
v^{+}_x-v_x^- = c\left(\bar U^+-\bar U^-+\bar V^+-\bar V^- \right) +\bar U_{x}^+-\bar U_{x}^-
\]</div>
Since $$\bar V$$ only varies on a scale of $$\epsilon^2$$, we neglect these terms and find:
<div class="math-container">\[
(v^{+}_x-v_x^-)_i = c_i\left(\bar U^+-\bar U^-\right) +\bar U_{x}^+-\bar U_{x}^-
\]</div>
We can find all the quantities in this set of equations exactly! 
Now we can force that our total solution has zero derivative as $$x\to\pm \infty$$. Then we can solve the set of equations actually. So define $$x^+_i$$ as $$(p_i+p_{i+1})/2$$. Then $$\bar U^+_i=\alpha_i^+ \exp()$$ 


Let's say for some reason we want $$v_x$$ to be equal on both ends, so combined with the boundary conditons, to be $$0$$ to leading order on the boundaries. Then:
<div class="math-container">\[
c_i= \frac{\bar U_{x}^+-\bar U_{x}^-}{\bar U^+-\bar U^-}
\]</div>
To leading order $$\bar U^+-\bar U^-$$ is constant! Let's call it $$U_d$$. Then we're left with:
<div class="math-container">\[
c_i = \frac{\bar U_{x}^+-\bar U_{x}^-}{U_d}
\]</div>
We have the leading order expression for $$U_x$$ on the plateaus:
<div class="math-container">\[
U_x = \alpha_\pm \exp(\mp\beta_\pm x)
\]</div>
So then:
<div class="math-container">\[
c_i = \frac{ \alpha_+ \exp(-\beta_+ x_p^+)- \alpha_- \exp(\beta_- x_p^-)}{U_d}
\]</div>
Oke maar nu geen koppeling meer, nee das niet waar.
We set the boundary in the middle between the two fronts, so we obtain:
<div class="math-container">\[
c_i  = \frac{ \alpha_+ \exp(-\beta_+ \Delta_{i+1})- \alpha_- \exp(\beta_- \Delta_{i})}{U_d}
\]</div>
Where:
<div class="math-container">\[
\Delta_{i} = p_{i}-p_{i-1}
\]</div>
And of course $$\alpha$$ and $$\beta$$ have to alternate for the rising/falling fronts!




<div class="math-container">\[
\partial_xf(U,V) = f_U(U,V)U_x+f_V(U,V)V_x
\]</div>

[View Raw Markdown](/assets/md/Nog eens een interactie poging.md)
