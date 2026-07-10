# 100 Days of Python Bootcamp

This repository captures my hands-on journey through selected projects and exercises from the 100 Days of Code: The Complete Python Pro Bootcamp. It is not just a folder of practice scripts. It is a progression of real problem-solving: from Python fundamentals and object-oriented programming to GUI apps, data analysis, web scraping, API integrations, and browser automation.

What makes this repo valuable is the evidence of growth. The early files focus on learning core language concepts. The later projects apply those concepts to build small but complete tools that handle user input, external data, file storage, and automation. Taken together, they show how I moved from writing isolated exercises to building practical, working Python applications.

## What You Will Find Here

- Core Python fundamentals: classes, methods, loops, conditionals, functions, and file handling.
- Object-oriented programming: reusable classes for games, quizzes, and UI-driven apps.
- Data work: CSV processing, pandas analysis, and simple data visualization.
- Desktop apps: Tkinter-based applications such as the flash card project.
- APIs and automation: requests-based scripts, email automation, weather/ISS alerts, and habit/workout tracking.
- Web scraping and browser automation: BeautifulSoup, Selenium, and automated workflows.
- Classic games and interactive programs: Snake, Pong, U.S. States quiz, and turtle-based projects.
- Notebook-based analysis: pandas and matplotlib exploration from the later bootcamp days.

## Learning Progression

The repo shows a clear progression across multiple phases:

1. Python foundations and OOP
	- Classes, constructors, instance methods, and basic data modeling.
	- Example: user objects, follow relationships, and reusable class design.

2. Turtle graphics and event-driven programming
	- Drawing patterns, controlling movement with keyboard input, and building interactive canvas-based programs.

3. File handling, CSVs, and pandas
	- Reading, writing, and appending files.
	- Working with tabular data, filtering rows, calculating statistics, and exporting results.

4. GUI applications
	- Building a Tkinter flash card app with timed card flips and persistent progress tracking.

5. APIs, email, and automation
	- Sending email, calling public APIs, and integrating third-party services for real-world utility.

6. Scraping and browser automation
	- Extracting structured information from websites.
	- Automating repetitive browser tasks with Selenium.

7. Analytical notebooks
	- Exploring datasets, cleaning data, reshaping tables, and plotting trends with matplotlib.

## Featured Projects

| Project | What It Demonstrates |
| --- | --- |
| QuizProject | OOP, modular design, and command-line application flow. |
| Snake Game | Game loops, collision detection, state management, and keyboard controls. |
| Pong Game | Two-player mechanics, object movement, scoring, and physics-like bounce logic. |
| U.S. States Game | Data lookup with pandas, map-based interaction, and CSV output for missed states. |
| Flash Card App | Tkinter GUI, timed events, and persistence of learning progress. |
| Top 100 Movies Scraper | Web scraping with BeautifulSoup and structured file output. |
| Automatic Gym Class Booker | Selenium automation, robust retries, and schedule-based decision logic. |
| Amazon Price Tracker | Scraping dynamic product data and sending price alerts by email. |
| ISS / Weather / Stock Alert Scripts | API requests, JSON parsing, and notification-driven automation. |
| Habit / Workout Tracker | API integration with Pixela and Sheety-style workflow tracking. |
| Day 72-73 Notebooks | Pandas analysis, grouping, reshaping, and visualization of real datasets. |

## Why This Repository Matters

Recruiters usually want to see more than syntax practice. They want proof that a candidate can break down a problem, ship something usable, and work with the tools that show up in real software projects. This repo demonstrates exactly that:

- I can move from toy examples to complete applications.
- I understand how to integrate Python with files, APIs, GUIs, and browsers.
- I can use data libraries like pandas to inspect, clean, and transform information.
- I can automate repetitive tasks and design scripts that save time.
- I can structure code into reusable parts instead of keeping everything in one file.

## Repository Structure

- `Day-16.py` to `Day-19.py`: early Python and OOP practice.
- `Day-24/` to `Day-33/`: file handling, pandas, Tkinter, APIs, and small automation tools.
- `Day-35/` to `Day-48/`: web scraping, Selenium, alerts, and web-driven projects.
- `Day-72/` and `Day-73/`: notebook-based data analysis and visualization.
- `QuizProject/`, `Snake Game/`, `Pong Game/`, `us-states-game/`, `top100-movies/`, `Automatic Gym Class Booker/`, and others: standalone portfolio projects.

## How To Run

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the project you want, for example:

```bash
python "Snake Game/main.py"
python "QuizProject/main.py"
python "Automatic Gym Class Booker/main.py"
```

Some projects require extra setup:

- API keys or email credentials for alerting scripts.
- Google Chrome and Selenium WebDriver support for browser automation.
- Additional data files included in the project folders.

## Notes

- This repo is intentionally iterative. Some files are practice-focused, while others are polished mini-projects.
- Secrets are not meant to be committed. Scripts that depend on APIs should be configured locally before running.
- Several projects are designed to be extended further, so they serve as a strong base for portfolio improvements.

## Highlights For Reviewers

If you are reviewing this repo for hiring or collaboration, the strongest signals are the ability to:

- build interactive applications with clean program flow,
- automate repeated tasks with Python,
- consume and transform external data,
- persist user progress and state,
- and move confidently across command-line apps, GUIs, scraping, and analytics.

## About The Author

This repository reflects my learning path as I built confidence in Python through consistent practice and progressively more ambitious projects. The goal was not only to complete exercises, but to develop the habit of turning concepts into working software.
