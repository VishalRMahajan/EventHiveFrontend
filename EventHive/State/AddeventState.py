import requests
import reflex as rx
from shared import Backend

class Addevent(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")
    committee_name: str
    event_name: str
    venue: str
    Date: str
    Time: str
    ticket_price: str
    contact_person: str
    contact_number: int
    error : bool = False
    error_text: str

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
            
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.committee_name = form_data.get("committee_name")
        self.event_name = form_data.get("event_name")
        self.venue = form_data.get("venue")
        self.Date = form_data.get("Date")
        self.Time = form_data.get("Time")
        self.ticket_price = form_data.get("ticket_price")
        self.contact_person = form_data.get("contact_person")
        self.contact_number = form_data.get("contact_number")
        print(self.committee_name, self.event_name, self.venue, self.Date, self.Time, self.ticket_price, self.contact_person, self.contact_number)
        print(form_data)
        response= requests.post(Backend+"/fest/add", json=form_data)
        if response.status_code == 201:
            return rx.redirect("/dashboard")
        else:
            self.error = True
            self.error_text = response.json()['message']
