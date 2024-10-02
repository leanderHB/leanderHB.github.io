---
layout: post
title: "Matchy matchy"
date: 2024-09-12
---
<div>\[\begin{aligned}
(v_l+\epsilon^2u_l)&=C\exp(a\xi)\\
(v_b+\epsilon^2u_b)&=C\exp(-b\xi)
\end{aligned}\]</div>
derivatives:
<div>\[
\begin{aligned}
(v_l+\epsilon^2u_l)_\xi&=aC\exp(a\xi)\\
(v_b+\epsilon^2u_b)_\xi&=-bC\exp(-b\xi)
\end{aligned}
\]</div>
inner:
<div>\[
\Delta (v_i+\epsilon^2u_i)_\xi  = \hat\lambda \int U_{0,\xi}^*
\]</div>
match to ders
and then $$C$$:
<div>\[
\Delta (v_i+\epsilon^2u_i)_\xi  = \hat\lambda \int U_{0,\xi}^*
\]</div>

<div>\[
v_i+\epsilon^2u_i = \int_A^x\int_B^x U_{0,\xi}^* =\int\int U_{0,\xi}^*+A'+B'\xi
\]</div>
kan $$C$$ niet gewoon op $$1$$ door tijd te schalen? heb ik dat zelfs niet al gedaan ergens? maybe niet hoor. 

uiteindelijk:
<div>\[
-C(a+b)  = \hat\lambda \int U_{0,\xi}^*
\]</div>

Ideally, we'd find: 
<div>\[\begin{aligned}
-Ca = \hat\lambda \int^0_{-\epsilon^\sigma} U_{0,\xi}^*\\
-Cb = \hat\lambda \int_0^{\epsilon^\sigma} U_{0,\xi}^*
\end{aligned}\]</div>
For that, we have to set the middle of the front to the "inflection point". 
Let's assume $$C>0$$, i.e: the perturbation is "rising" on the left, and "falling" on the right. Since 

So we center the front here. 


let's assume $$U_{0,\xi}^*>0$$. Then $$\Delta_{fast}(v+\epsilon^2)_{\xi} = \hat\lambda\Delta U=\hat\lambda(U^+-U^-)$$.
Let's say $$C>0$$, then $$\Delta_{slow}<0$$, so $$\lambda<0$$, so stable.  


let's assume $$U_{0,\xi}^*>0$$. Then $$\Delta_{fast}(v+\epsilon^2)_{\xi} = \hat\lambda\Delta U=\hat\lambda(U^+-U^-)$$.
Let's say $$C<0$$, then $$\Delta_{slow}>0$$, so $$\lambda>0$$, so unstable. 

to prove: $$C>0$$, how do? 