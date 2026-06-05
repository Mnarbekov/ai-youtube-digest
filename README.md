# AI YouTube Digest

A privacy-safe demo of an AI-assisted YouTube digest workflow.

## Why this exists

My wife wanted help choosing which podcasts and videos were worth watching, so I built a weekly digest workflow. It checks favourite YouTube channels, finds recent long-form videos, fetches available captions, summarizes each video into three useful bullets, renders a clean email-style digest with thumbnails and links, and can hand that digest to an email sender.

This repository is a sanitized demo of that workflow. It contains synthetic fixtures only; it does not include private channel lists, private run history, credentials, Gmail state, or real transcripts.

## What is included

- A small Python renderer for Gmail-safe, table-based HTML.
- Synthetic fixture data for channels, videos, transcript snippets, and summaries.
- A demo command that renders `examples/demo-digest.html` without network access.
- Documentation describing the production architecture and the sanitization boundary.

## Quick start

```powershell
python scripts\render_demo.py
```

Expected result:

```text
wrote examples\demo-digest.html (... bytes, 3 videos)
```

Open `examples/demo-digest.html` in a browser or email-preview workflow to review the digest.

## Repository layout

```text
.
├── channels.example.txt              # Example channel inputs only
├── state.example.json                # Example cutoff state, no message IDs
├── fixtures\                         # Synthetic demo data only
├── src\ai_youtube_digest\            # Sanitized renderer and helpers
├── scripts\render_demo.py            # Offline demo command
├── scripts\check_sanitization.py     # Local safety scan helper
├── docs\architecture.md              # Simple architecture notes
└── SANITIZATION.md                   # What was excluded and why
```

## Configuration

Copy `.env.example` to `.env` for local experimentation. Do not commit `.env` or any generated run artifacts.

## Status

Local demo ready for review. TODO: before publishing, add a license if desired and re-run `python scripts\check_sanitization.py`.
