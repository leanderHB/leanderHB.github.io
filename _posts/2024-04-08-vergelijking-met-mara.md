---
layout: post
title: "Vergelijking met Mara"
date: 2024-04-08
---
Ik ben het eens met mara tot het volgende stuk:
![Image](/assets/images/Pasted image 20240318121007.png)
De limieten van de afgeleiden $$\xi\to\pm\infty$$ zijn volgens mij niet nul, maar gewoon de afgeleiden op $$(u_-,v_-)$$ en $$(u_+,v_+)$$. Deze aanname zorgt ervoor dat de uitdrukking voor het exponent niet klopt volgens mij. 

Hieronder wat ik heb gedaan, ik heb geen change of variables gedaan (Mara wel), ik vond dat alleen maar verwarrend, en ik had al zat variabelen. Ik heb wel de notatie $$r,s$$ hetzelfde gehouden om het vergelijkbaarder te houden.
# Steady state solutions
Throughout the next text, $$\delta=\epsilon^2$$. Also we assume the derivatives of the reaction term to be non-zero at the plateaus, and in fact to be of $$O(\epsilon^0)=O(1)$$. 
## Flux-balance (Brauns)
we have the PDE:
<div>\[
\begin{aligned}
u_t &= \delta\Delta u + f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
We can introduce $$\eta=\delta u+ v$$ and write this in a more convenient form:
<div>\[
\begin{aligned}
0 &= \delta\Delta u + \tilde f(u,\eta):=\delta\Delta u +  f(u,\eta-\delta u)\\
0 &=  \Delta v +\delta\Delta u :=\Delta\eta\\
\end{aligned}
\]</div>
Then $$\eta=\eta_0$$ for some $$\eta_0$$. 
## Hamiltonian
So we have a Hamiltonian system given by:
<div>\[
E = \frac12 (u_x)^2 + \frac1\delta\int_{u_-}^u\tilde f(u',\eta_0)du':=\frac12 (u_x)^2 + F(u)
\]</div>
Note that we have a mesa solution when we can find a $$\eta_0$$ such that the equipotential solution of $$E=0$$ is a heteroclinic orbit. Let's say $$f$$ allows for such a solution. 
The heteroclinic orbit is an equipotential line of the hamiltonian, so $$E$$ parametrizes the orbit:
<div>\[
\frac12 (u_x)^2+F(u(x))=E\quad\forall x\\
\]</div>
Note that indeed:
<div>\[
\frac{d}{dx}E = u_{xx}+F'(u)=u_{xx}+\frac{1}{\delta}\tilde f(u,\eta_0)=0
\]</div>
so it satisfies the steady-state ODE, and indeed $$E$$ is conserved (hamiltonian property). 
We can solve this system:
<div>\[
u_x = \pm \sqrt{2E-2 F(u)}
\]</div>
This requires $$F(u)\leq E\quad\forall u$$ and $$F(u)<E$$ outside the limit points, which makes sense, to roll down the potential and come to a stop on the other side of the potential, we can't go over bigger hills than the one we started on. 
Consider a small translation: $$\tilde u(x)=u(x+dx)$$. The difference is given by $$u(x)-\tilde u(x)$$. Then of course for a small translation $$dx$$, the difference is to first order given by $$u_xdx$$. This is then the translational mode that has $$\lambda=0$$, and has no zeros, since $$u_x = \pm \sqrt{2E-2 F(u)}$$. 
With a bit of numerics, we can find $$\eta_0$$ and integrate the ODE starting barely outside one of the saddles (for the system that Braun chooses):
![hetero.png](../vergelijking-met-mara/)
# Slow and fast systems
We analyze the system on two separate scales, we define a boundary layer in the variable $$x$$: $$x\in I_f=[-\sqrt\epsilon,\sqrt\epsilon]$$, since the width of the front is on the order $$\epsilon$$, we can neglect the front in the slow regime, which corresponds to the plateaus. The next section treats this in more detail.
## Slow
<div>\[
\begin{aligned}
u_t &= \epsilon^2\Delta u + f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
The slow reduced limit is obtained by simply setting $$\epsilon=0$$. Then we get:
<div>\[
\begin{aligned}
u_t &= f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
In steady state, we then get:
<div>\[
\begin{aligned}
0 &= f(u,v)\\
0 &= \Delta v - f(u,v)\implies 0 = \Delta v\\
\end{aligned}
\]</div>
Since we only consider bounded solutions, this means $$v=\bar V$$, for some constant $$\bar V$$. But then $$u$$ has to be on the nullcline of $$f(u,\bar V)$$, assuming some non-degeneracy around the plateaus, this implies that $$u$$ is a constant. So in the slow reduced limit, we find $$(u,v) = (\bar U,\bar V)$$. 
## Fast
Choose $$x=\epsilon \xi$$ 
<div>\[
\begin{aligned}
u_t &= \epsilon^2 u_{xx} + f(u,v)\\
v_t &=  v_{xx} - f(u,v)\\
\end{aligned}
\]</div>
We can find the fast system by realizing that
<div>\[
u_{xx} = u_{\xi\xi}(\xi_{x})^2 = \frac1{\epsilon^2}u_{\xi\xi}
\]</div>
Then we obtain:
<div>\[
\begin{aligned}
u_t &=  u_{\xi\xi} + f(u,v)\\
\epsilon^2v_t &=  v_{\xi\xi} - \epsilon^2f(u,v)\\
\end{aligned}
\]</div>
looking at stationary conditions, we find
<div>\[
\begin{aligned}
0 &=  u_{\xi\xi} + f(u,v)\\
0 &=  v_{\xi\xi} - \epsilon^2f(u,v)\\
\end{aligned}
\]</div>
Again by the boundedness of the solutions, we have $$v=v_0$$ to leading order. So we're left with a hamiltonian system. The complete system is also Hamiltonian, and , so it makes sense to also require a heteroclinic solution here (needs cleaner argument, using the fact that to leading order $$v$$ is constant, so the Hamiltonians are actually equal (assuming some smoothness/independence on $$\epsilon$$)). Then this implies that the fast subsystem is also monotone (like the complete system).
# Stability
### Linearizing the fast system
The fast-reduced system is 1D, and gives front solutions. Earlier I showed that those have a translational eigenmode that corresponds to shifts, with eigenvalue $$0$$. Linearizing gives a sturm-liouville problem, which have the property that the largest eigenvalue corresponds to the eigenmode with no zeros. We showed that fronts are monotone, so translations have no zeros. Therefore the largest eigenvalue is 0, which corresponds to shifts. So the fast system is stable, the only thing it does is dictate the possible $$\lambda$$'s of the slow subsystem, which will make it stable or not. 
The linearization in more detail:
<div>\[
\begin{aligned}
\lambda s &=  s_{\xi\xi} + f_u(u_0,v_0)s+f_v(u_0,v_0)r\\
\epsilon^2\lambda r &=  r_{\xi\xi} - \epsilon^2f_u(u_0,v_0)s-\epsilon^2f_v(u_0,v_0)r
\end{aligned}
\]</div>
So $$r$$ is to leading order a constant across the fast subsystem: $$r=r_0+O(\epsilon)$$ (or maybe $$\epsilon^2$$? (I think it is...). I have to do perturbation theory to solve more neatly, but doesn't matter here, it's at least $$O(\epsilon)$$, and that's enough that even a nearly singular $$s$$ will not mess with the leading order behaviour easily). The system is linear, so for simplicity, let's put $$r_0=1$$. Then we're left with
<div>\[
\begin{aligned}
\lambda s &=  s_{\xi\xi} + f_u(u_0,v_0)s+f_v(u_0,v_0)\\
\end{aligned}
\]</div>
let's abbreviate notation, we call $$f_u(\xi)=f_u(u_0(\xi),v_0(\xi))$$ and $$f_v(\xi) = f_v(u_0(\xi),v_0(\xi))$$. Then we get:
<div>\[
\lambda s = s_{\xi\xi} +f_u(\xi)s+f_v(\xi)
\]</div>
This is an in-homogeneous Sturm-Liouville problem with operator
<div>\[
\mathcal L = (\partial_\xi^2+f_u(\xi))
\]</div>
By Sturm-Liouville theory, the homogeneous eigenvalue problem $$\mathcal L s=\lambda s$$ has a countable set of real solutions $$s_0,s_1,\dots$$ with eigenvalues $$\lambda_0>\lambda_1>\dots$$ ,  where $$s_i$$ has $$i$$ roots. We know that the fast subsystem has monotone solutions (it's a hamiltonian, heteroclinic system) so for $$\lambda>0$$ (the real part!) (which is of interest because those $$\lambda$$ give an unstable system), we can invert the problem to find:
<div>\[
s_{inner}(\xi) = (\mathcal L-\lambda)^{-1}f_v(\xi)
\]</div>
### Derivatives at the edge of the boundary layer. 
Putting $$\epsilon=0$$ in the slow system:
<div>\[
\begin{aligned}
u_t &= f(u,v)\\
v_t &= \Delta v - f(u,v)\\
\end{aligned}
\]</div>
Linearizing gives:
<div>\[\begin{aligned}
\lambda s&=f_u(u_0,v_0)s+f_v(u_0,v_0)r\\
\lambda r &= \Delta r - f_u(u_0,v_0)s-f_v(u_0,v_0)r\\
\end{aligned}\]</div>
at the boundary $$x=\pm\sqrt\epsilon$$, we have only slightly departed from the fixed points of the heteroclinic orbit, so we have to leading order $$f_{u,0}:=f_u(u_0,v_0)=f_u(\bar U,\bar V)$$ and the same for the $$v$$-derivative. Note this is a bit ambiguous as we don't know which side of the front we are on, but I'll make this clear as soon as we need specifics. This turns our equations into a constant coefficient linear system of equations. So we can solve it:
<div>\[
\begin{aligned}
\lambda s&=f_{u,0}s+f_{v,0}r\\
\lambda r &= \Delta r - f_{u,0}s-f_{v,0}r\\
\end{aligned}
\]</div>
If $$\lambda=f_{u,0}$$, then $$r=0$$ (since we assume non-degenerate $$f_{v,0}$$) and then also $$s=0$$ by the second equation and non-degeneracy. So for non-trivial solutions we can divide by $$\lambda-f_{u,0}$$ and find $$s$$ in terms of $$r$$:
<div>\[s= \frac{f_{v,0}}{\lambda-f_{u,0}}r\]</div>
So this leaves the equation for $$r$$:
<div>\[
\begin{aligned}
\Delta r&=\lambda \frac{\lambda-f_{u,0}}{\lambda-f_{u,0}}r+ \frac{f_{u,0}f_{v,0}}{\lambda-f_{u,0}}r+f_{v,0}\frac{\lambda-f_{u,0}}{\lambda-f_{u,0}}r \\
&= \frac{\lambda^2-\lambda f_{u,0}+f_{u,0}f_{v,0}+\lambda f_{v,0}-f_{u,0} f_{v,0}}{\lambda-f_{u,0}}r\\
&= \frac{\lambda^2-\lambda f_{u,0}+\lambda f_{v,0}}{\lambda-f_{u,0}}r\\
&= \left(\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}\right)r
\end{aligned}
\]</div>
We get:
<div>\[
r=r_0\exp\left(\mp \sqrt{\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}}x\right)
\]</div>
It has to match to the fast solution we found, so we put $$r_0=1$$. Then we find that, depending on the side, and therefore the $$\bar U,\bar V$$, we need a plus or minus to have a bounded solution. The derivatives should also match, hence we calculate:
<div>\[\begin{aligned}
r_\xi(\pm1/\sqrt\epsilon)=x_\xi r_x(\mp\sqrt\epsilon) &=\mp\epsilon \sqrt{\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}}\exp\left(\mp\epsilon \sqrt{\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}}(\pm\sqrt\epsilon)\right)\\
&=\mp\epsilon \sqrt{\lambda +\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}}+O(\epsilon^{5/2})\\
\end{aligned}\]</div>
So the total jump is:
<div>\[
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon }r_{\xi\xi}d\xi = r_\xi(1/\sqrt\epsilon)-r_\xi(-1/\sqrt\epsilon) = -\epsilon \sqrt{\lambda +\frac{\lambda f_{v,right}}{\lambda-f_{u,right}}}-\epsilon \sqrt{\lambda +\frac{\lambda f_{v,left}}{\lambda-f_{u,left}}}
\]</div>
Note that the sign is negative, this makes sense as we have exponential solutions going to the value $$1$$ at $$\pm\sqrt\epsilon$$, they are clearly pointing up around the origin, so to "go over the bump", there should be a negative change of derivative. 
Note that for real solutions, we require:
<div>\[
\lambda+\frac{\lambda f_{v,0}}{\lambda-f_{u,0}}>0
\]</div>
Which turns into:
<div>\[
\lambda-f_{u,0}+f_{v,0}>0\implies \lambda>f_{u,0}-f_{v,0}
\]</div>
So we have a lower bound on $$\lambda$$ for real $$\lambda$$. But they don't have to be? Don't think they have to actually, we can have oscillating solutions, I should check this!
# vergelijking met Mara
![Image](/assets/images/Pasted image 20240318121007.png)
Als ik ook aanneem dat $$f_{v},f_u\to 0$$ richting de rand van de boundary layer, krijg ik hetzelfde als Mara. Maar dat is een beetje een gekke aanname, want dat is je non-degeneracy. Het is niet dat het onmogelijk is om dan heterocliene orbits te krijgen, maar volgens mij is dit niet helemaal de bedoeling. 
Zij komt dan uiteindelijk met:
![Image](/assets/images/Pasted image 20240319120403.png)
Zoals je ziet, als ik $$f_{v,right}$$ en $$f_{v,left}$$ op nul zet, komt mijn minder elegante:
<div>\[\Delta_{slow}r_\xi=-\epsilon \sqrt{\lambda +\frac{\lambda f_{v,right}}{\lambda-f_{u,right}}}-\epsilon \sqrt{\lambda +\frac{\lambda f_{v,left}}{\lambda-f_{u,left}}}\]</div>
uit zoals zei het heeft, maar ik zie niet in waarom dat een oke aanname is, en het is in ieder geval niet iets wat ze noemt. 
# Verder met de inner solution integreren
Let's find $$r_{\xi\xi}$$ to leading order (inside $$I_f$$):
<div>\[\begin{aligned}
\epsilon^2v_t &=  v_{\xi\xi} - \epsilon^2f(u,v)\\
\epsilon^2\lambda r &=  r_{\xi\xi} - \epsilon^2f_u(u_0,v_0)s_{inner}-\epsilon^2f_v(u_0,v_0)r\\
%% \epsilon^2\lambda r &=  r_{\xi\xi} - \epsilon^2f_u(u_0,v_0)(\mathcal L-\lambda)^{-1}f_v(\xi)-\epsilon^2f_v(u_0,v_0)r\\ %%
\end{aligned}\]</div>
Where $$s_{inner} = (\mathcal L-\lambda)^{-1}f_v(\xi)$$. This is again an in-homogeneous Sturm-Liouville problem, but we can simplify to leading order, since $$r$$ is to leading order constant: $$r=r_0+O(\epsilon)$$ (using regular perturbation theory). Then the problem reduces to (using $$r_0=1$$):
<div>\[
\begin{aligned}
\epsilon^2\lambda  &=  r_{\xi\xi} - \epsilon^2f_u(u_0,v_0)s_{inner}-\epsilon^2f_v(u_0,v_0)\\
\end{aligned}
\]</div> 
Now we found the integral of $$r_{\xi\xi}$$:
<div>\[
\int_{I}r_{\xi\xi}d\xi = \epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[\lambda  + f_u(u_0,v_0)s_{inner}+f_v(u_0,v_0)]d\xi\\
\]</div>
we can evaluate the part with $$\lambda$$:
<div>\[
\epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}\lambda d\xi=\frac{2}{\sqrt{\epsilon}}\lambda  = 2\epsilon^{3/2}\lambda
\]</div>
Again shorthanding $$f_u$$ and $$f_v$$, we have the result:
<div>\[
 2\epsilon^{3/2}\lambda+\epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_u(\xi)s_{inner}+f_v(\xi)]d\xi= -\epsilon \sqrt{\lambda +\frac{\lambda f_{v,right}}{\lambda-f_{u,right}}}-\epsilon \sqrt{\lambda +\frac{\lambda f_{v,left}}{\lambda-f_{u,left}}}
