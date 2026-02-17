# 🌐 BrowserStack Scraper  
### Selenium Automation + BrowserStack Parallel Testing

**BrowserStack Customer Engineering Assignment**

A Python-based Selenium automation project that scrapes articles from the *El País Opinion* section, translates article titles to English, performs text analysis, and executes the workflow across multiple browsers in parallel using BrowserStack.

---

## 📋 Project Overview

This project demonstrates an end-to-end automation workflow combining:

- Web scraping using Selenium WebDriver  
- API-based language translation  
- Text processing and word-frequency analysis  
- Cross-browser testing on BrowserStack  
- Parallel execution across desktop and real mobile devices  
- Secure credential management using environment variables  

---

## ✨ Features

### Core Functionality
- Validates website content is in Spanish  
- Navigates to the El País Opinion section  
- Scrapes the first **5 opinion articles**
  - Article title (Spanish)
  - Full article content
  - Cover image (if available)  
- Translates article titles from **Spanish → English**  
- Identifies repeated words in translated titles  
- Automatically handles cookie popups  

---

### ⚙️ Technical Highlights

**Full Article Extraction**  
Articles are opened individually to capture complete content instead of preview snippets.

**Parallel BrowserStack Execution**  
Runs across 5 browsers/devices simultaneously using multithreading.

**Secure Credential Management**  
All credentials are stored in `.env` and never committed to Git.

**Cross-Platform Automation Strategy**  
Different navigation strategies for desktop vs mobile browsers ensure stability.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Chrome installed
- BrowserStack account

Install dependencies:

```bash
pip install -r requirements.txt
🔐 Environment Setup
Create a .env file in the project root:

BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key
The .env file is excluded from Git via .gitignore.

▶️ Running the Tests
Local Execution
Runs the scraper locally in Chrome and opens each article in a new tab.

python src/run_test.py
BrowserStack Execution (Parallel)
Runs the workflow across 5 browsers/devices simultaneously.

python src/browserstack_script.py

```

## 🚀 Project Structure
```bash
browserstack-el-pais/
├── article_images/              
├── src/
│  _{\*
│   ├── browserstack_script.py   
│   ├── run_test.py              
│   └── scraper.py               
├── .env                         
├── .gitignore                   
├── requirements.txt             
└── README.md          
```

## ☁️ BrowserStack Test Environments

| Browser | Platform           | Status   |
| ------- | ------------------ | -------- |
| Chrome  | Windows 10         | ✅ Passed |
| Firefox | macOS Monterey     | ✅ Passed |
| Safari  | macOS Ventura      | ✅ Passed |
| Chrome  | Samsung Galaxy S21 | ✅ Passed |
| Safari  | iPhone 13          | ✅ Passed |


📊 Example Output
Repeated Words in Translated Titles:

the = 2
to = 2


## 🛠 Tech Stack
Selenium WebDriver 4

BrowserStack Automate

Python

deep-translator (Google Translate wrapper)

Requests

ThreadPoolExecutor (parallel execution)

## 🔒 Securtiy Best Practices
No hardcoded credentials

Environment variables for secrets

.env excluded from version control

Safe API usage

## 📝 Assignment checklist
Visit El País website in Spanish

Navigate to Opinion section

Scrape first 5 articles

Download cover images

Translate titles to English

Analyze repeated words

Run locally

Run on BrowserStack in parallel

## 👨‍💻 Candidate

Harsh Vaishnav

BrowserStack — Customer Engineering Assignment

February 2026
