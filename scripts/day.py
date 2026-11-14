"""Study helper for the 100 Days of Code repo.

Commands:
    python scripts/day.py new [DAY] [--title TITLE] [--project NAME]
        Scaffold a day (the next one if DAY is omitted) and refresh the roadmap.
    python scripts/day.py done [DAY]
        Mark a day complete (the day in progress if DAY is omitted).
    python scripts/day.py roadmap
        Regenerate the progress line, roadmap tables and day navigation links.
    python scripts/day.py status
        Print progress, pace and the next step.

Standard library only; requires Python 3.10+.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAYS_DIR = ROOT / "days"
TEMPLATES_DIR = ROOT / "templates"
JOURNAL_DIR = ROOT / "_personal" / "journal"
README = ROOT / "README.md"
CURRICULUM = Path(__file__).with_name("curriculum.json")

TOTAL_DAYS = 100
NAV_MARKER = "<!-- nav -->"
NAV_LINE = re.compile(rf"^.*{re.escape(NAV_MARKER)}$", re.MULTILINE)
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
DAY_DIR_NAME = re.compile(r"^Day (\d+) - ")
# Not allowed in Windows paths, or breaks Obsidian links.
UNSAFE_CHARS = re.compile(r'[\\*?"<>|\[\]#^]')
STATUS_ICON = {"done": "✅", "in-progress": "🚧", "not-started": "⬜"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def url(path: str) -> str:
    return path.replace(" ", "%20")


def link(target: Path, start: Path) -> str:
    return url(Path(os.path.relpath(target, start)).as_posix())


def folder_name(entry: dict) -> str:
    """The course section name ("Day N - Level - Title") as a safe folder name."""
    name = f"Day {entry['day']} - {entry['level']} - {entry['title']}"
    name = UNSAFE_CHARS.sub("", name.replace(":", " -").replace("/", "-"))
    return re.sub(r"\s+", " ", name).strip(" .")


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower().replace("+", " plus")).strip("-")


def parse_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


# --- curriculum ------------------------------------------------------------


def load_curriculum() -> dict:
    return json.loads(read(CURRICULUM))


def save_curriculum(curriculum: dict) -> None:
    def block(key: str) -> str:
        rows = ",\n".join(f"    {json.dumps(item, ensure_ascii=False)}" for item in curriculum[key])
        return f'  "{key}": [\n{rows}\n  ]'

    extras = json.dumps(curriculum.get("extras", []), ensure_ascii=False)
    body = ",\n".join([block("phases"), block("days"), f'  "extras": {extras}'])
    write(CURRICULUM, "{\n" + body + "\n}\n")


def entry_for(curriculum: dict, day: int) -> dict:
    for entry in curriculum["days"]:
        if entry["day"] == day:
            return entry
    raise SystemExit(f"Day {day} is not in {CURRICULUM.name}.")


# --- day notes -------------------------------------------------------------


def note_in(folder: Path) -> Path | None:
    """The day note: named after its folder, or else the only note at the folder's top level."""
    named = folder / f"{folder.name}.md"
    if named.is_file():
        return named
    notes = sorted(folder.glob("*.md"))
    return notes[0] if notes else None


def existing_notes() -> dict[int, Path]:
    notes: dict[int, Path] = {}
    if not DAYS_DIR.is_dir():
        return notes
    for folder in DAYS_DIR.iterdir():
        match = DAY_DIR_NAME.match(folder.name)
        note = note_in(folder) if match and folder.is_dir() else None
        if note:
            notes[int(match.group(1))] = note
    return dict(sorted(notes.items()))


def get_field(text: str, key: str) -> str:
    match = FRONTMATTER.match(text)
    if not match:
        return ""
    field = re.search(rf"^{key}:[ \t]*(.*)$", match.group(1), re.MULTILINE)
    return field.group(1).strip().strip("\"'") if field else ""


def set_field(text: str, key: str, value: str) -> str:
    match = FRONTMATTER.match(text)
    if not match:
        raise SystemExit("The day note has no frontmatter.")
    block, count = re.subn(
        rf"^{key}:.*$", lambda _: f"{key}: {value}", match.group(1), count=1, flags=re.MULTILINE
    )
    if not count:
        block += f"\n{key}: {value}"
    return text[: match.start(1)] + block + text[match.end(1) :]


def statuses_of(notes: dict[int, Path]) -> dict[int, str]:
    return {day: get_field(read(note), "status") or "in-progress" for day, note in notes.items()}


