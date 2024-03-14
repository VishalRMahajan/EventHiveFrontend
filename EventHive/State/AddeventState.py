import requests
import reflex as rx
from shared import Backend

class Addevent(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")
    
    def login_required(self):
        access_token = self.access_token
        response = requests.get(Backend+"/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            response_json = response.json()
            print(response_json['Role'])
            if response_json['Role'] == 'student':
                return rx.redirect("/dashboard")
            else:
                return None