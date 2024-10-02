Here, I'll try to find a similar result as in DV_JDDE for heteroclinic orbits.
### Lemma Lea
Consider the problem $v_{xx}+f(v)=0$. We know this is a Hamiltonian problem with Hamiltonian $H=(v_x)^2+ F(v)$, where $F'=f$. Then if there are two distinct $v_-,v_+$, such that $f(v_\pm)=0$, $\rho_\pm:=f_v(v_\pm)\not=0$ and $F(v_-)=F(v_+)$, and also $F(v)< F(v_-)$ for all $v\in (v_-,v_+)$, then there exists a heteroclinic orbit between $v_-$ and $v_+$, with exponential decay towards the saddles with rates $\sqrt{\rho_\pm}$. Moreover, we can explicitly write down first order ODE's for this solution as:
$$
(v_h)_x = \pm\sqrt{2F(v_-)-2F(v)}
$$

Proof: WLOG, assume $v_-<v_+$. Note that the Hamiltonian $H$ is conserved under the ODE. So solutions must lie on curves parameterized by:
$$
(v_h)_x = \pm\sqrt{2E-2F(v)}
$$
Note that at $(v_\pm,0)$, we have fixed points, since we have $f(v_\pm)=0$. Since we require $F(v)<F(v')$ for all the points between $v_-$ and $v_+$, the smoothness of $f$ tells us that $\rho_\pm<0$. Then, these fixed points are saddles, and hence have a stable and unstable manifold. A heteroclinic then would exists when the unstable manifold of $v_-$ coincides with the stable manifold of $v_+$, or vice versa. I claim this is the case for our system. Let's start on the unstable manifold of $v_-$, the one going out in positive $v$-direction. Then we're on the $(v_h)_x = \sqrt{2F(v_-)-2F(v)}$ branch. Now, we can't have a fixed point anywhere before we end up at $v_+$, since the square root is a strictly positive number for $v<v_+$ here, and the monotonicity guarantees we don't get stuck somewhere between the saddles. As $v$ tends to $v_+$, which it will inevitably do (since it can't go anywhere else, but this needs a slight restriction on $F$ or $f$, easiest to require one minimum of $F$, but I'd like to find a slightly broader definition), the curve will get closer and closer to the stable manifold of $v_+$. The continuity in $v$ of the parametrization then guarantees we can only have that the stable manifold of $v_+$ overlaps with the unstable one of $v_-$. 

### Corollory Lea
Width is $O(\epsilon)$ under certain conditions: namely, the other extrema can't be too high. Let's say we get $\epsilon$ away from the saddles, call it $V_\pm = v_\mp\pm \epsilon$. Estimate of length:
$$
L =\int dx = \int \sqrt{F(v_-)-F(u)} du \leq \int \max\{\rho_\pm\} \epsilon du = O(\epsilon)
$$
If $v_{xx}=\frac{1}{\epsilon^2}f(x)$ and the other extrema of $F$ are $O(1)$ lower than the ones at $v_\pm$, the width of the front is $O(\epsilon)$. 
proof: Define the width of the front as the time it spends more than $\epsilon$ away from the saddles. Then at $v=v_-+\epsilon$, the function $F$ is $\rho_-\epsilon$ below $F(v_-)$ at leading order. 

tbd, zie 2.3.3 uit Spectral Stability. 

### Lemma 3.2
Let $v_h$ be a solution to $v_{xx}+f(v)=0$ which is heteroclinic to $(v_-,0)$ to $(v_+,0)$. Denote $\rho_- =f_v(v_-),\rho_+=f_v(v_+)$. Then the linear stability problem:
$$
\mathcal Lu=u_{xx}+f_v(v_h)u=\lambda u
$$
is an eigenvalue problem with the following properties:
(i) There is a finite amount of real eigenvalues $0=\lambda_0>\lambda_1>\dots \lambda_J>\rho=\max\{\rho_-,\rho_+\}$. 
(ii) The associated eigenfunctions $w_i$ to $\lambda_i$ have $i$ distinct, simple zeros. Moreover, $w_0=(v_h)_x$. 
(iii) The eigenfunctions can be normalized and then $\langle w_i,w_j\rangle=\delta_{i,j}$. Moreover, we have:
$$
w_i\sim 1\cdot \exp(-\sqrt{\lambda-\rho_+ }x)\quad \text{as }x\to\infty
$$
(iv) The spectrum is $\sigma = (-\infty,\rho)\cup \sigma_p$.
(v) For every $\lambda\not\in\sigma$, the problem is invertible, and we have two solutions:
$$\begin{aligned}
w^R_\lambda&\sim 1\exp(-\sqrt{\lambda-\rho_+})\quad\text{as }x\to\infty\\
w^L_\lambda&\sim 1\exp(\sqrt{\lambda-\rho_-})\quad\text{as }x\to-\infty
\end{aligned}$$
Moreover the solution space is spanned by $\{w^L_\lambda,w^R_\lambda\}$

Proof:
(i,ii) our heteroclinic orbit decays exponentially to the saddles as $x\to\pm\infty$, therefore we can apply theorem 2.3.2 from "Spectral and Dynamical stability of Nonlinear waves", and find:
$\rho$-weighed inner product is just the normal inner product, since there's no $v_x$-term. So:
- $\mathcal L$ is self-adjoint
- we get: $\lambda_0>\lambda_1>\dots \lambda_J>\rho_0=\max\{f_v(v_-),f_v(v_+)\}$. 
- the eigenfunctions $u_i$ belonging to $\lambda_i$ are orthonormal, and have $i$ simple zeros. 
Then, the goldstone (or translational) mode $(v_h)_x$ related to the translational symmetry. will have eigenvalue $0$, and since it's equal to the square root of some quantity (see Lemma Lea), $(v_h)_x$ is therefore of one sign, so it's the eigenfuction with no zeros, so $w_0$.
(iii) The eigenfunction $w_i$ is a bounded solution, which obeys the limiting ODE on both sides, hence has this decay behaviour. 
(iv) tbd, chapter 3 in Spectral and dynamical stability, for example page 65
(v) Note that the left and right reduced problems have a limiting behaviour that is explicit:
$$
\omega^{L/R}(x)\sim \exp(\pm\sqrt{\lambda-\rho_{\mp}}x)\quad\text{as }x\to\mp\infty
$$
Then by uniqueness of solutions, we can extend these to find the complete $w^{L/R}$. 
How do we know they span the space? Well by Abels theorem, a fundamental matrix solution should not become a singular matrix somewhere! So if two solutions span $\mathbb R^2$ for some $x$, then they will for all $x$! (but are they separated? so do they decay nicely? I dunno, should check)

### Lemma 3.3
A short version is: $W(\lambda)$ has simple poles at the eigenvalues of the problem. 
Proof: At eigenvalues $\lambda_i$, $w^R$ and $w^L$ collapse onto $w_i$, hence the columns in the Wronskian become linearly dependent. Hence the determinant becomes zero. The simpleness follows from a Taylor expansion: 

Expand in $\lambda$:
$$
w^R_{\lambda_i+\delta} = w_i+\delta u+R
$$
Insert into fast linear problem:
$$
(\mathcal L-(\lambda_i+\delta) )w:=w_{xx}+(f_U-(1+\lambda))w=0
$$
We know that $w_i$ is an eigenvalue, so it solves the equation, so that leaves us with:
$$
(\mathcal L-\lambda_i)u=w_i
$$
at order $\delta$. We write $u = cw_i$, and obtain:
$$
(\partial_{x}^2+(f_U-(1+\lambda_i)))cw_i=w_i
$$
we apply the product rule twice to obtain:
$$
c''w_i+2c'w_i'+c(\mathcal L-\lambda_i)w_i=w_i
$$
Using the fact that $w_i$ is an eigenvector, we then obtain:
$$
c''w_i+2c'w_i' = w_i
$$
a solution to this is:
$$
c' = \frac{1}{w_i^2}\left(\int_0^\xi w_i^2(\eta)d\eta+c_1\right)
$$
Where $c_1$ is a constant of integration: Check by filling in. 
Then, let's study the behaviour of $c'$ by the limiting behaviour. Up to this point, the analysis was true for both $w^{L/R}$. Now we fix $w^R$. Then we take the limit as $x\to \delta^{-\alpha}$, or maybe some other exponent, I should check that! (Poincare expansion theorem shenanigans)
Then, from the previous Lemma, we know:
$$
w_i\sim \exp(\mp\sqrt{\lambda_i-\rho_\pm}x) \quad\text{as }x\to\mp \delta^{-\alpha}
$$
Good, then we know $w^R$ should decay in positive direction, let's use that. 
$$
c'\sim \exp(2\sqrt{\lambda_i-\rho_+}x)\left[\int_0^{\delta^{-\alpha}} w_i^2(\eta)d\eta -\int_0^{\infty} w_i^2(\eta)d\eta+\int_0^{\infty} w_i^2(\eta)d\eta+c_1 \right]
$$
Then:
$$
c'\sim \exp(2\sqrt{\lambda_i-\rho_+}x)\left[ -\int_{\delta^{-\alpha}}^{\infty} w_i^2(\eta)d\eta+\int_0^{\infty} w_i^2(\eta)d\eta+c_1 \right]
$$
We have a leading order expression for the first integral, which gives:
$$
c'\sim \exp(2\sqrt{\lambda_i-\rho_+}x)\left[ \int_0^{\infty} w_i^2(\eta)d\eta+c_1 \right]-\frac{1}{2\sqrt{\lambda_i-\rho_+}}
$$
We know that $w^R$ decay, and that $w^R=cw_i$, so $c'$ can grow at most at $\sqrt{\lambda_i-\rho_+}$, so that means that:
$$
\left[ \int_0^{\infty} w_i^2(\eta)d\eta+c_1 \right] = 0
$$
And therefore:
$$
c_1 = -\int_0^{\infty} w_i^2(\eta)d\eta
$$
We use this to get:
$$
c' = -\frac{1}{w_i^2}\int_\xi^\infty w_i^2(\eta)d\eta
$$
#### Left side
Now let's do the same for $w^L$, so define $w^L = dw_i$. Then using the same reasoning, we get:
$$
d' = \frac{1}{w_i^2}\left(\int_0^\xi w_i^2(\eta)d\eta+d_1\right)
$$
We again want to find $d_1$. We use a similar reasoning, now to the left. 
$$\begin{aligned}
d'\sim \exp(2\sqrt{\lambda_i-\rho_-}x)\left[\int_0^{-\delta^{-\alpha}} w_i^2(\eta)d\eta +\int_{-\infty}^{0} w_i^2(\eta)d\eta-\int_{-\infty}^{0} w_i^2(\eta)d\eta+d_1 \right]\\
=\exp(2\sqrt{\lambda_i-\rho_-}x)\left[\int_{-\infty}^{-\delta^{-\alpha}} w_i^2(\eta)d\eta-\int_{-\infty}^{0} w_i^2(\eta)d\eta+d_1 \right]
\end{aligned}$$
Again the scaling argument shows that:
$$
d_1 =\int_{-\infty}^{0}w_i^2(\eta)d\eta
$$
And hence:
$$
d'=\frac{1}{w_i^2}\int_{-\infty}^\xi w_i^2(\eta)d\eta
$$
Now we have leading order expressions for $w^L$ and $w^R$, we can find a leading order expression of the wronskian! To do: treat error terms nicely, again this magical Poincare thm.
We get at leading order:
$$
\begin{aligned}
w^R &= w_i(1+\delta c)\\
w^L &= w_i(1+\delta d)\\
(w^R)' &= w_i'(1+\delta c)+\delta w_i c'\\
(w^L)' &= w_i'(1+\delta d)+\delta w_i d'
\end{aligned}
$$
Now we calculate the wronskian:
$$\begin{aligned}
W(\lambda_i+\delta) &= -w^R(w^L)'+w^L(w^R)'\\
&=-w_i(1+\delta c)(w_i'(1+\delta d)+\delta w_i d')+w_i(1+\delta d)(w_i'(1+\delta c)+\delta w_i c')\\
&=w_iw_i'-w_i w_i'-\delta ( w_i d w_i'+w_i^2d'+w_icw_i'-w_iw_i'c-w_i^2c'-w_idw_i')\\
&=-\delta w_i^2 (d'-c') = -\delta \|w_i\|^2_2
\end{aligned}$$
Here we used that:
$$
d'-c' = \frac{1}{w_i^2}\int_{-\infty}^\xi w_i^2(\eta)d\eta+\frac{1}{w_i^2}\int_\xi^\infty w_i^2(\eta)d\eta=\frac{1}{w_i^2}\|w_i\|^2_2
$$
Amazing :) Apparently the even functions aren't needed here! I'm just missing the $(-1)^i$ term, which I think is just reasoned into the derivation by continuity?  

