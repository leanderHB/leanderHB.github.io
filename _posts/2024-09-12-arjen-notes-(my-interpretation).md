---
layout: post
title: "Arjen Notes (my interpretation)"
date: 2024-09-12
---
<style>
.math-container {
    max-width: 100%; /* Set a maximum width to prevent it from expanding the page */
    overflow-x: auto; /* Enable horizontal scrolling */
    white-space: nowrap; /* Prevent the text from wrapping */
}
</style>
see [Expanden rond the volledige oplossing]({% link _posts/2024-06-25-expanden-rond-the-volledige-oplossing.md %}) for more. 

## Fast linearized system
<div class="math-container">\[\begin{aligned}
\hat\lambda \epsilon^\nu \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat v \\
\hat\lambda \epsilon^{\nu+2} \hat v = \hat v_{\xi\xi}-\epsilon^2 f_u^*(u^*_0,K_0^*)\hat u-\epsilon^2 f_v^*(u^*_0,K_0^*)\hat v 
\end{aligned}\]</div>
So: $$\hat v=\hat K+\mathcal O(\epsilon^2)$$
Then we get the following system:
<div class="math-container">\[
\hat\lambda \epsilon^\nu \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat K+\mathcal O(\epsilon^2) \\
\]</div>
We expand $$\hat u$$ as: 
<div class="math-container">\[\hat u=\hat u_0+\epsilon^\nu\hat u_1\]</div>
and $$\hat K$$ as $$\hat K = \epsilon^\nu \hat{\hat K}$$, order 1 is not possible because of the solvability criterion (Appendix). 
And obtain at leading order:
<div class="math-container">\[
\hat u_{0,\xi\xi}+f_u^*(u_0^*,K_0^*)\hat u_0=0
\]</div>
Which we recognize as the homogeneous fast reduced problem, to which $$Au_{0,\xi}^*$$ is the solution. For simplicity we set $$A=1$$ so we get $$\hat u= u^*_{0,\xi}+\epsilon^\nu\hat u_1$$ So we get at order $$\epsilon^\nu$$: (missen we niet een -$$u_0$$ term?)
<div class="math-container">\[
\hat\lambda u^*_{0,\xi} = \hat u_{1,\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u_1+f_v^*(u^*_0,K_0^*)\hat{\hat K}+\mathcal O(\epsilon^{2}+\epsilon^{2\nu}) \\
\]</div>
(is error idd $$O(\epsilon^2)$$ ipv $$O(\epsilon^{2-\nu}$$?)
Which is a homogeneous SL problem with again the same operator $$\mathcal L=\partial_{\xi\xi}+f_u^*(u_0^*,K_0^*)$$. The Fredholm alternative tells us that this equations has solutions which obey:
<div class="math-container">\[
\langle u_{0,\xi}^*, \hat\lambda  u^*_{0,\xi} -f_v^*(u^*_0,K_0^*)\hat{\hat K} \rangle =0
\]</div>
Which gives:
<div class="math-container">\[
\hat{\hat K} = \hat\lambda \frac{\int_I (u_{0,\xi}^*(\xi))^2d\xi}{\int_I f_v^*(u_0^*(\xi),K_0^*)u_{0,\xi}^*(\xi)d\xi}
\]</div>
Since $$u_{0,\xi}^*(\xi)$$ decays exponentially on both sides, the integrals converge and can be replaced by integrals over the entirety of $$\mathbb R$$. 

## Slow linearized system
We now look at the slow system, where:
<div class="math-container">\[
\begin{aligned}
\hat\lambda \epsilon^\nu \hat u =\epsilon^2 \hat u_{xx}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat v \\
\hat\lambda \epsilon^{\nu} \hat v = \hat v_{xx}- f_u^*(u^*_0,K_0^*)\hat u- f_v^*(u^*_0,K_0^*)\hat v 
\end{aligned}
\]</div>
We find that:
Well we require the orders to match so let's substitute $$\hat u=\epsilon^\nu \hat{\hat u}$$ (why u?? I guess to match $$\hat v$$) and $$\hat v=\epsilon^\nu \hat{\hat v}$$. This doesn't really change the equations much:
<div class="math-container">\[
\begin{aligned}
\hat\lambda \epsilon^\nu \hat{\hat u} =\epsilon^2 \hat{\hat u}_{xx}+f_u^*(u^*_0,K_0^*)\hat{\hat u}+f_v^*(u^*_0,K_0^*)\hat{\hat v} \\
\hat\lambda \epsilon^{\nu} \hat{\hat v} = \hat{\hat v}_{xx}- f_u^*(u^*_0,K_0^*)\hat{\hat u}- f_v^*(u^*_0,K_0^*)\hat{\hat v }
\end{aligned}
\]</div>
Now we find:
<div class="math-container">\[
\hat{\hat u} =- \frac{f_v^*}{f_u^*}\hat{\hat v}+\mathcal O(\epsilon^\nu)
\]</div>
Then we also find by adding the two equations:
<div class="math-container">\[
\hat{\hat v}_{xx} =\hat\lambda \epsilon^\nu(\hat{\hat u}+\hat{\hat v})+\mathcal O(\epsilon^2)=\hat\lambda\epsilon^\nu\frac{f_u^*-f_v^*}{f_u}\hat{\hat v^*}+\mathcal O(\epsilon^2+\epsilon^{2\nu})
\]</div>
To have localized solutions we require 
<div class="math-container">\[
\hat\lambda\frac{f_u^*-f_v^*}{f_u^*}>0
\]</div>
Since existence of fronts requires $$f_u<0$$, this implies that for positive (unstable) $$\lambda$$, we need, $$f_u^*>f_v^*$$. Trace determinant analysis of the plateaus shows that this is the case for stable fronts (plateaus?). So small, positive lambda are possible here, so let's carry on in our analysis.

To leading order then, the equations are given by:
<div class="math-container">\[
\hat{\hat v}(x) = A_\pm\exp\left(\mp \epsilon^{\nu/2}x\sqrt{\frac{f_u^*-f_v^*}{f_u^*}} \right)
\]</div>
By continuity: 
<div class="math-container">\[\hat{\hat v}(0)=A_\pm=\hat{\hat K}=\hat\lambda \frac{\int_I (u_{0,\xi}^*(\xi))^2d\xi}{\int_I f_v^*(u_0^*(\xi),K_0^*)u_{0,\xi}^*(\xi)d\xi}\]</div>
Changing to the fast coordinate:
<div class="math-container">\[
\hat{\hat v}(\xi) = \hat{\hat K}\exp\left(\mp \epsilon^{1+\nu/2}\xi\sqrt{\frac{f_u^*-f_v^*}{f_u^*}} \right)
\]</div>
Then the derivative at zero equals:
<div class="math-container">\[
\hat{\hat v}_\xi(\xi) = \mp\hat{\hat K} \epsilon^{1+\nu/2}\sqrt{\frac{f_u^*-f_v^*}{f_u^*}} 
\]</div>
Hence the slow jump is of order $$O(\epsilon^{1+\nu/2})$$.



### Little intermezzo
We can write the fast equations:
<div class="math-container">\[
\begin{aligned}
\hat\lambda \epsilon^\nu \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+\epsilon^{\nu}f_v^*(u^*_0,K_0^*)\hat{\hat v} \\
\hat\lambda \epsilon^{2\nu+2} \hat{\hat v} = \epsilon^\nu \hat{\hat v}_{\xi\xi}-\epsilon^2 f_u^*(u^*_0,K_0^*)\hat u- \epsilon^{2+\nu} f_v^*(u^*_0,K_0^*)\hat{\hat v }
\end{aligned}
\]</div>
So we have:
<div class="math-container">\[
\hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u=\mathcal O(\epsilon^{\nu})=-\epsilon^{\nu}(f_v^*(u^*_0,K_0^*)\hat{\hat v} -\hat\lambda \hat u)
\]</div>
Integrating, we find:
<div class="math-container">\[
\int \hat u_{\xi\xi}(\xi)+f_u^*(u^*_0(\xi),K_0^*)\hat u(\xi)d\xi=-\int \epsilon^{\nu}(f_v^*(u^*_0,K_0^*)\hat{\hat v} -\hat\lambda \hat u)=\mathcal O(\epsilon^\nu)
\]</div>
Where we assume that $$\int \hat{\hat v}$$ and $$\int \hat u$$ converge ($$L^2$$ doesn't imply this, needs argument, I guess we have leading order behaviour in slow, where they go to zero! So they are integrable? Width is $$\mathcal O(1)$$ in fast, so this should be enough, needs to be worked out $$L^2$$ and ).
Since $$\int \hat u_{\xi\xi}=\lim_{L\to \infty} \hat u_\xi(L)-\hat u_\xi(-L)$$, this term is zero, hence  
<div class="math-container">\[\int f_u^*(u^*_0(\xi),K_0^*)\hat u(\xi)d\xi=O(\epsilon^\nu)\]</div>
Using the expansion of $$\hat u$$, this becomes
<div class="math-container">\[\int f_u^*(u^*_0(\xi),K_0^*)u^*_0(\xi)d\xi=O(\epsilon^\nu)\]</div>
again assuming $$\hat u_1$$ is integrable.
## Fast jump
<div class="math-container">\[
\epsilon^\nu \hat{\hat v}_{\xi\xi}=\hat\lambda \epsilon^{2\nu+2} \hat{\hat v}+\epsilon^2 f_u^*(u^*_0,K_0^*)\hat u+ \epsilon^{2+\nu} f_v^*(u^*_0,K_0^*)\hat{\hat v } 
\]</div>
Or dividing by $$\epsilon^\nu$$, this turns into:
<div class="math-container">\[
\hat{\hat v}_{\xi\xi}=\hat\lambda \epsilon^{2+\nu} \hat{\hat v}+\epsilon^{2-\nu} f_u^*(u^*_0,K_0^*)\hat u+ \epsilon^{2} f_v^*(u^*_0,K_0^*)\hat{\hat v } 
\]</div>
Integrating over the fast interval, we find:
<div class="math-container">\[
\Delta_{fast}\hat{\hat v}_\xi = \int\hat\lambda \epsilon^{2+\nu} \hat{\hat v}+\epsilon^{2-\nu} f_u^*(u^*_0,K_0^*)\hat u+ \epsilon^{2} f_v^*(u^*_0,K_0^*)\hat{\hat v } d\xi = \mathcal O(\epsilon^2)
\]</div>
Hmm, so to match orders, we require $$\nu = 2$$, and then everything becomes a mess... [Nu is twee!]({% link _posts/2024-10-02-nu-is-twee!.md %})


# Appendices
## K order 1
We have the following system:
<div class="math-container">\[
\hat\lambda \epsilon^\nu \hat u = \hat u_{\xi\xi}+f_u^*(u^*_0,K_0^*)\hat u+f_v^*(u^*_0,K_0^*)\hat K+\mathcal O(\epsilon^2) \\
\]</div>
We expand $$\hat u$$ as: 
<div class="math-container">\[\hat u=\hat u_0+\epsilon^\nu\hat u_1\]</div>
Then we get at leading order:
<div class="math-container">\[
\hat u_{0,\xi\xi}+f_u^*(u_0^*,K_0^*)\hat u_0=-f_v^*(u_0^*,K_0^*)\hat K
\]</div>
Solvability: 
<div class="math-container">\[
\hat K\langle u_{0,\xi}^* ,f_v^*(u_0^*,K_0^*)\rangle=\hat K\int_I f_v^*(u_0^*(\xi),K_0^*)u_{0,\xi}^*(\xi)d\xi = 0
\]</div>
If we assume $$f$$ to be such that the inner product is non-zero, this shows that we need $$\hat K=0$$. 
