# 100 Days of Code: The Complete Python Pro Bootcamp

Day-by-day study notes, exercises and projects for the Udemy course [100 Days of Code™: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu. The notes are written as reusable learning material, and the repository doubles as an [Obsidian](https://obsidian.md) vault.

<!-- progress:start -->
**Progress:** 10 / 100 days completed `██░░░░░░░░░░░░░░░░░░` 10%
<!-- progress:end -->

> [!NOTE]
> These are independent study notes, not affiliated with or endorsed by Udemy or The App Brewery. The notes are original summaries rather than transcripts. The full lessons are only available in the course.

## What's inside

Every course day has one note that works both as a study guide and as a quick recap:

| Section | Use it to |
| --- | --- |
| TL;DR | Refresh the key ideas in under a minute |
| Lessons | Follow the explanations lesson by lesson |
| Key concepts and Cheat sheet | Look up syntax and patterns quickly |
| Common pitfalls | Avoid the usual beginner mistakes |
| Exercises and Project | Practise, then run and extend the code |
| Recall questions | Test yourself before revealing the answers |

Notes that span the whole course:

- [Concepts](concepts/concepts.md): one reference note per topic (lists, functions, classes, ...), each linking back to every day where it appears.
- [Glossary](concepts/glossary.md): one-line definitions of the terms used in the notes.
- [Reviews](reviews/reviews.md): milestone reviews that consolidate each level of the course.

## How to recap

1. Read the TL;DR of the day.
2. Answer its recall questions from memory, then expand the answers to check.
3. Re-read only the lessons behind the questions you missed.
4. Re-run the project and try one of its "Ideas to extend it".
5. At the end of each level, work through the milestone review.

## Getting started

### Read the notes in Obsidian

1. Install [Obsidian](https://obsidian.md), choose **Open folder as vault** and select the root folder of this repository.
2. Follow the [Obsidian cheat sheet](guides/obsidian-cheatsheet.md) to turn on the core plugins and install the recommended community plugins (Folder notes, Shell commands, Git, Advanced Tables, Homepage).

The shared settings in `.obsidian/app.json` store links as relative Markdown links, save pasted images to an `assets/` folder next to the note, and render line breaks the same way GitHub does. Notes therefore look the same in Obsidian and on GitHub. The cheat sheet also covers the daily routine, hotkeys, and how to create each kind of note. [dashboard.base](dashboard.base) gives a table view of all days and concepts inside Obsidian.

### Run the code

Requires Python 3.10 or newer.

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Projects run from their day folder, for example:

```bash
cd "days/Day 1 - Beginner - Working with Variables in Python to Manage Data"
python project/main.py
```

## Repository structure

```text
.
├── days/                     One folder per course day, named after the course section
│   └── Day 1 - Beginner - Working with Variables in Python to Manage Data/
│       ├── Day 1 - Beginner - Working with Variables in Python to Manage Data.md
│       │                     The day note: start here
│       ├── exercises/        Coding exercises from the lessons
│       ├── project/          The day's project
│       ├── assets/           Images used by the note
│       └── _raw/             Local only: transcripts and course downloads
├── concepts/                 Topic reference notes and the glossary
├── reviews/                  Milestone reviews, one per level
├── guides/                   How to use the vault (Obsidian cheat sheet)
├── templates/                Templates for day, concept, review and journal notes
├── scripts/
│   ├── day.py                Study helper: new / done / status / roadmap
│   └── curriculum.json       Titles, levels and projects for all 100 days
├── _personal/                Local only: journal and private notes
├── dashboard.base            Obsidian table view of days and concepts
├── AGENTS.md                 Note-writing conventions (for people and AI assistants)
└── requirements.txt          Third-party packages, added as the course needs them
```

Two kinds of folders are **local only**: they are listed in `.gitignore` and never pushed.

- `days/*/_raw/` holds lecture transcripts (saved as `.md` files), slides and course downloads, which are the source material for the notes and remain the course's property.
- `_personal/` holds the study journal and any private notes.

## Daily workflow

```bash
python scripts/day.py new      # scaffold the next day (+ a local journal entry)
python scripts/day.py done     # mark the day in progress as complete
python scripts/day.py status   # progress, pace and the next step
python scripts/day.py roadmap  # rebuild the roadmap and day navigation links
```

The titles of all 100 course sections are stored in [scripts/curriculum.json](scripts/curriculum.json), and `new` names the day's folder after its section. `new` also accepts a day number, and `--title "<section title>"` corrects a title if the course changes it. The progress line, the roadmap and the navigation links in day notes are generated, so change the day notes or `curriculum.json` instead of editing them by hand.

A typical day:

1. Run `python scripts/day.py new`.
2. Save the transcripts as `.md` files, plus the course downloads, in the day's `_raw/` folder.
3. Work through the lessons: exercises go in `exercises/`, the project in `project/`.
4. Write the day note following the conventions in [AGENTS.md](AGENTS.md).
5. Add or extend concept notes and glossary entries.
6. Run `python scripts/day.py done` and commit, e.g. `git commit -m "Day 1: Working with Variables"`.

## Roadmap

<!-- roadmap:start -->
### Beginner · Days 1–14

| Day | Topic | Project | Status |
| ---: | --- | --- | :---: |
| 1 | [Working with Variables in Python to Manage Data](days/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data.md) | Band Name Generator | ✅ |
| 2 | [Understanding Data Types and How to Manipulate Strings](days/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings.md) | Tip Calculator | ✅ |
| 3 | [Control Flow and Logical Operators](days/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators.md) | Treasure Island | ✅ |
| 4 | [Randomisation and Python Lists](days/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists.md) | Rock Paper Scissors | ✅ |
| 5 | [Python Loops](days/Day%205%20-%20Beginner%20-%20Python%20Loops/Day%205%20-%20Beginner%20-%20Python%20Loops.md) | Password Generator | ✅ |
| 6 | [Python Functions & Karel](days/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel.md) | Escaping the Maze (Reeborg's World) | ✅ |
| 7 | [Hangman](days/Day%207%20-%20Beginner%20-%20Hangman/Day%207%20-%20Beginner%20-%20Hangman.md) | Hangman | ✅ |
| 8 | [Function Parameters & Caesar Cipher](days/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher.md) | Caesar Cipher | ✅ |
| 9 | [Dictionaries, Nesting and the Secret Auction](days/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction.md) | Secret Auction | ✅ |
| 10 | [Functions with Outputs](days/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs.md) | Calculator | ✅ |
| 11 | The Blackjack Capstone Project | Blackjack | ⬜ |
| 12 | Scope & Number Guessing Game | Number Guessing Game | ⬜ |
| 13 | Debugging: How to Find and Fix Errors in your Code | — | ⬜ |
| 14 | Higher Lower Game Project | Higher Lower Game | ⬜ |

### Intermediate · Days 15–31

| Day | Topic | Project | Status |
| ---: | --- | --- | :---: |
| 15 | Local Development Environment Setup & the Coffee Machine | Coffee Machine | ⬜ |
| 16 | Object Oriented Programming (OOP) | Coffee Machine in OOP | ⬜ |
| 17 | The Quiz Project & the Benefits of OOP | Quiz Game | ⬜ |
| 18 | Turtle & the Graphical User Interface (GUI) | Hirst Spot Painting | ⬜ |
| 19 | Instances, State and Higher Order Functions | Etch-A-Sketch & Turtle Race | ⬜ |
| 20 | Build the Snake Game Part 1: Animation & Coordinates | Snake Game | ⬜ |
| 21 | Build the Snake Game Part 2: Inheritance & List Slicing | Snake Game | ⬜ |
| 22 | Build Pong: The Famous Arcade Game | Pong | ⬜ |
| 23 | The Turtle Crossing Capstone Project | Turtle Crossing | ⬜ |
| 24 | Files, Directories and Paths | Mail Merge | ⬜ |
| 25 | Working with CSV Data and the Pandas Library | U.S. States Game | ⬜ |
| 26 | List Comprehension and the NATO Alphabet | NATO Alphabet | ⬜ |
| 27 | Tkinter, \*args, \*\*kwargs and Creating GUI Programs | Mile to Km Converter | ⬜ |
| 28 | Tkinter, Dynamic Typing and the Pomodoro GUI Application | Pomodoro Timer | ⬜ |
| 29 | Building a Password Manager GUI App with Tkinter | Password Manager | ⬜ |
| 30 | Errors, Exceptions and JSON Data: Improving the Password Manager | Password Manager (improved) | ⬜ |
| 31 | Flash Card App Capstone Project | Flash Card App | ⬜ |

### Intermediate+ · Days 32–58

| Day | Topic | Project | Status |
| ---: | --- | --- | :---: |
| 32 | Send Email (smtplib) & Manage Dates (datetime) | Automated Birthday Wisher | ⬜ |
| 33 | API Endpoints & API Parameters - ISS Overhead Notifier | ISS Overhead Notifier | ⬜ |
| 34 | API Practice - Creating a GUI Quiz App | Quizzler | ⬜ |
| 35 | Keys, Authentication & Environment Variables: Send SMS | Rain Alert | ⬜ |
| 36 | Stock Trading News Alert Project | Stock News Alert | ⬜ |
| 37 | Habit Tracking Project: API Post Requests & Headers | Habit Tracker | ⬜ |
| 38 | Workout Tracking Using Google Sheets | Workout Tracker | ⬜ |
| 39 | Capstone Part 1: Flight Deal Finder | Flight Deal Finder | ⬜ |
| 40 | Capstone Part 2: Flight Club | Flight Club | ⬜ |
| 41 | Introduction to HTML *(Web Foundation)* | — | ⬜ |
| 42 | Intermediate HTML *(Web Foundation)* | — | ⬜ |
| 43 | Introduction to CSS *(Web Foundation)* | — | ⬜ |
| 44 | Intermediate CSS *(Web Foundation)* | — | ⬜ |
| 45 | Web Scraping with Beautiful Soup | 100 Movies to Watch | ⬜ |
| 46 | Create a Spotify Playlist using the Musical Time Machine | Musical Time Machine | ⬜ |
| 47 | Create an Automated Amazon Price Tracker | Amazon Price Tracker | ⬜ |
| 48 | Selenium Webdriver Browser and Game Playing Bot | Cookie Clicker Bot | ⬜ |
| 49 | Automating your Exercise Routine at the Gym | Gym Booking Bot | ⬜ |
| 50 | Auto Tinder Swiping Bot | Swiping Bot | ⬜ |
| 51 | Internet Speed X Complaint Bot | Internet Speed Complaint Bot | ⬜ |
| 52 | Instagram Follower Bot | Instagram Follower Bot | ⬜ |
| 53 | Web Scraping Capstone - Data Entry Job Automation | Data Entry Automation | ⬜ |
| 54 | Introduction to Web Development with Flask | — | ⬜ |
| 55 | HTML & URL Parsing in Flask and the Higher Lower Game | Higher Lower (Flask) | ⬜ |
| 56 | Rendering HTML/Static files and using Website Templates | Personal Site | ⬜ |
| 57 | Templating with Jinja in Flask Applications | Blog (Part 1) | ⬜ |
| 58 | Bootstrap *(Web Foundation)* | — | ⬜ |

### Advanced · Days 59–81

| Day | Topic | Project | Status |
| ---: | --- | --- | :---: |
| 59 | Blog Capstone Project Part 2 - Adding Styling | Blog (Part 2) | ⬜ |
| 60 | Make POST Requests with Flask and HTML Forms | Blog Contact Form | ⬜ |
| 61 | Building Advanced Forms with Flask-WTForms | Login Form | ⬜ |
| 62 | Flask, WTForms, Bootstrap and CSV - Coffee & Wifi Project | Coffee & Wifi | ⬜ |
| 63 | Databases with SQLite and SQLAlchemy | Virtual Bookshelf | ⬜ |
| 64 | My Top 10 Movies Website | Top 10 Movies | ⬜ |
| 65 | How to Create a Website that People will Love *(Web Design School)* | — | ⬜ |
| 66 | Building Your Own API with RESTful Routing | Cafe API | ⬜ |
| 67 | Blog Capstone Project Part 3 - RESTful Routing | Blog (Part 3) | ⬜ |
| 68 | Authentication with Flask | — | ⬜ |
| 69 | Blog Capstone Project Part 4 - Adding Users | Blog (Part 4) | ⬜ |
| 70 | Git, Github and Version Control | — | ⬜ |
| 71 | Deploying Your Web Application | Deploy the Blog | ⬜ |
| 72 | Data Exploration with Pandas: College Major v.s. Your Salary | College Majors vs. Salaries | ⬜ |
| 73 | Data Visualisation with Matplotlib: Programming Languages | Programming Language Popularity | ⬜ |
| 74 | Aggregate & Merge Data with Pandas: Analyse the LEGO Dataset | LEGO Dataset Analysis | ⬜ |
| 75 | Google Trends Data: Resampling and Visualising Time Series | Google Trends Analysis | ⬜ |
| 76 | Beautiful Plotly Charts & Analysing the Android App Store | Google Play Store Analysis | ⬜ |
| 77 | Computation with NumPy and N-Dimensional Arrays | — | ⬜ |
| 78 | Linear Regression and Data Visualisation with Seaborn | Movie Budgets & Revenue | ⬜ |
| 79 | Analysing the Nobel Prize with Plotly, Matplotlib & Seaborn | Nobel Prize Analysis | ⬜ |
| 80 | The Tragic Discovery of Handwashing: t-Tests & Distributions | Handwashing Analysis | ⬜ |
| 81 | Capstone Project - Predict House Prices | House Price Predictor | ⬜ |

### Professional Portfolio Project · Days 82–100

| Day | Topic | Project | Status |
| ---: | --- | --- | :---: |
| 82 | Python Scripting | Text to Morse Code Converter | ⬜ |
| 83 | Python Web Development | Portfolio Website | ⬜ |
| 84 | Python Scripting | Tic Tac Toe | ⬜ |
| 85 | GUI | Image Watermarking App | ⬜ |
| 86 | GUI | Typing Speed Test | ⬜ |
| 87 | Game | Breakout | ⬜ |
| 88 | Web Development | Cafe & Wifi Website | ⬜ |
| 89 | Web Development | To-Do List | ⬜ |
| 90 | GUI Desktop App | Disappearing Text Writing App | ⬜ |
| 91 | HTTP Requests & APIs | PDF to Audiobook | ⬜ |
| 92 | Image Processing & Data Science | Image Colour Palette Generator | ⬜ |
| 93 | Web Scraping | Custom Web Scraper | ⬜ |
| 94 | GUI Automation | Google Dinosaur Game Bot | ⬜ |
| 95 | Game | Space Invaders | ⬜ |
| 96 | HTTP Requests & APIs | Custom API-Based Website | ⬜ |
| 97 | Web Development | Online Shop | ⬜ |
| 98 | Python Automation | Automate a Task | ⬜ |
| 99 | Data Science | Deaths Involving Police in the US | ⬜ |
| 100 | Data Science | Predict Earnings with Multivariable Regression | ⬜ |

**After Day 100:** Final Stretch · Bonus Lecture: Succeed in the Age of AI

✅ done · 🚧 in progress · ⬜ not started
<!-- roadmap:end -->

## Resources

- [Python documentation](https://docs.python.org/3/), including the official [tutorial](https://docs.python.org/3/tutorial/) and [standard library reference](https://docs.python.org/3/library/)
- [PEP 8: Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Obsidian Help](https://help.obsidian.md/)
- [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github): GitHub-flavoured Markdown, alerts and more
