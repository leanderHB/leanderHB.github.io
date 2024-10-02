---
layout: post
title: "r en s orgineel"
date: 2024-03-18
---
# linearizing fast
<div>\[
\begin{aligned}
\lambda r &=  r_{\xi\xi} + f_u(u_0,v_0)r+f_v(u_0,v_0)s\\
0 &=  s_{\xi\xi}\\\\
\end{aligned}
\]</div>
So $$s$$ is a constant across the fast subsystem, the system is linear, so for simplicity, let's say it's equal to 1. 
<div>\[
\begin{aligned}
\lambda r &=  r_{\xi\xi} + f_u(u_0,v_0)r+f_v(u_0,v_0)\\
\end{aligned}
\]</div>
let's abbreviate notation, we call $$f_u(\xi)=f_u(u_0(\xi),v_0(\xi))$$ and $$f_v(\xi) = f_v(u_0(\xi),v_0(\xi))$$. Then we get:
<div>\[
\lambda r = r_{\xi\xi} +f_u(\xi)r+f_v(\xi)
\]</div>
This is an in-homogeneous Sturm-Liouville problem with operator
<div>\[
\mathcal L = (\partial_\xi^2+f_u(\xi))
\]</div>
These problems have solutions, so we can assume we have their eigenvalues, then for $$\lambda$$ unequal to those, we get:
<div>\[
r(\xi) = (\mathcal L-\lambda)^{-1}f_v(\xi)
\]</div>

## slow-reduced linearized
Mara argues that $$r\to 0$$ when we approach the boundary layer? (don't see why exactly tbh) 
<div>\[
\begin{aligned}
\lambda r &= f_u(u_0,v_0)r+f_v(u_0,v_0)s\\
\lambda s &= s_{xx} - f_u(u_0,v_0)r-f_v(u_0,v_0)s\\
\end{aligned}
\]</div>
but if so:
<div>\[
\begin{aligned}
\lambda s &= s_{xx}-f_v(u_0,v_0)s
\end{aligned}
\]</div>
describes the behaviour of $$s$$ near the boundary: $$x=\pm\sqrt{\epsilon}$$. Then we can substitute $$\xi$$ back in:
<div>\[
\begin{aligned}
s_{\xi\xi}=\epsilon^2(\lambda s+f_v(\xi)s )
\end{aligned}
\]</div>
This has (local) solutions near $$\pm\sqrt\epsilon$$:
<div>\[
s(\pm\sqrt\epsilon) = \exp\left(\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)}\xi\right)
\]</div>
We can analyse the derivative here!
<div>\[
s_\xi(\pm\sqrt\epsilon) =\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)} \exp\left(\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)}\xi\right)
\]</div>
Now expand the exponential:
<div>\[\begin{aligned}
s_\xi(\pm\sqrt\epsilon) &=\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)} \left(1\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)}\xi+\dots\right)\\
&=\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)} +O(\epsilon^2)
\end{aligned}\]</div>
Now if we integrate $$s_{\xi\xi}$$ across the fast system, the fundamental theorem of calculus tells us:
<div>\[
\int_{-\sqrt\epsilon}^\sqrt\epsilon s_{\xi\xi}d\xi = s_\xi(\sqrt\epsilon)-s_\xi(-\sqrt\epsilon) = -\epsilon\left(\sqrt{\lambda+ f_v(\sqrt\epsilon)}+\sqrt{\lambda+ f_v(-\sqrt\epsilon)} \right)
\]</div>
Actually, we know what $$f_v(\pm\sqrt\epsilon)$$ is, the slow system tells us it's just $$0$$. So then we get:
<div>\[
\int_{-\sqrt\epsilon}^\sqrt\epsilon s_{\xi\xi}d\xi = -2\epsilon\sqrt\lambda
\]</div>
So all that's left is to insert $$s_{\xi\xi}$$: oh but we said it's equal to zero :P



# thrash



Mara argues that $$s\to 0$$ when we approach the boundary layer? (don't see why exactly tbh) 
<div>\[
\begin{aligned}
\lambda s &= f_u(u_0,v_0)s+f_v(u_0,v_0)r\\
\lambda r &= r_{xx} - f_u(u_0,v_0)s-f_v(u_0,v_0)r\\
\end{aligned}
\]</div>
but if so:
<div>\[
\begin{aligned}
\lambda r &= r_{xx}-f_v(u_0,v_0)r
\end{aligned}
\]</div>
describes the behaviour of $$r$$ near the boundary: $$x=\pm\sqrt{\epsilon}$$. Then we can substitute $$\xi$$ back in:
<div>\[
\begin{aligned}
r_{\xi\xi}=\epsilon^2(\lambda r+f_v(\xi)r )
\end{aligned}
\]</div>
This has (local) solutions near $$\pm\sqrt\epsilon$$:
<div>\[
r(\pm\sqrt\epsilon) = \exp\left(\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)}\xi\right)
\]</div>
We can analyse the derivative here!
<div>\[
r_\xi(\pm\sqrt\epsilon) =\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)} \exp\left(\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)}\xi\right)
\]</div>
Now expand the exponential:
<div>\[\begin{aligned}
r_\xi(\pm\sqrt\epsilon) &=\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)} \left(1\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)}\xi+\dots\right)\\
&=\mp\epsilon\sqrt{\lambda+ f_v(\pm\sqrt\epsilon)} +O(\epsilon^2)
\end{aligned}\]</div>
Now if we integrate $$r_{\xi\xi}$$ across the fast system, the fundamental theorem of calculus tells us:
<div>\[
\int_{-\sqrt\epsilon}^\sqrt\epsilon r_{\xi\xi}d\xi = r_\xi(\sqrt\epsilon)-r_\xi(-\sqrt\epsilon) = -\epsilon\left(\sqrt{\lambda+ f_v(\sqrt\epsilon)}+\sqrt{\lambda+ f_v(-\sqrt\epsilon)} \right)
\]</div>
Actually, we know what $$f_v(\pm\sqrt\epsilon)$$ is, the slow system tells us it's just $$0$$. So then we get:
<div>\[
\int_{-\sqrt\epsilon}^\sqrt\epsilon r_{\xi\xi}d\xi = -2\epsilon\sqrt\lambda
\]</div>
So all that's left is to insert $$r_{\xi\xi}$$: oh but we said it's equal to zero :P