import unittest
from src.scraper import BookScraper
from bs4 import BeautifulSoup

class TestBookScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = BookScraper('https://example-books-website.com')

    def test_parse_books(self):
        # Sample HTML content for testing
        html_content = '''
        <article class="book">
            <h2>Test Book</h2>
            <span class="author">Test Author</span>
            <span class="rating">4.5</span>
        </article>
        '''
        soup = BeautifulSoup(html_content, 'html.parser')
        self.scraper._parse_books(soup)
        
        self.assertEqual(len(self.scraper.books), 1)
        self.assertEqual(self.scraper.books[0]['title'], 'Test Book')
        self.assertEqual(self.scraper.books[0]['author'], 'Test Author')
        self.assertEqual(self.scraper.books[0]['rating'], '4.5')

if __name__ == '__main__':
    unittest.main()
