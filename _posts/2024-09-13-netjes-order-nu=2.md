---
layout: post
title: "Netjes order nu=2"
date: 2024-09-13
---
We start with the set of equations:
<div>\[\begin{aligned}
U_t &= \epsilon^2U_{xx}+f(U,V)\\
V_t &= V_{xx}-f(U,V)
\end{aligned}
\]</div>
By previous analysis, we know that we get a 1 parameter family in $$K$$ of pulses and fronts described by a Hamiltonian system in $$U$$, for which there is a specific $$K^*$$ for which we obtain a front solution. Take this $$K^*$$ and the front $$(U^*,V^*)=(U^*,K^*-\epsilon^2 U^*)$$ that comes with it. We can expand these values and obtain:
<div>\[
\begin{aligned}
K^*&=K^*_0+\epsilon^2K_1^*+\mathcal O(\epsilon^4)\\
U^*&=U^*_0+\epsilon^2U_1^*+\mathcal O(\epsilon^4)\\
V^*&=V^*_0+\epsilon^2V_1^*+\mathcal O(\epsilon^4) = K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*+\mathcal O(\epsilon^4)
\end{aligned}
\]</div>
Let's perturb the system to check stability, take $$\delta$$ smaller than all system scales, and define:
<div>\[\begin{aligned}
U(\xi) &= U^*(\xi)+\delta \exp(\lambda t)u(\xi)\\
V(\xi) &= V^*(\xi)+\delta \exp(\lambda t)v(\xi)
\end{aligned}\]</div>
Inserting this into the PDE and throwing out terms of order $$\delta^2$$, we get the linearized equations:
<div>\[
\begin{aligned}
\lambda u &= \epsilon^2u_{xx}+f_U(U^*,V^*)u+f_V(U^*,V^*)v\\
\lambda v&= v_{xx}-f_U(U^*,V^*)u-f_V(U^*,V^*)v
\end{aligned}
\]</div>
Now we expand $$U^*,V^*$$ and get something we might describe as appalling:
<div>\[
\begin{aligned}
\lambda u &= \epsilon^2u_{xx}+f_U(U^*_0,V^*_0)u+\epsilon^2f_{UU}(U^*_0,V^*_0)U_1^*u+\epsilon^2f_{UV}(U^*_0,V^*_0)(K_1^*-U_0^*)u\\&+f_V(U^*_0,V^*_0)v+\epsilon^2f_{VU}(U^*_0,V^*_0)U_1^*v+\epsilon^2f_{VU}(U^*_0,V^*_0)(K^*_1-U_0^*)v+\mathcal O(\epsilon^4)\\
\lambda v&= v_{xx}-f_U(U^*_0,V^*_0)u-\epsilon^2f_{UU}(U^*_0,V^*_0)U_1^*u-\epsilon^2f_{UV}(U^*_0,V^*_0)(K_1^*-U_0^*)u\\&-f_V(U^*_0,V^*_0)v-\epsilon^2f_{VU}(U^*_0,V^*_0)U_1^*v-\epsilon^2f_{VU}(U^*_0,V^*_0)(K^*_1-U_0^*)v+\mathcal O(\epsilon^4)\\
\end{aligned}
\]</div>
We're not done yet, however, we also will expand $$u,v$$ as 
<div>\[u=u_0+\epsilon^2 u_1+\dots\quad v=v_0+\epsilon^2 v_1+\epsilon^4 v_2\dots\]</div>
And we take $$\lambda$$ small: $$\lambda = \epsilon^2 \hat\lambda$$. Therefore, let's introduce notation to reduce the clutter ever so slightly: $$f^*$$ will indicate the function is around $$(U_0^*,V_0^*)$$. Then we obtain:
<div>\[
\begin{aligned}
\epsilon^2 \hat\lambda (u_0+\epsilon^2 u_1) &= \epsilon^2(u_0+\epsilon^2 u_1)_{xx}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^4)\\
\epsilon^2 \hat\lambda (v_0+\epsilon^2 v_1)&= (v_0+\epsilon^2 v_1+\epsilon^4 v_2)_{xx}+[-f_U^* -\epsilon^2f_{UU}^* U_1^*-\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[-f_V^* -\epsilon^2f_{VU}^* U_1^*-\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^4)\\
\end{aligned}
\]</div>
### Fast equations
Great, and there is of course the fast variant which we'll study first:
<div>\[
\begin{aligned}
\epsilon^2 \hat\lambda (u_0+\epsilon^2 u_1) &= (u_0+\epsilon^2 u_1)_{\xi\xi}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^4)\\
\epsilon^4\hat\lambda (v_0+\epsilon^2 v_1)&= (v_0+\epsilon^2 v_1+\epsilon^4 v_2)_{\xi\xi}+[-\epsilon^2f_U^* -\epsilon^4f_{UU}^* U_1^*-\epsilon^4f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[-\epsilon^2f_V^* -\epsilon^4f_{VU}^* U_1^*-\epsilon^4f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^6)\\
\end{aligned}
\]</div>
Let's start by studying the $$\mathcal O(1)$$ equations:
<div>\[
\begin{aligned}
0&= (u_0)_{\xi\xi}+f_U^*u_0+f_V^*v_0\\
0&= (v_0)_{\xi\xi}\end{aligned}
\]</div>
The second equation tells us $$v_0$$ is constant, the above tells us that via the Fredholm integrability condition, $$v_0$$ should in general be $$0$$. Then we're left with $$\mathcal L^*_0 u_0=0$$, so the translational eigenmode is the solution to the top equations $$u_0^*=AU_{0,\xi}^*$$. For convenience, set $$A=1$$ and we get $$u_0^*=U_{0,\xi}^*$$. The next order equations read:
<div>\[
\begin{aligned}
\epsilon^2 \hat\lambda u_0 &= \epsilon^2( u_1)_{\xi\xi}+f_U^*\epsilon^2 u_1+[ \epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)]u_0+\\
&+\epsilon^2 v_1f_V^*+[\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)]v_0\\
0&= (\epsilon^2 v_1)_{\xi\xi}-\epsilon^2f_U^*u_0-\epsilon^2f_V^* v_0
\end{aligned}
\]</div>
With the information that $$v_0=0$$, this becomes: 
<div>\[
\begin{aligned}
 \hat\lambda u_0 &= u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+ v_1f_V^*\\
0&= ( v_1)_{\xi\xi}-f_U^*u_0
\end{aligned}
\]</div>
Okay that's workable, we find something interesting, when the equation for $$v_1$$ is added to the equation for $$u_0$$, we get:
<div>\[
(u_0+v_1)_{\xi\xi}  =0\quad\implies \quad u_0=-v_1
\]</div>
if we ask our perturbations to have finite norm/be local (integration constant is zero, note we don't need this in further analysis). The intuition behind this is that to leading order, our perturbations "conserve" $$K$$ and stay on the line through the phase space, or in other words, to leading order, the perturbation is just the translational mode, in both $$u$$ and $$v$$. 
#### Is dit zo ja? 
Next we need one more order of $$v$$:
<div>\[\begin{aligned}
0&= v_{2,\xi\xi}-f_U^* u_1+[ -f_{UU}^* U_1^*-f_{UV}^* (K_1^*-U_0^*)]u_0-f_V^*v_1
\end{aligned}
\]</div>
Now, we find the fast jump by integrating $$v_{\xi\xi}$$ over the fast interval, which gives us:
<div>\[
\begin{aligned}
\Delta_{fast} v_{\xi}^*&=\int_\mathbb R v_{\xi\xi}d\xi= \int_\mathbb R v_0+\epsilon^2 v_1+\epsilon^4 v_2 d\xi+O(\epsilon^6) = \\
&=-\epsilon^2\int_\mathbb R u_{0,\xi\xi}d\xi+\epsilon^4\int_\mathbb R f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+f_V^*v_1 d\xi+O(\epsilon^6)
\end{aligned}
\]</div>
Note that $$u_{0}$$ is a heteroclinic orbit, so the integral its curvature is zero (it becomes flat on both ends). So the leading order expression for the fast jump is:
<div>\[
\begin{aligned}
\Delta_{fast} v_{\xi}^*&=\epsilon^4\int_\mathbb R [f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+f_V^*v_1 ]d\xi+O(\epsilon^6)
\end{aligned}
\]</div>
Note that we haven't used the expression for $$u_1$$ yet:
<div>\[
\hat\lambda u_0= u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+ f_V^*v_1
\]</div>
We can substitute the term in there and obtain:
<div>\[
\begin{aligned}
\Delta_{fast} v_{\xi}^*&=\epsilon^4\int_\mathbb R [\hat\lambda u_0-u_{1,\xi,\xi}]d\xi+O(\epsilon^6)
\end{aligned}
\]</div>
Hmm, what to do with this $$u_1$$ term? I'd like to reduce all this to:
<div>\[
\begin{aligned}
\Delta_{fast} v_{\xi}^*&=\epsilon^4\hat\lambda\int_\mathbb R  U_{0,\xi}^*d\xi+O(\epsilon^6)
\end{aligned}
\]</div>

### Stability
I haven't worked out the slow regime nicely yet, but we get the following intuition: The leading order behaviour of the slow jump should be a linear ODE with constant coefficients. Then to get bounded solutions, they should grow "towards" the front. If we ask a continuous solution, then a perturbation that is positive in the slow regime, should connect to the translational eigenmode and be positive in the fast regime too. This then tells us that the jump needs to be negative: we were going up, now we're going down. But meanwhile the expression above is only negative when $$\hat\lambda$$ is, hence our solution is stable!

Verder ook: de fast jump is $$O(\epsilon^4)$$, maar dat komt vooral omdat ik nu niet naar de dubbele hoedjes ben gegaan, eerder wat $$\hat{\hat v}$$ al order $$\epsilon^2$$, en dan was de jump dat zelf ook.



### Slow equations
Note: if we do perturbation on all terms, this seems to not work, which scares me a little, I should check that.
<div>\[
\begin{aligned}
\epsilon^2 \hat\lambda u &= \epsilon^2u_{xx}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)]u\\
&+[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)]v+\mathcal O(\epsilon^4)\\
\epsilon^2 \hat\lambda v&= v_{xx}+[-f_U^* -\epsilon^2f_{UU}^* U_1^*-\epsilon^2f_{UV}^* (K_1^*-U_0^*)]u\\
&+[-f_V^* -\epsilon^2f_{VU}^* U_1^*-\epsilon^2f_{VU}^* (K^*_1-U_0^*)]v+\mathcal O(\epsilon^4)\\
\end{aligned}
\]</div>
We find at leading order:
<div>\[
u = -\frac{f_V^*}{f_U^*}v+\mathcal O(\epsilon^2)
\]</div>
Now we add the equations and find:
<div>\[
\begin{aligned}
\epsilon^2 \hat\lambda u+\epsilon^2 \hat\lambda v &= \epsilon^2u_{xx}+v_{xx}
\end{aligned}
\]</div>
The second order derivative is simply:
<div>\[
u_{xx} = \frac{f_V^*}{f_U^*}v_{xx}
\]</div>
Is it??? Probably smooth enough, but seems wrong somehow.
Then to leading order we're left with:
<div>\[
\begin{aligned}
\epsilon^2\hat\lambda\frac{f_U^*-f_V^*}{f_U^*}  v &= v_{xx}
\end{aligned}
\]</div>
Then:
<div>\[
v = A\exp\left(\epsilon\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }x\right)+B\exp\left(-\epsilon\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }x\right)
\]</div>
Of course, on the left, $$B=0$$, and on the right, $$A=0$$. We'd like to have continuous solutions, $$v(x=0)=v(\xi=0)$$, so agreement between the fast and slow solutions at the origin. The leading order equation for $$v$$ in the fast region is $$\epsilon^2 v_1$$, where $$v_1=-u_0=-U^*_{0,\xi}$$. But we actually know what the translational mode is, it's plus or minus the square root of two times the potential term of the Hamiltonian. WLOG, let's assume the front goes from low $$U$$ to high $$U$$ as $$x$$ increases. Then $$U_{0,\xi}^*$$ is larger than $$0$$ for all 