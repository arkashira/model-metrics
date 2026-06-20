import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    email: str
    password: str
    verified: bool = False

class AuthManager:
    def __init__(self):
        self.users = {}

    def create_account(self, email: str, password: str) -> bool:
        if email in self.users:
            return False
        if not self._check_password_complexity(password):
            return False
        self.users[email] = User(email, password)
        return True

    def _check_password_complexity(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        return True

    def verify_email(self, email: str) -> bool:
        if email not in self.users:
            return False
        self.users[email].verified = True
        return True

    def login(self, email: str, password: str) -> bool:
        if email not in self.users:
            return False
        if not self.users[email].verified:
            return False
        if self.users[email].password != password:
            return False
        return True
