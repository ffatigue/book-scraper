from scraper import GutenbergScraper

def main():
    # Initialize scraper
    scraper = GutenbergScraper()
    
    # Scrape books
    print("Starting to scrape Project Gutenberg's top 100 books...")
    books = scraper.scrape_books()
    
    if books:
        # Save results to CSV
        filename = scraper.save_to_csv()
        print(f"Successfully scraped {len(books)} books and saved to {filename}")
        
        # Print first 5 books as example
        print("\nFirst 5 books scraped:")
        for i, book in enumerate(books[:5], 1):
            print(f"{i}. {book['title']} ({book['downloads']} downloads)")
    else:
        print("No books were scraped. Please check your internet connection or try again later.")

if __name__ == "__main__":
    main()
