import requests
import reflex as rx
from shared import Backend

class VerifyTicket(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")
    email:str

    event_name: str = ""
    email1: str = ""
    committee: str = ""
    ticket_details: str = ""
    valid : bool = False
    
    def verify_ticket(self):
        if isinstance(self.ticket_details, str):
            event_name, email,committee = self.ticket_details.split('+')
            self.event_name = event_name
            self.email1 = email
            self.committee = committee
        elif isinstance(self.ticket_details, list):
            for ticket in self.ticket_details:
                if isinstance(ticket, str):
                    event_name, email,committee = ticket.split('+')
                    self.event_name = event_name
                    self.email1 = email
                    self.committee = committee  
        else:
            raise TypeError("ticket_details must be a string or a list of strings")
        response = requests.post(Backend + "/verify_ticket",params={"email":self.email1,"event_name":self.event_name,"committee":self.committee})
        if response.status_code == 200:
            self.valid = True
        else:
            self.valid = False
        return None

    