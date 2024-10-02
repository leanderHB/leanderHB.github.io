---
layout: post
title: "Een aantal combinaties"
date: 2024-04-03
---
Consider traveling wave coordinates $$x = \chi+\epsilon^\alpha c t$$ where $$\chi$$ is the ordinary space coordinate. Then:
<div>\[
U_{t} = U_xx_t = \epsilon^\alpha c U_x
\]</div>
Our pde then becomes:
<div>\[
\begin{aligned}
\epsilon^\alpha c U_x &= \epsilon^2 U_{xx}+f(U,V)\\
\epsilon^\alpha c V_x &= V_{xx}-f(U,V)\\
\end{aligned}
\]</div>

We can expand $$U$$ as $$U_0+\epsilon^{\beta}U_1+\epsilon^{2\beta}U_2+\dots$$ and similarly for $$V$$, then we get, in all its glory:
<div>\[
\begin{aligned}
\epsilon^\alpha c (U_0+\epsilon^{\beta}U_1+\dots)_x &= \epsilon^2 (U_0+\epsilon^{\beta}U_1+\dots)_{xx}+f(U_0+\epsilon^{\beta}U_1+\dots,(V_0+\epsilon^{\beta}V_1+\dots))\\
\epsilon^\alpha c (V_0+\epsilon^{\beta}V_1+\dots)_x &= (V_0+\epsilon^{\beta}V_1+\dots)_{xx}-f((U_0+\epsilon^{\beta}U_1+\dots),(V_0+\epsilon^{\beta}V_1+\dots))\\
\end{aligned}
\]</div>
We can Taylor expand $$f$$ to get:
<div>\[
f(U_0+\epsilon^{\beta}U_1+\dots,(V_0+\epsilon^{\beta}V_1+\dots))=f(U_0,V_0)+\epsilon^\beta f_U(U_0,V_0)U_1+\epsilon^\beta f_V(U_0,V_0)V_1+\dots
\]</div>

# $$\alpha=1$$ en $$\beta$$ groot 
#### Leading
slow subsystem ($$\alpha=1,\beta=100$$), order=0 
<div>\[\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}\]</div>
fast subsystem ($$\alpha=1,\beta=100$$), order=0 
<div>\[\begin{aligned} c(U_{0})_{\xi} &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}\]</div>
#### Next
slow subsystem ($$\alpha=1,\beta=100$$), order=1 
<div>\[\begin{aligned} c(U_{0})_{x} &=0 \\ c(V_{0})_{x} &=0 \end{aligned}\]</div>
fast subsystem ($$\alpha=1,\beta=100$$), order=1 
<div>\[\begin{aligned} c(U_{1})_{\xi} &=(U_{1})_{\xi\xi}+f_{V}+f_{U} \\ 0 &=(V_{1})_{\xi\xi} \end{aligned}\]</div>

# $$\alpha=2$$ en $$\beta$$ groot 
#### Leading
slow subsystem ($$\alpha=2,\beta=100$$), order=0 
<div>\[\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}\]</div>
fast subsystem ($$\alpha=2,\beta=100$$), order=0 
<div>\[\begin{aligned} 0 &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}\]</div>
#### Next
slow subsystem ($$\alpha=2,\beta=100$$), order=1 
<div>\[\begin{aligned} c(U_{0})_{x} &=(U_{0})_{xx} \\ c(V_{0})_{x} &=0 \end{aligned}\]</div>
fast subsystem ($$\alpha=2,\beta=100$$), order=1 
<div>\[\begin{aligned} c(U_{0})_{\xi} &=0 \\ 0 &=0 \end{aligned}\]</div>
# $$\alpha=2$$ en $$\beta=1$$ (had ik uitgewerkt)
Dit geeft geen closed systeem aan vergelijkingen :(
#### Leading
slow subsystem ($$\alpha=2,\beta=1$$), order=0 
<div>\[\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}\]</div>
fast subsystem ($$\alpha=2,\beta=1$$), order=0 
<div>\[\begin{aligned} 0 &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}\]</div>
#### Next
slow subsystem ($$\alpha=2,\beta=1$$), order=1 
<div>\[\begin{aligned} 0 &=f_{V}+f_{U} \\ 0 &=(V_{1})_{xx}+f_{V}+f_{U} \end{aligned}\]</div>
fast subsystem ($$\alpha=2,\beta=1$$), order=1
<div>\[\begin{aligned} c(U_{0})_{\xi} &=(U_{1})_{\xi\xi}+f_{V}+f_{U} \\ 0 &=(V_{1})_{\xi\xi} \end{aligned}\]</div>
#### Even higher
slow subsystem ($$\alpha=2,\beta=1$$), order=2 
<div>\[\begin{aligned} c(U_{0})_{x} &=(U_{0})_{xx}+f_{VV}+2f_{UV}+f_{UU} \\ c(V_{0})_{x} &=(V_{2})_{xx}+f_{VV}+2f_{UV}+f_{UU} \end{aligned}\]</div>
fast subsystem ($$\alpha=2,\beta=1$$), order=2 
<div>\[\begin{aligned} c(U_{1})_{\xi} &=(U_{2})_{\xi\xi}+f_{VV}+2f_{UV}+f_{UU} \\ 0 &=(V_{2})_{\xi\xi}+f_{} \end{aligned}\]</div>
# $$\alpha=2=\beta$$ (nieuw)
Ook geen closed systeem :(
#### Leading order
slow subsystem ($$\alpha=2,\beta=2$$), order=0 
<div>\[\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}\]</div>
fast subsystem ($$\alpha=2,\beta=2$$), order=0 
<div>\[\begin{aligned} 0 &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}\]</div>
#### Next order

