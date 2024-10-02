---
layout: post
title: "Grid based derivation"
date: 2024-10-02
---
If the plant is there and the food is there, there's a certain probability of the plant uptaking the food. Also, plant have a certain chance of "duplicating", by taking up the food. Besides that, the plants and the food do a random walk with a certain rate. 
- plant eats food: $$P+F \xrightarrow{\alpha(P,F)} 2P$$
- plant dies: $$P\xrightarrow{\beta(P,F)} F$$
- plant hops: $$P_i \xrightarrow{d_P}P_{i\pm 1}$$ 
- food hops: $$F_i \xrightarrow{d_F}F_{i\pm 1}$$ 
We do the classic thing of finding how the probability at a site changes:
<div>\[\begin{aligned}
\frac{dP_i}{dt} = \underbrace{d_P\left( P_{i-1}+P_{i+1} \right)}_{\text{hopping to i}}-\underbrace{2d_PP_i}_{\text{hopping away}}+\underbrace{\alpha(P,F)PF}_{\text{plant duplicates}}-\underbrace{\beta(P,F) P}_{\text{plant dies}}\\
\frac{dF_i}{dt} = \underbrace{d_F\left( F_{i-1}+F_{i+1} \right)}_{\text{hopping to i}}-\underbrace{2d_FF_i}_{\text{hopping away}}-\underbrace{\alpha(P,F)PF}_{\text{food eaten}}+\underbrace{\beta(P,F) P}_{\text{new food}}
\end{aligned}\]</div>
Taking the continuum limit, we get:
<div>\[\begin{aligned}
P_t = D_P P_{xx}+\alpha(P,F)PF-\beta(P,F) P\\
F_t = D_F F_{xx}-\alpha(P,F)PF+\beta(P,F) P
\end{aligned}\]</div>
More generally, with a bit of rescaling, we get:
<div>\[\begin{aligned}
U_t&=D U_{xx}+f(U,V)\\
V_t &=V_{xx}-f(U,V)
\end{aligned}\]</div>
with $$f$$ now a general function of $$U$$ and $$V$$, now some generalized concentrations. 

This is called a reaction diffusion system, with conserved concentration :)


# Slides for fourier
Integral should have a real value. Then the left hand side should be real too. Then for positive, real $$\lambda$$, we require that the square roots be real. If they aren't, we can't have positive, real $$\lambda$$, which is interesting. This implies:
<div>\[
f_{V,r}<f_{U,r},\quad f_{V,l}<f_{U,l}
\]</div>

is necessary for instability in the form of a real (non-oscillating) eigenvalue.



Let's check the stability around $$(U_+,V_+)$$. We linearize again:
<div>\[
\begin{aligned}
u_t &= \epsilon^2 u_{xx}+f_U(U_+,V_+)u+f_V(U_+,V_+)v\\
v_t &= v_{xx}-f_U(U_+,V_+)u-f_V(U_+,V_+)v
\end{aligned}
\]</div>
A quick Fourier transform (we assume we're far away enough from any structure that we can do this, other words, the slow reduced system), shows us that:
<div>\[\begin{aligned}
\hat{u}_t = \epsilon^2(ik)^2\hat{u}+f_U \hat{u}+f_V\hat{v}\\
\hat{v}_t = (ik)^2\hat{v}-f_U\hat{u}-f_V\hat{v}
\end{aligned}
\]</div>
We now write this as:
<div>\[
\begin{pmatrix}\hat{u}\\\hat{v}\end{pmatrix}_t=
\begin{pmatrix}f_U-\epsilon^2k^2&f_V\\-f_U&-f_V-k^2\end{pmatrix}
\begin{pmatrix}\hat{u}\\\hat{v}\end{pmatrix}
\]</div>
Which has determinant:
<div>\[\begin{aligned}
\Delta\begin{pmatrix}f_U-\epsilon^2k^2&f_V\\-f_U&-f_V-k^2\end{pmatrix} &=(f_U-\epsilon^2k^2)(-f_V-k^2)+f_Uf_V \\
&= -f_Uk^2+\epsilon^2 k^2 f_V+ \epsilon^2k^4\\
&= k^2(\epsilon^2 k^2+\epsilon^2 f_V-f_U)
\end{aligned}\]</div>
We require the determinant to be positive for non-growing waves. We see that a bifurcation happens, if it does at all, for $$k=0$$, since that makes the determinant closest to 0. Then we find that for stability of all wavenumbers, we need $$\epsilon^2 f_V-f_U>0$$. Next, we look at the trace, and find that 
<div>\[
\operatorname{Tr}\begin{pmatrix}f_U-\epsilon^2k^2&f_V\\-f_U&-f_V-k^2\end{pmatrix} =f_U-\epsilon^2k^2-f_V-k^2
\]</div>
For stability, we require $$\operatorname{Tr}<0$$, so here we get another inequality for stability:
<div>\[
f_V-f_U>0
\]</div>


