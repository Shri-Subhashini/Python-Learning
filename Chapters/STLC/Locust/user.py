from locust import User, task, constant, HttpUser

class MyTest(HttpUser):
    # wait_time = constant(1)

    # @task
    # def say_hello(self):
    #     print("Hello world")

    # @task
    # def say_goodbye(Self):
    #     print("Goodbye world")

    @task
    def get_users(self):
        res = self.client.get("/")
        print("Get method status is: ",res.status_code)

    @task
    def post_status(self):
        res = self.client.post("/?status=success")
        print("Post method status is: ", res.status_code)

