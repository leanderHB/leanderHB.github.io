---
layout: post
title: "Thesis first time looking ever"
date: 2024-10-02
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

<div class="math-container">\[
\begin{align}
u_t = f(u,v)+\delta\Delta u\\
v_t = -f(u,v)+\Delta v
\end{align}
\]</div>
Now consider $$u_t=v_t=0$$, then:
<div class="math-container">\[
\begin{align}
0 = f(u,v)+\delta\Delta u\\
0 = -f(u,v)+\Delta v
\end{align}
\]</div>
Just add these two expressions to obtain:
<div class="math-container">\[
\begin{align}
0 = f(u,v)+\delta\Delta u-f(u,v)+\Delta v\\
0=\delta \Delta u+\Delta v\implies \Delta v=\delta \Delta u
\end{align}
\]</div>
Now also:
<div class="math-container">\[
\begin{align}
0 = f(u,v)+\delta\Delta u\\
0 = -f(u,v)+\Delta v
\end{align}
\]</div>

<img src="/assets/images/Pasted image 20231201202900.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20231201202900.png">
<img src="/assets/images/Pasted image 20231201202910.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20231201202910.png">

# Vragen
- is er een soort theorie om van systeem integraal vergelijking te maken? (En is dat nuttig?)
- en dan lokale operator norm oid te definieren
- plaatje klopt niet met [formule: link](https://www.wolframalpha.com/input?i=ContourPlot%5Bu*v+-+%284*u%29%2F%28u+%2B+2%29+%3D+0%2C+%7Bu%2C+0%2C+10%7D%2C+%7Bv%2C+0%2C+10%7D%5D)? 
- 


<img src="/assets/images/Pasted image 20231206133814.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20231206133814.png">

[53] V. Maz’ya, J. Rossmann, On the Agmon–Miranda maximum principle for solutions of strongly elliptic equa-
tions in domains of R n with conical points, Ann. Global Anal. Geom. 10 (1992) 125–150



<img src="/assets/images/Pasted image 20240127230545.png" class="img-fluid rounded z-depth-1" alt="Pasted image 20240127230545.png">

[View Raw Markdown](/assets/md/Thesis first time looking ever.md)
