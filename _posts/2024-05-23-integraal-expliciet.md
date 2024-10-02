---
layout: post
title: "Integraal expliciet"
date: 2024-05-23
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>


Some algebra shows that $$\epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}\lambda d\xi=2\epsilon^{3/2}\lambda$$ cannot match the order of the slow timescale so we put those away in the higher order terms.
<div class="math-container">\[
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_U(\bar U,\bar V)u_{inner}+f_V(\bar U,\bar V)]d\xi= -\frac{\sqrt\lambda}{\epsilon} \left(\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}+\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}\right)
\]</div>

We've argued why $$\lambda<<1$$, so we can use insight from corollary 3.6 from DV_JDDE:
**Corollary 3.6:** For $$j$$ even,
<div class="math-container">\[
v_{i n}(\xi ; \lambda) \leadsto\left(\frac{w_{f, j}(\xi)}{\left\|w_{f, j}\right\|_2^2} \int_{-\infty}^{\infty} \frac{\partial G}{\partial U}\left(u_*, v_{f, h}\left(\tilde{\xi} ; u_*\right)\right) w_{f, j}(\tilde{\xi}) d \tilde{\xi}\right) \cdot \frac{1}{\lambda-\lambda_{f, j}} \text { as } \lambda \rightarrow \lambda_{f, j}
\]</div>
We don't expand around homoclinics, so it's the question how applicable this Corollary is to our situation, but if it is, we can posit that:
<div class="math-container">\[
u_{inner}\leadsto  \frac{C(x)}{0-\lambda} = \frac{C(x)}{\lambda}
\]</div>
Where C is some function of space, determined by $$f$$ and the eigenfunctions of the Sturm-Liouville problem. This we can fill into our integral, and we find:
<div class="math-container">\[
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_U(\bar U,\bar V)\frac{C(x)}{\lambda}+f_V(\bar U,\bar V)]d\xi= -\frac{\sqrt\lambda}{\epsilon} \left(\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}+\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}\right)
\]</div>
Then clearly the $$f_V$$ term is not leading order, since $$\lambda\ll 1$$, so we're left with:
<div class="math-container">\[
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}f_U(\bar U,\bar V) C(x)d\xi= -\frac{\lambda\sqrt\lambda}{\epsilon} \left(\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}+\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}\right)
\]</div>
Then, anticipating that the integral is $$O(\epsilon^{\eta})$$, we get:
<div class="math-container">\[
I\epsilon^{\eta+1} = -\lambda^{3/2}S
\]</div>
Where $$I$$ is now the order $$1$$ coefficient from the integral, and $$S$$ the square root terms. Then, as long as the plateaus are stable enough, so $$f_V/f_U$$ not super close to $$1$$, and therefore $$S=O(1)$$, we get:
<div class="math-container">\[
\lambda = O(\epsilon^{(2\eta+2)/3})
\]</div>
Furthermore, the stability is now determined by the sign of $$I$$. If $$I$$ is negative, we can expect unstable solutions, so $$\lambda>0$$, since $$S$$ is the square root of some numbers, so for real solutions, $$S$$ is positive itself. 

<img src="/assets/images/Pasted image 20240521194827.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240521194827.png">




<img src="/assets/images/Pasted image 20240521171808.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240521171808.png">
kunnen we beredeneren dat $$w(\xi)\to0$$? 
Hoe toepasbaar met geen even $$w$$? 


insert 
<img src="/assets/images/Pasted image 20240522144257.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240522144257.png">
into
<img src="/assets/images/Pasted image 20240522144241.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240522144241.png">
where:
<img src="/assets/images/Pasted image 20240522144447.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240522144447.png">
In my words:
<div class="math-container">\[
v =A w^R+Bw^L
\]</div>
into:
<div class="math-container">\[
v_{xx}+(G_V-1+\lambda)v = -G_U
\]</div>
This gives:
<div class="math-container">\[
(A w^R+Bw^L)_{xx}+(G_V-1+\lambda)(A w^R+Bw^L) = -G_U
\]</div>
expanding the first term:
<div class="math-container">\[\begin{aligned}
(A w^R+Bw^L)_{xx} = A''w^R+2A'(w^{R})'+A(w^R)'' \\+B''w^L+2B'(w^{L})'+B(w^L)'' 
\end{aligned}\]</div>


### Wronskian has zeros
**Lemma 5.9.** The Wronskian $$W (z) = W (u_b (z), u_a (z))$$ is an entire function
which vanishes precisely at the eigenvalues of L. (Verhulst, F.: Nonlinear Differential Equations and Dynamical Systems)

### Variation of constants
$$n=2$$:
<div class="math-container">\[
w^{(2)}+\alpha_0 w^{(0)} = b
\]</div>
where:
<div class="math-container">\[\alpha_0 =(G_V-1+\lambda)\]</div>
and 
<div class="math-container">\[
b = G_U
\]</div>
Then we get:
<div class="math-container">\[
W^A = \begin{vmatrix}
0&w^L\\ G_U&\partial_\xi w^L
\end{vmatrix}
\]</div>
<div class="math-container">\[
W^B = \begin{vmatrix}
w^R&0\\ \partial_\xi w^R&G_U
\end{vmatrix}
\]</div>
So:
<div class="math-container">\[
A' = \frac{W^A}{W(\lambda)} = -\frac{G_Uw^L}{W(\lambda)}
\]</div>
and:
<div class="math-container">\[
B' = \frac{W^B}{W(\lambda)} = \frac{G_Uw^R}{W(\lambda)}
\]</div>
Relabel $$A\to A^R$$ and $$B\to A^L$$ and integrate to get:
<div class="math-container">\[
A^{R/L} = A^{R/L}(0)\mp \frac{1}{W(\lambda)}\int_0^x G_U w^{L/R} dy
\]</div>
Basically a bit uglier version of Arjen's 



[View Raw Markdown](/assets/md/Integraal expliciet.md)
