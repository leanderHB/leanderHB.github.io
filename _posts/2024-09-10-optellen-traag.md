---
layout: post
title: "Optellen traag"
date: 2024-09-10
---
<div>\[
\begin{aligned}
\epsilon^2 \hat\lambda (u_0+\epsilon^2 u_1) &= \epsilon^2(u_0+\epsilon^2 u_1)_{xx}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^4)\\
\epsilon^2 \hat\lambda (v_0+\epsilon^2 v_1)&= (v_0+\epsilon^2 v_1+\epsilon^4 v_2)_{xx}+[-f_U^* -\epsilon^2f_{UU}^* U_1^*-\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[-f_V^* -\epsilon^2f_{VU}^* U_1^*-\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^4)\\
\end{aligned}
\]</div>

adding together:
<div>\[
\begin{aligned}
\epsilon^2 \hat\lambda (u_0+\epsilon^2 u_1+v_0+\epsilon^2 v_1) &= (\epsilon^2u_0+\epsilon^4 u_1+v_0+\epsilon^2 v_1+\epsilon^4 v_2)_{xx}+O(\epsilon^6)\\
\end{aligned}
\]</div>
by order:
<div>\[
\begin{aligned}
O(1):\quad 0&= v_0\\
O(\epsilon^2):\quad  \hat\lambda (u_0 +v_0) &= (u_0+ v_1)_{xx}\\
O(\epsilon^4):\quad  \hat\lambda ( u_1+ v_1) &= ( u_1+ v_2)_{xx}\\
\end{aligned}
\]</div>
we can quickly fill in $$v_0$$ to find:
<div>\[
\begin{aligned}
O(1):\quad v_0&= 0\\
O(\epsilon^2):\quad  \hat\lambda u_0  &= (u_0+ v_1)_{xx}\\
O(\epsilon^4):\quad  \hat\lambda ( u_1+ v_1) &= ( u_1+ v_2)_{xx}\\
\end{aligned}
\]</div>
we can use the equations for $$u$$:
<div>\[
\begin{aligned}
0 &= f_U^*u_0+f_V^*v_0\\
\epsilon^2 \hat\lambda u_0 &= \epsilon^2(u_0)_{xx}+[f_U^* +\epsilon^2f_{UU}^* U_1^*+\epsilon^2f_{UV}^* (K_1^*-U_0^*)](u_0+\epsilon^2 u_1)\\
&+[f_V^* +\epsilon^2f_{VU}^* U_1^*+\epsilon^2f_{VU}^* (K^*_1-U_0^*)](v_0+\epsilon^2 v_1+\epsilon^4 v_2)+\mathcal O(\epsilon^4)\\
\end{aligned}
\]</div>
and now we're very sad haha :(