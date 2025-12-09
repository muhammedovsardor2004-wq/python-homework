
# task 1

import json 

students = [
           {'name':'sardor','age':21,'cty':'navoi'},
           {'name':'aziz','age':20,'cty':'toshkent'}
]

with open('students.json','w') as file:
    json.dump(students,file,indent=4)
    

with open('students.json','r') as file:
    new_json = json.load(file)

for student in new_json:
    print('Name:',student['name'])
    print("Age:", student["age"])
    print("Cty:", student["cty"])


# task 2
  #(berilgan sytni api bulmagani uchun boshqa saytdan foydalanildi)

import requests

city = 'Tashkent'

url = f'https://wttr.in/{city}?format=j1'

response = requests.get(url)
data = response.json()

temperature = data["current_condition"][0]["temp_C"]
humidity = data["current_condition"][0]["humidity"]
description = data["current_condition"][0]["weatherDesc"][0]["value"]

print("City:", city)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Weather:", description)


# task 3 



import json
import os
import tempfile

BOOKS_FILE = "books.json"


def load_books(path=BOOKS_FILE):
    """Load books from JSON file. If file doesn't exist, return empty list."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: JSON file is malformed. Starting with an empty list.")
        return []


def save_books(books, path=BOOKS_FILE):
    """Save books to JSON file safely using a temp file then rename."""
    dirpath = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp_path = tempfile.mkstemp(prefix="books_", dir=dirpath, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as tmpf:
            json.dump(books, tmpf, indent=4, ensure_ascii=False)
        os.replace(tmp_path, path)
    except Exception as e:
        print("Error saving file:", e)
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


def next_id(books):
    """Return the next id (1 + max existing id) or 1 if none."""
    if not books:
        return 1
    try:
        return max(b.get("id", 0) for b in books) + 1
    except Exception:
        return 1


def list_books(books):
    if not books:
        print("No books found.")
        return
    print("\nCurrent books:")
    for b in books:
        print(f"ID: {b.get('id')}")
        print(f"  Title : {b.get('title')}")
        print(f"  Author: {b.get('author')}")
        print(f"  Year  : {b.get('year')}")
        print(f"  ISBN  : {b.get('isbn')}")
        print("-"*30)


def add_book(books):
    print("\nAdd a new book")
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty. Aborting.")
        return
    author = input("Author: ").strip()
    year_input = input("Year (optional): ").strip()
    year = int(year_input) if year_input.isdigit() else None
    isbn = input("ISBN (optional): ").strip() or None

    book = {
        "id": next_id(books),
        "title": title,
        "author": author or None,
        "year": year,
        "isbn": isbn,
    }
    books.append(book)
    save_books(books)
    print(f"Book added with ID {book['id']}")


def find_book(books, book_id):
    for b in books:
        if b.get("id") == book_id:
            return b
    return None


def update_book(books):
    print("\nUpdate a book")
    id_input = input("Enter book ID to update: ").strip()
    if not id_input.isdigit():
        print("Invalid ID.")
        return
    book_id = int(id_input)
    book = find_book(books, book_id)
    if not book:
        print("Book not found.")
        return
    print("Press Enter to keep current value.")
    title = input(f"Title [{book.get('title')}]: ").strip()
    author = input(f"Author [{book.get('author')}]: ").strip()
    year_input = input(f"Year [{book.get('year')}]: ").strip()
    isbn = input(f"ISBN [{book.get('isbn')}]: ").strip()

    if title:
        book['title'] = title
    if author:
        book['author'] = author
    if year_input.isdigit():
        book['year'] = int(year_input)
    if isbn:
        book['isbn'] = isbn

    save_books(books)
    print("Book updated.")


def delete_book(books):
    print("\nDelete a book")
    id_input = input("Enter book ID to delete: ").strip()
    if not id_input.isdigit():
        print("Invalid ID.")
        return
    book_id = int(id_input)
    book = find_book(books, book_id)
    if not book:
        print("Book not found.")
        return
    confirm = input(f"Are you sure you want to delete '{book.get('title')}'? (y/N): ").strip().lower()
    if confirm == 'y':
        books.remove(book)
        save_books(books)
        print("Book deleted.")
    else:
        print("Aborted.")


def main_menu():
    books = load_books()
    while True:
        print("\n=== Books Manager ===")
        print("1. List books")
        print("2. Add book")
        print("3. Update book")
        print("4. Delete book")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            list_books(books)
        elif choice == '2':
            add_book(books)
        elif choice == '3':
            update_book(books)
        elif choice == '4':
            delete_book(books)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-5.")


if __name__ == '__main__':
    main_menu()



# task 4 (berilgan sayt bilan ayrim moommolar tufayli avval jadval yaratilib sun shu asosida bu saytdan qidirildi malumorlar)
# movie_recommender.py
import os
import random
import requests

# 1) Mahalliy janr->film ro'yxati (bu ro'yxatni kengaytiring)
movies_by_genre = {
    "action": [
        "Mad Max: Fury Road",
        "Die Hard",
        "John Wick"
    ],
    "comedy": [
        "Groundhog Day",
        "The Grand Budapest Hotel",
        "Superbad"
    ],
    "drama": [
        "The Shawshank Redemption",
        "Forrest Gump",
        "The Godfather"
    ],
    "sci-fi": [
        "Inception",
        "The Matrix",
        "Blade Runner 2049"
    ],
    "horror": [
        "Get Out",
        "The Conjuring",
        "Hereditary"
    ]
}

def get_api_key():
    # 1) Avvalo muhit o'zgaruvchisidan o'qib ko'ramiz
    key = os.getenv("OMDB_API_KEY")
    if key:
        return key.strip()
    # 2) Yo'q bo'lsa, foydalanuvchidan so'raymiz
    key = input("Enter your OMDb API key (or press Enter to abort): ").strip()
    if not key:
        print("API key kerak. Dastur to'xtadi.")
        return None
    return key

def fetch_movie_details(title, api_key):
    """OMDb ga so'rov yuboradi va JSON qaytaradi (title bo'yicha)."""
    url = "http://www.omdbapi.com/"
    params = {
        "t": title,
        "apikey": api_key,
        "plot": "short",   # yoki "full"
        "r": "json"
    }
    resp = requests.get(url, params=params, timeout=10)
    # xato holatlarni tekshirish
    if resp.status_code != 200:
        print("HTTP xato:", resp.status_code)
        return None
    data = resp.json()
    if data.get("Response", "False") == "False":
        # OMDb xabar: Movie not found! yoki Invalid API key!
        print("OMDb xabar:", data.get("Error"))
        return None
    return data

def recommend_by_genre():
    api_key = get_api_key()
    if not api_key:
        return

    genre = input("Qaysi janrni xohlaysiz? (masalan action, comedy, drama, sci-fi, horror): ").strip().lower()
    if genre not in movies_by_genre:
        print("Kechirasiz — bizda bunday janr yo'q. Mavjud janrlar:", ", ".join(movies_by_genre.keys()))
        return

    # 1) Tasodifiy film tanlash
    title = random.choice(movies_by_genre[genre])
    print(f"\nTanlangan film (ma'lumot olinmoqda): {title}")

    # 2) OMDb dan batafsil ma'lumotni olish
    details = fetch_movie_details(title, api_key)
    if not details:
        print("Film haqida ma'lumot olinmadi.")
        return

    # 3) Natijani chiroyli chiqarish
    print("\n--- Tavsiya qilingan film ---")
    print("Title:", details.get("Title"))
    print("Year :", details.get("Year"))
    print("Rated:", details.get("Rated"))
    print("Runtime:", details.get("Runtime"))
    print("Genre:", details.get("Genre"))
    print("Director:", details.get("Director"))
    print("Actors:", details.get("Actors"))
    print("IMDB Rating:", details.get("imdbRating"))
    print("Plot:", details.get("Plot"))
    print("Poster URL:", details.get("Poster"))

if __name__ == "__main__":
    recommend_by_genre()
