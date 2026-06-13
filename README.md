# AI YouTube Digest

A simple weekly email that tells my wife and me which YouTube videos are actually worth our time, so we stop scrolling and start watching the good ones.

This repo is a demo-safe version of the project. It uses made-up example data — no private channel lists, recipients, or history — but the code that builds the email is real and you can run it.

## Why I built it

My wife follows a handful of channels but never has time to check which ones posted something good. The videos pile up, and choosing what to watch becomes its own little chore.

So I built a small automation that does the checking for us. Once a week it looks at our favourite channels, finds the new long-form videos, reads what each one is about, and sends a short email with the highlights. We open one email instead of digging through YouTube.

## What it does

- Checks a list of favourite YouTube channels for recent long-form videos.
- Pulls the captions so it knows what each video is actually about.
- Summarises every video into three short, useful bullet points.
- Builds a clean email with thumbnails and direct links.
- Sends the digest on a weekly schedule.

## Screenshots and workflow

![Weekly digest email with video thumbnails and three-bullet summaries](assets/screenshots/youtube-digest-email.png)

The weekly email, using demo content.

![How the digest is built, from channels to summary to email](assets/diagrams/youtube-digest-flow.png)

The flow: check channels, get captions, summarise, build the email, send it.

## Try the demo

The demo runs offline from example data and writes the email to `examples/demo-digest.html`:

```powershell
python scripts/render_demo.py
```

Then open `examples/demo-digest.html` in a browser to see the result.

## What's in this repo

- `src/ai_youtube_digest/` — the code that turns summarised videos into the email.
- `scripts/render_demo.py` — runs the offline demo, no internet needed.
- `fixtures/` — example channel, video, and summary data (all made up).
- `examples/demo-digest.html` — a rendered example email.
- `docs/architecture.md` — a short walkthrough of how the pieces fit together.
- `*.example` files — example config so you can see the inputs without any private values.

## Privacy

This is a demo-safe version. Our real channel list, email address, summaries, and send history stay private and are not in this repo. The example data is invented.

## Built with AI assistance

I'm not a software developer. I had the idea, decided how the email should read, and used AI tools to help build and refine it. The point of this project is taking a small everyday annoyance and turning it into something that quietly saves us time every week.

## Related

- Portfolio: https://www.mikhailnarbekov.com
- Medium story: [Proving AI's value to my wife: I built a weekly YouTube digest](https://medium.com/@mikhail.narbekov/proving-ais-value-to-my-wife-i-built-a-weekly-youtube-digest-d3a797b9f69b)
- GitHub: https://github.com/Mnarbekov
