"""Stores value objects related to the product"""
from pages.utils import random_str, random_num, random_text


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

    def fill_data(self):
        """Fill data by random generated text"""
        self.username = f"{random_str()}{random_num()}"
        self.email = f"{self.username}@mail.com"
        self.password = f"{self.username}PwD"

    def __repr__(self):
        return f"User:(username={self.username}, email={self.email}, password={self.password})"


class Post:

    def __init__(self, title="", body=""):
        self.title = title
        self.body = body

    def fill_data(self):
        """Fill post data by random text"""
        self.title = random_text(10)
        self.body = random_text(120)

    def __repr__(self):
        return f"Post:(title={self.title})"
