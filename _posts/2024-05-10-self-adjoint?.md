---
layout: post
title: "Self adjoint?"
date: 2024-05-10
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

The linear stability problem can be written as:
<div class="math-container">\[
\begin{aligned}
\lambda u=\epsilon^2u_{xx}+f_U(\bar U,\bar V)u+f_V(\bar U,\bar V)v\\
\lambda v=v_{xx}-f_U(\bar U,\bar V)u-f_V(\bar U,\bar V)v
\end{aligned}
\]</div>
Or in matrix form:
<div class="math-container">\[
\lambda \begin{pmatrix}u\\v\end{pmatrix}=\left(\begin{pmatrix}\epsilon^2\partial_{xx}&0\\0&\partial_{xx}\end{pmatrix}+\begin{pmatrix}f_U(\bar U,\bar V)&f_V(\bar U,\bar V)\\ -f_U(\bar U,\bar V)&-f_V(\bar U,\bar V)\end{pmatrix}\right)\begin{pmatrix}u\\v\end{pmatrix}
\]</div>
Or the shorthand, using $$p=\begin{pmatrix}u\\v\end{pmatrix}$$, $$D=\begin{pmatrix}\epsilon^2\partial_{xx}&0\\0&\partial_{xx}\end{pmatrix}$$ and $$A(x)=\begin{pmatrix}f_U(\bar U,\bar V)&f_V(\bar U,\bar V)\\ -f_U(\bar U,\bar V)&-f_V(\bar U,\bar V)\end{pmatrix}$$, we can write it as:
<div class="math-container">\[
L(x)p=(A(x)+D)p = \lambda p
\]</div>
Now the question becomes, is $$L(x)$$ self-adjoint? Well we check using the definition:
<div class="math-container">\[\begin{aligned}
\langle g,Lh\rangle&=
\int g(x)\cdot L(x)h(x)dx\\
&=\int g(x)\cdot A(x)h(x)dx +\int g(x)\cdot Dh(x)dx 
\end{aligned}\]</div>
We can partially integrate twice, use zero-flux BC's and get:
<div class="math-container">\[\begin{aligned}
&\int g(x)\cdot A(x)h(x)dx +\int g(x)\cdot Dh(x)dx \\
=&\int g(x)\cdot A(x)h(x)dx +\int Dg(x)\cdot h(x)dx
\end{aligned}
\]</div>
But $$A$$ is not selfadjoint :(



[View Raw Markdown](/assets/md/Self adjoint?.md)
