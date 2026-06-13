from __future__ import annotations

import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_youtube_digest import render_digest


def main() -> None:
    fixture = ROOT / "fixtures" / "summaries.synthetic.json"
    output = ROOT / "examples" / "demo-digest.html"
    data = json.loads(fixture.read_text(encoding="utf-8"))
    html = render_digest(data)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    video_total = sum(len(channel.get("videos", [])) for channel in data.get("channels", []))
    print(f"wrote {output.relative_to(ROOT)} ({len(html)} bytes, {video_total} videos)")


if __name__ == "__main__":
    main()
