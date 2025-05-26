from article import Article
from author import Author
from magazine import Magazine

def main() -> None:
    # Create authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    # Create magazines
    tech_mag = Magazine("Tech Weekly", "Technology")
    science_mag = Magazine("Science Now", "Science")

    # Create articles
    Article(author1, tech_mag, "Python Today")
    Article(author1, tech_mag, "Web Dev 2025")
    Article(author2, science_mag, "Future Science")

    # Test the functionality
    print("\n=== Testing Author ===")
    print(f"Author name: {author1.name}")
    print(f"Author's articles: {[article.title for article in author1.articles()]}")
    print(f"Author's magazines: {[mag.name for mag in author1.magazines()]}")

    print("\n=== Testing Magazine ===")
    print(f"Magazine name: {tech_mag.name}")
    print(f"Magazine articles: {tech_mag.article_titles()}")
    print(f"Magazine contributors: {[author.name for author in tech_mag.contributors()]}")

    print("\n=== Testing Article ===")
    article = author1.articles()[0]
    print(f"Article title: {article.title}")
    print(f"Article author: {article.author.name}")
    print(f"Article magazine: {article.magazine.name}")

if __name__ == "__main__":
    main()