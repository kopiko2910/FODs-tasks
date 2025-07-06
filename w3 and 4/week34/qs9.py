#this program add the detail of 5 books in the dictionary
def get_book_details():
    print("\nEnter Book Details:")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    cost = float(input("Cost: $"))
    return {
        'title': title,
        'author': author,
        'isbn': isbn,
        'cost': cost
    }

def main():
    print("BOOK COLLECTION MANAGER")
    
    books = {}  
    
    for i in range(1, 6):
        print(f"\nBook {i}:")
        book = get_book_details()
        books[book['isbn']] = book
    print("\nYOUR BOOK COLLECTION:")
    for isbn, book in books.items():
        print(f"\nISBN: {isbn}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Cost: ${book['cost']:.2f}")

if __name__ == "__main__":
    main()
