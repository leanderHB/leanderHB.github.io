---
layout: post
title: "Expanden rond the volledige oplossing"
date: 2024-06-25
---
<style>
.math-container {
    max-width: 100%; /* Set a maximum width to prevent it from expanding the page */
    overflow-x: auto; /* Enable horizontal scrolling */
    white-space: nowrap; /* Prevent the text from wrapping */
}
</style>
connected to [Arjen Notes (my interpretation)]({% link _posts/2024-09-12-arjen-notes-(my-interpretation).md %})
Take the stationary equation for $$u$$:
<div class="math-container">\[
u_{\xi\xi}+f(u,K-\epsilon^2u)=0
\]</div>
Let's assume there exists a $$K=K^*$$ such that this equation has a heteroclinic orbit. 
Then expand $$u$$ and $$K$$:
<div class="math-container">\[
\begin{aligned}
u^* = u^*_0+\epsilon^2u^*_1+\dots\\
K^* = K^*_0+\epsilon^2K^*_1+\dots\\
\end{aligned}
\]</div>
Inserting this into the equation, we find at order $$1$$:
<div class="math-container">\[
u_{0,\xi\xi}^* +f(u^*_0,K^*_0)=0
\]</div>
and at order $$\epsilon^2$$:
<div class="math-container">\[
u_{1,\xi\xi}^*+f_u(u^*_0,K^*_0)u_1^*+f_v(u^*_0,K^*_0)(K_1^*-u_0^*)
\]</div>
Here we recognize the SL operator that we keep getting, and therefore note that to have a solution, we require:
<div class="math-container">\[
\int_\mathbb R u_0^*(\xi)u_{0,\xi}^*(\xi)f_v(u_0^*(\xi),K_0^*)d\xi = K_1^*\int_\mathbb R u_{0,\xi}^*f_v(u_0^*(\xi),K_0^*)d\xi
\]</div>
So we have:
<div class="math-container">\[
K_1^*=\frac{\int_\mathbb R u_0^*(\xi)u_{0,\xi}^*(\xi)f_v(u_0^*(\xi),K_0^*)d\xi}{\int_\mathbb R u_{0,\xi}^*f_v(u_0^*(\xi),K_0^*)d\xi} 
\]</div>



# Stability next order
We set $$\lambda = \epsilon^2 \hat\lambda$$ 
<div class="math-container">\[
\begin{aligned}
u = u^*+\delta \hat u\exp(\lambda t)\\
v = v^*+\delta v\exp(\lambda t) 
\end{aligned}
\]</div>
<div class="math-container">\[\begin{aligned}
\epsilon^2 \hat\lambda \hat u&=\hat u_{\xi\xi}+f_u(u^*,v^*)\hat u+f_v(u^*,v^*)\hat v\\
\epsilon^4\hat\lambda \hat v&=\hat v_{\xi\xi}-\epsilon^2f_u(u^*,v^*)\hat u-\epsilon^2f_v(u^*,v^*)\hat v
\end{aligned}\]</div>
Using our expansions: 
<div class="math-container">\[\begin{aligned}
u^*&=u^*_0+\epsilon^2u_1^* \\ 
v^*&=K^*-\epsilon^2 u^* = K_0^*+\epsilon^2 (K_1^* -u^*_0)\\
\hat u&=\hat u_0+\epsilon^2\hat u_1\\
\hat v&=\epsilon^2\hat{\hat v}_0+\epsilon^4\hat{\hat v}_1
\end{aligned}\]</div>
Here we use $$\hat{\hat v}$$ as otherwise, we get no solutions, see [Problem]({% link _posts/2024-06-24-problem.md %})
we get:
<div class="math-container">\[
\begin{aligned}
0&=\hat u_{0,\xi\xi}+f_u(u^*_0,v^*_0)\hat u_0\\
0&=\hat{\hat v}_{0,\xi\xi}-f_u(u^*,v^*)\hat u_0
\end{aligned}
\]</div>
at leading order.
Note the implications, like you might expect, at leading order, the perturbations have to be mass conserving, this is reassuring (and actually the first thing I said to Arjen haha). This is described by a similar relation as before: 
<div class="math-container">\[
\hat {\hat v}_0+\hat u_0=C
\]</div>
I feel like $$C$$ should be zero, but that's again my intuition about massless perturbations. 

