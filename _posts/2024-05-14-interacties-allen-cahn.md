---
layout: post
title: "Interacties Allen Cahn"
date: 2024-05-14
---
![Image](/assets/images/Pasted image 20240514105657.png)
Small spectrum, comes from translational eigenvalues of the individual fronts. Projecting the PDE onto an ODE somehow, apparently well supported by literature. 



1.2:
![Image](/assets/images/Pasted image 20240514163316.png)






### Outer equations
order: $$\epsilon^0$$
<div>\[\begin{aligned}0&=f \\0&=-f + (V_0)_{xx} \end{aligned}\]</div>
order: $$\epsilon^1$$
<div>\[\begin{aligned}0&=-c(U_0)_x + f_{U}U_1 + f_{V}V_1 \\0&=-c(V_0)_x - f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} \end{aligned}\]</div>
### Inner equations
order: $$\epsilon^0$$
<div>\[\begin{aligned}0&=-c(U_0)_\xi  + f + (U_0)_{\xi \xi } \\0&=(V_0)_{\xi \xi } \end{aligned}\]</div>
order: $$\epsilon^1$$
<div>\[\begin{aligned}0&=-c(U_1)_\xi  + f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\0&=-c(V_0)_\xi  + (V_1)_{\xi \xi } \end{aligned}\]</div>
#### outer gives:
<div>\[
V_0(x)=V_0, \quad U_0(x)=U_0
\]</div>
then to second order we add the equations to get (note $$(V_0)_x=(U_0)_x=0$$):
<div>\[\begin{aligned}
0&=-0 + f_{U}U_1 + f_{V}V_1 \\
0&=-0 - f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} 
\end{aligned}\]</div>
Then:
<div>\[
(V_1)_{xx} = 0\implies V_1(x)=V_1
\]</div>
So:
<div>\[
U_1 =-f_V /f_UV_1
\]</div>

#### Inner gives:
order: $$\epsilon^0$$
<div>\[\begin{aligned}
0&=-c(U_0)_\xi  + f(U_0(\xi),V_0) + (U_0)_{\xi \xi } \\
V_0(\xi)&=V_0
\end{aligned}\]</div>
Which is a non-linear problem, 
order: $$\epsilon^1$$
<div>\[\begin{aligned}
0&=-c(U_1)_\xi  + f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\
V_1(\xi)&=V_1 
\end{aligned}\]</div>
another Sturm-Liouville problem
