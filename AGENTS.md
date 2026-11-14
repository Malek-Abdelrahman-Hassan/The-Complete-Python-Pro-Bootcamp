# AGENTS.md

Conventions for anyone (people or AI assistants) writing in this repository: a public, day-by-day study repo for the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*, which is also used as an Obsidian vault.

## Audience and tone

- Notes are public learning material for anyone taking the course. Write in a neutral, instructional voice: "A variable stores...", "Use an f-string to...". Addressing the reader as "you" is fine.
- Public files contain no first person, no references to the repository owner, and no personal anecdotes, study times, feelings or progress remarks. Personal content goes in `_personal/`, which is gitignored.
- Explain at the level of the course at that day. Topics the course has not reached yet are only mentioned as "covered on Day N".

## Source material and copyright

- Transcripts, slides and course downloads live in the day's `_raw/` folder, which is gitignored. Never copy them anywhere that gets committed.
- In `_raw/`, save each transcript as a `.md` file named after the lecture (`6. Printing to the Console in Python.md`) and each coding exercise brief as `Coding Exercise N Title.md`. Leave PDFs and other downloads unchanged. A lecture whose transcript is missing gets a file with a `> [!WARNING]` placeholder, so the gap stays visible.
- Write notes in your own words. No verbatim transcript passages; quote a short phrase only when the exact wording matters.
- Course starter files that a project needs in order to run may be committed inside `project/`.

## Processing a day's material

When a day's material is provided (transcripts, files, lecture list):

1. Make sure the day exists: `python scripts/day.py new N`. The titles of all 100 course sections are already in `scripts/curriculum.json`. If the course shows a different title, pass it with `--title "<Title>"`: sections are named "Day N - Level - Title", so pass only the Title part.
2. Read everything in the day's `_raw/` folder and any material pasted in the conversation.
3. Fill in the day note `days/Day N - Level - Title/Day N - Level - Title.md`, keeping the template's sections and their order:
   - **TL;DR**: 3-5 bullets with the ideas worth remembering.
   - **Learning objectives**: start each one with an action verb.
   - **Lessons**: one numbered `###` subsection per lecture, in course order, using the lecture's title. Cover the idea, a small code example, and why it matters. Fold housekeeping lectures into one line or skip them.
   - **Key concepts**: table rows, linking to concept notes where they exist.
   - **Cheat sheet**: minimal, runnable snippets of every new piece of syntax.
   - **Common pitfalls**: real beginner mistakes, with the error message when it helps.
   - **Exercises**: the course's coding exercises, linking the code files in `exercises/` when present.
   - **Project**: goal, how it works (steps or a Mermaid flowchart), how to run it, and ideas to extend it. Delete the section on days without a project.
   - **Recall questions**: 5-10 questions, mixing conceptual questions with "what does this code print?".
   - **Further reading**: official documentation first.
4. Concept notes: for each significant new topic, create `concepts/<kebab-case-name>.md` from `templates/concept.md`, or extend the existing note (new syntax, a new line under **Appears in**). List every new note in `concepts/concepts.md` under the matching section, replacing the italic placeholder line when the section gets its first entry. Add one-line definitions to `concepts/glossary.md` in alphabetical order.
5. Run `python scripts/day.py roadmap`. Run `python scripts/day.py done N` only once the day is actually finished.
6. Do not write exercise or project solutions unless asked. Starter files hold the brief in a module docstring and a marked place for the solution. Own code goes in `exercises/` and `project/`; the note describes the approach and shows only the key lines.

## Day folder layout

Each day folder is named after its course section, `Day N - Level - Title`, and holds a note with the same name, so the Folder notes plugin opens it when the folder is clicked. `scripts/day.py` creates both. Characters that Windows paths or Obsidian links cannot handle are adjusted: `:` becomes ` -`, `/` becomes `-`, and `\ * ? " < > | [ ] # ^` are dropped.

```text
days/Day 1 - Beginner - Working with Variables in Python to Manage Data/
├── Day 1 - Beginner - Working with Variables in Python to Manage Data.md   the day note
├── exercises/   NN_short_name.py, e.g. 01_printing_practice.py
├── project/     main.py plus its assets; one subfolder per project if there are several
├── assets/      images used by the note
└── _raw/        local-only source material
```

Rename or move files inside Obsidian, which updates the links pointing to them. See [guides/obsidian-cheatsheet.md](guides/obsidian-cheatsheet.md) for the plugins and the daily routine.

## Markdown rules

Every note must render the same in Obsidian and on GitHub.

- Links: relative Markdown links including `.md`, e.g. `[Lists](../../concepts/lists.md)`. No `[[wikilinks]]`, no `![[embeds]]`. Write spaces in link targets as `%20`: `[Day 1](../days/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data.md)`.
- Callouts: only `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]` and `> [!CAUTION]`, without custom titles or folding (`> [!TIP]-`).
- No Obsidian-only syntax: `==highlights==`, `%%comments%%`, Dataview queries, block references. Use `<!-- -->` for comments.
- Hidden answers: `<details><summary>Question?</summary>Answer.</details>`. Keep answers plain text, since Obsidian does not render Markdown inside HTML; use `<code>` for code.
- Code blocks always name a language (`python`, `text`, `bash`, `html`, ...). Show program output in a separate `text` block.
- Diagrams use Mermaid. Images go in the note's `assets/` folder.
- A single newline is not a line break (strict line breaks, as on GitHub). Separate paragraphs with a blank line.
- Frontmatter keeps the template keys. Tags are lowercase and hierarchical: `day/001`, `level/beginner`, `concept`.
- Never hand-edit lines ending in `<!-- nav -->` or the README blocks between the `progress` and `roadmap` markers; `scripts/day.py` regenerates them.

## Code conventions

- Python 3.10+, PEP 8, `snake_case`, 4-space indentation.
- Secrets live in a `.env` file (gitignored) and are read from environment variables; commit a `.env.example` with placeholder values.
- When a day introduces a third-party package, add it to `requirements.txt` with a `# Day N - Title` comment.