### Lemma 3.5
The inhomogeneous problem has a bounded solution given by:
$$
v_{in}=A^Lw^L+A^Rw^R
$$
Where:
$$
A^{R/L} = A^{R/L}(0)\mp \frac{1}{W(\lambda)}\int_0^x G_U w^{L/R} dy
$$
proof:
In terms of the wiki on variation of constants, with $n=2$:
$$
w^{(2)}+\alpha_0 w^{(0)} = b
$$
where:
$$\alpha_0 =(G_V-1+\lambda)$$
and 
$$
b = G_U
$$
Then we get:
$$
W^A = \begin{vmatrix}
0&w^L\\ G_U&\partial_\xi w^L
\end{vmatrix}
$$
$$
W^B = \begin{vmatrix}
w^R&0\\ \partial_\xi w^R&G_U
\end{vmatrix}
$$
So:
$$
A' = \frac{W^A}{W(\lambda)} = -\frac{G_Uw^L}{W(\lambda)}
$$
and:
$$
B' = \frac{W^B}{W(\lambda)} = \frac{G_Uw^R}{W(\lambda)}
$$
Relabel $A\to A^R$ and $B\to A^L$ and integrate to get:
$$
A^{R/L} = A^{R/L}(0)\mp \frac{1}{W(\lambda)}\int_0^x G_U w^{L/R} dy
$$
If we want solutions to be bounded, we require $A^L$ to become small when $x\to \infty$, and $A^R$ to be small when $x\to-\infty$. Then we require:
$$
\lim_{x\to\infty} A^{R/L}(x) = A^{R/L}(0)\mp \frac{1}{W(\lambda)}\int_0^{\mp \infty} G_U w^{L/R} dy = 0
$$
So then: 
$$
A^R(0) = -\frac{1}{W(\lambda)}\int_{-\infty}^0G_U w^L dy
$$
and:
$$
A^L(0) = -\frac{1}{W(\lambda)}\int_{0}^\infty G_U w^R dy
$$
putting it all together, we find:
$$
A^{R} = - \frac{1}{W(\lambda)}\int_{-\infty}^x G_U w^{L} dy
$$
and:
$$
A^{L} = - \frac{1}{W(\lambda)}\int_x^\infty G_U w^{R} dy
$$
Combining these, we get:
$$
v_{in} = - \frac{w^L}{W(\lambda)}\int_x^\infty G_U w^{R} dy-\frac{w^R}{W(\lambda)}\int_{-\infty}^x G_U w^{L} dy
$$
### Lemma 3.6
Close to the zeros of $W(\lambda)$, we get the leading order approximation of $v_{in}$:
$$
v_{in} = -\frac{w_i}{W(\lambda_i)}\int_{-\infty}^\infty G_U w_i dy+O(1)
$$
Proof:
We have leading order approximations of $w^R$ and $w^L$, which are:
$$
\begin{aligned}
w^R &= w_i(1+\delta c)\\
w^L &= w_i(1+\delta d)
\end{aligned}
$$
Filling these in, we find:
$$
v_{in} = - \frac{w_i(1+\delta d)}{W(\lambda)}\int_x^\infty G_U w_i(1+\delta c) dy-\frac{w_i(1+\delta c)}{W(\lambda)}\int_{-\infty}^x G_U w_i(1+\delta d) dy
$$
Neglecting terms of order $1$, we then get:
$$
v_{in} = -\frac{w_i}{W(\lambda)}\int_{-\infty}^\infty G_U w_i dy+O(1)
$$
as a leading order approximation of $v_{in}$. 

