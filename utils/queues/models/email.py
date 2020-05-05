import typing


class Email:
    def __init__(self, email: str, subject: str, message: str):
        self.email = email
        self.subject = subject
        self.message = message
