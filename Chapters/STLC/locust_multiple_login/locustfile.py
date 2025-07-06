import csv
from locust import HttpUser, task, between
import random

def load_users():
    with open("users.csv") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

users = load_users()


class LoginUser(HttpUser):
    wait_time = between(1, 3)  # Simulate user think time between 1-3s

    token = "e51227d24fa0fcf758ea242a755743f0b10f88933adaec0398c5a1e851fa2ec7"

    def on_start(self):
        # Initialize book IDs list empty
        self.book_ids = []

    # @task
    # def login(self):
    #     # Pick a random user from the list
    #     user = random.choice(users)
    #     response = self.client.get("/books")

    #     if response.status_code == 200:
    #         print("✅ Successfully viewed books")
    #         books = response.json()
    #         print(books)
    #         # for book in books[:3]:  # print first 3 book names
    #         #     print(f"- {book['name']} ({book['type']})")
    #     else:
    #         print(f"❌ Failed to view books, status code: {response.status_code}")

    @task(2)  # weight 2 for listing books
    def view_books(self):
        response = self.client.get("/books")
        if response.status_code == 200:
            books = response.json()
            print(f"✅ Viewed {len(books)} books")
            self.book_ids = [book['id'] for book in books]  # store IDs for detail fetch
        else:
            print(f"❌ Failed to view books: {response.status_code}")

    @task(1)  # weight 1 for getting book details
    def get_book_details(self):
        if hasattr(self, 'book_ids') and self.book_ids:
            book_id = random.choice(self.book_ids)
            response = self.client.get(f"/books/{book_id}")
            if response.status_code == 200:
                book = response.json()
                print(f"📖 Details for book: {book['name']} (ID: {book_id})")
            else:
                print(f"❌ Failed to get details for book ID {book_id}: {response.status_code}")
        else:
            print("⚠️ No book IDs available yet")

    @task(1)
    def submit_order(self):
        if not self.book_ids:
            print("⚠️ No book IDs available to submit order")
            return

        book_id = random.choice(self.book_ids)
        customer_name = f"LocustUser{random.randint(1, 1000)}"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "bookId": book_id,
            "customerName": customer_name
        }

        response = self.client.post("/orders", json=payload, headers=headers)

        if response.status_code == 201:
            print(f"✅ Order submitted for book ID {book_id} by {customer_name}")
        else:
            print(f"❌ Failed to submit order: {response.status_code} - {response.text}")