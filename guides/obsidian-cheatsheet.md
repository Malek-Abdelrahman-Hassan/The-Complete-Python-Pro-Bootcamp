---
tags:
  - guide
aliases:
  - Obsidian cheat sheet
---

# Obsidian cheat sheet

How to use this repository as an [Obsidian](https://obsidian.md) vault: which plugins to install, how to set them up, the daily routine, and how to create every kind of note so that it renders the same in Obsidian and on GitHub.

[README](../README.md) · [AGENTS.md](../AGENTS.md) (note-writing conventions)

## First-time setup

1. Install Obsidian, choose **Open folder as vault** and select the root folder of the repository.
2. Turn on the core plugins listed under [Core plugins](#core-plugins).
3. Install and configure the [community plugins](#community-plugins).
4. Restart Obsidian whenever `.obsidian/app.json` changes, for example after a `git pull`.

The repository already contains the shared settings, so nothing needs to be changed under **Settings → Files and links** or **Settings → Editor**:

| Setting in `.obsidian/app.json` | Effect |
| --- | --- |
| `useMarkdownLinks`, `newLinkFormat: relative` | Links are written as `[text](../path/note.md)`, which also works on GitHub |
| `alwaysUpdateLinks` | Renaming or moving a file inside Obsidian updates every link to it |
| `attachmentFolderPath: ./assets` | Pasted images go to an `assets/` folder next to the note |
| `strictLineBreaks` | A single newline is not a line break, as on GitHub |
| `showUnsupportedFiles` | `.py`, `.json` and `.txt` files appear in the file explorer and can be linked |
| `userIgnoreFilters` | `templates/` and every `_raw/` folder are left out of search, the graph and link suggestions |
| `.obsidian/templates.json` | The Templates plugin reads from `templates/` |

> [!WARNING]
> Rename and move files **inside Obsidian**, not in the system file explorer. Only Obsidian updates the links that point to them.

## Core plugins

**Settings → Core plugins**:

| Plugin | Setting | Use it for |
| --- | --- | --- |
| Templates | On | Inserting the concept and review templates |
| Command palette | On | Running any command with `Ctrl + P` |
| Quick switcher | On | Opening any note by typing part of its name (`Ctrl + O`) |
| Slash commands | On | Typing `/` in a note to run a command at the cursor |
| Backlinks | On | Seeing which notes link to the current one, such as every day that uses a concept |
| Outline | On | Jumping between the lessons of a long day note |
| Page preview | On | Previewing a link by hovering over it (with `Ctrl` held in editing view) |
| Properties view | On | Reading and editing the frontmatter (`status`, `started`, ...) |
| Bookmarks | On | Pinning the README, the concepts index and the current day |
| Graph view | On | Seeing how days and concepts connect |
| Bases | On | The progress dashboard in `dashboard.base` |
| File recovery | On | Restoring earlier versions of a note |
| Daily notes | Off | Not needed: day notes come from `scripts/day.py`, and daily notes would add date-named files to the vault |

## Community plugins

**Settings → Community plugins → Turn on community plugins → Browse**, search for the plugin by name, then **Install** and **Enable**.

### Recommended

| Plugin | Author | Use it for |
| --- | --- | --- |
| Folder notes | LostPaul | Clicking a day folder to open its day note |
| Shell commands | Taitava | Running `scripts/day.py` from the command palette |
| Git | Vinzent03 | Committing and pushing without leaving Obsidian |
| Advanced Tables | tgrosinger | Formatting Markdown tables while typing |
| Homepage | novov | Opening the README when the vault starts |

### Optional

| Plugin | Author | Use it for |
| --- | --- | --- |
| Execute Code | twibiral | Running the `python` code blocks of a note inside Obsidian |
| Omnisearch | scambier | Search that tolerates typos and ranks results |

### Folder notes

Each day folder already holds a note with the same name as the folder (`Day 1 - .../Day 1 - ....md`), which is exactly what this plugin expects.

| Setting | Value |
| --- | --- |
| Folder note name | `{{folder_name}}` (default) |
| Storage location | Inside the folder (default) |
| Hide folder note | On, so the note does not appear twice in the file explorer |

Day notes are created by `scripts/day.py`, so the plugin's "Create folder note" command is not needed for day folders.

### Shell commands

**Settings → Shell commands → New shell command**. Add these four commands, then open each command's extra options (the gear icon) to give it an alias:

| Shell command | Alias |
| --- | --- |
| `python scripts/day.py new` | Day: start the next day |
| `python scripts/day.py done` | Day: mark the current day done |
| `python scripts/day.py status` | Day: show progress |
| `python scripts/day.py roadmap` | Day: rebuild the roadmap |

For each command, set **Output channel for stdout** to **Notification/Error balloon** in the extra options, so the script's messages appear in Obsidian. Commands run in the vault root, where `scripts/` is. If `python` is not found, use `py` on Windows or the full path to the Python executable.

The commands then appear in the command palette as `Shell commands: Execute: Day: ...`. Hotkeys can be assigned under **Settings → Hotkeys**.

### Git

The plugin uses the Git installed on the computer. `_personal/` and every `_raw/` folder are gitignored, so they are never committed.

| Command (`Ctrl + P`) | Does |
| --- | --- |
| `Git: Open source control view` | Shows changed files, with buttons to stage, commit and push |
| `Git: Commit all changes` | Commits everything that changed |
| `Git: Commit-and-sync` | Commits, pulls, then pushes |
| `Git: Pull` | Downloads changes made on another computer |

Leave automatic commits switched off (the auto commit-and-sync interval set to `0`), so every commit is a deliberate one with a clear message, such as `Day 2: Understanding Data Types`.

### Homepage

Set **Homepage** to `README` and turn on **Open on startup**. The README shows the progress line and the roadmap with a link to every day.

### Advanced Tables

Type the header row of a table (`| Term | Definition |`) and press `Tab`: the plugin adds the separator row and aligns the columns. `Tab` moves to the next cell, `Enter` to the next row.

## Plugins and syntax to avoid

These only work in Obsidian. On GitHub they show up as raw text or code:

| Avoid | Use instead |
| --- | --- |
| Dataview queries | The generated README roadmap, or `dashboard.base` for local views |
| Templater (`<% %>`) | The core Templates plugin; `day.py` fills the day template |
| Excalidraw drawings | Mermaid diagrams, or an image in `assets/` |
| Admonition blocks | Callouts: `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]` |
| Spaced repetition cards (`question::answer`) | Recall questions in `<details>` blocks |
| `[[wikilinks]]` and `![[embeds]]` | Markdown links; the vault settings create them automatically |
| `==highlights==` and `%%comments%%` | `**bold**` and `<!-- comments -->` |

## Daily routine

| Step | In Obsidian | In a terminal |
| --- | --- | --- |
| 1. Start the day | `Ctrl + P` → `Day: start the next day` | `python scripts/day.py new` |
| 2. Save the material | Paste transcripts into `.md` files in the day's `_raw/` folder, next to the PDFs | |
| 3. Code along | Keep the note open beside the editor | Save code in `exercises/` and `project/` |
| 4. Write the note | Open it with `Ctrl + O` → `Day 2`, or click the folder | |
| 5. Update concepts | Extend or create concept notes and glossary entries | |
| 6. Finish the day | `Ctrl + P` → `Day: mark the current day done` | `python scripts/day.py done` |
| 7. Commit | `Git: Commit-and-sync` | `git add -A`, `git commit -m "Day 2: ..."`, `git push` |
| 8. Recap tomorrow | Answer yesterday's recall questions before starting the new day | |

## Creating notes

### A day note

Always with the script: `python scripts/day.py new` (or the Shell commands button). It creates the folder with `exercises/`, `project/` and `_raw/`, the day note from the template, a local journal entry, and updates the README roadmap and the navigation links.

> [!IMPORTANT]
> Do not insert `templates/day.md` or `templates/journal.md` with the Templates plugin. Their `{{day}}` and `{{nav}}` placeholders are only filled by the script.

### A concept note

1. Right-click the `concepts` folder → **New note**. Name it in kebab-case, for example `for-loops`.
2. `Ctrl + P` → `Templates: Insert template` → `concept`. Obsidian fills in `{{title}}` and `{{date}}`.
3. Change the heading to a readable title, such as `# For loops`.
4. Add a line under **Appears in** linking the day, and list the note in [Concepts](../concepts/concepts.md).

### A glossary entry

Add a row to the table in [Glossary](../concepts/glossary.md), keeping the terms in alphabetical order.

### A milestone review

At the end of a level, create `reviews/<level>.md` (for example `reviews/beginner.md`), insert the `review` template, and link it from [Reviews](../reviews/reviews.md).

## Writing in a note

| To add | Type | Notes |
| --- | --- | --- |
| A link to a note | `[[` then the note name | Obsidian converts it to a relative Markdown link |
| A link to a heading | `[[note#` then the heading | Headings in the same note: `[Project](#project)` |
| A link to a website | `Ctrl + K`, or `[text](https://...)` | |
| An image | Paste or drag it into the note | Saved to `assets/`; rename it inside Obsidian afterwards |
| A callout | `> [!TIP]` then the text on the next `>` line | Only NOTE, TIP, IMPORTANT, WARNING, CAUTION, in capitals, without titles |
| Code | ```` ```python ```` ... ```` ``` ```` | Always name the language; put output in a separate `text` block |
| A diagram | ```` ```mermaid ```` | Renders in Obsidian and on GitHub |
| A recall question | `<details><summary>Question?</summary>Answer.</details>` | Plain text inside; use `<code>` for code |
| A table | The header row, then `Tab` | Advanced Tables adds the separator row |
| A comment | `<!-- hidden text -->` | Hidden in both Obsidian and GitHub |

## Hotkeys

Defaults on Windows and Linux; on macOS use `Cmd` instead of `Ctrl`.

| Hotkey | Action |
| --- | --- |
| `Ctrl + P` | Command palette: run any command |
| `Ctrl + O` | Quick switcher: open a note by name |
| `Ctrl + N` | New note |
| `Ctrl + E` | Switch between editing and reading view |
| `Ctrl + F` / `Ctrl + H` | Find / replace in the current note |
| `Ctrl + Shift + F` | Search all notes |
| `Ctrl + G` | Graph view |
| `Ctrl + K` | Insert a Markdown link |
| `Ctrl + B` / `Ctrl + I` | Bold / italic |
| `Ctrl + L` | Toggle a checkbox |
| `Alt + Enter` | Follow the link under the cursor |
| `Ctrl + Enter` | Open the link under the cursor in a new tab |
| `Ctrl + Alt + ←` / `→` | Go back / forward |
| `Ctrl + Tab` | Next tab |
| `Ctrl + W` | Close the tab |
| `Ctrl + Shift + T` | Reopen the last closed tab |
| `Ctrl + ,` | Settings |

Worth adding under **Settings → Hotkeys**:

| Command | Suggested hotkey |
| --- | --- |
| `Templates: Insert template` | `Alt + T` |
| `Shell commands: Execute: Day: start the next day` | `Alt + N` |
| `Shell commands: Execute: Day: mark the current day done` | `Alt + D` |

> [!CAUTION]
> In Obsidian, `Ctrl + /` wraps the selection in `%%` comments, which GitHub shows as plain text. Type `<!-- -->` for a hidden comment instead. In code editors such as PyCharm, `Ctrl + /` comments out Python code as usual.

## Searching

`Ctrl + Shift + F` accepts operators that can be combined:

| Search | Finds |
| --- | --- |
| `path:concepts loop` | "loop" in the concept notes only |
| `tag:#day/001` | The Day 1 note |
| `tag:#level/beginner` | Every Beginner day |
| `"f-string"` | The exact phrase |
| `line:(input string)` | Lines that contain both words |
| `section:(pitfalls NameError)` | `NameError` in a section whose heading mentions pitfalls |
| `-path:_personal` | Excludes the personal folder |

## Graph view

In the graph's settings (the gear icon at the top right of the graph):

- **Filters**: enter `-path:_personal` to hide personal notes, and turn off **Attachments** to hide images.
- **Groups**: add `path:concepts` and `path:days` with two colours to tell concepts and days apart.
- Open **Local graph** from the command palette (`Graph view: Open local graph`) to see only the notes connected to the current one.

## Progress dashboard

[`dashboard.base`](../dashboard.base) is a Bases file (Obsidian 1.9 or newer) with three table views built from the notes' frontmatter:

| View | Shows |
| --- | --- |
| Days | Every day note with its project, status and dates |
| In progress | Day notes whose `status` is not `done` |
| Concepts | Every concept note and the date it was created |

Open it from the file explorer and switch views from the view menu at the top left. Bases files only work in Obsidian; on GitHub the README roadmap gives the same overview.

## Further reading

- [Obsidian Help](https://help.obsidian.md/), including [hotkeys](https://help.obsidian.md/hotkeys), [search](https://help.obsidian.md/plugins/search) and [Bases](https://help.obsidian.md/bases)
- [Shell commands documentation](https://publish.obsidian.md/shellcommands)
- [Folder notes documentation](https://lostpaul.github.io/obsidian-folder-notes/)
- [Git plugin documentation](https://publish.obsidian.md/git-doc)
- [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github): GitHub-flavoured Markdown and alerts