### Filling in
Remember our integral condition on $\lambda$:
$$
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_U(\bar U,\bar V)u_{inner}+f_V(\bar U,\bar V)]d\xi= -\frac{\sqrt\lambda}{\epsilon} \left(\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}+\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}\right)
$$
We fill in $u_{inner}$ according to what we just found, around $\lambda=0$:
$$
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[-f_U(\bar U,\bar V)\frac{w_0}{W(\lambda)}\int_{-\infty}^\infty (f_U-\epsilon^2f_V) w_0 dy+f_V(\bar U,\bar V)]d\xi= -\frac{\sqrt\lambda}{\epsilon} S
$$
Lovely, the inner integral is a constant, so we can just get it out of there. Since $W(\lambda)\sim\lambda$, the second term is not leading order close to $\lambda=0$, so we toss it. 
$$
\frac{1}{W(\lambda)}\int_{-\infty}^\infty (f_U-\epsilon^2f_V) w_0 d\xi \int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}f_Uw_0d\xi= -\frac{\sqrt\lambda}{\epsilon} S
$$
So to leading order in $\epsilon$, we have:
$$
-\frac{1}{W(\lambda)}\left(\int_{-\infty}^{\infty}f_Uw_0d\xi\right)^2=-\frac{\sqrt\lambda}{\epsilon} S
$$
here, we assume that $w_0$ decays fast enough to replace the integrals to leading order. Which is fair, since the heteroclinic orbit has exponential tails, so also its derivative has exponential tails. 
So, the stability is given by the sign of $W(\lambda)$. If $W(\lambda)>0$ for $\lambda>0$, we have instability. 

However, by a counting argument, we can show that this can't happen! The limiting behaviour for large $\lambda$ is given by the following lemma:
### Lemma 3.4
We have that the limiting behaviour for large $\lambda$ is $W(\lambda)\sim -2\sqrt{\lambda}$, hence by counting zeros and the insight that $W(\lambda)=0$ for the eigenvalues only (book and lemma 3.2), we find that the wronskian is negative for positive $\lambda$. Hence, the system is unconditionally stable (under the right assumptions haha).


# Vragen
moet $\nu$ hetzelfde zijn aan beide kanten? Voelt veel meer restrictive dan nodig.
![[Pasted image 20240523124733.png]]
Wat is poincare expansion theorem? 
![[image001.png]]
![[image002.png]]


hoe krijg je de $(-1)^i$ voor $w^L$? 
