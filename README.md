
# EventHive Frontend

Welcome to EventHiveFrontend, the frontend repository for EventHive! This repository contains the frontend code for the [EventHive](https://github.com/VishalRMahajan/EventHive) project, which is built using the Reflex and FastAPI Python frameworks. Reflex is used for creating websites entirely in Python, while FastAPI is used for building the backend API, providing a seamless full-stack development experience.


## Project Structure

```bash
├── README.md
├── assets
├── rxconfig.py
├── shared.py                        (This File Contains the Backend Url)
├── requirements.txt
└── EventHive
    ├── __init__.py
    ├── components
    │   ├── __init__.py
    │   └── sidebar.py                (SideBar Component)
    │
    ├── pages (Pages which return rx.component)
    │   ├── __init__.py
    │   ├── dashboard.py              (Main Dashboard Page)
    │   ├── login.py                  (Login Page)
    │   ├── register.py               (Register Page)
    │   ├── addevent.py               (Add Event Page for Committee)
    │   ├── mytickets.py              (Tickets Page)
    │   ├── profile.py                (Profile Page)
    │   ├── verify_ticket.py          (Ticket Verification Page)
    │   ├── viewdetails.py            (Event Details Page)
    │   └── EventBookData.py          (Event Status Page)
    │
    ├── State (Python scripts facilitating POST and GET requests between frontend and backend. )
    │   ├── __init__.py
    │   ├── dashboardState.py         (rx.state of Dashboard Page)
    │   ├── LoginState.py             (rx.state of Login Page)
    │   ├── RegisterState.py          (rx.state of Register Page)
    │   ├── addeventstate.py          (rx.state of Addevent Page)
    │   ├── myticketsstate.py         (rx.state of Mytickets Page)
    │   ├── profileState.py           (rx.state of Profile Page)
    │   ├── VerifyTicketState.py      (rx.state of verify_ticket Page)
    │   ├── loginrequired.py          (rx.state for jwt and logout fn)
    │   ├── viewdetails.py            (rx.state of viewdetails Page)
    │   └── EventBookedstate.py       (rx.state of EventBookData Page)
    │
    ├── styles.py                     (Py file similar to styles.css)
    ├── templates
    │   ├── __init__.py
    │   └── template.py               (Base Template)
    └── EventHive.py                  (main file which create app)
```
## Disclaimer

**Important:** Before running the EventHive frontend, ensure that the backend server is running. Additionally, update the backend URL in the `shared.py` file to match your backend server's URL. Failure to do so may result in the frontend not functioning correctly.

## Run Locally

Clone the project

```bash
  git clone https://github.com/VishalRMahajan/EventHiveFrontend
```

Go to the project directory

```bash
  cd EventHiveFrontEnd
```

Install all the required Python packages for this project, run the following command:

```bash
   pip install -r requirements.txt
```

Before running for first time, run the following command:

```bash
  reflex init
```
Run the following command to run app in development mode:
```bash
  reflex run
```

Your website will be running Locally at [http://localhost:3000](http://localhost:3000)




## Docs

For any queries, Refer following Docs:
- [Reflex Docs](https://reflex.dev/docs/ui/overview/)
