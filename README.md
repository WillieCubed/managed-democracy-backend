# Managed Democracy Backend

This is a service that provides backend functionality for the Managed Democracy
project. (The web client can be found [here](https://github.com/WillieCubed/managed-democracy).)
It is written in Python and uses the FastAPI framework.

## Installation

Set up a virtual environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Now run the server:

```bash
fastapi dev app/main.py
```

To run in production:

```bash
fastapi run
```

To see the interactive API docs generated by Swagger UI, navigate to `http://localhost:8000/docs`.

## Deployment

## About

The service supports the following endpoints:

- GET `/api/v1/health`: Check whether the service is running.
- POST `/api/v1/legislation`: Create a new piece of legislation.
- POST `/api/v1/public-perception`: Generates a public perception report on a piece of proposed legislation.
- GET `/api/v1/precedents`: Given a query.
- GET `/api/v1/reports/{report_id}`: Get a final report on a piece of proposed legislation.