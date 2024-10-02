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
$$
f(U_0+\epsilon^{\beta}U_1+\dots,(V_0+\epsilon^{\beta}V_1+\dots))=f(U_0,V_0)+\epsilon^\beta f_U(U_0,V_0)U_1+\epsilon^\beta f_V(U_0,V_0)V_1+\dots
$$

## Full, slow system
$$
\begin{gather}
\epsilon^\alpha c (U_0)_x+ \epsilon^{\alpha+\beta}c (U_1)_x \\=  \epsilon^2(U_0)_{xx}+\epsilon^{\beta+2}(U_1)_{xx}+f(U_0,V_0)+\epsilon^\beta f_U(U_0,V_0)U_1+\epsilon^\beta f_V(U_0,V_0)V_1+\dots \\
\epsilon^\alpha c(V_0)_x+\epsilon^{\beta+\alpha}c(V_1)_x \\= (V_0)_{xx}+\epsilon^{\beta}(V_1)_{xx}-f(U_0,V_0)-\epsilon^\beta f_U(U_0,V_0)U_1-\epsilon^\beta f_V(U_0,V_0)V_1+\dots
\end{gather}
$$
Assuming $\alpha,\beta>0$, we get at leading order:
$$
\begin{aligned}
0=  f(U_0,V_0) \\
0= (V_0)_{xx}-f(U_0,V_0)
\end{aligned}
$$
Cool takeaway: any wavespeed or expansion-> to leading order at fixedpoints in slow region.
## Full, fast system
Consider the slow traveling coordinate $\epsilon\xi=x$. Then we get $u_x=u_\xi\xi_x=u_\xi/\epsilon$:
$$
\begin{gather}
\epsilon^{\alpha-1} c (U_0)_\xi+ \epsilon^{\alpha+\beta-1}c (U_1)_\xi \\=  (U_0)_{\xi\xi}+\epsilon^{\beta}(U_1)_{\xi\xi}+f(U_0,V_0)+\epsilon^\beta f_U(U_0,V_0)U_1+\epsilon^\beta f_V(U_0,V_0)V_1+\dots \\
\epsilon^{\alpha+1} c(V_0)_\xi+\epsilon^{\beta+\alpha+1}c(V_1)_\xi \\= (V_0)_{\xi\xi}+\epsilon^{\beta}(V_1)_{\xi\xi}-\epsilon^{2}f(U_0,V_0)-\epsilon^{\beta+2} f_U(U_0,V_0)U_1-\epsilon^{\beta+2} f_V(U_0,V_0)V_1+\dots
\end{gather}
$$

If $\alpha=1$, to leading order, these equations read:
$$
\begin{aligned}
c (U_0)_\xi=  (U_0)_{\xi\xi}+f(U_0,V_0) \\
0= (V_0)_{\xi\xi}
\end{aligned}
$$
This should be a heteroclinic orbit that connects the plateaus+corrections from nearby other fronts. 
Takeaway: $\forall \alpha,\beta$ is $V_0$ to leading order constant. 
#### Niet mogelijk??
$$
\epsilon^{2+0\beta}(U_{0})_{xx}+\epsilon^{2+1\beta}(U_{1})_{xx}+\epsilon^{2+2\beta}(U_{2})_{xx}+\epsilon^{2+3\beta}(U_{3})_{xx}+\epsilon^{2+4\beta}(U_{4})_{xx}+\epsilon^{2+5\beta}(U_{5})_{xx}+\epsilon^{2+6\beta}(U_{6})_{xx}+\epsilon^{2+7\beta}(U_{7})_{xx}+\epsilon^{2+8\beta}(U_{8})_{xx}+\epsilon^{2+9\beta}(U_{9})_{xx}
$$


slow subsystem ($\alpha=1,\beta=1$), order=0 $$\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}$$ fast subsystem ($\alpha=1,\beta=1$), order=0 $$\begin{aligned} c(U_{0})_{\xi} &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}$$



slow subsystem ($\alpha=1,\beta=1$), order=1 $$\begin{aligned} c(U_{0})_{x} &=f_{V}+f_{U} \\ c(V_{0})_{x} &=(V_{1})_{xx}+f_{V}+f_{U} \end{aligned}$$ fast subsystem ($\alpha=1,\beta=1$), order=1 $$\begin{aligned} c(U_{1})_{\xi} &=(U_{1})_{\xi\xi}+f_{V}+f_{U} \\ 0 &=(V_{1})_{\xi\xi} \end{aligned}$$



slow subsystem ($\alpha=1,\beta=100$), order=0 $$\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}$$ fast subsystem ($\alpha=1,\beta=100$), order=0 $$\begin{aligned} c(U_{0})_{\xi} &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}$$
## $\alpha=2$ en $\beta$ klein 
#### Leading
slow subsystem ($\alpha=2,\beta=100$), order=0 $$\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}$$ fast subsystem ($\alpha=2,\beta=100$), order=0 $$\begin{aligned} 0 &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}$$
#### Next
slow subsystem ($\alpha=2,\beta=100$), order=1 $$\begin{aligned} c(U_{0})_{x} &=(U_{0})_{xx} \\ c(V_{0})_{x} &=0 \end{aligned}$$ fast subsystem ($\alpha=2,\beta=100$), order=1 $$\begin{aligned} c(U_{0})_{\xi} &=0 \\ 0 &=0 \end{aligned}$$

