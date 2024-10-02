---
layout: post
title: "Kerstboom"
date: 2024-05-29
---
<style>
.math-container {
    max-width: 100%; /* Set a maximum width to prevent it from expanding the page */
    overflow-x: auto; /* Enable horizontal scrolling */
    white-space: nowrap; /* Prevent the text from wrapping */
}
</style>
<div class="math-container">\[\begin{aligned}
U_t &=\epsilon^2 U_{xx}+f(U,V)\\
V_t &= V_{xx}-f(U,V)
\end{aligned}\]</div>
Do the $$\epsilon^2 U+V=K$$ trick, and define:
<div class="math-container">\[
(U_{het},V_{het})
\]</div>
as the heteroclinic solution to the planar Hamiltonian system (parameterized by K) that arises:
<div class="math-container">\[
(U_{het})_{xx}+f(U_{het},K-\epsilon^2 U_{het})=0
\]</div>
Define the fast subsystem as:
<div class="math-container">\[\begin{aligned}
\tilde U_t=\tilde U_{xx}+f(\tilde U,\tilde V)\\
\epsilon^2\tilde V_t=\tilde V_{xx}-\epsilon^2f(\tilde U,\tilde V)
\end{aligned}\]</div>
We find: $$\tilde V=\tilde V_0+\epsilon^2 \tilde V_2+O(\epsilon^3)$$, hence:
<div class="math-container">\[
\tilde U_t=\tilde U_{xx}+f(\tilde U,\tilde V_0+\epsilon^2 \tilde V_2)\\
\]</div>
We'd like to paste things together, so we pick $$\tilde V_0=K$$? voelt niet helemaal legaal dit.
<div class="math-container">\[
\tilde U_t=\tilde U_{xx}+f(\tilde U,\tilde V_0+\epsilon^2 \tilde V_2)\\
\]</div>

