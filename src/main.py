from scraper import BookScraper

def main():
    # Initialize scraper with the target website
    scraper = BookScraper('https://example-books-website.com')
    
    # Scrape 5 pages of books
    books = scraper.scrape_books(pages=5)
    
    # Save results to CSV
    filename = scraper.save_to_csv()
    print(f"Scraped {len(books)} books and saved to {filename}")

if __name__ == "__main__":
    main()
