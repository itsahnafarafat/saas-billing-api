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
```

Available endpoints:

* `plans/` – List all subscription plans
* `subscriptions/` – View and create subscriptions
* `invoices/` – View billing invoices
* `payments/` – View payment history

Example request:

```bash
GET /api/billing/plans/
```

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

## Screenshots

### API - Plans Endpoint

![Plans Endpoint](<img width="1594" height="768" alt="Screenshot 2025-07-25 101405" src="https://github.com/user-attachments/assets/d4cb8f5b-75c1-4517-87c3-595edbc873af" />
)

### API - Invoices Endpoint

![Invoices Endpoint](<img width="1592" height="771" alt="Screenshot 2025-07-25 101327" src="https://github.com/user-attachments/assets/b558e0dd-68e6-47bf-b13a-ad2db6d22951" />
)

