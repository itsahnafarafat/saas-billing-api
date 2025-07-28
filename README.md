# SaaS Billing API

A **production-ready SaaS Billing API** built with **Django REST Framework** for managing subscription-based services.  
It provides endpoints for **plans, subscriptions, invoices, and payments**, making it easy to integrate with SaaS platforms.

---

## Features

* **Plan Management** – Create and list subscription plans with duration and pricing.
* **User Subscriptions** – Manage active subscriptions linked to users.
* **Invoices & Payments** – Track billing history and payment statuses.
* **Secure REST Endpoints** – Authentication & permission-based access.
* **Scalable Deployment** – Dockerized and deployed on **Railway** for production use.
* **Automated Unit Testing** – Ensures reliability and correctness of models and API endpoints.

---

## Tech Stack

* **Backend:** Python, Django, Django REST Framework  
* **Database:** SQLite (development), PostgreSQL (production-ready)  
* **Deployment:** Docker, Railway  
* **Authentication:** Django's built-in authentication  

---

## API Endpoints

Base URL:

```

https://saas-billing-api-production.up.railway.app/api/billing/

````

Available endpoints:

* `plans/` – List all subscription plans  
* `subscriptions/` – View and create subscriptions  
* `invoices/` – View billing invoices  
* `payments/` – View payment history  

Example request:

```bash
GET /api/billing/plans/
````

Example response:

```json
[
    {
        "id": 1,
        "name": "Basic Plan",
        "price": "10.00",
        "description": "Basic features only",
        "duration_months": 30
    }
]
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/itsahnafarafat/saas-billing-api.git
cd saas-billing-api
```

### 2. Set up the environment

```bash
python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations and run the server

```bash
python django_app/manage.py migrate
python django_app/manage.py runserver
```

---

## Deployment

This project is fully containerized with Docker and deployed on **Railway**.
To build and run the Docker container locally:

```bash
docker build -t saas-billing-api .
docker run -p 8000:8000 saas-billing-api
```

---

## ✅ Running Tests

This project includes unit tests to ensure reliability of both model logic and REST API functionality.

### Run all tests:

```bash
python django_app/manage.py test
```

### Run with test coverage:

```bash
coverage run --source='.' django_app/manage.py test
coverage report
```

### What’s covered:

* `PlanModelTest`: Validates model creation and field accuracy
* `BillingAPITest`: Validates key API endpoints (create, retrieve, etc.)


---

## Screenshots

### API - Plans Endpoint

https://drive.google.com/file/d/1lmIR3MOwV89zX5SMfZ_dGCMr3W-Qzbt7/view?usp=sharing

### API - Invoices Endpoint

https://drive.google.com/file/d/1AlNdKRXkfcmpxXxrtmiIN65tiw3-D2Tu/view?usp=sharing

