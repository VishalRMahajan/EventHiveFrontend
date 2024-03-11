import requests
from rxconfig import config
from typing import List
import reflex as rx
import re
from shared import Backend

class RegisterFormState(rx.State):
    # These track the user input real time for validation
    user_entered_email: str
    user_entered_password: str

    # These are the submitted data
    usertype: str
    email: str
    password: str
    fname: str
    lname: str
    form_data: dict = {}
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
        self.fname = form_data.get("fname")
        self.lname = form_data.get("lname")
        self.email = form_data.get("email")
        self.password = form_data.get("password")
        print(self.usertype, self.email, self.password)
        print(form_data)
        response= requests.post(Backend+"/auth/register", json=form_data)
        if response.status_code == 201:
            return rx.redirect("/")
        else:
            self.error = True
            self.error_text = response.json()['message']