---
layout: post
title: "Integraal expliciet"
date: 2024-05-23
---

Some algebra shows that $$\epsilon^2\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}\lambda d\xi=2\epsilon^{3/2}\lambda$$ cannot match the order of the slow timescale so we put those away in the higher order terms.
<div>\[
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_U(\bar U,\bar V)u_{inner}+f_V(\bar U,\bar V)]d\xi= -\frac{\sqrt\lambda}{\epsilon} \left(\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}+\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}\right)
\]</div>

We've argued why $$\lambda<<1$$, so we can use insight from corollary 3.6 from DV_JDDE:
**Corollary 3.6:** For $$j$$ even,
<div>\[
v_{i n}(\xi ; \lambda) \leadsto\left(\frac{w_{f, j}(\xi)}{\left\|w_{f, j}\right\|_2^2} \int_{-\infty}^{\infty} \frac{\partial G}{\partial U}\left(u_*, v_{f, h}\left(\tilde{\xi} ; u_*\right)\right) w_{f, j}(\tilde{\xi}) d \tilde{\xi}\right) \cdot \frac{1}{\lambda-\lambda_{f, j}} \text { as } \lambda \rightarrow \lambda_{f, j}
\]</div>
We don't expand around homoclinics, so it's the question how applicable this Corollary is to our situation, but if it is, we can posit that:
<div>\[
u_{inner}\leadsto  \frac{C(x)}{0-\lambda} = \frac{C(x)}{\lambda}
\]</div>
Where C is some function of space, determined by $$f$$ and the eigenfunctions of the Sturm-Liouville problem. This we can fill into our integral, and we find:
<div>\[
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}[f_U(\bar U,\bar V)\frac{C(x)}{\lambda}+f_V(\bar U,\bar V)]d\xi= -\frac{\sqrt\lambda}{\epsilon} \left(\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}+\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}\right)
\]</div>
Then clearly the $$f_V$$ term is not leading order, since $$\lambda\ll 1$$, so we're left with:
<div>\[
\int_{-1/\sqrt\epsilon}^{1/\sqrt\epsilon}f_U(\bar U,\bar V) C(x)d\xi= -\frac{\lambda\sqrt\lambda}{\epsilon} \left(\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}+\sqrt{1-\frac{f_{V,r}}{f_{U,r}}}\right)
\]</div>
Then, anticipating that the integral is $$O(\epsilon^{\eta})$$, we get:
<div>\[
I\epsilon^{\eta+1} = -\lambda^{3/2}S
\]</div>
Where $$I$$ is now the order $$1$$ coefficient from the integral, and $$S$$ the square root terms. Then, as long as the plateaus are stable enough, so $$f_V/f_U$$ not super close to $$1$$, and therefore $$S=O(1)$$, we get:
<div>\[
\lambda = O(\epsilon^{(2\eta+2)/3})
\]</div>
Furthermore, the stability is now determined by the sign of $$I$$. If $$I$$ is negative, we can expect unstable solutions, so $$\lambda>0$$, since $$S$$ is the square root of some numbers, so for real solutions, $$S$$ is positive itself. 

![Image](/assets/images/Pasted image 20240521194827.png)




![Image](/assets/images/Pasted image 20240521171808.png)
kunnen we beredeneren dat $$w(\xi)\to0$$? 
Hoe toepasbaar met geen even $$w$$? 


insert 
![Image](/assets/images/Pasted image 20240522144257.png)
into
![Image](/assets/images/Pasted image 20240522144241.png)
where:
![Image](/assets/images/Pasted image 20240522144447.png)
In my words:
<div>\[
v =A w^R+Bw^L
\]</div>
into:
<div>\[
v_{xx}+(G_V-1+\lambda)v = -G_U
\]</div>
This gives:
<div>\[
(A w^R+Bw^L)_{xx}+(G_V-1+\lambda)(A w^R+Bw^L) = -G_U
\]</div>
expanding the first term:
<div>\[\begin{aligned}
(A w^R+Bw^L)_{xx} = A''w^R+2A'(w^{R})'+A(w^R)'' \\+B''w^L+2B'(w^{L})'+B(w^L)'' 
\end{aligned}\]</div>


### Wronskian has zeros
**Lemma 5.9.** The Wronskian $$W (z) = W (u_b (z), u_a (z))$$ is an entire function
which vanishes precisely at the eigenvalues of L. (Verhulst, F.: Nonlinear Differential Equations and Dynamical Systems)

### Variation of constants
$$n=2$$:
<div>\[
w^{(2)}+\alpha_0 w^{(0)} = b
\]</div>
where:
<div>\[\alpha_0 =(G_V-1+\lambda)\]</div>
and 
<div>\[
b = G_U
\]</div>
Then we get:
<div>\[
W^A = \begin{vmatrix}
0&w^L\\ G_U&\partial_\xi w^L
\end{vmatrix}
\]</div>
<div>\[
W^B = \begin{vmatrix}
w^R&0\\ \partial_\xi w^R&G_U
\end{vmatrix}
\]</div>
So:
<div>\[
A' = \frac{W^A}{W(\lambda)} = -\frac{G_Uw^L}{W(\lambda)}
\]</div>
and:
<div>\[
B' = \frac{W^B}{W(\lambda)} = \frac{G_Uw^R}{W(\lambda)}
\]</div>
Relabel $$A\to A^R$$ and $$B\to A^L$$ and integrate to get:
<div>\[
A^{R/L} = A^{R/L}(0)\mp \frac{1}{W(\lambda)}\int_0^x G_U w^{L/R} dy
\]</div>
Basically a bit uglier version of Arjen's 

