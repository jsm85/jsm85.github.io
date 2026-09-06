---
title: "New site, new cartridge"
date: 2026-09-05 09:00:00 +0100
category: meta
tags: [jekyll, site]
description: >-
  Rebuilt the site from scratch. Fewer posts, more projects, and a gallery for
  the drawing.
---

The old version of this site had been running since about 2010. It was a blog
in the proper sense — post regularly, keep the streak, feel guilty when you
don't. I stopped enjoying that a long time ago, so I've torn it down and
started again.

<!--more-->

## What changed

Everything, more or less. The old posts are gone — most of them were notes to
myself about tooling that no longer exists, and I don't miss them. What's left
is a much smaller site with two jobs:

- **A project log.** When I build something I'm pleased with, I'll write it up
  here. No schedule, no streak.
- **A gallery.** Comics and games are the hobbies that have stuck, and drawing
  is where the two meet. The [art page]({{ '/art/' | relative_url }}) is where
  that lives now.

The look is deliberate. I was born in the 80s, grew up through the 90s, and my
taste never really left — so there are scanlines, neon, halftone dots and a
pixel typeface, all sitting on a layout that behaves itself on a phone.

## Under the hood

Still [Jekyll](https://jekyllrb.com), now on version 4. The whole thing builds
in a dev container, so getting a local copy running is:

```bash
bundle install
bundle exec jekyll serve --livereload
```

Deploys happen from GitHub Actions on every push to `master`. No frameworks, no
build step beyond Jekyll itself, and one hand-written stylesheet — which is
about the right amount of machinery for a site this size.

More soon. Probably.
