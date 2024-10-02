We start with the set of equations:
$$\begin{aligned}
U_t &= \epsilon^2U_{xx}+f(U,V)\\
V_t &= V_{xx}-f(U,V)
\end{aligned}
$$
By previous analysis, we know that we get a 1 parameter family in $K$ of pulses and fronts described by a Hamiltonian system in $U$, for which there is a specific $K^*$ for which we obtain a front solution. Take this $K^*$ and the front $(U^*,V^*)=(U^*,K^*-\epsilon^2 U^*)$ that comes with it. We can expand these values and obtain:
$$
\begin{aligned}
K^*&=K^*_0+\epsilon^2K_1^*+\mathcal O(\epsilon^4)\\
U^*&=U^*_0+\epsilon^2U_1^*+\mathcal O(\epsilon^4)\\
V^*&=V^*_0+\epsilon^2V_1^*+\mathcal O(\epsilon^4) = K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*+\mathcal O(\epsilon^4)
\end{aligned}
$$
Let's perturb the system to check stability, take $\delta$ smaller than all system scales, and define:
$$\begin{aligned}
U(\xi) &= U^*(\xi)+\delta \exp(\lambda t)u(\xi)\\
V(\xi) &= V^*(\xi)+\delta \exp(\lambda t)v(\xi)
\end{aligned}$$
Inserting this into the PDE and throwing out terms of order $\delta^2$, we get the linearized equations:
$$
\begin{aligned}
\lambda u &= \epsilon^2u_{xx}+f_U(U^*,V^*)u+f_V(U^*,V^*)v\\
\lambda v&= v_{xx}-f_U(U^*,V^*)u-f_V(U^*,V^*)v
\end{aligned}
$$

next, expand $u,v$ as:
$$\begin{aligned}
u&=u_0+\epsilon^2 u_1+\dots\\ 
v&=v_0+\epsilon^2 v_1+\epsilon^4 v_2\dots
\end{aligned}$$

