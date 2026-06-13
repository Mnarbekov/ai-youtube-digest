# How it works

A short walkthrough of how the digest is built.

```text
channel list
      |
      v
find recent uploads
      |
      v
keep only long-form videos
      |
      v
get captions when available
      |
      v
summarise each video into 3 bullets (AI)
      |
      v
build the email (HTML)
      |
      v
send it / save the demo email
```

## The steps

1. **Channels** — a plain list of channels, easy to edit without touching code.
2. **Cutoff** — a small state file remembers the last time a digest was sent, so each run only picks up newer videos.
3. **Find videos** — the workflow looks up recent uploads for each channel and skips short clips before doing any heavier work.
4. **Summarise** — the captions for each video are turned into three short bullets: what it's about, what stands out, and whether it's worth watching.
5. **Build the email** — the email is built as a simple table-based layout with inline styles, because many email apps strip out modern styling.
6. **Send** — the live version hands the finished email to an email sender. This demo stops before that and just saves the email to a file.

## The demo

The demo skips the internet and starts from the example data in `fixtures/summaries.synthetic.json`. That makes it repeatable and safe to share. Run it with:

```powershell
python scripts/render_demo.py
```

It writes `examples/demo-digest.html`, which you can open in a browser.
