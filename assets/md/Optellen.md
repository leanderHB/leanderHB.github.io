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
Completely expanded we find (check order error lieve makker):
$$
\begin{aligned}
\epsilon^2 \hat\lambda (u_0+\epsilon^2 u_1) &= \epsilon^2(u_0+\epsilon^2 u_1)_{xx}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^6)\\
\epsilon^2 \hat\lambda (v_0+\epsilon^2 v_1)&= (v_0+\epsilon^2 v_1+\epsilon^4 v_2)_{xx}+[-f_U^* -\epsilon^2f_{UU}^* U_1^*-\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[-f_V^* -\epsilon^2f_{VU}^* U_1^*-\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^6)\\
\end{aligned}
$$adding these two we get:
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
Furthermore, we know that $u_0=U^*_{0,\xi}$ solves the equation, so we can assume we know $u_0$. Then we also know $v_1$ (integration constant = 0 because Fredholm?). Unknowns are then $u_1,v_2$, which will in essence be the first order correction to the translational mode. The question is if this correction will then push $\lambda$ into the positive or negative region. So all that's left is to solve $u_1$, then we should find $v_2$ by the third equation. 
The equation for $u_1$ is the following:
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+ v_1f_V^*
$$
In principle, the operator is the same as what we found earlier:
$$
u_1 = \mathcal L^{-1}g(\xi)
$$
Where $g(\xi)$ is:
$$

$$




# Equations for $U_1^*$ etc
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
collecting powers:
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
Finally, note that $v_1=-u_0$ as we found earlier. Then we can replace a lot of terms and end up with:
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1-[U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*]
$$
This seems nice, we got rid of the annoying second derivatives and we don't need $K_1$ anymore. However, we are now stuck with $U_1$. 
So, let's use the Fredholm alternative to find that solutions should satisfy:
$$
\langle \hat\lambda u_0 +U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*,u_0\rangle = 0
$$
Since $u_0$ goes to zero exponentially, we can maybe use partial integration to find some relations. 
Something else we could do is fill our result into the equation for $\Delta v_\xi$ [[Netjes order nu=2]] and we get:
(does this integral converge? can i replace with over entire R?)
$$
\begin{aligned}
\Delta_{fast} v_{\xi}^*&=\epsilon^4\int_\mathbb R [\hat\lambda u_0-u_{1,\xi\xi}]d\xi+O(\epsilon^6)
\end{aligned}
$$
Then we find after filling in:
$$
\begin{aligned}
\Delta_{fast} v_{\xi}^*&=\epsilon^4\int_\mathbb R [\hat\lambda f_U^* u_1-[U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*]]d\xi+O(\epsilon^6)
\end{aligned}
$$
The integral over $U^*_{1,\xi\xi\xi}$ will be zero, by the boundary conditions, so we're left with:
$$
\begin{aligned}
\Delta_{fast} v_{\xi}^*&=\epsilon^4\int_\mathbb R [\hat\lambda f_U^* u_1-f_U^*U_{1,\xi}^*]d\xi+O(\epsilon^6)
\end{aligned}
$$


oke maar waarom doe ik moeilijk, kan niet gewoon $\Delta_{fast}(v+u)_\xi$ gematched worden?

