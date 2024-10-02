---
layout: post
title: "Update text natuurkunde"
date: 2024-09-16
---

<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>

Hi! I've got an update, I've been working on the stability part of my thesis for a couple of months now, and feel I've found a solution to it. It's rather technical, but a short summary: 
I formalize an eigenvalue problem by linearizing around a steady state solution (front), the eigenvalues being the decay/growth rate (positive: growing, negative: decaying). The eigenfunctions are the perturbations that will either grow/decay based on the eigenvalue. 
Solving for the eigenvalues is a bit tricky. Solving exactly is infeasible, so I find approximate solutions, and some functional analysis theory then tells me that under certain conditions, these approximate solutions are close enough to guarantee stability (hence "physical solutions", things you see in nature, that don't decay by themselves). This has a cool basis both in geometry (stable/unstable manifolds) and functional analysis (the eigenvalue problem with Sturm-Liouville type operators). 
To find these approximate solutions, I cut up the real axis into three parts: two "slow" regions, and one "fast" region. This is similar to what you do in boundary layer problems in, for example, fluid dynamics. Or two-timescale problems in neuroscience. I then solve the simplified solutions perturbatively in all regimes (left slow, center fast, right slow). Then to have a smooth solution (which I require as solutions to the PDE), I match amplitude of the boundaries of these regimes, and I match the first order derivative. The main work I've done is finding the values to match at, and finding the right perturbations (I was stuck at the wrong order of expansions for a while). This is basically a whole lot of calculus and Fredholm theory to find that some integrals should equal each-other. 
I'll link two documents, the first of which I think highlights the problem more completely, but goes wrong at the stability analysis (the wrong order of expansion), the second has the right expansion, and my results, but lacks the context. I completely understand if you don't want to dive into these at this moment. If you do however, I'll draft up a more readable document, but if no-one is going to read it anyways, I'll save my time. So let me know if you want a document with some context. 
If you like, I would love to drop by some time and explain with a presentation etc, let me know if you're interested/have time. 
We agreed that I'd reach out if I needed help, so far that hasn't been the case. The next part I will study will probably be similar, and I think won't take extremely long, now I've gotten a good feeling for this first part, but the part after that deals with some topics similar to surface tension, at that point I'd love to chat a bit, as I think the physics insight would be very helpful. 


[View Raw Markdown](/assets/md/Update text natuurkunde.md)
