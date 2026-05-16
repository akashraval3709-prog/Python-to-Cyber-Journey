## 🌐 Website Utilities

### 🔎 Website Status Checker (`website_status_checker.py`)

Checks whether a website is online and retrieves basic server information.

#### ✨ Features:

* Sends HTTP requests using `requests`
* Detects website availability
* Displays HTTP status codes
* Extracts server information from headers

---

### 📏 Content Size Checker (`content_size_checker.py`)

Analyzes webpage content size.

#### ✨ Features:

* Calculates webpage size in KB
* Uses HTTP response data
* Demonstrates practical web response handling

---

### 🌐 Website Health Scanner (`website_health_scanner.py`)

Scans websites and generates detailed health reports.

#### ✨ Features:

* Validates URLs automatically
* Checks website availability and status codes
* Measures response time
* Extracts server and content-type information
* Generates scan reports in a text file
* Handles connection and timeout errors gracefully

---

### 🕸️ H1 Tag Scraper (`h1_tag_scraper.py`)

Extracts the first H1 tag from a webpage using BeautifulSoup.

#### ✨ Features:

* Fetches webpage HTML using requests
* Parses HTML using BeautifulSoup
* Extracts H1 tag content
* Handles invalid URLs and connection errors gracefully

---

## 🔐 GitHub Login Automation (`selenium_github_login.py`)

A Selenium mini project that automates the GitHub login process and captures authentication error messages.

#### ✨ Features

* 🌐 Opens GitHub login page automatically
* 👤 Enters username/email and password
* 🖱️ Clicks the Sign In button
* ⚠️ Captures and prints login error messages
* 🔍 Uses Selenium locators (`NAME`, `XPATH`)
* ⏳ Demonstrates browser automation with delays

#### 🛠️ Technologies Used

* 🐍 Python
* 🌍 Selenium
* 🚗 WebDriver Manager

#### 📚 Learning Concepts

* Selenium Web Automation
* Form Handling
* Element Locators
* Browser Interaction
* Error Message Extraction
* Automation Testing Basics
  
---

# ☑️ Checkbox & Dropdown Automation

A Selenium mini project that automates checkbox selection and dropdown handling.

## ✨ Features

- Automatically selects and deselects checkboxes
- Checks checkbox state using `is_selected()`
- Automates dropdown selection
- Uses `select_by_index()`
- Uses `select_by_visible_text()`
- Demonstrates Selenium form interaction

## 🛠️ Technologies Used

- Python
- Selenium
- WebDriver Manager

## 📚 Learning Concepts

- Checkbox Automation
- Dropdown Handling
- Selenium Select Class
- Conditional Automation Logic
- Browser Interaction

----
# 🔗 Google Links Extractor

A Selenium mini project that extracts and analyzes links from Google homepage.

## ✨ Features

- Opens Google homepage automatically
- Extracts all anchor (`a`) tags
- Counts total links on the page
- Displays link text and URLs
- Demonstrates Selenium element extraction
- Searches elements using class names

## 🛠️ Technologies Used

- Python
- Selenium
- WebDriver Manager

## 📚 Learning Concepts

- Selenium Web Automation
- Element Locators
- TAG_NAME Locator
- CLASS_NAME Locator
- Extracting Attributes
- Looping Through Web Elements  

---

# 🔍 Google Search Automation

A Selenium mini project that automates Google search using keyboard actions.

## ✨ Features

- Opens Google automatically
- Searches custom keywords
- Uses ENTER and ESCAPE keyboard keys
- Automates browser interaction
- Demonstrates Selenium search automation

## 🛠️ Technologies Used

- Python
- Selenium
- WebDriver Manager

## 📚 Learning Concepts

- Selenium Web Automation
- Keyboard Actions
- Element Locators
- Browser Interaction
- Search Box Automation

---

# ⏳ Dynamic Loading Automation

A Selenium mini project that handles dynamically loaded content using Explicit Waits.

## ✨ Features

- Opens dynamic loading webpage
- Clicks Start button automatically
- Waits for hidden content to appear
- Extracts dynamically loaded text
- Handles TimeoutException errors

## 🛠️ Technologies Used

- Python
- Selenium
- WebDriver Manager

## 📚 Learning Concepts

- Explicit Wait
- WebDriverWait
- Expected Conditions
- Dynamic Element Handling
- Selenium Automation
- Exception Handling

---

☕ JavaScript Alerts Automation

A Selenium mini project that automates handling different types of JavaScript alerts.

✨ Features
Handles JavaScript Alert popups
Accepts alerts using `accept()`
Dismisses confirmation alerts using `dismiss()`
Sends text into JS Prompt alerts
Uses Selenium `switch_to.alert`
Demonstrates browser interaction automation

🛠️ Technologies Used
Python
Selenium
WebDriver Manager

📚 Learning Concepts
JavaScript Alert Handling
Selenium Alert Switching
Alert Accept & Dismiss
Prompt Input Automation
Browser Automation Basics
