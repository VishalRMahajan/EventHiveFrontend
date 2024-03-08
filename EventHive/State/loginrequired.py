import requests
import reflex as rx

class LoginReqState(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")

    def login_required(self):
        access_token = self.access_token
        response = requests.get("http://127.0.0.1:4000/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            return None
        
    def already_logged_in(self):
        access_token = self.access_token
        response = requests.get("http://127.0.0.1:4000/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        if response.status_code == 200:
            return rx.redirect("/dashboard")
        else:
            return None
        
    def logout(self):
        return rx.remove_local_storage(
            "access_token"
        )