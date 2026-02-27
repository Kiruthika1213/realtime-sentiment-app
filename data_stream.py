import time

def stream_data():
    posts = [
        {"post": "I love this product"},
        {"post": "This service is bad"},
        {"post": "Amazing experience"},
        {"post": "Not satisfied with support"},
        {"post": "Very happy today"},
        {"post": "Worst experience ever"},
        {"post": "Customer care is good"}
    ]

    for p in posts:
        yield p
        time.sleep(1)
