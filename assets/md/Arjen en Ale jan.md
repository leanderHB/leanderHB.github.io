- heel kort hoe van PDE naar existence steady state
- neem aan dat steady state, dan lineariseer een groeiende mode eromheen

$$
\begin{aligned}
U_t &= \epsilon^2 U_{xx}+f(U,V)\\
V_t &= V_{xx}-f(U,V)\\
\end{aligned}
$$
In steady state:
$$
\begin{aligned}
0 &= \epsilon^2 U_{xx}+V_{xx}\\
\end{aligned}
$$
So: $V = \eta_0-\epsilon^2U$ in steady state ($\eta_0$ is constant of integration). Then:
$$
0=\epsilon^2U_{xx}+f(U,\eta_0-\epsilon^2U):=\epsilon^2U_{xx}+g(U)
$$
So a Hamiltonian system in $U$. 



When do we get front solutions? Heteroclinics of $\epsilon^2U_{xx}+g(U)=0$. Writing $F'(U)=\epsilon^{-2} g(U)$ we get the Hamiltonian form:
$$
\frac12 (U_x)^2+F(U(x))=E\quad\forall x\\
$$
If we can find an $E$ and $U_+\not =U_-$ such that $F(U_+)=F(U_-)=E$, $F_U(U_+)=F_U(U_-)=0$ and $F((U_-,U_+))\subseteq [L,E)$ for some $L$ smaller than $E$, we can expect a front solution.  



When we have a steady state front: $(\bar U,\bar V)$, we can linearize around it to find its stability. Write:
$$
U = \bar U+\epsilon\exp(\lambda t)u+O(\epsilon^2),\,\,V = \bar V+\epsilon\exp(\lambda t)v +O(\epsilon^2)
$$
Noting that $U_{xx}=O(\epsilon^{-2})$ we find to leading order the steady state equations:
$$
\begin{aligned}
0 &= \epsilon^2 \bar U_{xx}+f(\bar U,\bar V)\\
0 &=\bar V_{xx}-f(\bar U,\bar V)\\
\end{aligned}
$$
And the next order equations read:
$$
\begin{aligned}
\lambda u &= \epsilon^2 u_{xx}+f_U(\bar U,\bar V)u+f_V(\bar U,\bar V)v\\
\lambda v &= v_{xx}-f_U(\bar U,\bar V)u-f_V(\bar U,\bar V)v\\
\end{aligned}
$$




Introduce a fast variable $x=\epsilon\xi$:
$$
\begin{aligned}
\lambda u &=  u_{\xi\xi} + f_U(\bar U,\bar V)u+f_V(\bar U,\bar V)v\\
\epsilon^2\lambda v &=  v_{\xi\xi} - \epsilon^2f_U(\bar U,\bar V)u-\epsilon^2f_V(\bar U,\bar V)v
\end{aligned}
$$
So we find that $v(\xi) = v_0+\epsilon^2v_2(\xi)$, choose $v = 1+\epsilon^2v_2$, we can use this to find:
$$
\lambda u =  u_{\xi\xi} + f_U(\bar U,\bar V)u+f_V(\bar U,\bar V)
$$
An inhomogeneous Sturm-Liouville problem:
$$
u =  (\mathcal L-\lambda)^{-1}f_V(\bar U,\bar V)
$$
With $\mathcal L = \partial_{\xi\xi}+f_U(\bar U,\bar V)$. Since $\mathcal L$ is the operator corresponding to a heteroclinic with translational symmetry, it has an eigenvalue zero corresponding to shifts, so $\mathcal L \bar U_{\xi}=0$, but $U_\xi$ has strictly one sign, so $0$ is the largest eigenvalue of $\mathcal L$. So for growing modes ($\lambda>0$), this defines $u$. 



We split space into two outer layers and one boundary layer: $I_f=[-\sqrt{\epsilon},\sqrt{\epsilon}]$, fast variable $\xi = x/\epsilon$, then in the fast coordinate, the boundary layer is $[-1/\sqrt\epsilon,1/\sqrt\epsilon]$, so in the limit of $\epsilon\to0$, this becomes the whole line. 
![[Pasted image 20240401171104.png]]



In the slow subsystems, to leading order (here $\bar U,\bar V$ are constant):
$$
\begin{aligned}
\lambda u&=f_U(\bar U,\bar V)u+f_V(\bar U,\bar V)v\\
\lambda v &=  v_{xx} -f_U(\bar U,\bar V)u-f_V(\bar U,\bar V)v\\
\end{aligned}
$$
denote $f_{U,l},f_{V,l}$ as the derivatives on the left side and similarly the right side are $f_{U,r},f_{V,r}$. Here, $u$ is determined in terms of $v$, so we can do a bit of calculus and find that at $\xi=\pm1/\sqrt\epsilon$, we have:
$$
v_{\xi}(\xi=\pm1/\sqrt\epsilon)=\mp\epsilon \sqrt{\lambda +\frac{\lambda f_{V,r/l}}{\lambda-f_{U,r/l}}}+O(\epsilon^{5/2})
$$
Now we can match this to the inner solution. 




$$
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon }v_{\xi\xi}d\xi = v_\xi(1/\sqrt\epsilon)-v_\xi(-1/\sqrt\epsilon) = -\epsilon \sqrt{\lambda +\frac{\lambda f_{V,r}}{\lambda-f_{U,r}}}-\epsilon \sqrt{\lambda +\frac{\lambda f_{V,l}}{\lambda-f_{U,l}}}
$$
Note that:
$$
\begin{aligned}
v_{\xi\xi}=\epsilon^2\lambda +\epsilon^2f_U(\bar U,\bar V)u_{inner}+\epsilon^2f_V(\bar U,\bar V) 
\end{aligned}
$$
Then we find:
$$
\int_{I}r_{\xi\xi}d\xi = \epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[\lambda +f_U(\bar U,\bar V)u_{inner}+f_V(\bar U,\bar V)]d\xi\\
$$




Some algebra shows that $\epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}\lambda d\xi=2\epsilon^{3/2}\lambda$ cannot match the order of the slow timescale so we put those away in the higher order terms.
$$
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_U(\bar U,\bar V)u_{inner}+f_V(\bar U,\bar V)]d\xi= -\frac{\sqrt\lambda}{\epsilon} \left(\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}+\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}\right)
$$


After a small discussion, we agree that the interactions are weak: only the exponential tails interact. 



![[Pasted image 20240409141447.png]]

