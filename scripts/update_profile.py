from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


README = Path("README.md")
START = "<!-- PROFILE-PULSE:START -->"
END = "<!-- PROFILE-PULSE:END -->"


def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    readme = README.read_text(encoding="utf-8")

    replacement = f"""{START}
**Derniere mise a jour:** {now}

**Focus du moment:** garder ce profil vivant avec une petite automatisation GitHub Actions.
{END}"""

    before, marker, tail = readme.partition(START)
    if not marker:
        raise SystemExit("Start marker not found")

    _, marker_end, after = tail.partition(END)
    if not marker_end:
        raise SystemExit("End marker not found")

    README.write_text(before + replacement + after, encoding="utf-8")


if __name__ == "__main__":
    main()
