books = []
while True:
    cmd = input("Enter command (add, search, exit): ").lower()
    if cmd == "exit": print("Goodbye!"); break
    elif cmd == "add":
        title, author, isbn = input("Title: "), input("Author: "), input("ISBN: ")
        books.append({"title": title, "author": author, "isbn": isbn})
        print("Book added!")
    elif cmd == "search":
        query = input("Enter title or author: ").lower()
        results = [b for b in books if query in b["title"].lower() or query in b["author"].lower()]
        print("Results:" if results else "No books found.", *[f"{b['title']} by {b['author']}" for b in results])
    else: print("Invalid command.")