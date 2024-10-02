---
layout: post
title: "Verschillende keuzes voor kleine snelheid"
date: 2024-04-11
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

Consider traveling wave coordinates $$x = \chi+\epsilon^\alpha c t$$ where $$\chi$$ is the ordinary space coordinate. Then:
<div class="math-container">\[
U_{t} = U_xx_t = \epsilon^\alpha c U_x
\]</div>
Our pde then becomes:
<div class="math-container">\[
\begin{aligned}
\epsilon^\alpha c U_x &= \epsilon^2 U_{xx}+f(U,V)\\
\epsilon^\alpha c V_x &= V_{xx}-f(U,V)\\
\end{aligned}
\]</div>
We can expand $$U$$ as $$U_0+\epsilon^{\beta}U_1+\epsilon^{2\beta}U_2+\dots$$ and similarly for $$V$$, then we get, in all its glory:
<div class="math-container">\[
\begin{aligned}
\epsilon^\alpha c (U_0+\epsilon^{\beta}U_1+\dots)_x &= \epsilon^2 (U_0+\epsilon^{\beta}U_1+\dots)_{xx}+f(U_0+\epsilon^{\beta}U_1+\dots,(V_0+\epsilon^{\beta}V_1+\dots))\\
\epsilon^\alpha c (V_0+\epsilon^{\beta}V_1+\dots)_x &= (V_0+\epsilon^{\beta}V_1+\dots)_{xx}-f((U_0+\epsilon^{\beta}U_1+\dots),(V_0+\epsilon^{\beta}V_1+\dots))\\
\end{aligned}
\]</div>
We can Taylor expand $$f$$ to get:
<div class="math-container">\[\begin{gather}
f(U_0+\epsilon^{\beta}U_1+\dots,(V_0+\epsilon^{\beta}V_1+\dots))\\=f(U_0,V_0)+\epsilon^\beta f_U(U_0,V_0)(U-U_0)+\epsilon^\beta f_V(U_0,V_0)(V-V_0)+\dots
\end{gather}\]</div>
# $$\alpha=1, \beta=1$$
### Outer equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}0&=f \\0&=-f + (V_0)_{xx} \end{aligned}\]</div>
order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}0&=-c(U_0)_x + f_{U}U_1 + f_{V}V_1 \\0&=-c(V_0)_x - f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} \end{aligned}\]</div>
### Inner equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}0&=-c(U_0)_\xi  + f + (U_0)_{\xi \xi } \\0&=(V_0)_{\xi \xi } \end{aligned}\]</div>
order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}0&=-c(U_1)_\xi  + f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\0&=-c(V_0)_\xi  + (V_1)_{\xi \xi } \end{aligned}\]</div>



# $$\alpha=1, \beta=2$$
### Outer equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}
0&=f \\
0&=-f + (V_0)_{xx} 
\end{aligned}\]</div>
order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}
0&=-c(U_0)_x \\
0&=-c(V_0)_x 
\end{aligned}\]</div>
order: $$\epsilon^2$$
<div class="math-container">\[\begin{aligned}
0&=f_{U}U_1 + f_{V}V_1 + (U_0)_{xx} \\
0&=-f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} 
\end{aligned}\]</div>

### Inner equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}
0&=-c(U_0)_\xi  + f + (U_0)_{\xi \xi } \\
0&=(V_0)_{\xi \xi } 
\end{aligned}\]</div>
order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}
0&=0 \\
0&=-c(V_0)_\xi  
\end{aligned}\]</div>
order: $$\epsilon^2$$
<div class="math-container">\[\begin{aligned}
0&=-c(U_1)_\xi  + f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\
0&=-f + (V_1)_{\xi \xi } 
\end{aligned}\]</div>


# $$\alpha=2, \beta=1$$
### Outer equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}0&=f \\0&=-f + (V_0)_{xx} \end{aligned}\]</div>
order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}0&=f_{U}U_1 + f_{V}V_1 \\0&=-f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} \end{aligned}\]</div>
order: $$\epsilon^2$$
<div class="math-container">\[\begin{aligned}0&=-c(U_0)_x + f_{U}U_2 + f_{UU}U_1^2 + f_{UV}U_1V_1 + f_{V}V_2 + f_{VV}V_1^2 + (U_0)_{xx} \\0&=-c(V_0)_x - f_{U}U_2 - f_{UU}U_1^2 - f_{UV}U_1V_1 - f_{V}V_2 - f_{VV}V_1^2 + (V_2)_{xx} \end{aligned}\]</div>

### Inner equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}0&=f + (U_0)_{\xi \xi } \\0&=(V_0)_{\xi \xi } \end{aligned}\]</div>
order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}0&=-c(U_0)_\xi  + f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\0&=(V_1)_{\xi \xi } \end{aligned}\]</div>


# $$\alpha=2, \beta=2$$
### Outer equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}0&=f \\0&=-f + (V_0)_{xx} \end{aligned}\]</div>
order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}0&=0 \\0&=0 \end{aligned}\]</div>
order: $$\epsilon^2$$
<div class="math-container">\[\begin{aligned}0&=-c(U_0)_x + f_{U}U_1 + f_{V}V_1 + (U_0)_{xx} \\0&=-c(V_0)_x - f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} \end{aligned}\]</div>

### Inner equations
order: $$\epsilon^0$$
<div class="math-container">\[\begin{aligned}0&=f + (U_0)_{\xi \xi } \\0&=(V_0)_{\xi \xi } \end{aligned}\]</div>
order: $$\epsilon^1$$
<div class="math-container">\[\begin{aligned}0&=-c(U_0)_\xi  \\0&=0 \end{aligned}\]</div>
order: $$\epsilon^2$$
<div class="math-container">\[\begin{aligned}0&=f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\0&=-c(V_0)_\xi  - f + (V_1)_{\xi \xi } \end{aligned}\]</div>




[View Raw Markdown](/assets/md/Verschillende keuzes voor kleine snelheid.md)
