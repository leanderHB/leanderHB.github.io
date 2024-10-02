---
layout: post
title: "Proberen operator als perturbed"
date: 2024-10-01
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

<div class="math-container">\[
\mathcal L = \mathcal L_0+\epsilon \mathcal L_1+\dots
\]</div>
<div class="math-container">\[
	\lambda\begin{pmatrix}u\\v\end{pmatrix} = \begin{pmatrix}\partial_{\xi\xi}+f^*_U&f_V^* \\ -\epsilon^2 f^*_U&\partial_{\xi\xi}-\epsilon^2 f_V^* \end{pmatrix} \begin{pmatrix}u\\v\end{pmatrix}
\]</div>
expanding:
<div class="math-container">\[
(\lambda_0+\epsilon^2\lambda_1+\dots)\begin{pmatrix}u_0+\epsilon^2 u_1+\dots\\ v_0+\epsilon^2 v_1+\epsilon^4 v_2+\dots\end{pmatrix} = \begin{pmatrix}\partial_{\xi\xi}+f^*_U&f_V^* \\ \epsilon^2 f^*_U&\partial_{\xi\xi}-\epsilon^2 f_V^* \end{pmatrix} \begin{pmatrix}u_0+\epsilon^2 u_1+\dots\\ v_0+\epsilon^2 v_1+\epsilon^4 v_2+\dots\end{pmatrix}
\]</div>

collecting powers

<div class="math-container">\[
\lambda\begin{pmatrix}u\\v\end{pmatrix} = \begin{pmatrix}\partial_{\xi\xi}+f^*_U&f_V^* \\ 0&\partial_{\xi\xi} \end{pmatrix} \begin{pmatrix}u\\v\end{pmatrix}
\]</div>


<div class="math-container">\[
\lambda\begin{pmatrix}v+\epsilon^2 u\\v\end{pmatrix} = \begin{pmatrix}\partial_{\xi\xi}+f^*_U&f_V^* \\ -\epsilon^2 f^*_U&\partial_{\xi\xi}-\epsilon^2 f_V^* \end{pmatrix} \begin{pmatrix}u\\v\end{pmatrix}
\]</div>
dus:

<div class="math-container">\[
\mathcal L = \begin{pmatrix}\partial_{\xi\xi}+f^*_U&f_V^* \\ -\epsilon^2 f^*_U&\partial_{\xi\xi}-\epsilon^2 f_V^* \end{pmatrix} 
\]</div>

<div class="math-container">\[
v+\epsilon^2 u = \epsilon^2\partial_{\xi\xi} u+\partial_{\xi\xi}v+0
\]</div>

# expansion
<div class="math-container">\[
\lambda_0\begin{pmatrix}u_0\\ u_0+v_1\end{pmatrix} = \begin{pmatrix}\partial_{\xi\xi}+f^*_U&0 \\ 0&\partial_{\xi\xi} \end{pmatrix} \begin{pmatrix}u_0\\u_0+ v_1\end{pmatrix}
\]</div>

<div class="math-container">\[
		\hat\lambda \begin{pmatrix}u_1\\ u_1+v_2\end{pmatrix} = \begin{pmatrix}\partial_{\xi\xi}+f^*_U-f_V^*&f_V^* \\ 0&\partial_{\xi\xi} \end{pmatrix} \begin{pmatrix}u_1\\u_1+ v_2\end{pmatrix}
\]</div>





Got it! You want to express the original system in the form of a first-order differential equation involving a 4-component vector. Let's proceed.

We start by rewriting the system in a way that uses a first-order form for \(\partial_\xi\). Define:

\[
\mathbf{p} = \begin{pmatrix} u \\ v \\ u_\xi \\ v_\xi \end{pmatrix}
\]

Now, differentiate \(\mathbf{p}\) with respect to \(\xi\):

\[
\mathbf{p}_\xi = \begin{pmatrix} u_\xi \\ v_\xi \\ u_{\xi\xi} \\ v_{\xi\xi} \end{pmatrix}
\]

We know the original equations involve second-order derivatives of \(u\) and \(v\). Rewrite them to relate these to the components of \(\mathbf{p}\):

From:

1. \(\lambda u = (\partial_{\xi\xi} + f^*_U) u + f_V^* v\)

We can express the second derivative \(u_{\xi\xi}\) as:

\[
u_{\xi\xi} = \lambda u - f^*_U u - f_V^* v
\]

Similarly, from:

2. \(\lambda v = -\epsilon^2 f^*_U u + (\partial_{\xi\xi} - \epsilon^2 f_V^*) v\)

We get:

\[
v_{\xi\xi} = \lambda v + \epsilon^2 f^*_U u + \epsilon^2 f_V^* v
\]

Now, we can write this in matrix form as:

\[
\mathbf{p}_\xi = A \mathbf{p}
\]

where:

\[
A = \begin{pmatrix}
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\lambda - f^*_U & -f_V^* & 0 & 0 \\
\epsilon^2 f^*_U & \lambda + \epsilon^2 f_V^* & 0 & 0
\end{pmatrix}
\]

Thus:

\[
\mathbf{p}_\xi = A \mathbf{p}
\]

This expresses the original system as a first-order differential equation in terms of a 4-component vector \(\mathbf{p}\).

[View Raw Markdown](/assets/md/Proberen operator als perturbed.md)
