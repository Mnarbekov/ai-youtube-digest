# Architecture

```text
channels.example.txt
        |
        v
[discover recent uploads]
        |
        v
[filter long-form videos]
        |
        v
[fetch captions/transcripts when available]
        |
        v
[LLM summarizer: 3 useful bullets per video]
        |
        v
[HTML email renderer]
        |
        v
examples/demo-digest.html / optional email sender
```

## Production shape

1. **Channel input** — A plain text channel list is easy to edit without touching code.
2. **Cutoff state** — A small state file records the last successful send time so the next run only includes newer videos.
3. **Acquisition** — The workflow resolves channels, gets recent uploads, and ignores short videos before doing transcript work.
4. **Summarization** — Transcript text is summarized into three practical bullets: why it matters, what to notice, and whether it is worth watching.
5. **Rendering** — The email body is table-based with inline CSS for broad email-client compatibility.
6. **Sending** — This public repo stops before any real mail integration. In a private deployment, I can connect the rendered HTML to a chosen mailer.

## Sanitized demo shape

The demo skips network calls and starts from `fixtures/summaries.synthetic.json`. That makes it deterministic, safe to publish, and easy to review.
