# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown-it-py", "mdit-py-plugins"]
# ///
"""Print CHEATSHEET.md to CHEATSHEET.pdf (A4) with headless Chrome.

The post-commit hook in .githooks runs this whenever a commit changes
CHEATSHEET.md. To run it by hand: uv run scripts/cheatsheet_pdf.py
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "CHEATSHEET.md"
OUT = ROOT / "CHEATSHEET.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 14mm 13mm 16mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Apple SD Gothic Neo", "Helvetica Neue", sans-serif;
  font-size: 10pt; line-height: 1.5; color: #1a1a1a; background: #fff;
  margin: 0;
}
h1 { font-size: 20pt; margin: 0 0 8pt; }
h2 {
  font-size: 15pt; margin: 18pt 0 6pt; padding-bottom: 3pt;
  border-bottom: 1.5pt solid #333;
}
h3 {
  font-size: 12.5pt; margin: 16pt 0 4pt; padding: 3pt 6pt;
  background: #eef2f7; border-left: 3pt solid #4a6fa5;
}
h4 { font-size: 10.5pt; margin: 12pt 0 4pt; color: #234; }
h1, h2, h3, h4 { break-after: avoid; }
p { margin: 4pt 0; }
ul, ol { margin: 3pt 0; padding-left: 18pt; }
li { margin: 1pt 0; }
a { color: inherit; text-decoration: none; border-bottom: 0.5pt dotted #888; }
code {
  font-family: Menlo, monospace; font-size: 8.6pt;
  background: #f2f2f2; padding: 0 2pt; border-radius: 2pt;
}
pre {
  background: #f6f6f6; border: 0.5pt solid #ddd; border-radius: 3pt;
  padding: 5pt 7pt; margin: 5pt 0; line-height: 1.35;
  white-space: pre-wrap; word-break: break-word; break-inside: avoid;
}
pre code { background: none; padding: 0; font-size: 8.3pt; }
table {
  border-collapse: collapse; margin: 6pt 0; width: 100%;
  break-inside: avoid; font-size: 8.8pt; line-height: 1.3;
}
th, td {
  border: 0.6pt solid #999; padding: 1.5pt 5pt;
  vertical-align: top; text-align: left;
}
th { background: #e8e8e8; }
td[rowspan] { vertical-align: middle; font-weight: 600; background: #fafafa; }
"""


def github_slug(title):
    """Make heading ids the way GitHub does, so the table's #links work."""
    return re.sub(r"[^\w\- ]", "", title.strip().lower()).replace(" ", "-")


def main():
    md = (
        MarkdownIt("commonmark", {"html": True})
        .enable("table")
        .use(anchors_plugin, min_level=1, max_level=4, slug_func=github_slug)
    )
    body = md.render(SRC.read_text())
    html = (
        '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        f"<title>알고리즘 Cheat Sheet</title><style>{CSS}</style></head>"
        f"<body>{body}</body></html>"
    )

    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "cheatsheet.html"
        page.write_text(html)
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--user-data-dir={tmp}/profile",
                f"--print-to-pdf={OUT}",
                page.as_uri(),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
