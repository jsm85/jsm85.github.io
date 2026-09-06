# jsm85.github.io

Personal site for Joe Mendonca — project write-ups and an art gallery.
Built with [Jekyll 4](https://jekyllrb.com) and deployed to GitHub Pages by
GitHub Actions.

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

## Adding a project write-up

Create a file in `_posts/` named `YYYY-MM-DD-some-slug.md`:

```markdown
---
title: "What I built"
date: 2026-01-15 09:00:00 +0000
category: project          # shown as the badge on the card
tags: [dotnet, docker]
description: One line used on the card and in search results.
hero: /assets/images/posts/my-screenshot.png   # optional
---

Opening paragraph — this shows above the fold.

<!--more-->

The rest of the post.
```

Everything but `title` and `date` is optional.

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
| Site title, description, links | `_config.yml` |
| Nav items | `_data/nav.yml` |
| The stat bars on the character card | `_data/stats.yml` |
| Colours, fonts, spacing | the token block at the top of `assets/css/style.css` |
| Bio copy | `about.html` |
| Profile picture | `assets/images/profile.jpg` |

---

## Deploying

Pushing to `master` triggers `.github/workflows/deploy.yml`, which builds the
site and publishes it to GitHub Pages.

**One-time setup:** in the repo's **Settings → Pages**, set **Source** to
**GitHub Actions**. The classic "deploy from a branch" mode only supports
Jekyll 3, so it won't build this site.
