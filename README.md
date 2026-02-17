🌐 El País Opinion Scraper (Selenium + BrowserStack)

Automation script that scrapes the latest opinion articles from El País, translates the headlines to English and runs the workflow across 5 browsers in parallel using BrowserStack.

📸 What this project does

The script performs a complete end-to-end automation flow:

Opens the El País website in Spanish

Navigates to the Opinion section

Collects the first 5 articles

Extracts:

Article title (Spanish)

Full article content

Cover image (if available)

Translates titles → English

Finds repeated words in translated titles

Runs the workflow locally and on BrowserStack cloud browsers

⚡ Demo Flow
El País → Opinion → 5 Articles → Download Images → Translate Titles → Analyze Words


Example output:

Repeated Words in Translated Headlines:
the = 2
to = 2

🛠 Tech Stack

Python

Selenium WebDriver

BrowserStack Automate

deep-translator

Requests

ThreadPoolExecutor (parallel runs)

📂 Project Structure
.
├── src/
│   ├── browserstack_script.py   # Runs tests on 5 browsers in parallel
│   ├── run_test.py              # Local Chrome execution
│   └── scraper.py               # Scraping + translation + analysis
│
├── article_images/              # Downloaded article images
├── requirements.txt
└── README.md

🚀 Setup
1️⃣ Clone repo
git clone "https://github.com/HARSHHVAISHNAV/browserstack-el-pais-scraper.git"
cd browserstack-el-pais-scraper

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add BrowserStack credentials

Create a .env file in the project root:

BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key

▶️ Run Locally

Runs the scraper in Chrome and opens articles in new tabs.

python src/run_test.py

☁️ Run on BrowserStack (Parallel)

Executes the workflow across:

Chrome — Windows 10

Firefox — macOS

Safari — macOS

Chrome — Samsung Galaxy S21

Safari — iPhone 13

python src/browserstack_script.py

📦 Output

After execution you will find:

Downloaded article images → article_images/

Console logs with translations and word analysis

🔐 Environment Variables

This project uses environment variables for credentials.
.env is ignored via .gitignore.