## $\alpha=2$ en $\beta=1$ (had ik uitgewerkt)
Dit geeft geen closed systeem aan vergelijkingen :(
#### Leading
slow subsystem ($\alpha=2,\beta=1$), order=0 $$\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}$$ fast subsystem ($\alpha=2,\beta=1$), order=0 $$\begin{aligned} 0 &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}$$
#### Next
slow subsystem ($\alpha=2,\beta=1$), order=1 $$\begin{aligned} 0 &=f_{V}+f_{U} \\ 0 &=(V_{1})_{xx}+f_{V}+f_{U} \end{aligned}$$ fast subsystem ($\alpha=2,\beta=1$), order=1 $$\begin{aligned} c(U_{0})_{\xi} &=(U_{1})_{\xi\xi}+f_{V}+f_{U} \\ 0 &=(V_{1})_{\xi\xi} \end{aligned}$$
#### Even higher
slow subsystem ($\alpha=2,\beta=1$), order=2 $$\begin{aligned} c(U_{0})_{x} &=(U_{0})_{xx}+f_{VV}+2f_{UV}+f_{UU} \\ c(V_{0})_{x} &=(V_{2})_{xx}+f_{VV}+2f_{UV}+f_{UU} \end{aligned}$$ fast subsystem ($\alpha=2,\beta=1$), order=2 $$\begin{aligned} c(U_{1})_{\xi} &=(U_{2})_{\xi\xi}+f_{VV}+2f_{UV}+f_{UU} \\ 0 &=(V_{2})_{\xi\xi}+f_{} \end{aligned}$$


# $\alpha=2=\beta$ (nieuw)
Ook geen closed systeem :(
#### Leading order
slow subsystem ($\alpha=2,\beta=2$), order=0 $$\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}$$ fast subsystem ($\alpha=2,\beta=2$), order=0 $$\begin{aligned} 0 &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}$$
#### Next order

slow subsystem ($\alpha=2,\beta=2$), order=1 $$\begin{aligned} c(U_{0})_{x} &=(U_{0})_{xx}+f_{V}+f_{U} \\ c(V_{0})_{x} &=(V_{1})_{xx}+f_{V}+f_{U} \end{aligned}$$ fast subsystem ($\alpha=2,\beta=2$), order=1 $$\begin{aligned} c(U_{0})_{\xi} &=0 \\ 0 &=0 \end{aligned}$$
#### Even higher order
slow subsystem ($\alpha=2,\beta=2$), order=2 $$\begin{aligned} c(U_{1})_{x} &=(U_{1})_{xx}+f_{VV}+2f_{UV}+f_{UU} \\ c(V_{1})_{x} &=(V_{2})_{xx}+f_{VV}+2f_{UV}+f_{UU} \end{aligned}$$ fast subsystem ($\alpha=2,\beta=2$), order=2 $$\begin{aligned} 0 &=(U_{1})_{\xi\xi}+f_{V}+f_{U} \\ 0 &=(V_{1})_{\xi\xi}+f_{} \end{aligned}$$

# $\alpha=\beta=1$ (Nieuw, werkt hopelijk wel)
#### Leading
slow subsystem ($\alpha=1,\beta=1$), order=0 $$\begin{aligned} 0 &=f_{} \\ 0 &=(V_{0})_{xx}+f_{} \end{aligned}$$ fast subsystem ($\alpha=1,\beta=1$), order=0 $$\begin{aligned} c(U_{0})_{\xi} &=(U_{0})_{\xi\xi}+f_{} \\ 0 &=(V_{0})_{\xi\xi} \end{aligned}$$
#### Next
slow subsystem ($\alpha=1,\beta=1$), order=1 $$\begin{aligned} c(U_{0})_{x} &=f_{V}+f_{U} \\ c(V_{0})_{x} &=(V_{1})_{xx}+f_{V}+f_{U} \end{aligned}$$ fast subsystem ($\alpha=1,\beta=1$), order=1 $$\begin{aligned} c(U_{1})_{\xi} &=(U_{1})_{\xi\xi}+f_{V}+f_{U} \\ 0 &=(V_{1})_{\xi\xi} \end{aligned}$$
#### Even higher
slow subsystem ($\alpha=1,\beta=1$), order=2 $$\begin{aligned} c(U_{1})_{x} &=(U_{0})_{xx}+f_{VV}+2f_{UV}+f_{UU} \\ c(V_{1})_{x} &=(V_{2})_{xx}+f_{VV}+2f_{UV}+f_{UU} \end{aligned}$$ fast subsystem ($\alpha=1,\beta=1$), order=2 $$\begin{aligned} c(U_{2})_{\xi} &=(U_{2})_{\xi\xi}+f_{VV}+2f_{UV}+f_{UU} \\ c(V_{0})_{\xi} &=(V_{2})_{\xi\xi}+f_{} \end{aligned}$$
