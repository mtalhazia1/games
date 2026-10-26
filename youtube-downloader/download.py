#!/usr/bin/env python3
"""Download a YouTube video/short to ~/Downloads as MP4.

Usage: python download.py <url> [<url> ...]
Requires: pip install yt-dlp  (and ffmpeg on PATH for merging audio+video)
"""
import sys
from pathlib import Path

from yt_dlp import YoutubeDL

DOWNLOADS = Path.home() / "Downloads"


def download(urls):
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    opts = {
        "format": "bv*+ba/b",
        "merge_output_format": "mp4",
        "outtmpl": str(DOWNLOADS / "%(title)s [%(id)s].%(ext)s"),
    }
    with YoutubeDL(opts) as ydl:
        return ydl.download(urls)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(download(sys.argv[1:]))
