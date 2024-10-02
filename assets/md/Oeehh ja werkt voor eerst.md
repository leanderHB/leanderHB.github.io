Oke hier 1 vergelijking die $U_1^*$ geeft als inverse van SL probleem:
$$
0 = (U_1^*)_{\xi\xi}+f_U(U^*_0,K^*_0)U_1^*+f_V(U^*_0,K^*_0)( K_1^*- U_0^*)
$$
Hier een die het meest "promising" is, probleem is wel dat ik $U_1^*$ niet expliciet heb.
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0-u_0f_V^*
$$
Misschien vinden we de hoge afgeleiden niet leuk, dan kun je het volgende doen:
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1-[U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*]
$$


ben ik dom? 

$C>0,\int U_{0,\xi}>0$, dan $\Delta_{slow}<0$, dus $\lambda<0$. 
$C<0,\int U_{0,\xi}>0$, dan $\Delta_{slow}>0$, dus $\lambda>0$.  maar dat kan helemaal niet want 


In essentie heb ik:
$$\begin{aligned}
v_0&=0\\
(v_1+ u_0)_{\xi\xi}&=0\\
(v_2+ u_1)_{\xi\xi} &= \hat\lambda u_0
\end{aligned}$$
dus:
$$\begin{aligned}
\Delta_{fast}(v+ \epsilon^2 u)_{\xi}&=\int (v+\epsilon^2 u)_{\xi\xi} d\xi\\
&=\int (v_0+\epsilon^2v_1+\epsilon^4v_2+\epsilon^2 u_0+\epsilon^4 u_1)_{\xi\xi} d\xi \\
&=\int(\epsilon^4v_2+\epsilon^4 u_1)_{\xi\xi} d\xi 
\\&=\epsilon^4 \hat\lambda \int  u_0 d\xi
\end{aligned}$$

$$\begin{aligned}
(v_1+ u_0)_{\xi\xi}&=0\\
(v_1+ u_0)&=C
\end{aligned}$$
# Bad take I think
use this eqn:
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)]u_0+ v_1f_V^*
$$
filling $v_1$ in we find:
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1+[ f_{UU}^* U_1^*+f_{UV}^* (K_1^*-U_0^*)-f_V^*]u_0+ Cf_V^*
$$
Integrability shows:
$$
\langle  u_0[\hat \lambda- f_{UU}^* U_1^*-f_{UV}^* (K_1^*-U_0^*)+f_V^*],u_0 \rangle = C\int u_0f_V^*
$$
where:
$$
K_1^*  = \frac{\int U^*_0 U^*_{0,\xi} f_V^*}{\int U^*_{0,\xi} f_V^*}
$$
# maybe better?
$$
\hat\lambda u_0 = u_{1,\xi\xi}+f_U^* u_1-[U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*]+Cf_V^*
$$
integrability:
$$
\langle u_0,\hat\lambda u_0+ [U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*]\rangle = C\int f_V^*u_0 d\xi
$$
writing out int:
$$
\int [\hat\lambda u_0u_0+ u_0U_{1,\xi\xi\xi}^*+f_U^*U_{1,\xi}^*u_0] = C\int f_V^*u_0 d\xi
$$
partially integrating the middle term twice (boundary is zero? ?)
$$
\int [\hat\lambda u_0^2+ u_{0,\xi\xi}U_{1,\xi}^*+f_U^*U_{1,\xi}^*u_0] = C\int f_V^*u_0 d\xi
$$
using eqn for $u_{0,\xi\xi}$, namely $0= (u_0)_{\xi\xi}+f_U^*u_0+f_V^*v_0$, we get:
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


#### Staartjes

we krijgen iets als:
$$
\epsilon^2\hat\lambda\frac{\int  u_0^2d\xi}{\int f_V^*u_0 d\xi} \cdot \epsilon^2 \sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }=\epsilon^4\hat \lambda \int u_0 d\xi
$$
simplifying:
$$
\frac{\int  u_0^2d\xi}{\int f_V^*u_0 d\xi} \cdot  \sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }=  \int u_0 d\xi
$$
This solution with positive $\lambda$ can therefore only exist if the $f_V$ integral has a certain sign. Wonder if we can say more about this? 



ho dit klopt niet helemaal haha:
$$
v = A\exp\left(\epsilon\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }x\right)+B\exp\left(-\epsilon\sqrt{\hat\lambda\frac{f_U^*-f_V^*}{f_U^*} }x\right)
$$




Hoi Arjen,  

ik heb een vraag. Ik kwam er achter dat alles een stuk beter werkt als je de sprong in v+epsilon^2 u bekijkt in plaats van alleen v. Dan is de sprong gelijk aan lambda keer de integraal over U_0,\xi, de afgeleide van het front, en dus, de sprong is even groot als het verschil tussen de plateaus, keer lambda. Nou dat vond ik al wel een leuk resultaat, maar het probleem is nu het matchen aan de slow region. Ik heb gevonden dat de leading order termen voor v en u elkaar "cancellen" in v+epsilon^2 u (en dat u_0=U_0,xi, wat jij eerder ook had gevonden). Dus ik kijk naar de volgende orde benadering, en die wordt inderdaad niet exponentieel klein op de rand van de inner region, dus die is ergens aan te matchen. Het probleem is nu, dat ik de waarde op de rand niet weet te fixen, die is nodig om de amplitude van de afgeleide vast te zetten, en daarmee te kijken of lambda positief of negatief moet zijn. Als de amplitude negatief is, kun je met een positieve sprong de boel matchen, en kan lambda dus positief zijn. Ergens moet ik de keuze voor u_0 = U_0,\xi of u_0 = -U_0,\xi koppelen aan de amplitude van u_1 op de randen, maar ik kom er niet helemaal uit met de vergelijkingen. Ik heb een boel vergelijkingen die de SL operator hebben en een of andere, bekende, inhomogene term, maar ik zie niet hoe dat me gaat helpen met u_1 bepalen.  

ZIe hier een aantal voorbeelden:

![image.png](blob:https://mail.google.com/624c03db-16dd-47fc-9747-c93716c0e2ed)  

Eerder koppelde jij die waarde op de rand aan \hat K, die je via een Fredholm conditie kon vinden, en als ik me goed herinner, een vaste sign had. Dat is de "heilige graag" denk ik, maar doordat we lambda order epsilon^2 hebben, is v niet meer leading order constant in de fast region, het is nu dus epsilon^2 U_0,\xi, en dus heeft de leading order term niks meer te zeggen over de waarde op de rand (want exponentially klein daar). Ik hoop u_1 niet expliciet te kunnen vinden, want ik word niet heel blij van de SL problemen hier boven, dus ik vroeg me af of jij toevallig een truc in je trucendoos hebt voor dit type probleem. Sidenote:

omdat (v+epsilon^2 u)_xixi = \hat lambda u_0, kun je twee keer integreren en v+epsilon^2 u expliciet vinden in de fast region, behalve de integration constant, die precies de amplitude op de rand geeft.