\]</div>
Toevoeging na meeting maandag: "even de algebra", we vergelijken de linker $$\lambda$$ term met de rechter term:
Laten we zeggen dat $$\lambda=l\epsilon^{\alpha}$$. Als $$\alpha=0$$, dan kan de vergelijking nooit matchen qua order, en anders dan wordt bijvoorbeeld de term die bij rechts (van de overgang) hoort:
<div>\[
\sqrt{l\epsilon^{\alpha} +\frac{l\epsilon^{\alpha} f_{v,right}}{l\epsilon^{\alpha}-f_{u,right}}}=\epsilon^{\alpha/2}\sqrt{l +\frac{l f_{v,right}}{l\epsilon^{\alpha}-f_{u,right}}}
\]</div>
If $$\alpha<0$$ and $$\epsilon\to0$$, then this expression becomes:
<div>\[
\epsilon^{\alpha/2}\sqrt l
\]</div>
If $$\alpha>0$$ and $$\epsilon\to 0$$, then it becomes $$\epsilon^{\alpha/2}\sqrt{l-l f_{v,right}/f_{u,right})}$$. In both cases, scaling as $$\epsilon^{\alpha/2}$$. Let's plug this scaling into our equation:
<div>\[
2\epsilon^{3/2}l\epsilon^{\alpha}\sim-\epsilon \sqrt{l}\epsilon^{\alpha/2}
\]</div>
We find:
<div>\[
3/2+\alpha=1+\alpha/2
\]</div>
So $$\alpha=-1$$ would allow us to match solutions. Then we get an equation for $$l$$:
<div>\[
2l = -2\sqrt l
\]</div>
This has a solution when $$l=0$$, so not a solution we are interested in, and we can safely neglect it (needs better argument). 
<div>\[\begin{aligned}
\epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_u(\xi)s_{inner}+f_v(\xi)]d\xi&= -\epsilon \sqrt{\lambda +\frac{\lambda f_{v,right}}{\lambda-f_{u,right}}}-\epsilon \sqrt{\lambda +\frac{\lambda f_{v,left}}{\lambda-f_{u,left}}}\\
&=O(\epsilon\sqrt\lambda)
\end{aligned}\]</div>
Now remember that $$s_{inner}$$ is guaranteed to exist when $$\lambda>0$$ (or the real part at least). We find that the integral has to be rather large to accommodate for the order on the RHS. 
<div>\[\begin{aligned}
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_u(\xi)s_{inner}+f_v(\xi)]d\xi&= O(\sqrt\lambda/\epsilon)
\end{aligned}\]</div>
Note that $$s_{inner}$$ is given by the inverse of $$\mathcal L-\lambda$$. When $$\lambda$$ becomes close to one of the eigenvalues of the fast system, $$\|s_{inner}\|$$ can become very large, which implies that the order could be matched! The (fast) eigenvalue with the largest real part is the one at zero, so we can perturb that one a bit and see which orders cause $$\lambda$$ to become positive. So $$\lambda$$ is close to $$0$$, which means we can simplify the expression for the jump:

