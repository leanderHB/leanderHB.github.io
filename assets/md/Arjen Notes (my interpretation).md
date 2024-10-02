see [[Expanden rond the volledige oplossing]] for more. 

## Fast linearized system
$$\begin{aligned}
\hat\lambda \epsilon^\nu \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat v \\
\hat\lambda \epsilon^{\nu+2} \hat v = \hat v_{\xi\xi}-\epsilon^2 f_u^*(u^*_0,K_0^*)\hat u-\epsilon^2 f_v^*(u^*_0,K_0^*)\hat v 
\end{aligned}$$
So: $\hat v=\hat K+\mathcal O(\epsilon^2)$
Then we get the following system:
$$
\hat\lambda \epsilon^\nu \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat K+\mathcal O(\epsilon^2) \\
$$
We expand $\hat u$ as: 
$$\hat u=\hat u_0+\epsilon^\nu\hat u_1$$
and $\hat K$ as $\hat K = \epsilon^\nu \hat{\hat K}$, order 1 is not possible because of the solvability criterion (Appendix). 
And obtain at leading order:
$$
\hat u_{0,\xi\xi}+f_u^*(u_0^*,K_0^*)\hat u_0=0
$$
Which we recognize as the homogeneous fast reduced problem, to which $Au_{0,\xi}^*$ is the solution. For simplicity we set $A=1$ so we get $\hat u= u^*_{0,\xi}+\epsilon^\nu\hat u_1$ So we get at order $\epsilon^\nu$: (missen we niet een -$u_0$ term?)
$$
\hat\lambda u^*_{0,\xi} = \hat u_{1,\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u_1+f_v^*(u^*_0,K_0^*)\hat{\hat K}+\mathcal O(\epsilon^{2}+\epsilon^{2\nu}) \\
$$
(is error idd $O(\epsilon^2)$ ipv $O(\epsilon^{2-\nu}$?)
Which is a homogeneous SL problem with again the same operator $\mathcal L=\partial_{\xi\xi}+f_u^*(u_0^*,K_0^*)$. The Fredholm alternative tells us that this equations has solutions which obey:
$$
\langle u_{0,\xi}^*, \hat\lambda  u^*_{0,\xi} -f_v^*(u^*_0,K_0^*)\hat{\hat K} \rangle =0
$$
Which gives:
$$
\hat{\hat K} = \hat\lambda \frac{\int_I (u_{0,\xi}^*(\xi))^2d\xi}{\int_I f_v^*(u_0^*(\xi),K_0^*)u_{0,\xi}^*(\xi)d\xi}
$$
Since $u_{0,\xi}^*(\xi)$ decays exponentially on both sides, the integrals converge and can be replaced by integrals over the entirety of $\mathbb R$. 

## Slow linearized system
We now look at the slow system, where:
$$
\begin{aligned}
\hat\lambda \epsilon^\nu \hat u =\epsilon^2 \hat u_{xx}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat v \\
\hat\lambda \epsilon^{\nu} \hat v = \hat v_{xx}- f_u^*(u^*_0,K_0^*)\hat u- f_v^*(u^*_0,K_0^*)\hat v 
\end{aligned}
$$
We find that:
Well we require the orders to match so let's substitute $\hat u=\epsilon^\nu \hat{\hat u}$ (why u?? I guess to match $\hat v$) and $\hat v=\epsilon^\nu \hat{\hat v}$. This doesn't really change the equations much:
$$
\begin{aligned}
\hat\lambda \epsilon^\nu \hat{\hat u} =\epsilon^2 \hat{\hat u}_{xx}+f_u^*(u^*_0,K_0^*)\hat{\hat u}+f_v^*(u^*_0,K_0^*)\hat{\hat v} \\
\hat\lambda \epsilon^{\nu} \hat{\hat v} = \hat{\hat v}_{xx}- f_u^*(u^*_0,K_0^*)\hat{\hat u}- f_v^*(u^*_0,K_0^*)\hat{\hat v }
\end{aligned}
$$
Now we find:
$$
\hat{\hat u} =- \frac{f_v^*}{f_u^*}\hat{\hat v}+\mathcal O(\epsilon^\nu)
$$
Then we also find by adding the two equations:
$$
\hat{\hat v}_{xx} =\hat\lambda \epsilon^\nu(\hat{\hat u}+\hat{\hat v})+\mathcal O(\epsilon^2)=\hat\lambda\epsilon^\nu\frac{f_u^*-f_v^*}{f_u}\hat{\hat v^*}+\mathcal O(\epsilon^2+\epsilon^{2\nu})
$$
To have localized solutions we require 
$$
\hat\lambda\frac{f_u^*-f_v^*}{f_u^*}>0
$$
Since existence of fronts requires $f_u<0$, this implies that for positive (unstable) $\lambda$, we need, $f_u^*>f_v^*$. Trace determinant analysis of the plateaus shows that this is the case for stable fronts (plateaus?). So small, positive lambda are possible here, so let's carry on in our analysis.

To leading order then, the equations are given by:
$$
\hat{\hat v}(x) = A_\pm\exp\left(\mp \epsilon^{\nu/2}x\sqrt{\frac{f_u^*-f_v^*}{f_u^*}} \right)
$$
By continuity: 
$$\hat{\hat v}(0)=A_\pm=\hat{\hat K}=\hat\lambda \frac{\int_I (u_{0,\xi}^*(\xi))^2d\xi}{\int_I f_v^*(u_0^*(\xi),K_0^*)u_{0,\xi}^*(\xi)d\xi}$$
Changing to the fast coordinate:
$$
\hat{\hat v}(\xi) = \hat{\hat K}\exp\left(\mp \epsilon^{1+\nu/2}\xi\sqrt{\frac{f_u^*-f_v^*}{f_u^*}} \right)
$$
Then the derivative at zero equals:
$$
\hat{\hat v}_\xi(\xi) = \mp\hat{\hat K} \epsilon^{1+\nu/2}\sqrt{\frac{f_u^*-f_v^*}{f_u^*}} 
$$
Hence the slow jump is of order $O(\epsilon^{1+\nu/2})$.



### Little intermezzo
We can write the fast equations:
$$
\begin{aligned}
\hat\lambda \epsilon^\nu \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+\epsilon^{\nu}f_v^*(u^*_0,K_0^*)\hat{\hat v} \\
\hat\lambda \epsilon^{2\nu+2} \hat{\hat v} = \epsilon^\nu \hat{\hat v}_{\xi\xi}-\epsilon^2 f_u^*(u^*_0,K_0^*)\hat u- \epsilon^{2+\nu} f_v^*(u^*_0,K_0^*)\hat{\hat v }
\end{aligned}
$$
So we have:
$$
\hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u=\mathcal O(\epsilon^{\nu})=-\epsilon^{\nu}(f_v^*(u^*_0,K_0^*)\hat{\hat v} -\hat\lambda \hat u)
$$
Integrating, we find:
$$
\int \hat u_{\xi\xi}(\xi)+f_u^*(u^*_0(\xi),K_0^*)\hat u(\xi)d\xi=-\int \epsilon^{\nu}(f_v^*(u^*_0,K_0^*)\hat{\hat v} -\hat\lambda \hat u)=\mathcal O(\epsilon^\nu)
$$
Where we assume that $\int \hat{\hat v}$ and $\int \hat u$ converge ($L^2$ doesn't imply this, needs argument, I guess we have leading order behaviour in slow, where they go to zero! So they are integrable? Width is $\mathcal O(1)$ in fast, so this should be enough, needs to be worked out $L^2$ and ).
Since $\int \hat u_{\xi\xi}=\lim_{L\to \infty} \hat u_\xi(L)-\hat u_\xi(-L)$, this term is zero, hence  
$$\int f_u^*(u^*_0(\xi),K_0^*)\hat u(\xi)d\xi=O(\epsilon^\nu)$$
Using the expansion of $\hat u$, this becomes
$$\int f_u^*(u^*_0(\xi),K_0^*)u^*_0(\xi)d\xi=O(\epsilon^\nu)$$
again assuming $\hat u_1$ is integrable.
## Fast jump
$$
\epsilon^\nu \hat{\hat v}_{\xi\xi}=\hat\lambda \epsilon^{2\nu+2} \hat{\hat v}+\epsilon^2 f_u^*(u^*_0,K_0^*)\hat u+ \epsilon^{2+\nu} f_v^*(u^*_0,K_0^*)\hat{\hat v } 
$$
Or dividing by $\epsilon^\nu$, this turns into:
$$
\hat{\hat v}_{\xi\xi}=\hat\lambda \epsilon^{2+\nu} \hat{\hat v}+\epsilon^{2-\nu} f_u^*(u^*_0,K_0^*)\hat u+ \epsilon^{2} f_v^*(u^*_0,K_0^*)\hat{\hat v } 
$$
Integrating over the fast interval, we find:
$$
\Delta_{fast}\hat{\hat v}_\xi = \int\hat\lambda \epsilon^{2+\nu} \hat{\hat v}+\epsilon^{2-\nu} f_u^*(u^*_0,K_0^*)\hat u+ \epsilon^{2} f_v^*(u^*_0,K_0^*)\hat{\hat v } d\xi = \mathcal O(\epsilon^2)
$$
Hmm, so to match orders, we require $\nu = 2$, and then everything becomes a mess... [[Nu is twee!]]


# Appendices
## K order 1
We have the following system:
$$
\hat\lambda \epsilon^\nu \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat K+\mathcal O(\epsilon^2) \\
$$
We expand $\hat u$ as: 
$$\hat u=\hat u_0+\epsilon^\nu\hat u_1$$
Then we get at leading order:
$$
\hat u_{0,\xi\xi}+f_u^*(u_0^*,K_0^*)\hat u_0=-f_v^*(u_0^*,K_0^*)\hat K
$$
Solvability: 
$$
\hat K\langle u_{0,\xi}^* ,f_v^*(u_0^*,K_0^*)\rangle=\hat K\int_I f_v^*(u_0^*(\xi),K_0^*)u_{0,\xi}^*(\xi)d\xi = 0
$$
If we assume $f$ to be such that the inner product is non-zero, this shows that we need $\hat K=0$. 
