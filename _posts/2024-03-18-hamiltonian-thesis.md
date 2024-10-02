---
layout: post
title: "Hamiltonian Thesis"
date: 2024-03-18
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

The heteroclinic orbit is an equipotential line of the hamiltonian, so $$E$$ parametrizes the orbit:
<div class="math-container">\[
\frac12 (u_x)^2+F(u)=E\quad\forall u\\
\]</div>
Note that indeed:
<div class="math-container">\[
\frac{d}{dx}E = u_{xx}+F'(u)=u_{xx}+\frac{1}{\delta}\tilde f(u,\eta_0)=0
\]</div>
By the equations of motion. So indeed $$E$$ is conserved, and the system is hamiltonian.
We can solve now:
<div class="math-container">\[
u_x = \pm \sqrt{2E-2 F(u)}
\]</div>
Since $$F(u)\leq E\quad\forall u$$ and $$F(u)<E$$ outside the limit points, we know that this always exists for all $$u$$ and therefore all $$x$$. 
Consider a small translation: $$\tilde u(x)=u(x+dx)$$ The difference is given by $$u(x)-\tilde u(x)$$. Then of course for a small translation $$dx$$, the difference is to first order given by $$u_xdx$$. This is then the mode that has $$\lambda=0$$, and has no zeros, since $$u_x = \pm \sqrt{2E-2 F(u)}$$. Sturm-Liouville theory tells us that the mode with no zeros has the highest eigenvalue. Therefore, for 1D systems, the system is stable. 


# Numerics 
<div class="math-container">\[
\frac{\Delta u}{\Delta x} = \sqrt{2E-2F(u)}
\]</div>

[View Raw Markdown](/assets/md/Hamiltonian Thesis.md)
