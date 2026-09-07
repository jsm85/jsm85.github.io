# jsm85.github.io

Personal site — project write-ups and an art gallery. Built with
[Jekyll 4](https://jekyllrb.com) and deployed to GitHub Pages by GitHub
Actions.

Retro-futurist: a deep plum ground, a sunset horizon under the intro,
chrome-gradient display type and pill buttons — the outrun palette handled with
editorial restraint rather than neon. Influenced by
[Retrend](https://dribbble.com/shots/18116271-Retrend-NFTs-Landing-Page) by
Arhansyah APP for Plainthing Studio.

---

## Running it locally

### With the dev container (recommended)

Open the repo in VS Code and choose **Reopen in Container**, or run
`devcontainer up` with the CLI. Gems install automatically on first create.

```bash
bundle exec jekyll serve --livereload
```

The site is then on <http://localhost:4000>. Port 4000 is forwarded and
LiveReload (35729) refreshes the page as you save.

### Without the dev container

Needs Ruby 3.2+ and Bundler.

```bash
bundle install
bundle exec jekyll serve --livereload
```

---

## Adding a write-up

Create a file in `_posts/` named `YYYY-MM-DD-some-slug.md`:

```markdown
---
title: "What I built"
date: 2026-01-15 09:00:00 +0000
tags: [dotnet, docker]
description: One line, used on the Work list and in search results.
hero: /assets/images/posts/my-screenshot.png   # optional
---

Opening paragraph — this shows above the fold.

<!--more-->

The rest of the post.
```

Everything but `title` and `date` is optional. Posts appear at
`/work/YYYY/MM/slug/`.

## Adding artwork

1. Drop the image into `assets/images/art/`.
2. Add an entry to `_data/artwork.yml`:

```yaml
- title: Piece name
  image: /assets/images/art/piece-name.png
  alt: Description for screen readers
  medium: Ink        # also becomes a filter button on /art/
  year: 2026
  caption: Optional line shown in the lightbox.
```

The filter bar appears automatically once there's more than one `medium`.

## Other things you might want to edit

| What | Where |
| --- | --- |
| Site title, blurb, links | `_config.yml` |
| Nav items | `_data/nav.yml` |
| The "Working with" list on About | `_data/toolkit.yml` |
| Colours, fonts, spacing | the token block at the top of `assets/css/style.css` (re-run the contrast audit after) |
| Bio copy | `about.html` |
| Intro headline | `author.blurb_lead` / `blurb_accent` in `_config.yml` |
| Profile picture | `assets/images/profile.jpg` |

The site is branded as **JSM85** throughout — no real name appears anywhere
except behind the LinkedIn link.

## Accessibility

Colour choices are checked, not assumed:

```bash
python3 script/contrast-audit.py
```

It reads the palette tokens straight out of `assets/css/style.css` and checks
every text/background pair against WCAG 2.1 — including the awkward ones: every
stop of the sunset gradient (both as headline text and as the fill behind
button labels), the radial that brightens the top of every page, the lightbox
scrim, and the intro copy sitting over the horizon glow. Change the palette,
re-run it, and it'll tell you what broke. No dependencies.

Currently 44 pairs, all passing AA and most passing AAA, with the tightest at
1.25x its threshold.

Two notes on how the intro stays legible:

- The glow's `mask-image` on `.intro::after` is load-bearing, not decoration.
  Together with the intro's bottom padding it keeps the bright core of the
  horizon off the copy. See the comment on that rule in `style.css`.
- The `INTRO_BG` values in the audit are the brightest pixel actually rendered
  behind each element, sampled from the live page at 390 / 900 / 1280px wide.
  A flat worst-case model is misleading over a radial gradient. The script
  documents how to re-measure them if the hero layout changes.

The build was also run through axe-core across every page plus the open
lightbox and open mobile menu: **0 violations**. Everything axe reports as
"needs review" is a case it cannot compute — an element over a CSS gradient or
pseudo-element — which is precisely what the sampling above covers.

## Fonts

Syne (display), Space Grotesk (body) and IBM Plex Mono (labels) are self-hosted
from `assets/fonts/` — latin and latin-ext subsets only, ~170 KB total, all
under the SIL Open Font License. Pages make no third-party requests.

---

## Deploying

Pushing to `master` triggers `.github/workflows/deploy.yml`, which builds the
site and publishes it to GitHub Pages.

**One-time setup:** in the repo's **Settings → Pages**, set **Source** to
**GitHub Actions**. The classic "deploy from a branch" mode only supports
Jekyll 3, so it won't build this site.
