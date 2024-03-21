import requests
import reflex as rx
from shared import Backend

class EventBookedState(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")
    booked_tickets = []
    columns = ["First Name","Last Name","Email","Event"]

    def login_required(self):
        access_token = self.access_token
        response = requests.get(Backend+"/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        
        com ={
            "itsa@sfit.ac.in":"ITSA",
            "ieee@sfit.ac.in":"IEEE",
            "csi@sfit.ac.in":"CSI",
            "iste@sfit.ac.in":"ISTE",
            "mesa@sfit.ac.in":"MESA",
            "eesa@sfit.ac.in":"EESA",
            "sfitaa@sfit.ac.in":"SFITAA",
            "student@sfit.ac.in":"Student Council",
        }
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            response_json = response.json()
            print(response_json['Role'])
            if response_json['Role'] == 'student':
                return rx.redirect("/dashboard")
            else:
                committee = com[response_json['email']]
                response1= requests.post(Backend+"/bookedticketdata", params={"committee":committee})
                self.booked_tickets = response1.json()
                print(self.booked_tickets)
                return None
            
    