slow subsystem ($$\alpha=2,\beta=2$$), order=1 
<div>\[\begin{aligned} c(U_{0})_{x} &=(U_{0})_{xx}+f_{V}+f_{U} \\ c(V_{0})_{x} &=(V_{1})_{xx}+f_{V}+f_{U} \end{aligned}\]</div>
fast subsystem ($$\alpha=2,\beta=2$$), order=1 
<div>\[\begin{aligned} c(U_{0})_{\xi} &=0 \\ 0 &=0 \end{aligned}\]</div>
#### Even higher order
slow subsystem ($$\alpha=2,\beta=2$$), order=2 
<div>\[\begin{aligned} c(U_{1})_{x} &=(U_{1})_{xx}+f_{VV}+2f_{UV}+f_{UU} \\ c(V_{1})_{x} &=(V_{2})_{xx}+f_{VV}+2f_{UV}+f_{UU} \end{aligned}\]</div>
fast subsystem ($$\alpha=2,\beta=2$$), order=2 
<div>\[\begin{aligned} 0 &=(U_{1})_{\xi\xi}+f_{V}+f_{U} \\ 0 &=(V_{1})_{\xi\xi}+f_{} \end{aligned}\]</div>
# $$\alpha=\beta=1$$ (Nieuw, werkt hopelijk wel)
#### Leading
slow subsystem ($$\alpha=1,\beta=1$$), order=0 
<div>\[\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}\]</div>
fast subsystem ($$\alpha=1,\beta=1$$), order=0 
<div>\[\begin{aligned} c(U_{0})_{\xi} &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}\]</div>
#### Next
slow subsystem ($$\alpha=1,\beta=1$$), order=1 
<div>\[\begin{aligned} c(U_{0})_{x} &=f_{V}+f_{U} \\ c(V_{0})_{x} &=(V_{1})_{xx}+f_{V}+f_{U} \end{aligned}\]</div>
fast subsystem ($$\alpha=1,\beta=1$$), order=1 
<div>\[\begin{aligned} c(U_{1})_{\xi} &=(U_{1})_{\xi\xi}+f_{V}+f_{U} \\ 0 &=(V_{1})_{\xi\xi} \end{aligned}\]</div>
#### Even higher
slow subsystem ($$\alpha=1,\beta=1$$), order=2 
<div>\[\begin{aligned} c(U_{1})_{x} &=(U_{0})_{xx}+f_{VV}+2f_{UV}+f_{UU} \\ c(V_{1})_{x} &=(V_{2})_{xx}+f_{VV}+2f_{UV}+f_{UU} \end{aligned}\]</div>
fast subsystem ($$\alpha=1,\beta=1$$), order=2 
<div>\[\begin{aligned} c(U_{2})_{\xi} &=(U_{2})_{\xi\xi}+f_{VV}+2f_{UV}+f_{UU} \\ c(V_{0})_{\xi} &=(V_{2})_{\xi\xi}+f_{} \end{aligned}\]</div>



