#!/usr/bin/env python3
from pathlib import Path
import sys
if len(sys.argv) != 2:
    raise SystemExit("Usage: python3 set_base_url.py https://example.com/plus-player-review")
url = sys.argv[1].rstrip("/")
placeholder = "https://YOUR-HTTPS-HOST.example/plus-player-review"
for name in ["review.m3u", "APP_REVIEW_NOTES.txt"]:
    p = Path(__file__).parent / name
    p.write_text(p.read_text(encoding="utf-8").replace(placeholder, url), encoding="utf-8")
print("Updated review.m3u and APP_REVIEW_NOTES.txt to:", url)
