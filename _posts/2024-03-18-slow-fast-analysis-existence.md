---
layout: post
title: "Slow-fast analysis existence"
date: 2024-03-18
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

We analyze the system on two separate scales, we define a boundary layer in the variable $$x$$: $$x\in[-\sqrt\epsilon,\sqrt\epsilon]$$, since the width of the front is on the order $$\epsilon$$, we can neglect the front in the slow regime, which corresponds to the plateaus. 
## Slow
<div class="math-container">\[
\begin{aligned}
u_t &= \delta\Delta u + f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
The slow reduced limit is obtained by simply setting $$\delta=0$$. Then we get:
<div class="math-container">\[
\begin{aligned}
u_t &= f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
In steady state, we then get:
<div class="math-container">\[
\begin{aligned}
0 &= f(u,v)\\
0 &= \Delta v - f(u,v)\implies 0 = \Delta v\\
\end{aligned}
\]</div>
Since we only consider bounded solutions, this means $$v=C$$, for some constant $$C$$. But then $$u$$ has to be on the nullcline of $$f(u,C)$$, assuming some non-degeneracy, this implies that $$u$$ is a constant. So in the slow reduced limit, we find $$(u,v) = (\bar U,\bar V)$$. 

## Fast
Choose $$x=\epsilon \xi$$ 
<div class="math-container">\[
\begin{aligned}
u_t &= \epsilon^2 u_{xx} + f(u,v)\\
v_t &=  v_{xx} - f(u,v)\\
\end{aligned}
\]</div>
We can find the fast system by realizing that
<div class="math-container">\[
u_{xx} = u_{\xi\xi}(\xi_{x})^2 = \frac1{\epsilon^2}u_{\xi\xi}
\]</div>

Then we obtain:
<div class="math-container">\[
\begin{aligned}
u_t &=  u_{\xi\xi} + f(u,v)\\
\epsilon^2v_t &=  v_{\xi\xi} - \epsilon^2f(u,v)\\
\end{aligned}
\]</div>
Setting $$\epsilon=0$$, we get the slow-reduced system:
<div class="math-container">\[
\begin{aligned}
u_t &=  u_{\xi\xi} + f(u,v)\\
0&=  v_{\xi\xi} \\
\end{aligned}
\]</div>
Again by the boundedness of the solutions, we have $$v=v_0$$. 



# linearizing fast
The fast-reduced system is 1D, and gives front solutions. Earlier I showed that those have a translational eigenmode that corresponds to shifts, with eigenvalue $$0$$. Linearizing gives a sturm-liouville problem, which have the property that the largest eigenvalue corresponds to the eigenmode with no zeros. We showed that fronts are monotone, so translations have no zeros. Therefore the largest eigenvalue is 0, which corresponds to shifts. So the fast system is stable, the only thing it does is dictate properties of the slow subsystem, which will make it stable or not. 

<div class="math-container">\[
\begin{aligned}
\lambda s &=  s_{\xi\xi} + f_u(u_0,v_0)s+f_v(u_0,v_0)r\\
\epsilon^2\lambda r &=  r_{\xi\xi} - \epsilon^2f_u(u_0,v_0)s-\epsilon^2f_v(u_0,v_0)r
\end{aligned}
\]</div>
So $$r$$ is to leading order a constant across the fast subsystem. The system is linear, so for simplicity, let's say it's equal to $$r_0=1$$. 
<div class="math-container">\[
\begin{aligned}
\lambda s &=  s_{\xi\xi} + f_u(u_0,v_0)s+f_v(u_0,v_0)\\
\end{aligned}
\]</div>
let's abbreviate notation, we call $$f_u(\xi)=f_u(u_0(\xi),v_0(\xi))$$ and $$f_v(\xi) = f_v(u_0(\xi),v_0(\xi))$$. Then we get:
<div class="math-container">\[
\lambda s = s_{\xi\xi} +f_u(\xi)s+f_v(\xi)
\]</div>
This is an in-homogeneous Sturm-Liouville problem with operator
<div class="math-container">\[
\mathcal L = (\partial_\xi^2+f_u(\xi))
\]</div>
This eigenvalue problem has a solution, so we can assume we have its eigenvalues, then for $$\lambda$$ unequal to those, we get:
<div class="math-container">\[
s_{inner}(\xi) = (\mathcal L-\lambda)^{-1}f_v(\xi)
\]</div>
in de buurt van translatie blaast integraal conditie op

## slow-reduced linearized

<div class="math-container">\[
\begin{aligned}
u_t &= f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
Linearizing gives:
<div class="math-container">\[\begin{aligned}
\lambda u&=f_u(u_0,v_0)s+f_v(u_0,v_0)r\\
\lambda r &= \Delta r - f_u(u_0,v_0)s-f_v(u_0,v_0)r\\
\end{aligned}\]</div>
at the boundary $$x=\pm\sqrt\epsilon$$, we have only slightly departed from the fixed points of the heteroclinic orbit, so we have to leading order $$f_{u,0}:=f_u(u_0,v_0)=f_u(\bar U,\bar V)$$ and the same for the $$v$$-derivative. This turns our equations into a constant coefficient linear system of equations. So we can solve it:
<div class="math-container">\[
\begin{aligned}
\lambda s&=f_{u,0}s+f_{v,0}r\\
\lambda r &= \Delta r - f_{u,0}s-f_{v,0}r\\
\end{aligned}
\]</div>
If $$\lambda=f_{u,0}$$, then $$r=0$$ (since we assume non-degenerate $$f_{v,0}$$) and then also $$s=0$$ by the second equation and non-degeneracy. Otherwise we find $$s$$:
<div class="math-container">\[s= \frac{f_{v,0}}{\lambda-f_{u,0}}r\]</div>
So this leaves the equation for $$r$$:
<div class="math-container">\[
\begin{aligned}
\Delta r&=\lambda \frac{\lambda-f_{u,0}}{\lambda-f_{u,0}}r+ \frac{f_{u,0}f_{v,0}}{\lambda-f_{u,0}}r+f_{v,0}\frac{\lambda-f_{u,0}}{\lambda-f_{u,0}}r \\
&= \frac{\lambda^2-\lambda f_{u,0}+f_{u,0}f_{v,0}+\lambda f_{v,0}-f_{u,0} f_{v,0}}{\lambda-f_{u,0}}r\\
&= \frac{\lambda^2-\lambda f_{u,0}+\lambda f_{v,0}}{\lambda-f_{u,0}}r\\
&= \left(\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}\right)r
\end{aligned}
\]</div>
We get:
<div class="math-container">\[
r=r_0\exp\left(\pm \sqrt{\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}}x\right)
\]</div>
At leading order we have $$r_0=1$$, so at leading order:
It has to match to the fast solution we found, so we put $$r_0=1$$. Then we find that, depending on the side, and therefore the $$\bar U,\bar V$$, we need a plus or minus to have a bounded solution. The derivatives should also match, hence we calculate:
<div class="math-container">\[\begin{aligned}
r_\xi(\pm1/\sqrt\epsilon)=x_\xi r_x(\pm\sqrt\epsilon) &=\pm\epsilon \sqrt{\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}}\exp\left(\pm\epsilon \sqrt{\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}}(\pm\sqrt\epsilon)\right)\\
&=\pm\epsilon \sqrt{\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}}+O(\epsilon^{5/2})\\
\end{aligned}\]</div>
So the total jump is:
<div class="math-container">\[
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon }r_{\xi\xi}d\xi = r_\xi(1/\sqrt\epsilon)-r_\xi(-1/\sqrt\epsilon) = \pm\epsilon \sqrt{\lambda +\frac{\lambda f_{v,right}}{\lambda-f_{u,right}}}\mp\epsilon \sqrt{\lambda +\frac{\lambda f_{v,left}}{\lambda-f_{u,left}}}
\]</div>
#### Fast system integral
Let's find $$r_{\xi\xi}$$ to leading order (inside $$I_f$$):
<div class="math-container">\[\begin{aligned}
\epsilon^2v_t &=  v_{\xi\xi} - \epsilon^2f(u,v)\\
\epsilon^2\lambda r &=  r_{\xi\xi} - \epsilon^2f_u(u_0,v_0)s_{inner}-\epsilon^2f_v(u_0,v_0)r\\
\epsilon^2\lambda r &=  r_{\xi\xi} - \epsilon^2f_u(u_0,v_0)(\mathcal L-\lambda)^{-1}f_v(\xi)-\epsilon^2f_v(u_0,v_0)r\\
\end{aligned}\]</div>
This is again an in-homogeneous Sturm-Liouville problem, but we can simplify to leading order, since $$r=r_0+\epsilon^2 r_2$$ (using regular perturbation theory). Then the problem reduces to (using $$r_0=1$$):
<div class="math-container">\[
\begin{aligned}
\epsilon^2\lambda  &=  r_{\xi\xi} - \epsilon^2f_u(u_0,v_0)(\mathcal L-\lambda)^{-1}f_v(\xi)-\epsilon^2f_v(u_0,v_0)\\
\end{aligned}
\]</div> Now we found the integral of $$r_{\xi\xi}$$:
<div class="math-container">\[
\int_{I}r_{\xi\xi}d\xi = \epsilon^2\int[\lambda  + f_u(u_0,v_0)(\mathcal L-\lambda)^{-1}f_v(\xi)+f_v(u_0,v_0)]d\xi\\
\]</div>

we can evaluate the part with $$\lambda$$:
<div class="math-container">\[
\epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}\lambda d\xi=\frac{2}{\sqrt{\epsilon}}\lambda  = 2\epsilon^{3/2}\lambda
\]</div>
Again shorthanding $$f_u$$ and $$f_v$$, we have the result:
<div class="math-container">\[
 2\epsilon^{3/2}\lambda+\epsilon^2\int[f_u(\xi)s_{inner}+f_v(\xi)]d\xi\\ = O(\epsilon)
\]</div>
But we know what the jump should be! it should be of order $$\epsilon$$, so either $$\lambda$$ is of order $$1/\sqrt\epsilon$$, or this term drops out. 
#### Hopefully can show that $$\lambda$$ is small? 


Almost same as:
<img src="/assets/images/Pasted image 20240318152519.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240318152519.png">
<img src="/assets/images/Pasted image 20240318152307.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240318152307.png">
<img src="/assets/images/Pasted image 20240318152347.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240318152347.png">

<img src="/assets/images/Pasted image 20240318152434.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240318152434.png">
<img src="/assets/images/Pasted image 20240318152403.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240318152403.png">

[View Raw Markdown](/assets/md/Slow-fast analysis existence.md)
