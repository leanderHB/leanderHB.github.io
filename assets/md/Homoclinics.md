We start by slightly shifting $K$ and end up with $K+\delta$ with $\delta\ll 1$. Then we find the corrections to $U^\pm_{het},V^\pm_{het}$ as:
$$\begin{aligned}
U^\pm_{hom}=U^{\pm}_{het}+\delta \frac{f_V}{f_U}(U^\pm_{het},V^\pm_{het})\\
V^\pm_{hom}=V^\pm_{het}+\delta
\end{aligned}$$
Then the homoclinic Hamiltonian can be approximated (now for positive?? $\delta$):
$$
H_{hom}(U)=\int_{U^-_{hom}}^Uf(W, K+\delta-\epsilon^2 W)dW 
$$
Assuming for now that $\delta\ll \epsilon$, we can partially expand:
$$
H_{hom}(U)=\int_{U^{-}_{het}+\delta \frac{f_V^-}{f_U^-}}^Uf(W, K-\epsilon^2 W)+\delta f_V(W,K-\epsilon^2 W)dW 
$$
Which we can reduce to:
$$\begin{aligned}
H_{hom}(U)=H_{het}(U)+\int_{U^{-}_{het}+\delta \frac{f_V^-}{f_U^-}}^{U^{-}_{het}}f(W, K-\epsilon^2 W)dW\\
+\delta \int_{U_{het}^-}^U f_V(W,K-\epsilon^2 W)dW +\mathcal O(\delta^2)
\end{aligned}$$
but $f$ is close to zero, and will at most get to order $\delta$ as long as it stays $O(\delta)$ from $U_{het}^-$, so also this term can be neglected. So we're left with:
$$
\begin{aligned}
H_{hom}(U,\delta)=H_{het}(U)+\delta \int_{U_{het}^-}^U f_V(W,K-\epsilon^2 W)dW +\mathcal O(\delta^2)
\end{aligned}
$$
Now by similar argument we find that:
$$
\begin{aligned}
H_{hom}(U^+_{hom},\delta)&=H_{het}(U^+_{hom})+\delta \int_{U_{het}^-}^{U^+_{hom}} f_V(W,K-\epsilon^2 W)dW +\mathcal O(\delta^2)\\
&=\delta \int_{U_{het}^-}^{U^+_{het}} f_V(W,K-\epsilon^2 W)dW +\mathcal O(\delta^2)
\end{aligned}
$$
Cool, now we can estimate how far away the turning point of the homoclinic orbit is, by using a quadratic approximation of $H$ around $U^+_{hom}$. We find:
$$
H(U+\mu) = H(U)+\mu H_U(U)+\mu^2/2 H_{UU}(U)
$$
We know the value of $H(U)$ by above analysis, and know that $H_U$ there is zero (top of the peak), and we know that $H_{UU}=\partial_U f(U,K+\delta-\epsilon^2 U)$. So a leading order approximation of it is given by:
$$
H_{UU}=f_U(U^+_{het},V^+_{het})
$$
So then:
$$
H(U+\mu_0)=0\implies \mu_0 = \pm\sqrt{2\delta \frac{1}{f_U^+}\int_{U_{het}^-}^{U^+_{het}} f_V(W,K-\epsilon^2 W)dW }+\mathcal O(\delta)
$$
let's connect this to the rest of the theory to get an estimate of the width of the front:
$$
\epsilon^2 U_{xx}=f_U^+U
$$
is the equation close to the turning point. Then we solve it and find:
$$
U(x) = A\exp\left(\frac{\sqrt c}{\epsilon}x\right)+B\exp\left(-\frac{\sqrt c}{\epsilon}x\right)
$$
Solving for the initial conditions, we use $U(0)=\mu_0,U_x(0)=0$ and get:
$$
U(x) = \frac{\mu_0}{2}\left(\exp\left(\frac{\sqrt c}{\epsilon}x\right)+\exp\left(-\frac{\sqrt c}{\epsilon}x\right)\right)
$$
but the expression in brackets is actually a known quantity: the cosh. 
$$
U(x) = \mu_0\cosh\left(\frac{\sqrt c}{\epsilon}x\right)
$$
Let's find when $U(x)$ becomes order 1:
$$
\frac1{\mu_0} = \cosh\left(\frac{\sqrt c}{\epsilon}x\right)
$$
Solving for $x$:
$$
x=\frac{\epsilon}{\sqrt c}\cosh^{-1}\left(\frac1{\mu_0}\right)
$$
Since $\mu_0\ll 1$, we can approximate this by:
$$
x=\frac{\epsilon}{\sqrt c}\ln\left(\frac2{\mu_0}\right)
$$
Expanding the $\ln$:
$$
x=\frac{\epsilon}{\sqrt c}\left(\ln 2-\ln\mu_0\right)
$$
Of course, we know that $\ln 2\ll\ln\mu_0$, so to leading order, we get for the width:
$$
W=-\frac{2\epsilon}{\sqrt c}\ln\mu_0
$$
again tossing away non-leading terms, we then also get:
$$
W=-\frac{2\epsilon}{\sqrt c}\ln{\sqrt\delta}=-\frac{\epsilon}{\sqrt c}\ln{\delta}
$$
So then:
$$
\delta = \exp\left(-\frac{\sqrt c}{\epsilon }W \right)
$$
