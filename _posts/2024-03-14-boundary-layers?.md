---
layout: post
title: "Boundary layers?"
date: 2024-03-14
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

Oh we should use $$[-\sqrt\epsilon,\sqrt\epsilon]$$? Since is $$\epsilon<<1$$, then definitely $$[-\epsilon,\epsilon]\subseteq [-\sqrt\epsilon,\sqrt\epsilon]$$.  
Boundary layer is something like $$[-\epsilon,\epsilon]$$, using Brauns to note that the interface width scales as $$\sqrt{D_u/D_v}$$.  Outer layer left:
<div class="math-container">\[
\begin{aligned}
\lambda \begin{pmatrix}
r\\ e
\end{pmatrix}&=\begin{pmatrix}
\Delta +g_v& g_u\\ -g_u&-g_v
\end{pmatrix}\begin{pmatrix}
r\\ e
\end{pmatrix}
\end{aligned}
\]</div>
We know that to leading order: $$g_v= c_v\exp(k_lx)$$ and $$g_u= c_u\exp(k_lx)$$ on the left of the boundary layer. So we can explicitly write down an expression for $$r$$:

-- ergens hier moet ik de fast timescale erin moffelen!!!!

<div class="math-container">\[
r_{xx} =\lambda r-\frac{\lambda c_v\exp(k_lx)}{\lambda+c_u\exp(k_lx)}r
\]</div>
not what we like, so we expand of course, and get around the boundary layer:
<div class="math-container">\[
r_{xx} = (\lambda -\frac{\lambda c_v}{\lambda +c_u})r
\]</div>
This preterm is larger than zero, so we get exponentials as solution:
<div class="math-container">\[
r = \exp\left(\pm\sqrt{\lambda-\frac{\lambda c_v}{\lambda+c_u}}x\right)
\]</div>
Here we obviously need to pay attention to which side we are on for the sign. 
Note we can explicitly find the constants as function of the steady solutions tails.
Then we can find $$r_x$$ at the boundary layer:
<div class="math-container">\[
r_x(\epsilon) = \pm\sqrt{\lambda-\frac{\lambda c_v}{\lambda+c_u}}\exp\left(\pm\sqrt{\lambda-\frac{\lambda c_v}{\lambda+c_u}}\epsilon\right) = \pm\sqrt{\lambda-\frac{\lambda c_v}{\lambda+c_u}}+O(\epsilon)
\]</div>

Which implies that when we consider the interval $$[-\epsilon,\epsilon]$$ as the boundary layer, the derivative will make a jump of the order of $$\epsilon\sqrt{\lambda -\frac{\lambda c^-_v}{\lambda +c^-_u}}$$ on the left, and similarly, a jump of $$\epsilon\sqrt{\lambda -\frac{\lambda c^+_v}{\lambda +c^+_u}}$$ on the right. Here the $$+$$ and $$-$$ indicate the left and right sides. 

Integrating the fast system over the entire real line allows us to match the derivatives, which yields:

<div class="math-container">\[
\lambda e = e_{yy}- g_ue-g_vb
\]</div>



Stel je hebt:
<div class="math-container">\[\begin{aligned}
\vec x_1 = \begin{pmatrix}1\\1 \end{pmatrix}\\
\vec x_2 = \begin{pmatrix}0\\1 \end{pmatrix}\\
\vec x_3 = \begin{pmatrix}1\\2 \end{pmatrix}
\end{aligned}\]</div>
en $$\alpha^*_1=\alpha^*_2=\alpha^*_3=1$$ en $$\alpha_1=\alpha_2=\alpha_3=0$$ ofzo. Dan heb je:
<div class="math-container">\[
\vec w = (\alpha^*_1-\alpha_1) \vec x_1+(\alpha^*_2-\alpha_2) \vec x_2+(\alpha^*_3-\alpha_3) \vec x_3
\]</div>
als je invult:
<div class="math-container">\[
\begin{aligned}
\vec w = (1-0)\begin{pmatrix}1\\1 \end{pmatrix}+ (1-0)\begin{pmatrix}0\\1 \end{pmatrix}+ (1-0)\begin{pmatrix}1\\2 \end{pmatrix} \\
= \begin{pmatrix}1\\1 \end{pmatrix}+ \begin{pmatrix}0\\1 \end{pmatrix}+ \begin{pmatrix}1\\2 \end{pmatrix} =\begin{pmatrix}2\\4 \end{pmatrix}
\end{aligned}
\]</div>


[View Raw Markdown](/assets/md/Boundary layers?.md)