def render_template(name: str, values: dict[str, object]) -> str:
    text = read(TEMPLATES_DIR / name)
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    return text


def render_nav(day: int, notes: dict[int, Path]) -> str:
    here = notes[day].parent
    earlier = [d for d in notes if d < day]
    later = [d for d in notes if d > day]
    parts = []
    if earlier:
        prev = max(earlier)
        parts.append(f"[← Day {prev}]({link(notes[prev], here)})")
    parts.append(f"[Roadmap]({link(README, here)}#roadmap)")
    if later:
        nxt = min(later)
        parts.append(f"[Day {nxt} →]({link(notes[nxt], here)})")
    return " · ".join(parts) + " " + NAV_MARKER


def refresh_navigation(notes: dict[int, Path]) -> None:
    for day, note in notes.items():
        text = read(note)
        updated = NAV_LINE.sub(lambda _: render_nav(day, notes), text)
        if updated != text:
            write(note, updated)


# --- README ----------------------------------------------------------------


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("*", "\\*")


def render_progress(statuses: dict[int, str], notes: dict[int, Path]) -> str:
    done = sum(1 for status in statuses.values() if status == "done")
    filled = done * 20 // TOTAL_DAYS
    bar = "█" * filled + "░" * (20 - filled)
    line = f"**Progress:** {done} / {TOTAL_DAYS} days completed `{bar}` {done * 100 // TOTAL_DAYS}%"
    in_progress = [day for day, status in statuses.items() if status == "in-progress"]
    if in_progress:
        current = max(in_progress)
        line += f" · **Now:** [Day {current}]({url(rel(notes[current]))})"
    return line + "\n"


def render_roadmap(curriculum: dict, statuses: dict[int, str], notes: dict[int, Path]) -> str:
    lines: list[str] = []
    for phase in curriculum["phases"]:
        lines += [
            f"### {phase['name']} · Days {phase['first']}–{phase['last']}",
            "",
            "| Day | Topic | Project | Status |",
            "| ---: | --- | --- | :---: |",
        ]
        for entry in curriculum["days"]:
            day = entry["day"]
            if not phase["first"] <= day <= phase["last"]:
                continue
            title = cell(entry["title"])
            topic = f"[{title}]({url(rel(notes[day]))})" if day in notes else title
            if entry["level"] != phase["name"]:
                topic += f" *({entry['level']})*"
            project = cell(entry["project"]) or "—"
            icon = STATUS_ICON[statuses.get(day, "not-started")]
            lines.append(f"| {day} | {topic} | {project} | {icon} |")
        lines.append("")
    if curriculum.get("extras"):
        lines += [f"**After Day {TOTAL_DAYS}:** " + " · ".join(curriculum["extras"]), ""]
    lines.append("✅ done · 🚧 in progress · ⬜ not started")
    return "\n".join(lines) + "\n"


def replace_block(text: str, name: str, content: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:start -->\n).*?(<!-- {name}:end -->)", re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"README.md is missing the <!-- {name}:start --> / <!-- {name}:end --> markers.")
    return pattern.sub(lambda m: m.group(1) + content + m.group(2), text, count=1)


def update_readme(curriculum: dict, notes: dict[int, Path]) -> None:
    statuses = statuses_of(notes)
    text = read(README)
    text = replace_block(text, "progress", render_progress(statuses, notes))
    text = replace_block(text, "roadmap", render_roadmap(curriculum, statuses, notes))
    write(README, text)


# --- commands --------------------------------------------------------------


def cmd_new(args: argparse.Namespace) -> None:
    curriculum = load_curriculum()
    notes = existing_notes()
    day = args.day or (max(notes) + 1 if notes else 1)
    entry = entry_for(curriculum, day)
    old_title = entry["title"]

    if args.title:
        entry["title"] = args.title
    if args.project is not None:
        entry["project"] = args.project
    if args.title or args.project is not None:
        save_curriculum(curriculum)

    values = {
        "day": day,
        "day_padded": f"{day:03d}",
        "title": entry["title"],
        "level": entry["level"],
        "level_tag": slugify(entry["level"]),
        "project": entry["project"] or "—",
        "date": date.today().isoformat(),
        "nav": NAV_MARKER,
    }

    if day in notes:
        print(f"Day {day} already exists: {rel(notes[day])}")
        if args.title and args.title != old_title:
            write(notes[day], read(notes[day]).replace(old_title, args.title))
            print(f"Updated its title to: {args.title}")
            print("The folder keeps its old name; rename it inside Obsidian so links follow.")
    else:
        folder = DAYS_DIR / folder_name(entry)
        for sub in ("exercises", "project", "_raw"):
            (folder / sub).mkdir(parents=True, exist_ok=True)
        note = folder / f"{folder.name}.md"
        write(note, render_template("day.md", values))
        notes[day] = note
        print(f"Created {rel(note)}")
        print(f"Put transcripts and course downloads in {rel(folder / '_raw')}/ (local only)")

    journal = JOURNAL_DIR / f"day-{day:03d}.md"
    if not journal.exists():
        write(journal, render_template("journal.md", values))
        print(f"Created local journal {rel(journal)}")

    refresh_navigation(notes)
    update_readme(curriculum, notes)
    print("README roadmap updated.")


