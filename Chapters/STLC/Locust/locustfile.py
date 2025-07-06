from locust import HttpUser, task, between

class ECommerceUser(HttpUser):
    host = "http://localhost:8000"

    wait_time = between(1, 3)

    def on_start(self):
        self.client.post("/api/login", json ={"username": "Virat", "password": "Virat@18"})

        @task(2)
        def view_products(self):
            self.client.get("/api/products")

        @task(1)
        def add_to_cart(self):
            self.client.post("/api/cart/add", json = {"product_id": 101, "quantity": 2})

        @task(1)
        def checkout(self):
            self.client.post("/api/checkout")
