import json
import requests
from rxconfig import config
from typing import List
import reflex as rx
import re
import urllib.parse
from shared import Backend
from EventHive.pages import otp


class LoginFormState(rx.State):
    # These track the user input real time for validation
    user_entered_email: str
    user_entered_password: str

    # These are the submitted data
    usertype: str
    email: str
    password: str
    form_data: dict = {}
    my_local_storage: str = rx.LocalStorage(name="access_token")
    error : bool = False
    error_text: str 
    
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
        data = {
            "username": self.email,
            "password": self.password,
        }
        response= requests.post(Backend+"/auth/login",data=data)
        print(response.json())
        response_json = response.json()
        if response.status_code == 200:
            my_local_storage =response_json['access_token']
            self.my_local_storage = my_local_storage
            return rx.redirect("/dashboard")
        else:
            self.error = True
            self.error_text = response_json['detail']
