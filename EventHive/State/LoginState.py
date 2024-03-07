import json
import requests
from rxconfig import config
from typing import List
import reflex as rx
import re
import urllib.parse



class LoginFormState(rx.State):
    # These track the user input real time for validation
    user_entered_email: str
    user_entered_password: str

    # These are the submitted data
    usertype: str
    email: str
    password: str
    form_data: dict = {}
    
    @rx.var
    def invalid_email(self) -> bool:
        return not re.match(
            r"[^@]+@(student\.sfit\.ac\.in|sfit\.ac\.in)$", self.user_entered_email
        )

    @rx.var
    def invalid_password(self) -> bool:
        return len(self.user_entered_password) < 8

    @rx.var
    def input_invalid(self) -> bool:
        return (
            self.invalid_email
            or self.invalid_password
        )

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.usertype = form_data.get("usertype")
        self.email = form_data.get("email")
        self.password = form_data.get("password")
        print(self.usertype, self.email, self.password)
        print((form_data))
        data = {
            "username": self.email,
            "password": self.password,
        }
        params = {
            "usertype": self.usertype,
        }
        response= requests.post("http://127.0.0.1:4000/auth/login",params = params, data=data)
        print(response.json())