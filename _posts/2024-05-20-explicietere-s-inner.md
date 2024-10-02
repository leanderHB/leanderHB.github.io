---
layout: post
title: "Explicietere s inner"
date: 2024-05-20
---
Hier een poging om lemma 2.5 uit Arjen's paper te gebruiken voor mijn situatie!
### Using Lemma 2.5
Introduce a fast variable $$x=\epsilon\xi$$:
<div>\[
\begin{aligned}
\lambda u &=  u_{\xi\xi} + f_U(\bar U,\bar V)u+f_V(\bar U,\bar V)v\\
\epsilon^2\lambda v &=  v_{\xi\xi} - \epsilon^2f_U(\bar U,\bar V)u-\epsilon^2f_V(\bar U,\bar V)v
\end{aligned}
\]</div>
So we find that $$v(\xi) = v_0+\epsilon^2v_2(\xi)$$, choose $$v = 1+\epsilon^2v_2$$, we can use this to find:
<div>\[
\lambda u =  u_{\xi\xi} + f_U(\bar U,\bar V)u+f_V(\bar U,\bar V)
\]</div>
Previous analysis showed that $$\lambda$$ has to be asymptotically small for solutions with $$\mathcal R \lambda>0$$. So to leading order then:
<div>\[
\mathcal Lu:=(\partial_{\xi\xi} +f_U(\bar U,\bar V))u =  f_V(\bar U,\bar V)
\]</div>
Now fix the solution ($$\bar U,\bar V$$) where the inflection point lies at $$0$$. This will fix two constants $$\beta_\pm$$ later on.
Now we are in the setting of Lemma 2.5. Define now 
<div>\[\alpha_\pm=g_U(U_\pm)=f_U(U_\pm,V_\pm)-\epsilon^2 f_V(U_\pm,V_\pm)\]</div>
(I think? check this)
and with that $$E_\pm(\xi) = \exp(\mp \sqrt{\alpha_\pm}\xi)$$. Now as I found earlier, this implies that for $$\pm \xi\gg 1$$:
<div>\[
\bar U(\xi) = U_\pm \mp \exp(\mp \sqrt{\alpha_\pm }\xi)
\]</div>
Cool stuff, now the translation of the heteroclinic orbit is an eigenfunction with eigenvalue 0: $$\mathcal L \bar U_\xi=0$$, furthermore, we have an explicit formula for $$\bar U_\xi=\sqrt{2E-2F(\bar U)}$$. Note now that by fixing the inflection point to be at $$0$$, this fixes $$\beta_\pm$$. 


We get (by some magic I don't get) a second solution:
<div>\[
U_u(\xi)=U_b(\xi)\int_0^\xi\frac{d\xi'}{(U_b(\xi'))^2}
\]</div>
both these solutions have exponential behaviour in the tails, both related to the $$\alpha_\pm$$. 
Note that we get that $$\langle f_V,U_u\rangle =0$$ by Fredholm. 


#### Lemma (Fredholm)
Let $$\mathcal L$$ be selfadjoint. If $$\mathcal L v=0$$, so $$v\in \ker \mathcal L$$ , then $$\mathcal L u=h$$ has a solution only if $$\langle v,h\rangle=0$$. 
**Proof:**
<div>\[0=\langle 0,u \rangle=\langle Lv,u \rangle=\langle v,Lu \rangle=\langle v,h \rangle\]</div>



Hmm oke Fredholm is misschien cleaner?
<div>\[
\langle f_V(\bar U,\bar V),\bar U_\xi \rangle=0
\]</div>
So:
<div>\[
\int_{I_f}f_V(\xi)\bar U_\xi d\xi  = 0
\]</div>
geintje haha, maar wel coole relatie