<div>\[
\epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_u(\xi)s_{inner}+f_v(\xi)]d\xi= -\epsilon \sqrt\lambda\left(\sqrt{1-\frac{f_{v,right}}{f_{u,right}}}+\sqrt{1-\frac{f_{v,left}}{f_{u,left}}}\right)+\dots
\]</div>
We see that in the small $$\lambda$$ limit, we require $$f_v<f_u$$ on both sides of the plateau for real solutions, but again, don't think that's necessary (is dat zo Arjen?). To get some feeling for what $$s_{inner}$$ looks like, we might be able to use some approximation of the inverse operator, but I have no clue if I'm honest. 
I think that for certain values of $$\lambda$$, we can neglect the second term in the integral:
<div>\[\begin{aligned}
O\left(\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}f_v(\xi)d\xi\right) &= \frac{2}{\sqrt{\epsilon}}O(1) = O(1/\sqrt\epsilon)\\
\end{aligned}\]</div>
Here I assume $$f_v$$ to be order $$1$$ across the system. To match the right side then, we require $$\lambda=O(\epsilon)$$ exactly.  
# Vergelijking met Mara
Mara integreert hier $$r_{\xi\xi}$$, maar stopt vervolgens (volgens mij in ieder geval) de slow reduced $$r$$ erin, maar veranderd dan $$x$$ naar $$\xi$$. 
![Image](/assets/images/Pasted image 20240318213751.png)
Haar $$r_{\xi\xi}$$ is namelijk $$0$$ hier.
![Image](/assets/images/Pasted image 20240318213837.png)
Maar deze vergelijking voor het langzame systeem lijkt verdacht veel op wat ze in de integraal gebruikt:
![Image](/assets/images/Pasted image 20240318213733.png)

Verder is dit ook gek:
![Image](/assets/images/Pasted image 20240318221252.png)
De integraal over $$r$$ word hier $$O(\sqrt\epsilon)$$, terwijl we de snelle variabele integreren, dus juist een $$O(1/\sqrt{\epsilon})$$ zouden moeten krijgen. 

Het verhaal met de sign van de integraal over $$S_{in}$$ heb ik verder niet helemaal bestudeerd, omdat ik eerder niet snapte hoe ze daar op kwam, en nu denk dat het waarschijnlijk voortbouwt op verkeerde resultaten. 