The rest of the mess:
<div class="math-container">\[
\begin{aligned}
\epsilon^2 \hat\lambda (\hat u_0+\epsilon^2\hat u_1)&=(\hat u_0+\epsilon^2\hat u_1)_{\xi\xi}+f_u(u^*,v^*)(\hat u_0+\epsilon^2\hat u_1)+f_v(u^*,v^*)\epsilon^2\hat{\hat v}\\
\epsilon^4\hat\lambda (\hat{\hat v}_0+\epsilon^2\hat{\hat v}_1)&=(\hat{\hat v}_0+\epsilon^2\hat{\hat v}_1)_{\xi\xi}-f_u(u^*,v^*)(\hat u_0+\epsilon^2\hat u_1)-\epsilon^2f_v(u^*,v^*)(\hat{\hat v}_0+\epsilon^2\hat{\hat v}_1)
\end{aligned}
\]</div>
expanding $$f$$ too and tossing terms of order $$4$$:
<div class="math-container">\[
\begin{aligned}
\epsilon^2 \hat\lambda \hat u_0&=(\hat u_0+\epsilon^2\hat u_1)_{\xi\xi}+(f_{u}(u_0^*,K_0^*)+\epsilon^2(f_{uu}(u_0^*,K_0^*)u_1^* \\&+f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0)))(\hat u_0+\epsilon^2\hat u_1)+(f_{v}(u_0^*,K_0^*)+\epsilon^2(f_{vu}(u_0^*,K_0^*)u_1^* \\&+f_{vv}(u_0^*,K_0^*)(K_1^* -u^*_0)))\epsilon^2\hat{\hat v}_0\\
0&=\epsilon^2\hat{\hat v}_{1,\xi\xi}-f_u(u^*,v^*)\epsilon^2\hat u_1-\epsilon^2f_v(u^*,v^*)\hat{\hat v}_0
\end{aligned}
\]</div>
At order 2 we get:
<div class="math-container">\[
\begin{aligned}
\hat\lambda \hat u_0&=\hat u_{1,\xi\xi}+f_{u}(u_0^*,K_0^*)\hat u_1+(f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0\\&+f_{v}(u_0^*,K_0^*)\hat{\hat v}_0 \\
0&=\epsilon^2\hat{\hat v}_{1,\xi\xi}-f_u(u^*,v^*)\epsilon^2\hat u_1-\epsilon^2f_v(u^*,v^*)\hat{\hat v}_0
\end{aligned}
\]</div>
The top term is again an inhomogeneous SL problem:
<div class="math-container">\[
g(\xi)=\hat u_{1,\xi\xi}+f_{u}(u_0^*,K_0^*)\hat u_1
\]</div>
Where $$g$$ captures the horror that $$\nu=2$$ created...

### Fast jump
<div class="math-container">\[
\int \hat{\hat v}_{\xi\xi} = \int \hat{\hat v}_{0,\xi\xi}+\epsilon^2 \hat{\hat v}_{1,\xi\xi}d\xi
\]</div>
The first integral is zero:
<div class="math-container">\[
\int \hat{\hat v}_{0,\xi\xi}d\xi = -\int \hat u_{0,\xi\xi}d\xi = 0
\]</div>
As $$\hat u_0=u^*_0$$, therefore is heteroclinic, and has flat ends. So our fast jump is:
<div class="math-container">\[
\Delta_{fast} \hat{\hat v}_{\xi} = \epsilon^2\int_\mathbb R f_u(u^*,v^*)\hat u_1+f_v(u^*,v^*)\hat{\hat v}_0 d\xi
\]</div>
The good news is that both integrals now converge (i think?) It's also almost the same expression as before, except the fact that the functions here are a lot harder to find explicitly. 
### Enge dingen
We've got our fast jump:
<div class="math-container">\[
\Delta_{fast} \hat{\hat v}_{\xi} = \epsilon^2\int_\mathbb R f_u(u^*,v^*)\hat u_1+f_v(u^*,v^*)\hat{\hat v}_0 d\xi
\]</div>
Using the order $$2$$ equations for $$\hat u$$, we get:
<div class="math-container">\[
f_{u}(u_0^*,K_0^*)\hat u_1+f_{v}(u_0^*,K_0^*)\hat{\hat v}_0= \hat\lambda \hat u_0-(f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0-\hat u_{1,\xi\xi}
\]</div>
Substituting in our integral we get a bit of a mess:
<div class="math-container">\[
\Delta_{fast} \hat{\hat v}_{\xi}  = \int [\hat\lambda \hat u_0-\hat u_{1,\xi\xi}-(f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0]d\xi
\]</div>
The slow region is a linear, constant coefficient problem, so $$\hat u_1$$ will be a decaying function on both ends, hence the integral over the curvature of $$\hat u_1$$ is zero. 
<div class="math-container">\[
\Delta_{fast} \hat{\hat v}_{\xi}  = \int  [(\hat\lambda+f_{uu}(u_0^*,K_0^*)u_1^* +f_{uv}(u_0^*,K_0^*)(K_1^* -u^*_0))\hat u_0]d\xi
\]</div>
Good news: integral indeed converges. Bad news, I have no clue what to do with this (:

in enge termen schrijf ik dit om naar een integraal over alleen maar eerste afgeleiden van $$f$$, maar nu wel een $$\hat u_{1,\xi}$$ term... [Enge termen]({% link _posts/2024-06-25-enge-termen.md %})
<div class="math-container">\[
\begin{aligned}
\Delta_{fast} \hat{\hat v}_{\xi}  = -\int  [(\hat\lambda-f_u(u^*_0,K^*_0)u_{1,\xi}^*+f_{v}(u^*_0,K^*_0)u_{0,\xi}^*]d\xi
\end{aligned}
\]</div>

[oude versie fast jump]({% link _posts/2024-06-25-oude-versie-fast-jump.md %})

### afgeleide langs functie
<div class="math-container">\[
f_\xi(u^*,v^*) = f_u(u^*,v^*)u^*_\xi+f_v(u^*,v^*)v^*_\xi = f_u(u^*,v^*)u^*_\xi-\epsilon^2 f_v(u^*,v^*)u_\xi^*
\]</div>
inserting $$u^*$$ expansion:
<div class="math-container">\[
f_\xi(u^*,v^*) = f_u(u^*,v^*)(u^*_{0,\xi}+\epsilon^2u^*_{1,\xi})-\epsilon^2 f_v(u^*,v^*)u^*_{0,\xi}+O(\epsilon^4)
\]</div>
Integrating over the entire line, we find:
<div class="math-container">\[
0=\int_\mathbb R f_\xi(u^*,v^*)d\xi = \int_\mathbb R f_u(u^*,v^*)(u^*_{0,\xi}+\epsilon^2u^*_{1,\xi})-\epsilon^2 f_v(u^*,v^*)u^*_{0,\xi}d\xi +O(\epsilon^4)
\]</div>
So:
<div class="math-container">\[
\int_\mathbb R f_u(u^*,v^*)u^*_{1,\xi}- f_v(u^*,v^*)u^*_{0,\xi}d\xi= \frac{1}{\epsilon^2}\int_\mathbb R f_u(u^*,v^*)u^*_{0,\xi}d\xi +O(\epsilon^2) 
\]</div>