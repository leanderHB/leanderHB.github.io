Consider traveling wave coordinates $x = \chi+\epsilon^\alpha c t$ where $\chi$ is the ordinary space coordinate. Then:
$$
U_{t} = U_xx_t = \epsilon^\alpha c U_x
$$
Our pde then becomes:
$$
\begin{aligned}
\epsilon^\alpha c U_x &= \epsilon^2 U_{xx}+f(U,V)\\
\epsilon^\alpha c V_x &= V_{xx}-f(U,V)\\
\end{aligned}
$$
We can expand $U$ as $U_0+\epsilon^{\beta}U_1+\epsilon^{2\beta}U_2+\dots$ and similarly for $V$, then we get, in all its glory:
$$
\begin{aligned}
\epsilon^\alpha c (U_0+\epsilon^{\beta}U_1+\dots)_x &= \epsilon^2 (U_0+\epsilon^{\beta}U_1+\dots)_{xx}+f(U_0+\epsilon^{\beta}U_1+\dots,(V_0+\epsilon^{\beta}V_1+\dots))\\
\epsilon^\alpha c (V_0+\epsilon^{\beta}V_1+\dots)_x &= (V_0+\epsilon^{\beta}V_1+\dots)_{xx}-f((U_0+\epsilon^{\beta}U_1+\dots),(V_0+\epsilon^{\beta}V_1+\dots))\\
\end{aligned}
$$
We can Taylor expand $f$ to get:
$$\begin{gather}
f(U_0+\epsilon^{\beta}U_1+\dots,(V_0+\epsilon^{\beta}V_1+\dots))\\=f(U_0,V_0)+\epsilon^\beta f_U(U_0,V_0)(U-U_0)+\epsilon^\beta f_V(U_0,V_0)(V-V_0)+\dots
\end{gather}$$

### Outer equations
order: $\epsilon^0$
$$\begin{aligned}0&=f \\0&=-f + (V_0)_{xx} \end{aligned}$$
order: $\epsilon^1$
$$\begin{aligned}0&=-c(U_0)_x + f_{U}U_1 + f_{V}V_1 \\0&=-c(V_0)_x - f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} \end{aligned}$$
order: $\epsilon^2$:
$$\begin{aligned}0&=-c(U_1)_x + f_{U}U_2 + f_{UU}U_1^2 + f_{UV}U_1V_1 + f_{V}V_2 + f_{VV}V_1^2 + (U_0)_{xx} \\0&=-c(V_1)_x - f_{U}U_2 - f_{UU}U_1^2 - f_{UV}U_1V_1 - f_{V}V_2 - f_{VV}V_1^2 + (V_2)_{xx} \end{aligned}$$
### Inner equations
order: $\epsilon^0$
$$\begin{aligned}0&=-c(U_0)_\xi  + f + (U_0)_{\xi \xi } \\0&=(V_0)_{\xi \xi } \end{aligned}$$
order: $\epsilon^1$
$$\begin{aligned}0&=-c(U_1)_\xi  + f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\0&=-c(V_0)_\xi  + (V_1)_{\xi \xi } \end{aligned}$$

#### outer gives:
$$
V_0(x)=V_0, \quad U_0(x)=U_0
$$
then to second order we add the equations to get (note $(V_0)_x=(U_0)_x=0$):
$$\begin{aligned}
0&=-0 + f_{U}U_1 + f_{V}V_1 \\
0&=-0 - f_{U}U_1 - f_{V}V_1 + (V_1)_{xx} 
\end{aligned}$$
Then:
$$
(V_1)_{xx} = 0\implies V_1(x)=V_1
$$
So:
$$
U_1 =-f_V /f_UV_1
$$

#### Inner gives:
order: $\epsilon^0$
$$\begin{aligned}
0&=-c(U_0)_\xi  + f(U_0(\xi),V_0) + (U_0)_{\xi \xi } \\
V_0(\xi)&=V_0
\end{aligned}$$
Which is a non-linear problem, 
order: $\epsilon^1$
$$\begin{aligned}
0&=-c(U_1)_\xi  + f_{U}U_1 + f_{V}V_1 + (U_1)_{\xi \xi } \\
V_1(\xi)&=V_1 
\end{aligned}$$
another Sturm-Liouville problem
