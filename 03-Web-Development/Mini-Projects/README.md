# 🌐 Web Development Mini Projects

This folder contains mini web development and web scraping projects built using Python.

These projects focus on:

* HTTP requests
* HTML parsing
* Website monitoring
* Data extraction
* JSON handling
* Automation using web technologies

---

# 📁 Projects Included

## 📰 Smart News Scraper

A web scraping project that extracts headlines and links from websites using BeautifulSoup.

### 🔹 Version 1 (`news_scraper_v1.py`)

Basic implementation of the news scraper.

### ✨ Features:

* Extracts headlines from websites
* Supports custom HTML tag searching
* Converts relative links into absolute URLs
* Removes duplicate entries
* Saves scraped data into JSON format
* Displays response time

### ⚠️ Limitations:

* Basic filtering logic
* Console-only output
* No CSV export support
* Limited validation system

---
## 🔗 Website Link Analyzer (`website_link_analyzer.py`)

An advanced web scraping tool that analyzes website links and generates reports.

### ✨ Features:

* Extracts links and image sources from websites
* Supports custom HTML tag analysis (`a` / `img`)
* Detects internal and external links
* Removes duplicate entries
* Exports data into JSON format
* Generates detailed TXT reports
* Measures response time and validates URLs

---
## 📰 Smart News Scraper v2 (`news_scraper_v2.py`)

An improved version of the News Scraper project built using Python, `requests`, and `BeautifulSoup`.

This version provides better reporting, duplicate filtering, JSON export, and cleaner data handling.

### ✨ Features:

- Extracts headlines and links from websites
- Supports custom HTML tag scraping
- Converts relative URLs into absolute links
- Removes duplicate news entries
- Detects invalid links
- Exports scraped data into JSON format
- Generates detailed TXT report summaries
- Measures website response time
- Handles invalid URLs and request errors

---

### 🛠 Technologies Used

- Python
- requests
- BeautifulSoup (bs4)
- JSON
- urllib.parse
- time module

---

### 📂 Output Files

#### 📄 `news_data2.json`
Stores structured scraped news data in JSON format.

#### 📄 `news.txt`
Generates a detailed scraping report including:
- Website status
- Response time
- Total tags found
- Valid news collected
- Duplicate entries removed
- Invalid links detected

---

### 🎯 Learning Outcomes

- Advanced HTML parsing
- URL normalization using `urljoin`
- Duplicate filtering using sets
- JSON data handling
- File report generation
- Error handling in web scraping
- Building structured mini-projects with Python

---
# 🌐 Website Link Analyzer

A Python mini project that analyzes website links and generates detailed reports using web scraping.

---

## ✨ Features

- 🔍 Analyze website links and images
- 🌍 Detect internal and external links
- 🧹 Remove duplicate and invalid links
- 📦 Export collected data into JSON format
- 📄 Generate detailed TXT reports
- ⚡ Measure website response time
- 🛡️ Handle request and connection errors
- 🏷️ Support custom tag analysis (`a` / `img`)

---

## 🛠️ Technologies Used

- 🐍 Python
- 📡 Requests
- 🍲 BeautifulSoup4
- 📁 JSON
- 🔗 urllib.parse
- ⏱️ Time Module

---

## 📂 Output Files

- 📄 `data.json` → Stores extracted link data
- 📝 `report.txt` → Stores analysis summary report

---

## 📚 Learning Concepts

- 🌐 Web Scraping
- 📨 HTTP Requests
- 🧩 HTML Parsing
- 📂 File Handling
- 📦 JSON Handling
- ❌ Error Handling
- ✅ Data Validation
