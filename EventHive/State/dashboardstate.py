import requests
import reflex as rx
from shared import Backend

class DashboardState(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")
    events: list[dict] = []

    def login_required(self):
        access_token = self.access_token
        response = requests.get(Backend+"/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            response1= requests.get(Backend+"/fest/all", headers = {"Authorization": f"Bearer {access_token}"})
            self.events = response1.json()
            print(self.events)
            return None
        
    