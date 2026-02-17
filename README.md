El País Opinion Scraper
Selenium Automation + BrowserStack Parallel Testing

BrowserStack Customer Engineering Assignment

A Python-based Selenium automation project that scrapes articles from the El País Opinion section, translates article titles to English, performs text analysis, and executes the workflow across multiple browsers in parallel using BrowserStack.

Project Overview

This project demonstrates an end-to-end automation workflow combining:

Web scraping using Selenium WebDriver

API-based language translation

Text processing and word-frequency analysis

Cross-browser testing on BrowserStack

Parallel test execution across desktop and real mobile devices

Secure credential management using environment variables

Features
Core Functionality

Validates that the website content is in Spanish

Navigates to the El País Opinion section

Scrapes the first 5 opinion articles

Title (Spanish)

Full article content

Cover image (if available)

Translates article titles from Spanish → English

Identifies repeated words in translated titles

Automatically handles cookie consent popups

Technical Highlights

Full Article Extraction
Articles are opened individually to capture complete content instead of preview snippets.

Parallel BrowserStack Execution
Runs across 5 browsers/devices simultaneously using multithreading.

Secure Credential Management
All secrets are stored in .env and never committed to Git.

Cross-Platform Automation Strategy
Different navigation strategies for desktop vs mobile browsers ensure stability.

Quick Start
Prerequisites

Python 3.8+

Google Chrome installed

BrowserStack account

Install dependencies:

pip install -r requirements.txt

Environment Setup

Create a .env file in the project root:

BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key


The .env file is excluded from Git via .gitignore.

Running the Tests
Local Execution

Runs the scraper in Chrome and opens each article in a new tab.

python src/run_test.py

BrowserStack Execution

Runs the workflow in parallel across 5 environments:

python src/browserstack_script.py

Project Structure
browserstack-el-pais/
├── article_images/              # Downloaded article images
├── src/
│   ├── browserstack_script.py   # BrowserStack parallel execution
│   ├── run_test.py              # Local Selenium runner
│   └── scraper.py               # Scraping + translation + analysis
├── .env                         # Environment variables (ignored)
├── .gitignore
├── requirements.txt
└── README.md

Test Results
Local Execution

Articles scraped: 5/5

Images downloaded: 5/5

Translation: Successful

Word analysis: Successful

BrowserStack Cross-Browser Execution

Executed across 5 parallel environments:

Browser	Platform	Status
Chrome	Windows 10	Passed
Firefox	macOS Monterey	Passed
Safari	macOS Ventura	Passed
Chrome	Samsung Galaxy S21	Passed
Safari	iPhone 13	Passed

Overall Result: 5/5 Environments Passed

Word Analysis Output (Example)
Repeated Words in Translated Titles:
the = 2
to = 2

Key Technologies

Selenium WebDriver 4

BrowserStack Automate

Python

deep-translator (Google Translate wrapper)

Requests

ThreadPoolExecutor (parallel execution)

Performance Optimizations
Parallel Execution

Five BrowserStack sessions run simultaneously, reducing total execution time.

Stable Cross-Browser Strategy

Separate automation flows for local debugging and cloud execution improve reliability.

Efficient Scraping Workflow

Minimal page reloads and optimized waits ensure faster execution.

Security Best Practices

No hardcoded credentials

Environment variables for secrets

.env excluded from version control

Safe API usage

Assignment Checklist

All required tasks have been completed:

Open El País website in Spanish

Navigate to Opinion section

Scrape first 5 articles

Download cover images

Translate titles to English

Analyze repeated words

Run locally

Run on BrowserStack

Execute in parallel across multiple browsers

Candidate

Harsh Vaishnav
BrowserStack — Customer Engineering Assignment
February 2026