import json
from datetime import datetime, timedelta

class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
    
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'quantity': self.quantity
        }
    
    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Available: {self.quantity}"

class Transaction:
    def __init__(self, book_isbn, user_id, transaction_type):
        self.book_isbn = book_isbn
        self.user_id = user_id
        self.type = transaction_type  # 'issue' or 'return'
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S") if transaction_type == 'issue' else None
    
    def to_dict(self):
        return {
            'book_isbn': self.book_isbn,
            'user_id': self.user_id,
            'type': self.type,
            'date': self.date,
            'due_date': self.due_date
        }

class Library:
    def __init__(self):
        self.books = []
        self.transactions = []
        self.load_data()
    
    def load_data(self):
        try:
            with open('books.json', 'r') as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]
        except FileNotFoundError:
            print("No existing book data found. Starting with empty library.")
        except Exception as e:
            print(f"Error loading book data: {e}")
        
        try:
            with open('transactions.json', 'r') as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            print("No existing transaction data found.")
        except Exception as e:
            print(f"Error loading transaction data: {e}")
    
    def save_data(self):
        try:
            with open('books.json', 'w') as file:
                json.dump([book.to_dict() for book in self.books], file, indent=4)
            
            with open('transactions.json', 'w') as file:
                json.dump(self.transactions, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_book(self, isbn, title, author, quantity):
        for book in self.books:
            if book.isbn == isbn:
                book.quantity += quantity
                print(f"Updated quantity for existing book. New quantity: {book.quantity}")
                self.save_data()
                return
        
        new_book = Book(isbn, title, author, quantity)
        self.books.append(new_book)
        self.save_data()
        print(f"Added new book: {title}")
    
    def search_book(self, search_term):
        results = []
        for book in self.books:
            if (search_term.lower() in book.title.lower() or 
                search_term.lower() in book.author.lower() or 
                search_term == book.isbn):
                results.append(book)
        return results
    
    def issue_book(self, isbn, user_id):
        for book in self.books:
            if book.isbn == isbn:
                if book.quantity > 0:
                    book.quantity -= 1
                    transaction = Transaction(isbn, user_id, 'issue')
                    self.transactions.append(transaction.to_dict())
                    self.save_data()
                    print(f"Book issued successfully. Due date: {transaction.due_date}")
                    return
                else:
                    print("Sorry, this book is currently not available.")
                    return
        print("Book not found in the library.")
    
    def return_book(self, isbn, user_id):
        for book in self.books:
            if book.isbn == isbn:
                # Check if this user has issued this book
                for transaction in reversed(self.transactions):
                    if (transaction['book_isbn'] == isbn and 
                        transaction['user_id'] == user_id and 
                        transaction['type'] == 'issue'):
                        book.quantity += 1
                        return_transaction = Transaction(isbn, user_id, 'return')
                        self.transactions.append(return_transaction.to_dict())
                        self.save_data()
                        print("Book returned successfully.")
                        return
                print("No active issue record found for this user and book.")
                return
        print("Book not found in the library.")
    
    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        
        print("\nLibrary Books:")
        for book in self.books:
            print(book)
    
    def display_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
            return
        
        print("\nTransaction History:")
        for i, transaction in enumerate(self.transactions, 1):
            print(f"{i}. Book ISBN: {transaction['book_isbn']}, User: {transaction['user_id']}, "
                  f"Type: {transaction['type'].title()}, Date: {transaction['date']}")
            if transaction['type'] == 'issue':
                print(f"   Due Date: {transaction['due_date']}")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Display Transaction History")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            try:
                isbn = input("Enter ISBN: ")
                title = input("Enter title: ")
                author = input("Enter author: ")
                quantity = int(input("Enter quantity: "))
                library.add_book(isbn, title, author, quantity)
            except ValueError:
                print("Invalid input. Please enter correct values.")
        
        elif choice == '2':
            search_term = input("Enter title, author or ISBN to search: ")
            results = library.search_book(search_term)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(book)
            else:
                print("No books found matching your search.")
        
        elif choice == '3':
            isbn = input("Enter ISBN of book to issue: ")
            user_id = input("Enter your user ID: ")
            library.issue_book(isbn, user_id)
        
        elif choice == '4':
            isbn = input("Enter ISBN of book to return: ")
            user_id = input("Enter your user ID: ")
            library.return_book(isbn, user_id)
        
        elif choice == '5':
            library.display_books()
        
        elif choice == '6':
            library.display_transactions()
        
        elif choice == '7':
            print("Thank you for using the Library Management System!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-7.")

if __name__ == "__main__":
    main()