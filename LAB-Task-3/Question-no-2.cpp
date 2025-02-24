#include <iostream>
#include <string>

using namespace std;

struct Book {
    string title;
    string author;
    string isbn;
};

int main() {
    Book library[100]; // Fixed array size for simplicity
    int bookCount = 0;
    
    while (true) {
        cout << "\nLibrary Management System\n";
        cout << "1. Add Book\n2. Search Book\n3. Exit\n";
        cout << "Enter your choice: ";
        
        int choice;
        cin >> choice;
        cin.ignore(); // Ignore newline after input

        if (choice == 1) {
            if (bookCount < 100) {
                cout << "Enter book title: ";
                getline(cin, library[bookCount].title);
                cout << "Enter author name: ";
                getline(cin, library[bookCount].author);
                cout << "Enter ISBN: ";
                getline(cin, library[bookCount].isbn);
                bookCount++;
                cout << "Book added successfully!\n";
            } else {
                cout << "Library is full!\n";
            }
        } else if (choice == 2) {
            string query;
            cout << "Enter title or author to search: ";
            getline(cin, query);
            bool found = false;
            
            for (int i = 0; i < bookCount; i++) {
                if (library[i].title == query || library[i].author == query) {
                    cout << "Found Book: \n";
                    cout << "Title: " << library[i].title << "\n";
                    cout << "Author: " << library[i].author << "\n";
                    cout << "ISBN: " << library[i].isbn << "\n";
                    found = true;
                }
            }
            if (!found) {
                cout << "No matching books found.\n";
            }
        } else if (choice == 3) {
            cout << "Exiting application.\n";
            break;
        } else {
            cout << "Invalid choice, try again.\n";
        }
    }
    return 0;
}
