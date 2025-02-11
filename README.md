# Project Gutenberg Top 100 Scraper
![](https://i.postimg.cc/cHry7Pn8/s-now-2.png)

A Python web scraper that collects information about the top 100 most downloaded books from Project Gutenberg.

## Features

- Scrapes book titles and download counts
- Saves results to CSV
- Includes error handling
- Includes unit tests

## Setup and Usage

1. Install requirements:
```pip install -r requirements.txt```

2. Run the scraper:
```python src/main.py```

The script will:
- Scrape the top 100 books
- Save them to 'gutenberg_top_100.csv'
- Display the first 5 books as a preview

## Sample Output
The CSV file will contain:
- Title: Book title
- Downloads: Number of downloads

## Note
Please be respectful of Project Gutenberg's servers and don't run this script too frequently.
