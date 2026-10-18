import urllib.request
import json
import os
from datetime import datetime, timezone

def fetch_status(url, label):
    try:
        req = urllib.request.urlopen(url, timeout=10)
        ts = int(req.read().decode('utf-8').strip())
        date_str = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        return {
            "schemaVersion": 1,
            "label": label,
            "message": date_str,
            "color": "brightgreen"
        }
    except Exception:
        return {
            "schemaVersion": 1,
            "label": label,
            "message": "Sync Failed",
            "color": "critical"
        }

def main():
    gist_id = os.environ.get("GIST_ID")
    gist_token = os.environ.get("GIST_TOKEN")

    if not gist_id or not gist_token:
        raise ValueError("GIST_ID and GIST_TOKEN environment variables must be set.")

    arch_data = fetch_status("https://pkg.evlstk.dev/archlinux/lastsync", "Arch Mirror")
    termux_data = fetch_status("https://pkg.evlstk.dev/termux/lastsync", "Termux Mirror")

    payload = {
        "files": {
            "arch-status.json": {"content": json.dumps(arch_data)},
            "termux-status.json": {"content": json.dumps(termux_data)}
        }
    }

    req = urllib.request.Request(
        f"https://api.github.com/gists/{gist_id}",
        data=json.dumps(payload).encode('utf-8'),
        headers={
            "Authorization": f"Bearer {gist_token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "Mirror-Badge-Updater"
        },
        method="PATCH"
    )

    with urllib.request.urlopen(req) as resp:
        print(f"Gist updated successfully: status {resp.status}")

if __name__ == "__main__":
    main()