# Expanding it all
Completely expanded we find (check order error lieve makker):
$$
\begin{aligned}
\epsilon^2 \hat\lambda (u_0+\epsilon^2 u_1) &= \epsilon^2(u_0+\epsilon^2 u_1)_{xx}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^6)\\
\epsilon^2 \hat\lambda (v_0+\epsilon^2 v_1)&= (v_0+\epsilon^2 v_1+\epsilon^4 v_2)_{xx}+[-f_U^* -\epsilon^2f_{UU}^* U_1^*-\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[-f_V^* -\epsilon^2f_{VU}^* U_1^*-\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^6)\\
\end{aligned}
$$
adding these two we get:
$$
\begin{aligned}
\epsilon^2 \hat\lambda (u_0+\epsilon^2 u_1+v_0+\epsilon^2 v_1) &= (\epsilon^2u_0+\epsilon^4 u_1+v_0+\epsilon^2 v_1+\epsilon^4 v_2)_{xx}+O(\epsilon^6)\\
\end{aligned}
$$
and in the fast coordinate:
$$
\begin{aligned}
\epsilon^4\hat\lambda (u_0+v_0) &= (\epsilon^2u_0+\epsilon^4 u_1+v_0+\epsilon^2 v_1+\epsilon^4 v_2)_{\xi\xi}+O(\epsilon^6)\\
\end{aligned}
$$
We can now check the equations of all orders:
$$
\begin{aligned}
O(1):\quad 0 &= (v_0)_{\xi\xi}\\
O(\epsilon^2):\quad0 &= (u_0+ v_1)_{\xi\xi}\\
O(\epsilon^4):\quad \hat\lambda (u_0+v_0) &= ( u_1+ v_2)_{\xi\xi}\\
\end{aligned}
$$
Via Fredholm alternative, and $O(1)$ $u$ equations, we need $v_0=0$. Then this reduces to:
$$
\begin{aligned}
O(1):\quad  v_0&=0\\
O(\epsilon^2):\quad0 &= (u_0+ v_1)_{\xi\xi}\\
O(\epsilon^4):\quad \hat\lambda u_0 &= ( u_1+ v_2)_{\xi\xi}\\
\end{aligned}
$$
Furthermore, we know that $u_0=U^*_{0,\xi}$ solves the equation, so we can assume we know $u_0$. Then we also know $v_1 = C-u_0$. Unknowns are then $u_1,v_2$, which will in essence be the first order correction to the translational mode. The question is if this correction will then push $\lambda$ into the positive or negative region. 
The equation for $u_1$ is the following:
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+ v_1f_V^*
$$


# Getting rid of the second order derivatives
$$
\begin{aligned}
0 &= \epsilon^2U^*_{xx}+f(U^*,V^*)\\
0 &= V^*_{xx}-f(U^*,V^*)
\end{aligned}
$$
We expand with:
$$
\begin{aligned}
K^*&=K^*_0+\epsilon^2K_1^*+\mathcal O(\epsilon^4)\\
U^*&=U^*_0+\epsilon^2U_1^*+\mathcal O(\epsilon^4)\\
V^*&=V^*_0+\epsilon^2V_1^*+\mathcal O(\epsilon^4) = K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*+\mathcal O(\epsilon^4)
\end{aligned}
$$
Then we get:
$$
\begin{aligned}
0 &= \epsilon^2(U^*_0+\epsilon^2U_1^*)_{xx}+f(U^*_0+\epsilon^2U_1^*,K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)\\
0 &= (K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)_{xx}-f(U^*_0+\epsilon^2U_1^*,K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)
\end{aligned}
$$
we can add the equations and obtain:
$$
\begin{aligned}
0 &= \epsilon^2(U^*_0+\epsilon^2U_1^*)_{xx}+(K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)_{xx}\\
\end{aligned}
$$
In the fast coordinates:
$$
\begin{aligned}
0 &= (U^*_0+\epsilon^2U_1^*)_{\xi\xi}+f(U^*_0+\epsilon^2U_1^*,K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)\\
0 &= (K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)_{\xi\xi}-\epsilon^2f(U^*_0+\epsilon^2U_1^*,K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)
\end{aligned}
$$
expanding:
$$
\begin{aligned}
f(U^*_0+\epsilon^2U_1^*,K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*) = \\
f(U^*_0,K^*_0)+\epsilon^2f_U(U^*_0,K^*_0)U_1^*+\epsilon^2f_V(U^*_0,K^*_0)( K_1^*- U_0^*)
\end{aligned}
$$
This gives the equations:
$$
\begin{aligned}
0 &= (U^*_0+\epsilon^2U_1^*)_{\xi\xi}+f(U^*_0,K^*_0)+\epsilon^2f_U(U^*_0,K^*_0)U_1^*+\epsilon^2f_V(U^*_0,K^*_0)( K_1^*- U_0^*)\\
0 &= (K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)_{\xi\xi}-\epsilon^2f(U^*_0+\epsilon^2U_1^*,K^*_0+\epsilon^2 K_1^*-\epsilon^2 U_0^*)
\end{aligned}
$$
collecting for real (second eqn not important?)
$$
\begin{aligned}
0 &= (U^*_0)_{\xi\xi}+f(U^*_0,K^*_0)\\
0 &= (U_1^*)_{\xi\xi}+f_U(U^*_0,K^*_0)U_1^*+f_V(U^*_0,K^*_0)( K_1^*- U_0^*)\\
\end{aligned}
$$
Fredholm tells us:
$$
K_1^*  = \frac{\int U^*_0 U^*_{0,\xi} f_V^*}{\int U^*_{0,\xi} f_V^*}
$$

Let's take the derivative of the second equation:
$$
\begin{aligned}
0 &= \partial_\xi(U_1^*)_{\xi\xi} \\
&+\partial_\xi (f_U(U^*_0,K^*_0)U_1^*)\\
&+\partial_\xi(f_V(U^*_0,K^*_0)( K_1^*- U_0^*))\\
&= (U_1^*)_{\xi\xi\xi} \\
&+ f_{UU}(U^*_0,K^*_0)U^*_{0,\xi}U_1^*+f_U(U^*_0,K^*_0)U_{1,\xi}^*\\
&+f_{UV}(U^*_0,K^*_0)U^*_{0,\xi}( K_1^*- U_0^*)+f_V(U^*_0,K^*_0)( - U_{0,\xi}^*)\\
\end{aligned}
$$
Now we look at our original equation for $u_1$:
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+ v_1f_V^*
$$
and we recognize a lot of terms. Let's write our derivative-equation as follows:
$$
\begin{aligned}
0 &= (U_1^*)_{\xi\xi\xi}+f_U^*U_{1,\xi}^* + [f_{UU}^* U_1^*+f_{UV}^*( K_1^*- U_0^*)-f_V^*] u_0\\
\end{aligned}
$$
Finally, note that $v_1=C-u_0$ as we found earlier. Then we can replace a lot of terms and end up with:
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1-[U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*]+Cf_V^*
$$
This seems nice, we got rid of the annoying second derivatives and we don't need $K_1$ anymore. However, we are now stuck with $U_1$. 

However, we can use the fredholm integrability criterion and get:
$$
\langle u_0,\hat\lambda u_0+ [U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*]\rangle = C\int f_V^*u_0 d\xi
$$
writing out int:
$$
\int [\hat\lambda u_0u_0+ u_0U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*u_0] = C\int f_V^*u_0 d\xi
$$
partially integrating the middle term twice (boundary is zero? ?) Aaah twee keer min 1 jaaaa mooi
$$
\int [\hat\lambda u_0^2+ u_{0,\xi\xi}U_{1,\xi}^*+f_U^*U_{1,\xi}^*u_0] = C\int f_V^*u_0 d\xi
$$
using eqn for $u_{0,\xi\xi}$, namely $0= (u_0)_{\xi\xi}+f_U^*u_0$, we get:
$$
\int [\hat\lambda u_0^2+ (-f_U^* u_0)U_{1,\xi}^*+f_U^*U_{1,\xi}^*u_0] = C\int f_V^*u_0 d\xi
$$
The terms neatly cancel, leaving:
$$
\int [\hat\lambda u_0^2] = C\int f_V^*u_0 d\xi
$$
So we find $C$ to be:
$$
C=\hat\lambda\frac{\int  u_0^2}{\int f_V^*u_0 d\xi} 
$$
Which is exactly the same again as $\nu<2$, but needs a whole lot of extra steps haha

# Slow equations
$$
\begin{aligned}
\epsilon^2 \hat\lambda u &= \epsilon^2u_{xx}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)]u\\
&+[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)]v+\mathcal O(\epsilon^4)\\
\epsilon^2 \hat\lambda v&= v_{xx}+[-f_U^* -\epsilon^2f_{UU}^* U_1^*-\epsilon^2f_{UV}^* (K_1^*-U_0^*)]u\\
&+[-f_V^* -\epsilon^2f_{VU}^* U_1^*-\epsilon^2f_{VU}^* (K^*_1-U_0^*)]v+\mathcal O(\epsilon^4)\\
\end{aligned}
$$
We find at leading order:
$$
u = -\frac{f_V^*}{f_U^*}v+\mathcal O(\epsilon^2)
$$
Now we add the equations and find:
$$
\begin{aligned}
\epsilon^2 \hat\lambda u+\epsilon^2 \hat\lambda v &= \epsilon^2u_{xx}+v_{xx}
\end{aligned}
$$
The second order derivative is simply:
$$
u_{xx} = \frac{f_V^*}{f_U^*}v_{xx}
$$
Is it??? Probably smooth enough, but seems wrong somehow, but yea everything is exponentially close to constant so this should definitely work.
Then to leading order we're left with:
$$
\begin{aligned}
\epsilon^2\hat\lambda\frac{f_U^*-f_V^*}{f_U^*}  v &= v_{xx}
\end{aligned}
$$
Then:
$$
v = A\exp\left(\epsilon\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }x\right)+B\exp\left(-\epsilon\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }x\right)
$$
in fast coordinate $x = \epsilon\xi$, we then get on the left:
$$
v = A\exp\left(\epsilon^2\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }\xi \right)
$$
We should match in amplitude to the inner solution, where leading order at the edge, we have $v=\epsilon^2v_1=\epsilon^2C$, so by continuity, $A=\epsilon^2 C$. And therefore the derivative at the edge:
$$
v_\xi(\epsilon^\sigma) = C\epsilon^4\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }
$$
left use the shorthand $\rho_l = \frac{f_U^*-f_V^*}{f_U^*}$ on the left and similarly for $\rho_r$. Then we get:
$$
\Delta_{slow}(v+\epsilon^2 u)_\xi = \Delta_{slow}v_\xi+O(\epsilon^2) = -C\epsilon^4\sqrt{\hat\lambda}(\sqrt{\rho_r}+\sqrt{\rho_l})
$$
Very nice, let's fill $C$ in too:
$$
\Delta_{slow}(v+\epsilon^2 u)_\xi = -\hat\lambda\frac{\int  u_0^2}{\int f_V^*u_0 d\xi}\epsilon^4\sqrt{\hat\lambda}(\sqrt{\rho_r}+\sqrt{\rho_l}) 
$$
At the same time however, we find:
$$
\Delta_{fast}(v+\epsilon^2 u)_\xi=\int (v+\epsilon^2 u)_{\xi\xi}=\epsilon^4\hat\lambda\int u_0 
$$
So comparing jumps, we end up with:
$$
\epsilon^4\hat\lambda\int u_0  = -\hat\lambda\frac{\int  u_0^2}{\int f_V^*u_0 d\xi}\epsilon^2\sqrt{\hat\lambda}(\sqrt{\rho_r}+\sqrt{\rho_l}) 
$$
and after some simplifying:
$$
\int u_0  = -\frac{\int  u_0^2}{\int f_V^*u_0 d\xi}\sqrt{\hat\lambda}(\sqrt{\rho_r}+\sqrt{\rho_l}) 
$$
So then we only get solutions with positive, order $\epsilon^2$ $\lambda$ when:
$$
\int u_0 d\xi\int f_V^*u_0 d\xi<0
$$
