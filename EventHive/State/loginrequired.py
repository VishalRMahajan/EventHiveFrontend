import requests
import reflex as rx

class LoginReqState(rx.State):
    access_token: str = rx.LocalStorage(name="access_token")

    def login_required(self):
        access_token = self.access_token
        print(rx.LocalStorage(name="access_token"))
        print(access_token)
        response = requests.get("http://127.0.0.1:4000/auth/protected", headers = {"Authorization": f"Bearer {access_token}"})
        print(response.status_code)
        if response.status_code == 401:
            return rx.redirect("/")
        else:
            return None