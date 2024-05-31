# Transaction Management API

This project provides a RESTful API for managing transactions using Django and Django REST Framework. The API supports CRUD operations (Create, Read, Update, Delete) on `Transaction` objects.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation Steps

1. **Clone the repository:**
    ```sh
    git clone git@github.com:Brenolima03/django-transaction-api.git
    cd django-transaction-api
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations to set up the database:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser to access the admin panel:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Get All Transactions

- **URL:** `/api/v1/`
- **Method:** `GET`
- **Query Parameters:** Optional filters to query transactions
- **Response:**
    - **200 OK:** Returns a list of transactions (empty list if none found)

### Get Transaction by ID

- **URL:** `/api/v1/<pk>/`
- **Method:** `GET`
- **URL Parameters:** 
    - `pk`: Primary key of the transaction
- **Response:**
    - **200 OK:** Returns the transaction data
    - **404 Not Found:** If the transaction does not exist

### Create a New Transaction

- **URL:** `/api/v1/post/`
- **Method:** `POST`
- **Request Body:** JSON representation of the transaction
- **Response:**
    - **201 Created:** If the transaction is successfully created
    - **400 Bad Request:** If the request data is invalid

### Update an Existing Transaction

- **URL:** `/api/v1/update/<pk>/`
- **Method:** `PUT`
- **URL Parameters:** 
    - `pk`: Primary key of the transaction
- **Request Body:** JSON representation of the updated transaction data
- **Response:**
    - **200 OK:** If the transaction is successfully updated
    - **400 Bad Request:** If the request data is invalid
    - **404 Not Found:** If the transaction does not exist

### Delete a Transaction

- **URL:** `/api/v1/delete/<pk>/`
- **Method:** `DELETE`
- **URL Parameters:** 
    - `pk`: Primary key of the transaction
- **Response:**
    - **204 No Content:** If the transaction is successfully deleted
    - **404 Not Found:** If the transaction does not exist
