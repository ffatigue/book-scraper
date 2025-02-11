import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

class GutenbergScraper:
    def __init__(self):
        self.base_url = "https://www.gutenberg.org/browse/scores/top"
        self.books = []

    def scrape_books(self):
        """Scrape top 100 books from Project Gutenberg"""
        try:
            response = requests.get(self.base_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Find the ordered list containing top 100 books
                book_list = soup.find('ol')
                if book_list:
                    self._parse_books(book_list)
                    return self.books
            return []
        except Exception as e:
            print(f"Error scraping books: {e}")
            return []

    def _parse_books(self, book_list):
        """Extract book information from the page"""
        for book_item in book_list.find_all('li')[:100]:  # Get top 100 books
            try:
                # Extract book information
                text = book_item.text.strip()
                if '(' in text and ')' in text:
                    title = text.split('(')[0].strip()
                    downloads = text.split('(')[1].split()[0].strip()
                    
                    self.books.append({
                        'title': title,
                        'downloads': downloads
                    })
            except Exception as e:
                print(f"Error parsing book: {e}")
                continue

    def save_to_csv(self, filename='gutenberg_top_100.csv'):
        """Save the scraped books to a CSV file"""
        if self.books:
            df = pd.DataFrame(self.books)
            df.to_csv(filename, index=False)
            return filename
        return None
