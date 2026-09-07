---
title: "Rebuilding this site"
date: 2026-09-05 09:00:00 +0100
category: meta
tags: [jekyll, site]
description: >-
  Tore down a fifteen-year-old blog and replaced it with something smaller:
  project write-ups and a gallery.
---

The previous version of this site had been running since about 2010. It was a
blog in the proper sense — post regularly, keep the streak going, feel guilty
when you don't. I stopped enjoying that a long time ago, so I've torn it down
and started again.

<!--more-->

## What changed

Nearly everything. The old posts are gone; most were notes to myself about
tooling that no longer exists, and I don't miss them. What's left is a much
smaller site with two jobs.

The first is [Work](/work/) — write-ups on things I've built. No schedule, no
streak, just an entry when a project is worth explaining. The second is the
[gallery](/art/), which is where the drawing goes. Comics and games are the two
hobbies that have outlasted every other one, and drawing is where they meet.

## Under the hood

Still [Jekyll](https://jekyllrb.com), now on version 4. The whole thing builds
in a dev container, so a local copy is two commands:

```bash
bundle install
bundle exec jekyll serve --livereload
```

Deploys run from GitHub Actions on every push to `master`. No framework, no
build step beyond Jekyll itself, one hand-written stylesheet, and about a
hundred lines of JavaScript for the menu and the gallery lightbox. Fonts are
self-hosted, so pages make no third-party requests at all.

That's roughly the right amount of machinery for a site this size.
