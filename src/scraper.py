import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

class BookScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.books = []

    def scrape_books(self, pages=1):
        """Scrape book information from multiple pages"""
        for page in range(1, pages + 1):
            url = f"{self.base_url}/page/{page}"
            response = requests.get(url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self._parse_books(soup)
                sleep(1)  # Be nice to the server
            
        return self.books

    def _parse_books(self, soup):
        """Extract book information from the page"""
        book_elements = soup.find_all('article', class_='book')
        
        for book in book_elements:
            title = book.find('h2').text.strip()
            author = book.find('span', class_='author').text.strip()
            rating = book.find('span', class_='rating').text.strip()
            
            self.books.append({
                'title': title,
                'author': author,
                'rating': rating
            })

    def save_to_csv(self, filename='books.csv'):
        """Save the scraped books to a CSV file"""
        df = pd.DataFrame(self.books)
        df.to_csv(filename, index=False)
        return filename
