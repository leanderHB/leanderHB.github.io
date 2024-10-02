---
layout: post
title: "Functional derivatives?"
date: 2024-06-24
---
<style>
.math-container {
    max-width: 100%; /* Set a maximum width to prevent it from expanding the page */
    overflow-x: auto; /* Enable horizontal scrolling */
    white-space: nowrap; /* Prevent the text from wrapping */
}
</style>
Maybe this:
<div class="math-container">\[
H=u_{1,\xi\xi}^*+f_u(u^*_0,K^*_0)u_1^*+f_v(u^*_0,K^*_0)(K_1^*-u_0^*)=0
\]</div>
Take functional derivative wrt to $$u_0^*$$:
<div class="math-container">\[
\int u_{1,\xi\xi}^*+f_u((u^*_0+\delta w),K^*_0)u_1^*+f_v((u^*_0+\delta w),K^*_0)(K_1^*-(u_0^*+\delta w))d\xi
\]</div>
Expanding $$f$$:
<div class="math-container">\[\begin{aligned}
\int u_{1,\xi\xi}^*+f_u(u^*_0,K^*_0)u_1^*+\delta wf_{uu}(u^*_0,K^*_0)u_1^*+f_v(u^*_0,K^*_0)(K_1^*-u_0^*)\\+f_{vu}(u^*_0,K^*_0)K_1^*\delta w+f_v(u^*_0,K^*_0)\delta wd\xi+O((\delta w)^2)
\end{aligned}\]</div>
The linear terms in $$\delta w$$ are:
<div class="math-container">\[
\begin{aligned}
\frac{d H}{d u_0^*}=f_{uu}(u^*_0,K^*_0)u_1^*+f_{vu}(u^*_0,K^*_0)K_1^*+f_v(u^*_0,K^*_0)
\end{aligned}
\]</div>
