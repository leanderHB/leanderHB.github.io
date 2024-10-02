We expand as follows: $U= \bar U+\epsilon^2 u$. Besides that, we choose wave coordinates and get $U_t= cU_x$ Then we obtain:
$$
\begin{aligned}
\hat c\bar U_x =\epsilon^2 \bar U_{xx}+\epsilon^4 u_{xx}+f(\bar U, \bar V)+\epsilon^2f_Uu+\epsilon^2f_V v\\
\hat c\bar V_x = \bar V_{xx}+\epsilon^2 v_{xx}-f(\bar U, \bar V)-\epsilon^2f_Uu-\epsilon^2f_V v
\end{aligned}
$$
anticipating that $c\ll 1$, we get the steady state solutions at leading order and are left with:
$$
\begin{aligned}
\hat c\bar U_x =\epsilon^2 \bar U_{xx}+\epsilon^2f_Uu+\epsilon^2f_V v\\
\hat c\bar V_x = \epsilon^2 v_{xx}-\epsilon^2f_Uu-\epsilon^2f_V v
\end{aligned}
$$
To match orders, we relabel $\hat c=\epsilon^2 c$ and find:
$$
\begin{aligned}
c\bar U_x &= \bar U_{xx}+f_Uu+f_V v\\
c\bar V_x &= v_{xx}-f_Uu-f_V v
\end{aligned}
$$
Now we can add these two equations to obtain:
$$
c(\bar U_x+\bar V_x)=v_{xx}+\bar U_{xx}
$$

We integrate once and find:
$$
v^{+}_x-v_x^- = c\int_-^+ \bar U_x+\bar V_xdx +\bar U_{x}^+-\bar U_{x}^-
$$
$$
v^{+}_x-v_x^- = c\left(\bar U^+-\bar U^-+\bar V^+-\bar V^- \right) +\bar U_{x}^+-\bar U_{x}^-
$$
Since $\bar V$ only varies on a scale of $\epsilon^2$, we neglect these terms and find:
$$
(v^{+}_x-v_x^-)_i = c_i\left(\bar U^+-\bar U^-\right) +\bar U_{x}^+-\bar U_{x}^-
$$
We can find all the quantities in this set of equations exactly! 
Now we can force that our total solution has zero derivative as $x\to\pm \infty$. Then we can solve the set of equations actually. So define $x^+_i$ as $(p_i+p_{i+1})/2$. Then $\bar U^+_i=\alpha_i^+ \exp()$ 


Let's say for some reason we want $v_x$ to be equal on both ends, so combined with the boundary conditons, to be $0$ to leading order on the boundaries. Then:
$$
c_i= \frac{\bar U_{x}^+-\bar U_{x}^-}{\bar U^+-\bar U^-}
$$
To leading order $\bar U^+-\bar U^-$ is constant! Let's call it $U_d$. Then we're left with:
$$
c_i = \frac{\bar U_{x}^+-\bar U_{x}^-}{U_d}
$$
We have the leading order expression for $U_x$ on the plateaus:
$$
U_x = \alpha_\pm \exp(\mp\beta_\pm x)
$$
So then:
$$
c_i = \frac{ \alpha_+ \exp(-\beta_+ x_p^+)- \alpha_- \exp(\beta_- x_p^-)}{U_d}
$$
Oke maar nu geen koppeling meer, nee das niet waar.
We set the boundary in the middle between the two fronts, so we obtain:
$$
c_i  = \frac{ \alpha_+ \exp(-\beta_+ \Delta_{i+1})- \alpha_- \exp(\beta_- \Delta_{i})}{U_d}
$$
Where:
$$
\Delta_{i} = p_{i}-p_{i-1}
$$
And of course $\alpha$ and $\beta$ have to alternate for the rising/falling fronts!




$$
\partial_xf(U,V) = f_U(U,V)U_x+f_V(U,V)V_x
$$