def cmd_done(args: argparse.Namespace) -> None:
    curriculum = load_curriculum()
    notes = existing_notes()
    statuses = statuses_of(notes)
    if args.day:
        day = args.day
    else:
        in_progress = [d for d, status in statuses.items() if status != "done"]
        if not in_progress:
            raise SystemExit("No day in progress. Start one with: python scripts/day.py new")
        day = max(in_progress)
    if day not in notes:
        raise SystemExit(f"Day {day} has not been started. Run: python scripts/day.py new {day}")

    text = read(notes[day])
    text = set_field(text, "status", "done")
    if not parse_date(get_field(text, "completed")):
        text = set_field(text, "completed", date.today().isoformat())
    write(notes[day], text)

    update_readme(curriculum, notes)
    statuses = statuses_of(notes)
    done = sum(1 for status in statuses.values() if status == "done")
    print(f"Day {day} marked done ({done}/{TOTAL_DAYS}).")
    in_progress = sorted(d for d, status in statuses.items() if status != "done")
    if in_progress:
        print(f"Still in progress: Day {', Day '.join(map(str, in_progress))}")
    elif max(notes) < TOTAL_DAYS:
        print(f"Next: python scripts/day.py new {max(notes) + 1}")


def cmd_roadmap(_: argparse.Namespace) -> None:
    notes = existing_notes()
    refresh_navigation(notes)
    update_readme(load_curriculum(), notes)
    print("README roadmap and day navigation updated.")


def cmd_status(_: argparse.Namespace) -> None:
    notes = existing_notes()
    if not notes:
        print("No days started yet. Start with: python scripts/day.py new")
        return

    texts = {day: read(note) for day, note in notes.items()}
    done = {day: text for day, text in texts.items() if get_field(text, "status") == "done"}
    in_progress = sorted(day for day in texts if day not in done)
    today = date.today()

    print(f"Completed:      {len(done)}/{TOTAL_DAYS}")
    starts = [d for d in (parse_date(get_field(t, "started")) for t in texts.values()) if d]
    if starts:
        first = min(starts)
        elapsed = (today - first).days + 1
        print(f"Started:        {first} ({elapsed} calendar day(s) so far)")
        if done:
            pace = len(done) / elapsed
            remaining = TOTAL_DAYS - len(done)
            finish = today + timedelta(days=math.ceil(remaining / pace))
            print(f"Pace:           {pace:.2f} course days per calendar day -> finish around {finish}")

    completed = [d for d in (parse_date(get_field(t, "completed")) for t in done.values()) if d]
    if completed:
        last = max(completed)
        print(f"Last completed: {last} ({(today - last).days} day(s) ago)")

    if in_progress:
        print(f"In progress:    Day {', Day '.join(map(str, in_progress))}")
        print(f"When finished:  python scripts/day.py done {in_progress[-1]}")
    elif max(notes) < TOTAL_DAYS:
        print("Next:           python scripts/day.py new")


def main() -> None:
    parser = argparse.ArgumentParser(description="Study helper for the 100 Days of Code repo.")
    commands = parser.add_subparsers(dest="command", required=True)

    new = commands.add_parser("new", help="scaffold a day (defaults to the next one)")
    new.add_argument("day", nargs="?", type=int)
    new.add_argument("--title", help="exact section title from the course")
    new.add_argument("--project", help="name of the day's project")

    done = commands.add_parser("done", help="mark a day complete (defaults to the day in progress)")
    done.add_argument("day", nargs="?", type=int)

    commands.add_parser("roadmap", help="regenerate the README roadmap and day navigation")
    commands.add_parser("status", help="show progress, pace and the next step")

    args = parser.parse_args()
    handlers = {"new": cmd_new, "done": cmd_done, "roadmap": cmd_roadmap, "status": cmd_status}
    handlers[args.command](args)


if __name__ == "__main__":
    main()
