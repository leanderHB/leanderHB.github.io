---
layout: post
title: "Singularly perturbed RDE"
date: 2024-03-14
---
<style>
.math-container {
    max-width: 100%; /* Set a maximum width to prevent it from expanding the page */
    overflow-x: auto; /* Enable horizontal scrolling */
    white-space: nowrap; /* Prevent the text from wrapping */
}
</style>
<div class="math-container">\[
\begin{aligned}
u_t &= \delta\Delta u + f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
Where $$\delta$$ is small, so $$u$$ diffuses on a completely different timescale than $$u$$. Now consider 
We'd like to use more convenient coordinates, since in steady state:
<div class="math-container">\[
\begin{aligned}
0 &= \delta\Delta u + \tilde f(u,\eta)\\
0 &=  \Delta v +\delta\Delta u =\Delta\eta\\
\end{aligned}
\]</div>
Note that in steady state, whether we consider an unbounded domain or bounded with no flux, or periodic BC, all dictate that $$\eta$$ be constant. So $$v+\delta u = \eta_0$$, meaning that all steady state solutions must lie on a line parametrized by $$\eta_0$$. Then we can rewrite the system, and for simplicity later we write $$\delta=\epsilon^2$$:
<div class="math-container">\[\begin{aligned}
\epsilon u_x &= w\\
\epsilon w_x &= -\tilde f(u,\eta_0)
\end{aligned}
\]</div>
Now we define our domain, and let's consider $$\mathbb R$$ for now. Then we can find a heteroclinic orbit (if $$f$$ permits one). Let's consider a mesa orbit, then $$u_{xx}=0$$ when $$x\to\pm \infty$$, therefore these lie at $$f(u,\eta_0)=0$$. Now note that our system is a Hamiltonian system, which means we might be able to use the Hamiltonian to find such a homoclinic orbit. The hamiltonian is the total energy, which we can read off to be $$\frac12\epsilon^2 (w)^2+\int_0^u\tilde f(u',\eta_0)du'$$. Note that the lower bound (constant of integration) here is arbitrary, we can put it to anything we like, as we're never interested in the absolute value of this quantity. 


Cool: is increasing: want state space symmetrisch, dus afgeleide blijft positief, anders intersection van lijnen! Oh of minder moeilijk: is $$u_x=\pm\sqrt{2E-2F(u)}$$, dus maar 1 sign mogelijk.
#### vergeet niet de $$\frac1\delta$$ hier

Where we implicitly define $$\eta=  v+\delta u$$. 

<div class="math-container">\[
kx=mx_{tt}
\]</div>
Hamiltonian: 
<div class="math-container">\[\frac{1}{2}kx^2+\frac{1}{2}mv^2\]</div>
for $$u$$:
<div class="math-container">\[
\frac{1}{2}(u_x)^2+ \frac1\delta \int_0^u f(u',\eta_0)du := \frac12 (u_x)^2+F(u)+C
\]</div>
Now the intuition is that $$u$$ is going to roll down the gradient of $$F(u)$$, and is going to end up at the same level as it started off at. So we require $$F(u(-\infty))=F(u(\infty))$$. This puts a constrain on what $$F$$ can be, note that $$F$$ is parametrized by $$\eta_0$$ still. We're looking for a mesa solution, so we require $$u(\infty)\neq u(-\infty)$$. The question then becomes, is this possible? The mesa-type solution we're looking for becomes flat for $$x\to \infty$$, so $$u_x\to 0$$ as $$x\to \infty$$. Then $$F(u)\to F(u^\pm)$$ depending on the direction, so apparently it becomes flat here. We can interpret this: $$f(u,\eta_0)=F'(u)$$, so when $$x\to\infty$$, we find $$F'(u(x))\to F^\pm$$. But the system is Hamiltonian, so then also $$F^+=F^-$$, since energy is conserved. So we're looking for a solution such that $$F(u^+)=F(u^-)$$, where $$u^\pm$$ are set by the constraint that they be fixed points of $$\tilde f(u,\eta_0)$$. But by the fundamental theorem of calculus, this is then equivalent to:
<div class="math-container">\[
F(u^+)-F(u^-)=\frac1\delta \int_{u^-}^{u^+} \tilde f(u,\eta_0)du = 0
\]</div>
So we have a neat constraint on $$\tilde f$$, and thereby on $$\eta_0$$. Now the question of course becomes, can this be satisfied? 
Note another thing: $$F$$ should allow us to roll down and back up again, so we need some kind of downward curvature at the endpoints. This amounts to the first nonzero derivative should be negative at the left side and similarly on the right side:
<div class="math-container">\[
\frac{d^k}{du^k}F(u^-)<0,\quad (-1)^l \frac{d^l}{du^l}F(u^+)<0
\]</div>
Where $$k$$ and $$l$$ give, for both equations, the first non-zero derivative.
When live isn't pathological, this just means that $$F''(u^-)<0$$ and $$F''(u^+)<0$$. 
Which comes down to $$f(u^-,\eta_0)>0$$ and $$f(u^+,\eta_0)>0$$. 
Okay well we narrowed down our functions that might work. Next, consider the fact that $$F$$ isn't allowed to become larger than $$F_0=F(u^\pm)$$ on $$[u^+,u^-]$$. This quickly follows from:
<div class="math-container">\[\begin{aligned}
\frac12 (u_x)^2+F(u)=E\quad\forall u\\
F(u)\leq E\quad\forall u
\end{aligned}\]</div>
Since $$(u_x)^2>0$$. Then finally, we need strictly smaller, since otherwise we'd never "get beyond" the point with equality. So really, $$F(u)<F_0$$ for all $$(u^-,u^+)$$. Now we can consider all continuous functions $$f(u,v)$$ defined by $$\tilde f(u,\eta)$$ such that there is an $$\eta$$ such that there are at least three intersections, with at least 2 of those with positive derivative. Take these two points, and call them $$u_-(\eta)$$ and $$u_+(\eta)$$. 

Requirements:
- $$F$$ exists
- $$F(u)<F_0$$ everywhere inside

Assuming we have a steady state solution $$u_0,v_0$$, we can expand around it: $$u(t)=u_0+e$$ and $$v(t)=v_0+r$$. 
<div class="math-container">\[
\begin{aligned}
(u_0+e)_t &= \delta\Delta (u_0+e) + f((u_0+e),v_0+r)\\
(v_0+r)_t &= \Delta (v_0+r) - f((u_0+e),v_0+r)\\
\end{aligned}
\]</div>
Now we expand $$f$$ to first order around $$u_0,v_0$$, and get:
<div class="math-container">\[
\begin{aligned}
(u_0+e)_t &= \delta\Delta (u_0+e) + f(u_0,v_0)+f_u(u_0,v_0)e+f_v(u_0,v_0)r\\
(v_0+r)_t &= \Delta (v_0+r) -  f(u_0,v_0)-f_u(u_0,v_0)e-f_v(u_0,v_0)r\\
\end{aligned}
\]</div>
The stationarity of $$u_0,v_0$$ gives $$(u_0)_t=0=(v_0)_t$$, and also $$\delta\Delta u_0+f(u_0+v_0)=0$$ and $$\Delta v_0-f(u_0+v_0)=0$$. Then we're left with:
<div class="math-container">\[
\begin{aligned}
e_t &= \delta\Delta e +f_u(u_0,v_0)e+f_v(u_0,v_0)r\\
r_t &= \Delta r -f_u(u_0,v_0)e-f_v(u_0,v_0)r\\
\end{aligned}
\]</div>
where $$f_u$$ and $$f_v$$ are now functions of only $$x$$. We'll drop some terms notation wise:
<div class="math-container">\[
\frac{\partial}{\partial t}\begin{pmatrix}e\\ r\end{pmatrix} = \begin{pmatrix}\delta \Delta+f_u&f_v\\ -f_u&\Delta+f_v\end{pmatrix}\begin{pmatrix}e\\r\end{pmatrix}
\]</div>
Assuming the growth will be exponential (or separation of variables) now gives us:
<div class="math-container">\[
\lambda\begin{pmatrix}e\\ r\end{pmatrix} = \begin{pmatrix}\delta \Delta+f_u&f_v\\ -f_u&\Delta-f_v\end{pmatrix}\begin{pmatrix}e\\r\end{pmatrix}
\]</div>
We now assume $$\delta$$ is small: $$O(\epsilon^2)$$, to get:
<div class="math-container">\[
\lambda e = f_ue+f_v r
\]</div>
Which fixes $$e$$ as function of $$r$$, as long as $$\lambda-f_u\neq 0$$. In fact, if it does equal zero, the function should still hold, so we cannot have $$\lambda\in \mathbb C\backslash ran(f_u)$$.

The other problem we have left is:
<div class="math-container">\[
\lambda r=-f_ue+\Delta r-f_v r
\]</div>
We can fill this in slightly more, and find again a Hamiltonian problem:
<div class="math-container">\[
\Delta r = g(x) r
\]</div>
Where $$g(x)=\lambda +f_v/(\lambda-f_u)+f_v$$.
Then we have a Sturm-Liouville problem, which dictates that the eigenvalues be real, therefore $$\lambda\in \mathbb R\backslash ran(f_u)$$, and since $$f_u$$ contains an open containing $$0$$, we know quite a bit already. We can find a potential term $$\frac{1}{2}g r^2$$, and this gives us again solutions. The solutions should start at $$0$$, so there better be zeros at $$x=\pm \infty$$, this is guaranteed by the previous part:  

<div class="math-container">\[
\begin{aligned}
y_x&=g(x)r\\
r_x&=y
\end{aligned}
\]</div>
## meneer je moet u of v ook herschalen!

# Nieuwe poging (:
Change of vars:
<div class="math-container">\[\begin{aligned}
\eta_t+(1-\delta)u_t&=\Delta\eta\\
u_t&=\delta\Delta u- f(u,\eta-\delta u)\\
\end{aligned}\]</div>
We expand these: $$\eta = \eta_0+r$$ and $$u = u_0+e$$, with $$r,e$$ small (we'll specify their order later). Then:
<div class="math-container">\[
\begin{aligned}
r_t+(1-\delta)e_t&=\Delta r+\Delta \eta_0\\
e_t&=\delta \Delta u_0+\delta\Delta e- f(u_0+e,(\eta_0+r)-\delta (u_0+e))
\end{aligned}
\]</div>
Expanding $$f$$ around $$u_0,\delta u_0+\eta_0$$ and using the stationarity:
<div class="math-container">\[
\begin{aligned}
r_t+(1-\delta)e_t&=\Delta r \\
e_t&=\delta\Delta e- f_u(u_0,\delta u_0+\eta_0)e-f_v(u_0,\delta u_0+\eta_0)(r-\delta e)
\end{aligned}
\]</div>
To reduce clutter a bit, let's define $$g_u(x)=f_u(u_0,\delta u_0+\eta_0)$$ and $$g_v(x)=f_v(u_0,\delta u_0+\eta_0)$$. Then we get, in 1D:
<div class="math-container">\[
\begin{aligned}
r_t+(1-\delta)e_t&= r_{xx} \\
e_t&=\delta e_{xx}- g_ue-g_v(r-\delta e)
\end{aligned}
\]</div>
#### Small 
We can define a length-scale $$y=\sqrt{\delta}x$$, to find $$r_{xx}=r_{\delta yy} = \frac1\delta r_{yy}$$. Then we get the system of equations:
<div class="math-container">\[
\begin{aligned}
r_t+(1-\delta)e_t&= \frac1\delta r_{yy} \\
e_t&=\frac1\delta \delta e_{yy}- g_ue-g_v(r-\delta e)
\end{aligned}
\]</div>
To leading order, the equations become:
<div class="math-container">\[
\begin{aligned}
0&= r_{yy} \\
e_t&= e_{yy}- g_ue-g_vr
\end{aligned}
\]</div>
Integrating twice, we find $$r = ay+b$$, but because our solutions are bounded, we get $$r=b$$. So on a small spatial-scale, the equations become second order again, which allows us to solve for them using similar techniques as earlier. Using separation of variables, we get:
<div class="math-container">\[
\begin{aligned}
\lambda e &= e_{yy}- g_ue-g_vb
\end{aligned}
\]</div>
#### Large
On the large scale, we don't change anything and the equations are to leading order:
<div class="math-container">\[
\begin{aligned}
r_t+e_t&= r_{xx} \\
e_t&=- g_ue-g_vr
\end{aligned}
\]</div>
We can subtract the second eqn from the first:
<div class="math-container">\[
\begin{aligned}
r_t&= r_{xx}+g_ue+g_vr \\
e_t&=- g_ue-g_vr
\end{aligned}
\]</div>
With separation of variables, or simply assuming the growth will be exponential, we get:
<div class="math-container">\[
\begin{aligned}
\lambda r&= r_{xx}+g_ue+g_vr \\
\lambda e&=- g_ue-g_vr
\end{aligned}
\]</div>
We can then solve $$e$$:
<div class="math-container">\[
e=\frac{-g_v}{\lambda +g_u}r
\]</div>
Filling this in gives us:
<div class="math-container">\[
\lambda r =r_{xx}+\frac{\lambda g_v}{\lambda+g_u}r
\]</div>
or:
<div class="math-container">\[
r_{xx} =\lambda r-\frac{\lambda g_v}{\lambda+g_u}r
\]</div>
Or written differently:
<div class="math-container">\[
\lambda r(\lambda+g_u)=r_{xx}(\lambda +g_u)+\lambda g_v r
\]</div>

<div class="math-container">\[
\begin{aligned}
\lambda \begin{pmatrix}
r\\ e
\end{pmatrix}r&=\begin{pmatrix}
\Delta +g_v& g_u\\ -g_u&-g_v
\end{pmatrix}\begin{pmatrix}
r\\ e
\end{pmatrix}
\end{aligned}
\]</div>
Or the Evan's function formulation:

<div class="math-container">\[
\begin{aligned}
\lambda r&= r'_{x}+g_ue+g_vr \\
r_x&=r
\\
\lambda e&=- g_ue-g_vr
\end{aligned}
\]</div>

# Evans function construction?

<div class="math-container">\[
\begin{aligned}
e_t &= \delta\Delta e +f_u(u_0,v_0)e+f_v(u_0,v_0)r\\
r_t &= \Delta r -f_u(u_0,v_0)e-f_v(u_0,v_0)r\\
\end{aligned}
\]</div>
Seperation of vars:
<div class="math-container">\[
\begin{aligned}
\frac1\delta\lambda e &= \Delta e +\frac1\delta f_ue+\frac1\delta f_vr\\
\lambda r &= \Delta r -f_ue-f_vr\\
\end{aligned}
\]</div>
Shuffling:
<div class="math-container">\[
\begin{aligned}
\Delta e  &= \frac1\delta\lambda e -\frac1\delta f_ue-\frac1\delta f_vr\\
\lambda r &= \Delta r -f_ue-f_vr\\
\end{aligned}
\]</div>
Turning into first order ODE's:
<div class="math-container">\[
\begin{aligned}
e'&=\frac1{\sqrt\delta}E\\
E'  &= \frac1{\sqrt\delta}\lambda e -\frac1{\sqrt\delta} f_ue-\frac1{\sqrt\delta} f_vr\\
r' &= R\\
R'&=\lambda r  +f_ue+f_vr\\
\end{aligned}
\]</div>
Or as a matrix:
<div class="math-container">\[
\begin{pmatrix} e\\ E\\ r\\ R\end{pmatrix}_x = \begin{pmatrix} 0&\frac1{\sqrt\delta}&0&0\\ \frac1{\sqrt\delta}\lambda-\frac1{\sqrt\delta} f_u&0&-\frac1{\sqrt\delta} f_v&0\\ 0&0&0&1\\ f_u&0&\lambda+f_v&0\end{pmatrix}\begin{pmatrix} e\\ E\\ r\\ R\end{pmatrix}
\]</div>
By 2.1.1 of (Spectral and Dynamical Stability of Nonlinear Waves), we know that this system of equations has a unique solution for all $$x$$ if we give it initial conditions $$\Psi_0$$. Fix an $$x_0$$ in the lower plateau $$(u_-,v_-)$$ and take a basis $$A=(\Psi_1,\Psi_2,\Psi_3,\Psi_4)$$ of the 4D space spanned by the above coefficients. Then by Liouville's formula (2.1.2), we know that the fundamental matrix solution (FMS) to the initial conditions $$x_0,A$$ has the property:
<div class="math-container">\[
\det A(x)=\det(A(x_0))\exp\left(\int_{x_0}^x tr(A(s))ds \right)
\]</div>
Now, note that $$tr(A(s))=0$$ for all $$s$$. So the determinant is constant. 
Great, so $$\det A$$ is not determined by $$x$$ at all. Now let's consider zeroes of $$\det A$$. 
<div class="math-container">\[
\det\begin{pmatrix} 0&\frac1{\sqrt\delta}&0&0\\ \frac1{\sqrt\delta}\lambda-\frac1{\sqrt\delta} f_u&0&-\frac1{\sqrt\delta} f_v&0\\ 0&0&0&1\\ f_u&0&\lambda+f_v&0\end{pmatrix}=\frac{\lambda^2}{\delta} - \frac{\lambda f_u}{\delta} + \frac{\lambda f_v}{\delta}
\]</div>
#### maybe interesting:
<div class="math-container">\[
\lambda=f_u-f_v
\]</div>
Gives a zero which should correspond to an eigenvalue of the operator we're considering. Note this is a function, so we can consider the two limits 
<div class="math-container">\[
\lambda^-=f^-_u-f_v^-,\quad \lambda^+=f_u^+-f_v^+
\]</div>
If either of these is positive, I reckon the whole thing would collapse? Or perhaps it's based on the direction, $$\lambda^-$$ should be positive, $$\lambda^+$$ should be negative? Seems to work out...
Maar dit voelt veel te simpel (:


And we find the characteristic polynomial:
<div class="math-container">\[
\frac{\lambda^2}{\delta} - \frac{\lambda f_u}{\delta} + \frac{\Lambda^2 f_u}{\delta} + \frac{\lambda f_v}{\delta} - \Lambda^2 f_v + \Lambda^4 - \frac{\lambda \Lambda^2}{\delta} - \lambda \Lambda^2
\]</div>
Which we can group as
<div class="math-container">\[
\frac{\lambda^2}{\delta} + \lambda\left(-\frac{\Lambda^2}{\delta} - \frac{f_u}{\delta} + \frac{f_v}{\delta} - \Lambda^2\right)  +\left(\Lambda^4 + \frac{\Lambda^2 f_u}{\delta}- \Lambda^2 f_v\right)
\]</div>
Or grouped differently:
<div class="math-container">\[
\left(\frac{\lambda^2}{\delta} - \frac{\lambda f_u}{\delta}+ \frac{\lambda f_v}{\delta}\right) + \Lambda^2 \left(-\frac{\lambda}{\delta} + \frac{f_u}{\delta} - f_v - \lambda\right)  + \Lambda^4
\]</div>
multiplying by $$\delta$$ gives the same eigenvalues:
<div class="math-container">\[
{\lambda^2} - \lambda\left({ f(u)} + { f(v)} - { \Lambda^2} - \delta\Lambda^2\right) + {\Lambda^2 f(u)}  -\delta \Lambda^2 f(v) +\delta \Lambda^4
\]</div>




## aahh
<div class="math-container">\[
\begin{aligned}
\lambda r&= r_{xx}+g_ue+g_vr \\
\lambda e&=- g_ue-g_vr
\end{aligned}
\]</div>

<div class="math-container">\[
\begin{aligned}
\frac1\delta\lambda e &= \Delta e +\frac1\delta f_ue+\frac1\delta f_vr\\
\lambda r &= \Delta r -f_ue-f_vr\\
\end{aligned}
\]</div>












<img src="/assets/images/Pasted image 20240215174124.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240215174124.png">


<div class="math-container">\[
v_{in}(\xi)=(L_0-\lambda)^{-1}H_u(\xi)
\]</div>
<img src="/assets/images/Pasted image 20240216130223.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240216130223.png">


<div class="math-container">\[
\begin{aligned}
e'&=\frac1{\sqrt\delta}E\\
E'  &= \frac1{\sqrt\delta}\lambda e -\frac1{\sqrt\delta} f_ue-\frac1{\sqrt\delta} f_vr\\
r' &= R\\
R'&=\lambda r  +f_ue+f_vr\\
\end{aligned}
\]</div>
A priori, we have the expansion around the steady state:
<div class="math-container">\[\begin{aligned}
G(U, V ) &=G(\bar U,\bar V)+ g_u U + g_v V + G_2 (U, V ; ε)\\ 
H(U, V ) &=H(\bar U,\bar V)+ h_u U + h_v V + H_2 (U, V ; ε)
\end{aligned}\]</div>
In our system, $$H=-G$$, so we can focus solely on $$G$$. Also, we assume $$G_2$$ is independent of $$\epsilon$$.
<div class="math-container">\[
G(\bar U+\epsilon^\alpha u,\bar V+\epsilon^\alpha v) =G(\bar U,\bar V)+ G_U(\bar U,\bar V) \epsilon^\alpha u + G_V(\bar U,\bar V) \epsilon^\alpha v + \epsilon^{2\alpha} G_2 (U, V)\\ 
\]</div>




<div class="math-container">\[
\begin{pmatrix} e\\ r\\ E\\ R\end{pmatrix}_x = \begin{pmatrix} 0&0&\frac1{\sqrt\delta}&0&\\ 
0&0&0&1\\ 
\frac1{\sqrt\delta}\lambda-\frac1{\sqrt\delta} f_u&-\frac1{\sqrt\delta} f_v&0&0\\ 
f_u&\lambda+f_v&0&0
\end{pmatrix}\begin{pmatrix} e\\ r\\ E\\ R\end{pmatrix}
\]</div>