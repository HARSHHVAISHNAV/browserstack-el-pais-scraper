🌐 El País Opinion Scraper
Selenium Automation + BrowserStack Parallel Testing

This repository contains a production-style Selenium automation workflow built for the BrowserStack Customer Engineering Assignment.

The project scrapes Spanish news articles from El País, translates the headlines to English, performs text analysis, and executes the entire workflow across desktop and real mobile browsers in parallel using BrowserStack.

🎯 What This Project Demonstrates

This solution was designed to reflect real-world test automation practices:

Writing stable cross-browser Selenium scripts

Handling differences between desktop and mobile web

Running tests in parallel on BrowserStack

Integrating external APIs

Performing lightweight NLP/text analysis

Structuring automation projects professionally

🧩 Assignment Workflow

The automation performs the following end-to-end pipeline:

1️⃣ Open El País (Spanish news website)
2️⃣ Navigate to the Opinion section
3️⃣ Scrape the first 5 articles
4️⃣ Extract:

Article title (Spanish)

Full article content

Cover image (if available)

5️⃣ Translate article titles → English
6️⃣ Analyze translated titles to find repeated words
7️⃣ Execute the entire workflow locally and on BrowserStack across 5 environments in parallel

☁️ Cross-Browser Execution (BrowserStack)

The workflow runs simultaneously on:

Platform	Browser
Windows 10	Chrome
macOS Monterey	Firefox
macOS Ventura	Safari
Samsung Galaxy S21	Chrome (Real Device)
iPhone 13	Safari (Real Device)

This demonstrates handling:

Desktop vs mobile rendering differences

Real device execution

Parallel cloud testing

🏗 Architecture & Design Decisions
Separate Local vs Cloud Strategies

To ensure reliability, two scraping approaches were implemented:

Mode	Strategy	Why
Local execution	Multi-tab scraping	Easier debugging & demonstration
BrowserStack execution	Same-tab navigation	Stable on Safari & real mobile devices

This mirrors how automation is typically written for local debugging vs CI/CD pipelines.

Stability Over UI Fragility

Mobile websites often use different layouts and navigation menus.
For test stability, mobile runs navigate directly to the Opinion URL rather than relying on hamburger menus.

This ensures consistent cross-browser execution.

🛠 Tech Stack
Category	Tools
Language	Python
Automation	Selenium WebDriver 4
Cloud Testing	BrowserStack Automate
Translation	deep-translator (Google Translate wrapper)
Networking	Requests
Parallel Execution	ThreadPoolExecutor
📂 Project Structure
browserstack-el-pais/
│
├── article_images/               # Downloaded article images
├── src/
│   ├── run_test.py               # Local execution (multi-tab scraping)
│   ├── browserstack_script.py   # Parallel BrowserStack execution
│   └── scraper.py               # Scraping + translation + analysis logic
│
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Setup Instructions
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Configure BrowserStack Credentials
macOS / Linux
export BROWSERSTACK_USERNAME="your_username"
export BROWSERSTACK_ACCESS_KEY="your_access_key"

Windows
set BROWSERSTACK_USERNAME=your_username
set BROWSERSTACK_ACCESS_KEY=your_access_key

▶️ Running the Project
Local Execution

Runs scraper in Chrome and opens articles in new tabs.

python src/run_test.py

BrowserStack Execution (Parallel)

Runs the workflow across 5 browsers/devices simultaneously.

python src/browserstack_script.py

📊 Example Output
Repeated Words in Translated Headlines:
the = 2
to = 2

🔐 Security Practices

Credentials stored using environment variables

No secrets committed to the repository

.env excluded via .gitignore

💡 Skills Highlighted

This project showcases skills relevant to a Customer Engineering role:

Cross-browser automation strategy

Debugging real mobile browser behaviour

Writing resilient Selenium tests

API integration

Parallel cloud test execution

Clear technical documentation

👨‍💻 Candidate

Harsh Vaishnav
BrowserStack – Customer Engineering Assignment
2026
