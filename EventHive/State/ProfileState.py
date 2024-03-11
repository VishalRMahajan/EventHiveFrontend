import requests
import reflex as rx
from shared import Backend

class ProfileState(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")
    fname : str
    lname : str
    email : str
    role : str
    disabled: bool = True
    
    def enable_edit(self):
        self.disabled = False

    def login_required(self):
        access_token = self.access_token
        response = requests.get(Backend+"/profile/me", headers = {"Authorization": f"Bearer {access_token}"})
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            print(response.content)
            response_json = response.json()
            self.fname = response_json['fname']
            self.lname = response_json['lname']
            self.email = response_json['email']
            self.role = response_json['role']
            return None