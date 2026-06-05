from __future__ import annotations

from datetime import datetime
from html import escape
from typing import Any

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def html_escape(value: Any) -> str:
    return escape(str(value or ""), quote=True)


def format_date(iso_value: str | None) -> str:
    if not iso_value:
        return ""
    try:
        dt = datetime.fromisoformat(str(iso_value).replace("Z", "+00:00"))
    except ValueError:
        return ""
    return f"{DAYS[dt.weekday()]} {dt.day} {MONTHS[dt.month - 1]}"


def format_duration(seconds: int | str | None) -> str:
    try:
        total = int(seconds or 0)
    except (TypeError, ValueError):
        return ""
    if total <= 0:
        return ""
    hours, remainder = divmod(total, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{hours}h {minutes}m" if hours else f"{minutes} min"


def short_url(url: str | None) -> str:
    return (url or "").replace("https://www.", "").replace("https://", "")


def render_digest(data: dict[str, Any]) -> str:
    """Render a Gmail-safe HTML digest from summarized video data.

    The renderer intentionally uses table layout and inline styles because many
    email clients strip modern CSS, external stylesheets, and scripts.
    """
    channels = data.get("channels", [])
    video_total = sum(len(channel.get("videos", [])) for channel in channels)
    channel_total = len(channels)
    eyebrow = data.get("eyebrow_label") or "YouTube Digest"
    today = datetime.now()
    header_date = f"{DAYS[today.weekday()]} {today.day} {MONTHS[today.month - 1]} {today.year}"

    out: list[str] = [
        "<!doctype html>",
        '<html lang="en"><head>',
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        '<meta name="x-apple-disable-message-reformatting">',
        f"<title>YouTube digest &mdash; {html_escape(header_date)}</title>",
        "</head>",
        '<body style="background:#fbfcfe; color:#1a2b4a; font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,sans-serif; font-size:15px; line-height:1.6; margin:0; padding:0;">',
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; border-collapse:collapse; background:#fbfcfe;"><tr><td align="center" style="padding:0;">',
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="640" style="width:640px; max-width:640px; border-collapse:collapse;"><tr><td style="padding:0 24px;">',
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; border-collapse:collapse;"><tr><td style="padding:44px 0 28px; border-bottom:2px solid #1a2b4a;">',
        f'<div style="font-size:10px; font-weight:600; letter-spacing:0.18em; color:#5b8db8; margin-bottom:10px;">{html_escape(eyebrow)}</div>',
        f'<div style="font-size:26px; font-weight:300; letter-spacing:-0.015em; color:#1a2b4a; line-height:1.2; margin:0 0 4px;">{html_escape(header_date)}</div>',
        f'<div style="font-size:13px; color:#6b7a90;">{video_total} videos across {channel_total} channels</div>',
        "</td></tr></table>",
    ]

    for channel in channels:
        label = channel.get("channel_label") or channel.get("channel") or "Channel"
        channel_url = channel.get("channel_url") or ""
        out.extend([
            '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; border-collapse:collapse; margin-top:44px; margin-bottom:8px;"><tr>',
            '<td width="4" style="width:4px; background:#5b8db8; font-size:0; line-height:0;">&nbsp;</td>',
            '<td style="padding:4px 0 4px 14px;">',
            f'<div style="font-size:10px; font-weight:700; letter-spacing:0.14em; color:#1a2b4a; margin-bottom:2px;">{html_escape(label)}</div>',
        ])
        if channel_url:
            out.append(f'<a href="{html_escape(channel_url)}" style="font-size:11px; color:#6b7a90; text-decoration:none;">{html_escape(short_url(channel_url))}</a>')
        out.append("</td></tr></table>")

        for video in channel.get("videos", []):
            title = video.get("title", "")
            url = video.get("url") or "#"
            thumb = video.get("thumbnail_url") or ""
            duration = video.get("duration") or format_duration(video.get("duration_sec"))
            published = format_date(video.get("published"))
            out.extend([
                '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; border-collapse:collapse; border-top:1px solid #e6ecf3;"><tr><td style="padding:18px 0;">',
                '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; border-collapse:collapse;"><tr>',
                '<td width="168" style="width:168px; padding:0 18px 0 0; vertical-align:top;">',
                f'<a href="{html_escape(url)}" style="text-decoration:none;"><img src="{html_escape(thumb)}" width="168" height="94" alt="{html_escape("Thumbnail for " + title)}" style="display:block; width:168px; height:94px; border:0; border-radius:12px; background:#e6ecf3; object-fit:cover;"></a>',
                '</td><td style="padding:0; vertical-align:top;">',
                '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; border-collapse:collapse; margin-bottom:4px;"><tr>',
                '<td style="padding:0; vertical-align:top;">',
                f'<a href="{html_escape(url)}" style="font-size:15px; font-weight:500; line-height:1.35; color:#1a2b4a; text-decoration:none;">{html_escape(title)}</a>',
                "</td>",
            ])
            if duration:
                out.append('<td style="padding:2px 0 0 10px; vertical-align:top; white-space:nowrap;">')
                out.append(f'<span style="display:inline-block; font-size:10.5px; font-weight:600; letter-spacing:0.04em; color:#5b8db8; border:1px solid #c4d7ed; border-radius:10px; padding:2px 8px; white-space:nowrap; line-height:1.4; background-color:#f5f9fd;">{html_escape(duration)}</span>')
                out.append("</td>")
            out.append("</tr></table>")
            if published:
                out.append(f'<div style="font-size:11px; color:#6b7a90; margin-bottom:10px;">{html_escape(published)}</div>')
            out.append('<ul style="margin:0; padding-left:16px; list-style:disc;">')
            for bullet in video.get("bullets", []):
                out.append(f'<li style="font-size:13px; color:#2a3a55; margin-bottom:5px; line-height:1.5;">{html_escape(bullet)}</li>')
            out.extend(["</ul>", "</td></tr></table>", "</td></tr></table>"])

    out.extend([
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; border-collapse:collapse; margin-top:40px; border-top:1px solid #dfe7f0;"><tr><td style="padding:18px 0 34px; font-size:11px; color:#6b7a90;">Synthetic portfolio demo. No private transcripts, recipients, auth files, or run history included.</td></tr></table>',
        "</td></tr></table></td></tr></table>",
        "</body></html>",
    ])
    return "\n".join(out)
