
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



