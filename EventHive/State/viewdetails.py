import requests
import reflex as rx
from shared import Backend

class viewdetailsState(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")
    email:str

    event : str 
    event_name : str
    committee : str
    contact_person : str
    description : str
    date : str
    time : str
    ticket_price : str
    venue : str
    contact_number : str
    disabled: bool = True
    
    def onclick(self,event):
        self.event = event
        return rx.redirect("/viewdetails")
    
    def login_required(self):
        access_token = self.access_token
        response = requests.get(Backend+"/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        response_json = response.json()
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            self.email = response_json['email']
            print(self.event)
            response1 = requests.get(Backend+"/fest/fetch", headers = {"Authorization": f"Bearer {access_token}"}, params = {"event_name": self.event})
            if response1.status_code == 404:
                return rx.redirect("/dashboard")
            else:
                print(response1.content)
                response_json = response1.json()
                self.event_name = response_json['event_name']
                self.committee = response_json['committee']
                self.contact_person = response_json['contact_person']
                self.description = response_json['description']
                self.date = response_json['date']
                self.time = response_json['time']
                self.ticket_price = response_json['ticket_price']
                self.venue = response_json['venue']
                self.contact_number = response_json['contact_number']     
                return None
    
    def payment(self,ticket_price,event_name,committee):
        print(committee)
        access_token = self.access_token
        response = requests.get(Backend+"/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        response_json = response.json()
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            self.email = response_json['email']
        return rx.redirect(f"{Backend}/pay?amount={ticket_price}&email={self.email}&event_name={event_name}&committee={committee}")
        