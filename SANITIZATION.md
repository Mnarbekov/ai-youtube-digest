# Sanitization notes

This repository is a sanitized demo of my local YouTube digest workflow. It intentionally does not publish or include the private production workflow.

## Excluded

- Gmail credentials, OAuth state, mailer configuration, and message IDs.
- Recipient email addresses and personal delivery history.
- Real generated digest history, logs, cache folders, run state, and transient JSON files.
- Real channel list from the private workflow.
- Real full transcript dumps or copied YouTube transcript text.
- Hardcoded local machine paths.
- Private project orchestration notes.

## Included instead

- Synthetic example channels in `channels.example.txt`.
- Synthetic video metadata in `fixtures/videos.synthetic.json`.
- Synthetic short transcript snippets in `fixtures/transcripts.synthetic.json`.
- Synthetic three-bullet summaries in `fixtures/summaries.synthetic.json`.
- A deterministic offline renderer command: `python scripts\render_demo.py`.

## Review rule

Before any public push, run:

```powershell
python scripts\render_demo.py
python scripts\check_sanitization.py
```

The sanitizer may report expected placeholder/documentation words such as API key labels or references to excluded auth artifacts. Treat any real value, real recipient, real path, or generated run artifact as a blocker.
