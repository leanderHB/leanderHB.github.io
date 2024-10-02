Oh we should use $[-\sqrt\epsilon,\sqrt\epsilon]$? Since is $\epsilon<<1$, then definitely $[-\epsilon,\epsilon]\subseteq [-\sqrt\epsilon,\sqrt\epsilon]$.  
Boundary layer is something like $[-\epsilon,\epsilon]$, using Brauns to note that the interface width scales as $\sqrt{D_u/D_v}$.  Outer layer left:
$$
\begin{aligned}
\lambda \begin{pmatrix}
r\\ e
\end{pmatrix}&=\begin{pmatrix}
\Delta +g_v& g_u\\ -g_u&-g_v
\end{pmatrix}\begin{pmatrix}
r\\ e
\end{pmatrix}
\end{aligned}
$$
We know that to leading order: $g_v= c_v\exp(k_lx)$ and $g_u= c_u\exp(k_lx)$ on the left of the boundary layer. So we can explicitly write down an expression for $r$:

-- ergens hier moet ik de fast timescale erin moffelen!!!!

$$
r_{xx} =\lambda r-\frac{\lambda c_v\exp(k_lx)}{\lambda+c_u\exp(k_lx)}r
$$
not what we like, so we expand of course, and get around the boundary layer:
$$
r_{xx} = (\lambda -\frac{\lambda c_v}{\lambda +c_u})r
$$
This preterm is larger than zero, so we get exponentials as solution:
$$
r = \exp\left(\pm\sqrt{\lambda-\frac{\lambda c_v}{\lambda+c_u}}x\right)
$$
Here we obviously need to pay attention to which side we are on for the sign. 
Note we can explicitly find the constants as function of the steady solutions tails.
Then we can find $r_x$ at the boundary layer:
$$
r_x(\epsilon) = \pm\sqrt{\lambda-\frac{\lambda c_v}{\lambda+c_u}}\exp\left(\pm\sqrt{\lambda-\frac{\lambda c_v}{\lambda+c_u}}\epsilon\right) = \pm\sqrt{\lambda-\frac{\lambda c_v}{\lambda+c_u}}+O(\epsilon)
$$

Which implies that when we consider the interval $[-\epsilon,\epsilon]$ as the boundary layer, the derivative will make a jump of the order of $\epsilon\sqrt{\lambda -\frac{\lambda c^-_v}{\lambda +c^-_u}}$ on the left, and similarly, a jump of $\epsilon\sqrt{\lambda -\frac{\lambda c^+_v}{\lambda +c^+_u}}$ on the right. Here the $+$ and $-$ indicate the left and right sides. 

Integrating the fast system over the entire real line allows us to match the derivatives, which yields:

$$
\lambda e = e_{yy}- g_ue-g_vb
$$



Stel je hebt:
$$\begin{aligned}
\vec x_1 = \begin{pmatrix}1\\1 \end{pmatrix}\\
\vec x_2 = \begin{pmatrix}0\\1 \end{pmatrix}\\
\vec x_3 = \begin{pmatrix}1\\2 \end{pmatrix}
\end{aligned}$$
en $\alpha^*_1=\alpha^*_2=\alpha^*_3=1$ en $\alpha_1=\alpha_2=\alpha_3=0$ ofzo. Dan heb je:
$$
\vec w = (\alpha^*_1-\alpha_1) \vec x_1+(\alpha^*_2-\alpha_2) \vec x_2+(\alpha^*_3-\alpha_3) \vec x_3
$$
als je invult:
$$
\begin{aligned}
\vec w = (1-0)\begin{pmatrix}1\\1 \end{pmatrix}+ (1-0)\begin{pmatrix}0\\1 \end{pmatrix}+ (1-0)\begin{pmatrix}1\\2 \end{pmatrix} \\
= \begin{pmatrix}1\\1 \end{pmatrix}+ \begin{pmatrix}0\\1 \end{pmatrix}+ \begin{pmatrix}1\\2 \end{pmatrix} =\begin{pmatrix}2\\4 \end{pmatrix}
\end{aligned}
$$
