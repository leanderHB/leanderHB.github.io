---
layout: post
title: "Exponential tails (niet goed)"
date: 2024-02-28
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

<div class="math-container">\[
\newcommand{\Tr}{\operatorname{Tr}}
\]</div>
we have the PDE:
<div class="math-container">\[
\begin{aligned}
u_t &= \delta\Delta u + f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
Acording to FB. we can write this in a more convenient form:
<div class="math-container">\[
\begin{aligned}
0 &= \delta\Delta u + \tilde f(u,\eta)\\
0 &=  \Delta v +\delta\Delta u :=\Delta\eta\\
\end{aligned}
\]</div>
Then $$\eta=\eta_0$$ for some $$\eta_0$$. And we have a Hamiltonian system given by:
<div class="math-container">\[
E = \frac12 (u_x)^2 + \frac1\delta\int_{u_-}^u\tilde f(u',\eta_0)du':=\frac12 (u_x)^2 + F(u)
\]</div>
Note that we have a mesa solution when we can find a $$\eta_0$$ such that the equipotential solution of $$E=0$$ is a heteroclinic orbit. Let's say $$f$$ allows for such a solution, and that it's sufficiently smooth. Then we can approximate $$F(u)$$ around $$u_-$$ as a parabola to leading order:
<div class="math-container">\[
F(u)|_{u_-} =\frac1{2\delta} \tilde f_u(u_-, \eta_0) u^2
\]</div>
Well then we can solve $$u_x$$ around $$u_-$$ by taking the derivative:

<div class="math-container">\[
\frac{d}{dx}E = u_{xx}+F'(u)=u_{xx}+\frac{1}{\delta}\tilde f_u(u_-,\eta_0)u=0
\]</div>
This then yields solutions of the form $$u=C\exp(-l_-x)$$ where $$l_-^2 = \frac{1}{\delta}\tilde f_u(u_-,\eta_0)$$. One of these is stable, the other unstable, depending on the order of the wave. Similarly for the other side we find $$u=C\exp(-l_+x)$$ where $$l_+^2 = \frac{1}{\delta}\tilde f_u(u_+,\eta_0)$$. Note this is only the leading order approximation in the tails. 

## Do the tails attract each other?
#### I lost the tildes somewhere

Well that's a nice and vague question :P The flux balance guarantees that the $$u$$ and $$v$$ part have the same exponent. So we can write (to first order), assuming the fronts keep their shape and only just add together in their non-constant part, and assuming symmetry:
<div class="math-container">\[\begin{aligned}
u &= A(t)(\exp(lx)+\exp(-lx))\\
v &= B(t)(\exp(lx)+\exp(-lx))
\end{aligned}\]</div>
Here we use that the linearized equation around $$u_-$$ is linear, so sums of solutions are also solutions, we also use shift symmetry $$\mathbb R^+$$ to center around zero, and then by symmetry of solutions, we can use 
<div class="math-container">\[\exp(l(x+s(t)))+\exp(-l(x-s(t))=A(t)(\exp(lx)+\exp(-lx))\]</div>
Where $$s(t)$$ is some function of time, giving the shift. 
Also, we assume that the tails are so thin on the point that they overlap with the fronts, that we can neglect effects from this. Next, we also use the fact that the fronts have something like a rigidity at steady state (ja dat werkt dus niet maat). Of course when they move this will change slightly, but assuming the speed they move at is small enough, we can use a quasi-static approximation. 

Where there is some relation between $$A,B$$ given by the FBS. We'll assume the fronts are quite far apart, meaning that $$A,B$$ are small too. 
Filling this into the PDE gives:
<div class="math-container">\[
\begin{aligned}
A_t(t)(\exp(lx)+\exp(-lx)) &= \delta\Delta (A(t)(\exp(lx)+\exp(-lx))) \\&+ f(A(t)(\exp(lx)+\exp(-lx)), B(t)(\exp(lx)+\exp(-lx)))\\
 B_t(t)(\exp(lx)+\exp(-lx)) &= \Delta ( B(t)(\exp(lx)+\exp(-lx))) \\
&- f(A(t)(\exp(lx)+\exp(-lx)), B(t)(\exp(lx)+\exp(-lx)))\\
\end{aligned}
\]</div>
Lovely... Now since $$A,B$$ are small, we can expand $$f$$ around the plateaus again:
<div class="math-container">\[
\begin{aligned}
A_t(t)(\exp(lx)+\exp(-lx)) &= \delta l^2 (A(t)(\exp(lx)+\exp(-lx))) \\&+ f_u(u_-)A(t)(\exp(lx)+\exp(-lx))+f_v(u_-) B(t)(\exp(lx)+\exp(-lx))\\
 B_t(t)(\exp(lx)+\exp(-lx)) &= l^2 ( B(t)(\exp(lx)+\exp(-lx))) \\
&- f_u(u_-)A(t)(\exp(lx)+\exp(-lx))-f_v(u_-) B(t)(\exp(lx)+\exp(-lx))\\
\end{aligned}
\]</div>
Note we can divide away the exponents on both sides:
<div class="math-container">\[
\begin{aligned}
A_t(t) &= \delta l^2 A(t) + f_u(u_-)A(t)+f_v(u_-) B(t)\\
 B_t(t) &= l^2 B(t) - f_u(u_-)A(t)-f_v(u_-) B(t)\\
\end{aligned}
\]</div>
Dropping some arguments, we can write this cleanly:
<div class="math-container">\[
\begin{aligned}
A_t &= (\delta l^2  + f_u^-)A+f_v^- B\\
B_t &=  - f_u^-A(t)+(l^2-f_v^-) B\\
\end{aligned}
\]</div>
Which is a simple system of ODE's, which gives an attracting point (bridge gets smaller -> fronts repel) when the determinant is positive, and the trace negative.
<div class="math-container">\[\begin{aligned}
\det M &= (\delta l^2+f_u^-)(l^2-f_v^-)+f_u^-f_v^-\\
&=\delta l^4-\delta l^2f_v^-+f_u^- l^2-f_u^-f_v^-+f_u^-f_v^-\\
& = \delta l^4-\delta l^2f_v^-+f_u^- l^2
\end{aligned}\]</div>
Note that $$l^2 = \frac{\delta}{f_u^-}$$, and then note that $$l^2>0$$, so we get:
<div class="math-container">\[
\begin{aligned}
\operatorname{sign}\det M & = \delta \frac{\delta}{f_u^-}-\delta f_v^-+f_u^- 
\end{aligned}
\]</div>
Which is positive at leading order. Next we find the trace:
<div class="math-container">\[
\Tr M=\delta l^2+f_u^-+l^2-f_v^- 
\]</div>
Note that $$l^2 = \frac{\delta}{f_u^-}$$, so we get:
<div class="math-container">\[
\Tr M=\delta \frac{\delta}{f_u^-}+f_u^-+\frac{\delta}{f_u^-}-f_v^- 
\]</div>
So at leading order, we have $$\Tr M = f_u^--f_v^-$$, which implies growing $$A,B$$ when $$f_u^->f_v^-$$, which means attracting fronts. 




More thorough:
<div class="math-container">\[
\begin{aligned}
\frac{d}{dt}\begin{pmatrix}A\\ B\end{pmatrix} &=\begin{pmatrix}\delta^2 /f_u^-  + f_u^-&f_v^- \\
 - f_u^-&\delta /f_u^--f_v^- \end{pmatrix}\begin{pmatrix}A\\ B\end{pmatrix}
\end{aligned}
\]</div>
which has eigenvalues:
<div class="math-container">\[\begin{aligned}
\lambda_1 = \frac{\delta^2 - \sqrt{(-\delta^2 - \delta - (f^-_u)^2 + f^-_u f^-_v)^2 - 4 (\delta^3 - \delta^2 f^-_u f^-_v + \delta (f^-_u)^2)} + \delta + (f^-_u)^2 - f^-_u f^-_v}{2f^-_u}\\
\lambda_2 = \frac{\delta^2 + \sqrt{(-\delta^2 - \delta - (f^-_u)^2 + f^-_u f^-_v)^2 - 4 (\delta^3 - \delta^2 f^-_uf^-_v + \delta (f^-_u)^2)} + \delta + (f^-_u)^2 - f^-_uf^-_v}{2f^-_u}
\end{aligned}\]</div>
At leading order we lose the $$O(1)$$ terms, and they reduce to:
<div class="math-container">\[
\begin{aligned}
\lambda_1 &=  \delta\frac{1}{2f_u^-} \left(\frac{ (f_u^- + f_v^-)}{ (f_u^- - f_v^-)} + 1\right)+O(\delta^2)
\\
\lambda_2 &= f_u^-+f_v^-+O(\delta)
\end{aligned}
\]</div>
So we have a very slow direction and a fast direction. The ratio of $$A,B$$ are know via the FBS, 


### single fronts not moving??
Filling this into the PDE gives:
<div class="math-container">\[
\begin{aligned}
A_t(t)\exp(lx) &= \delta\Delta A(t)\exp(lx) + f(A(t)\exp(lx), B(t)\exp(lx))\\
 B_t(t)\exp(lx) &= \Delta  B(t)\exp(lx) - f(A(t)\exp(lx), B(t)\exp(lx))
\end{aligned}
\]</div>
Since $$A,B$$ are small, we can expand $$f$$ around the plateaus again:
<div class="math-container">\[
\begin{aligned}
A_t(t)\exp(lx) &= \delta l^2 A(t)\exp(lx) + f_uA(t)\exp(lx)+f_v B(t)\exp(lx)\\
 B_t(t)\exp(lx) &= l^2  B(t)\exp(lx) - f_uA(t)\exp(lx) - f_vB(t)\exp(lx)
\end{aligned}
\]</div>
Note we can divide away the exponents on both sides:
<div class="math-container">\[
\begin{aligned}
A_t &= \delta l^2 A(t) + f_uA+f_v B\\
 B_t &= l^2  B- f_uA- f_vB
\end{aligned}
\]</div>
hmm zelfde systeem, dus ik dacht iets te makkelijk :((
jammer jammer :(


[View Raw Markdown](/assets/md/Exponential tails (niet goed).md)
