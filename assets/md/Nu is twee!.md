
## Nu order 2 Slow

We now look at the slow system, where:
$$
\begin{aligned}
\hat\lambda \epsilon^2 \hat u =\epsilon^2 \hat u_{xx}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat v \\
\hat\lambda \epsilon^{2} \hat v = \hat v_{xx}- f_u^*(u^*_0,K_0^*)\hat u- f_v^*(u^*_0,K_0^*)\hat v 
\end{aligned}
$$
We find that:
Well we require the orders to match so let's substitute $\hat u=\epsilon^2 \hat{\hat u}$ (why u?? I guess to match $\hat v$) and $\hat v=\epsilon^2 \hat{\hat v}$. This doesn't really change the equations much:
$$
\begin{aligned}
\hat\lambda \epsilon^2 \hat{\hat u} =\epsilon^2 \hat{\hat u}_{xx}+f_u^*(u^*_0,K_0^*)\hat{\hat u}+f_v^*(u^*_0,K_0^*)\hat{\hat v} \\
\hat\lambda \epsilon^{2} \hat{\hat v} = \hat{\hat v}_{xx}- f_u^*(u^*_0,K_0^*)\hat{\hat u}- f_v^*(u^*_0,K_0^*)\hat{\hat v }
\end{aligned}
$$
Now we find:
$$
\hat{\hat u} =- \frac{f_v^*}{f_u^*}\hat{\hat v}+\mathcal O(\epsilon^2)
$$
Because of the constant coefficients, we also get $\hat{\hat u}_{xx}= - \frac{f_v^*}{f_u^*}\hat{\hat v}_{xx}$ (is this true? can't higher order terms have $O(\epsilon^-1)$ derivatives or something like that?)
Then we also find by adding the two equations:
$$
\hat{\hat v}_{xx} =\hat\lambda \epsilon^2(\hat{\hat u}+\hat{\hat v})-\epsilon^2 \hat u_{xx}=\hat\lambda\epsilon^2\frac{f_u^*-f_v^*}{f_u}\hat{\hat v^*}+ \epsilon^2\frac{f_v^*}{f_u^*}\hat{\hat v}_{xx}+\mathcal O(\epsilon^4)
$$
So we get:
$$
\hat{\hat v}_{xx}\left(1+\epsilon^2\frac{f_v^*}{f_u^*}\right) =\hat\lambda\epsilon^2\frac{f_u^*-f_v^*}{f_u}\hat{\hat v^*}+\mathcal O(\epsilon^4)
$$
Now we can just divide by this new term, and get the same expression as for $2<2$:
$$
\hat{\hat v}_{xx} =\hat\lambda\epsilon^2\frac{f_u^*-f_v^*}{f_u}\hat{\hat v^*}+\mathcal O(\epsilon^4)
$$


#### Nu order 2 fast
$$\begin{aligned}
\hat\lambda \epsilon^2 \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat v \\
\hat\lambda \epsilon^{2+2} \hat v = \hat v_{\xi\xi}-\epsilon^2 f_u^*(u^*_0,K_0^*)\hat u-\epsilon^2 f_v^*(u^*_0,K_0^*)\hat v 
\end{aligned}$$
So: $\hat v=\hat K+\mathcal O(\epsilon^2)$
Then we get the following system:
$$
\hat\lambda \epsilon^2 \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat K+\mathcal O(\epsilon^2) \\
$$
We expand $\hat u$ as: 
$$\hat u=\hat u_0+\epsilon^2\hat u_1$$
and $\hat K$ as $\hat K = \epsilon^2 \hat{\hat K}$, order 1 is not possible because of the solvability criterion (Appendix). 
And obtain at leading order:
$$
\hat u_{0,\xi\xi}+f_u^*(u_0^*,K_0^*)\hat u_0=0
$$
Which we recognize as the homogeneous fast reduced problem, to which $Au_{0,\xi}^*$ is the solution. For simplicity we set $A=1$ so we get $\hat u= u^*_{0,\xi}+\epsilon^2\hat u_1$ So we get at order $\epsilon^2$:
$$
\hat\lambda u^*_{0,\xi} = \hat u_{1,\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u_1+f_v^*(u^*_0,K_0^*)\hat{\hat K}+\mathcal O(\epsilon^{2}) \\
$$
Which is a homogeneous SL problem with again the same operator $\mathcal L=\partial_{\xi\xi}+f_u^*(u_0^*,K_0^*)$. The Fredholm alternative tells us that this equations has solutions which obey:
$$
\langle u_{0,\xi}^*, \hat\lambda  u^*_{0,\xi} -f_v^*(u^*_0,K_0^*)\hat{\hat K} \rangle =0
$$
Which gives:
$$
\hat{\hat K} = \hat\lambda \frac{\int_I (u_{0,\xi}^*(\xi))^2d\xi}{\int_I f_v^*(u_0^*(\xi),K_0^*)u_{0,\xi}^*(\xi)d\xi}
$$
Since $u_{0,\xi}^*(\xi)$ decays exponentially on both sides, the integrals converge and can be replaced by integrals over the entirety of $\mathbb R$. 


### Andere techniek voor fast jump? :)

$$
\begin{aligned}
\hat\lambda \epsilon^2 \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+\epsilon^{2}f_v^*(u^*_0,K_0^*)\hat{\hat v} \\
\hat\lambda \epsilon^{4} \hat{\hat v} = \epsilon^0 \hat{\hat v}_{\xi\xi}-\epsilon^0 f_u^*(u^*_0,K_0^*)\hat u- \epsilon^{2} f_v^*(u^*_0,K_0^*)\hat{\hat v }
\end{aligned}
$$
Again our favorite trick: we add the equations and get:
$$
\begin{aligned}
\hat\lambda \epsilon^2 \hat u +\hat\lambda \epsilon^{4} \hat{\hat v}= \hat u_{\xi\xi}+\epsilon^0 \hat{\hat v}_{\xi\xi}\end{aligned}
$$
We expand $\hat u$ and find:
$$
\begin{aligned}
\hat\lambda \epsilon^2 (u_{0,\xi}^*+\epsilon^2\hat u_1) +\hat\lambda \epsilon^{4} \hat{\hat v}= (u_{0,\xi}^*+\epsilon^2\hat u_1)_{\xi\xi}+\epsilon^0 \hat{\hat v}_{\xi\xi}\end{aligned}
$$
Integrating this equation, and using the fact that $u_{0,\xi}^0$ is a heteroclinic orbit, hence the derivatives go to zero for $\xi\to\pm \infty$, we find:
$$
\Delta_{fast} \hat{\hat v}_\xi=\begin{aligned}
\int\hat{\hat v}_{\xi\xi}d\xi=\epsilon^2\int \hat\lambda  u_{0,\xi}^*- \hat u_{1,\xi\xi}d\xi+\mathcal O(\epsilon^4)
\end{aligned}
$$
Note how the integral over the correction might have something to do with the interaction term! The difference in derivatives will be matched to $\lambda$, hence (possibly) connecting to the velocity of the wave too!

From [[Arjen Notes (my interpretation)#Fast linearized system]] we know that:
$$
\hat\lambda u^*_{0,\xi} = \hat u_{1,\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u_1+f_v^*(u^*_0,K_0^*)\hat{\hat K}+\mathcal O(\epsilon^{2}+\epsilon^{2\nu}) 
$$
As the order $\epsilon^2$ equation for $u$. Solving for $\hat u_1$ and inserting in the equation above then yields:
$$
\begin{aligned}
\Delta_{fast} \hat{\hat v}_\xi=\epsilon^2\int f_u^*(u^*_0,K_0^*)\hat u_1+f_v^*(u^*_0,K_0^*)\hat{\hat K}d\xi+\mathcal O(\epsilon^4)
\end{aligned}
$$
We get an integral condition on the fast jump, which we match to the square root business we found earlier. 

We get the same equation as Arjen, except the lambda term, but I think he forgot an $\epsilon^\nu$ there. :)



Probleem: integraal convergeert over het algemeen niet? :((
