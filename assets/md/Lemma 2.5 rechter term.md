![[Pasted image 20240416103234.png]]
Via Fredholm hebben we $\langle v_b,h \rangle=0$, dan kunnen we schrijven:
$$\begin{aligned}
\int_{-\infty}^X h(\tilde X)v_b(\tilde X)d\tilde X &= \int_{-\infty}^\infty h(\tilde X)v_b(\tilde X)d\tilde X -\int_{X}^\infty h(\tilde X)v_b(\tilde X)d\tilde X \\
&=\langle h,v_b\rangle - \int_{X}^\infty h(\tilde X)v_b(\tilde X)d\tilde X\\
&= -\int_{X}^\infty h(\tilde X)v_b(\tilde X)d\tilde X
\end{aligned}$$
Aangezien het limiet van $h$ naar $\infty$ bestaat, is het limiet-gedrag van deze integraal:
$$
-\int_{X}^\infty h(\tilde X)v_b(\tilde X)d\tilde X\leadsto  h_\infty  \exp(-\sqrt{\alpha_+}X)+O(E_+^2)
$$
Waar ik gebruik maak van (voor $b<0$):
$$
\int_a^\infty \exp(bx)dx = \frac1b \exp(ba)
$$


waar $h_\infty=\lim_{X\to\infty} h(X)$


#### Lemma (Fredholm)
Let $\mathcal L$ be selfadjoint. If $\mathcal L v=0$, so $v\in \ker \mathcal L$ , then $\mathcal L u=h$ has a solution only if $\langle v,h\rangle=0$. 
**Proof:**
$$0=\langle 0,u \rangle=\langle Lv,u \rangle=\langle v,Lu \rangle=\langle v,h \rangle$$

