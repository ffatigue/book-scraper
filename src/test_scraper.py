import unittest
from src.scraper import GutenbergScraper
from bs4 import BeautifulSoup

class TestGutenbergScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = GutenbergScraper()

    def test_parse_books(self):
        # Sample HTML content for testing
        html_content = '''
        <ol>
            <li>Test Book (1,234 downloads)</li>
            <li>Another Book (5,678 downloads)</li>
        </ol>
        '''
        soup = BeautifulSoup(html_content, 'html.parser')
        self.scraper._parse_books(soup.find('ol'))
        
        self.assertEqual(len(self.scraper.books), 2)
        self.assertEqual(self.scraper.books[0]['title'], 'Test Book')
        self.assertEqual(self.scraper.books[0]['downloads'], '1,234')

if __name__ == '__main__':
    unittest.main()
