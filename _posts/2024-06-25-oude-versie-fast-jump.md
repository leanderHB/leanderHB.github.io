---
layout: post
title: "oude versie fast jump"
date: 2024-06-25
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>



### Enge dingen
#### sign ding, v hat 0 doet weg gaan denk ik, signs kloppen niet 100% 
<div class="math-container">\[
I = \int_\mathbb R f_u(u^*,v^*)\hat u_1 d\xi
\]</div>

Using 
<div class="math-container">\[\hat\lambda \hat u_0=\hat u_{1,\xi\xi}+f_{u}(u_0^*,K_0^*)\hat u_1+(f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0+f_{v}(u_0^*,K_0^*)\hat{\hat v}_0\]</div>
We get:
<div class="math-container">\[
I = \int [\hat\lambda \hat u_0-\hat u_{1,\xi\xi}-(f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0-f_{v}(u_0^*,K_0^*)\hat{\hat v}_0]d\xi
\]</div>
The slow region is a linear, constant coefficient problem, so $$\hat u_1$$ will be a decaying function on both ends, hence the integral over the curvature of $$\hat u_1$$ is zero. 
<div class="math-container">\[
I = \int  [(\hat\lambda+f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0-f_{v}(u_0^*,K_0^*)\hat{\hat v}_0]d\xi
\]</div>
Let's assume $$C=0$$ (I think needed for this integral to converge), then:
<div class="math-container">\[
\hat{\hat v}=-\hat u
\]</div>
Next, we use the fact that $$\hat u_0=u^*_{0,\xi}$$ and write:
<div class="math-container">\[
I = -\int  [(\hat\lambda+f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0)+f_{v}(u_0^*,K_0^*)) u_{0,\xi}^*]d\xi
\]</div>
Good news: integral indeed converges. Bad news, I have no clue what to do with this (:


in enge termen schrijf ik dit om naar een integraal over alleen maar eerste afgeleiden van $$f$$, maar nu wel een $$\hat u_{1,\xi}$$ term... [Enge termen]({% link _posts/2024-06-25-enge-termen.md %})
<div class="math-container">\[
\begin{aligned}
I = -\int  [(\hat\lambda+f_{v}(u_0^*,K_0^*)) u_{0,\xi}^*-f_u(u^*_0,K^*_0)u_{1,\xi}^*+f_{u}(u^*_0,K^*_0)u_{0,\xi}^*]d\xi
\end{aligned}
\]</div>
Volgens mij valt de $$f_v$$ term weg als ik de boel even netjes doe, ik mis ergens sign, en dan in totale jump, moet ie wegvallen vgm! :) 
Dan houd je die integraal over de afgeleiden keer $$f_u$$ over, geen idee wat daar mee gaat gebeuren!







[View Raw Markdown](/assets/md/oude versie fast jump.md)
