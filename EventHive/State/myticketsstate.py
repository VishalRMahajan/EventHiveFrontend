import requests
import reflex as rx
from shared import Backend
from .viewdetails import viewdetailsState

class MyTicketState(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")
    tickets: list[dict] = []

    def login_required(self):
        access_token = self.access_token
        response = requests.get(Backend+"/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            response1= requests.post(Backend+"/mytickets", headers = {"Authorization": f"Bearer {access_token}"})
            self.tickets = response1.json()
            print(self.tickets)
            return None
    
        
    