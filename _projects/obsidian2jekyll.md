---
layout: page
title: Automating Obsidian to Jekyll
description: A semi-streamlined pipeline to transform my notes into a Jekyll site
img: assets/img/obs2jek.webp
importance: 2
category: study
related_publications: true
---
sorry about the terrible DALL-E thumbnail, but I love it too much. 

# Why again?
After being bothered by Wiert to have a look at github actions and jekyll, I finally decided to give it a spin. What content to throw on there though? Well it better be slightly useful. So I got the biggest volume of text I've recently produced, my thesis notes. I don't want to manually make them jekyll-publishable of course, so with some help of our AI overlords, I made a little script to get from Obsidian files to jekyll markdown. The process isn't completely smooth unfortunately. Equations are different, and changing mathjax's settings seems to only make things worse, so I had to comply to jekyll's standards, time for some python. 

## Code for math
```python
    # Replace block math with a scrollable div
    content = re.sub(r'\$\$(.*?)\$\$', r'<div class="math-container">\\[\1\\]</div>', content, flags=re.DOTALL)
    # Replace inline math
    content = re.sub(r'\$(.*?)\$', r'$$\1$$', content)
```
In the end, this is the magic regex to make the math not be an ugly string of badly parsed LaTeX. The class makes sure that the math-boxes don't overflow, making them scrollable (like on wiki on mobile). For some reason that took me way too long to figure out, jekyll uses double $$'s, or at least my template does. Of course, this was properly documented, but also of course, I didn't read that in time. 

## Links
The links were bad, jekyll wants a certain format for the "posts", which are meant for blogs. They keep the date in the file, but my obsidian files don't have that. So I had to look up the files in the system and get the date, but obsidian also allows for not keeping track of the full path, so I had to look in all directories of my vault, which made all this a mess. 

## Raw markdown
I too often want to grab some markdown or latex from a document but can't find the source code quickly, so I made an option to view the raw data. The raw file is simply copied into the jekyll project and a link is added to the markdown that gets parsed. 

## Images
Images suck as well, they are copied to the assets folder, then the link is changed to that image instead. 

## Overview
The overview text on top of the listing of all the files, is also just a markdown file, in Obsidian, so this gets treated differently. 

# Full code
complaints about ugly code can be sent to OpenAI
[Download code (very safe yes)](/assets/py/Obs2Jek.py)
