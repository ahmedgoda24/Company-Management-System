# Company Management System

This is a Django-based Company Management System that includes several core features for managing companies, departments, employees, projects, and performance review workflows. The system provides role-based access control (RBAC) to ensure secure data handling and only allows authorized personnel to perform certain actions. It also includes a RESTful API to interact with the system programmatically.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [API Documentation](#api-documentation)



---

## Overview

The Company Management System is designed to help manage various entities, including companies, departments, employees, projects, and the performance review cycle of employees. The system features CRUD functionality for each entity, secure role-based access, and an Employee Performance Review Cycle workflow.

### Core Components:
1. **Company**: Manage company data, including the number of departments, employees, and projects.
2. **Department**: Manage department-specific data under each company.
3. **Employee**: Store and manage employee-related data, including performance reviews.
4. **Project**: Manage projects, including assignment of employees.
5. **Performance Review Workflow**: A staged process with specific transitions for employee performance reviews.
6. **Role-Based Access Control (RBAC)**: Ensures only authorized personnel can perform certain actions (Admin, Manager, Employee).
7. **RESTful API**: Full CRUD support for all entities, secured with JWT authentication.

---

## Features

1. **Company Management**: Create, read, update, and delete companies.
2. **Department Management**: CRUD operations for departments under each company.
3. **Employee Management**: CRUD operations for employee records, including personal and professional details.
4. **Performance Review Workflow**: A staged process with specific transitions for employee performance reviews.
5. **Role-Based Access Control (RBAC)**: Ensures only authorized personnel can perform certain actions.
6. **JWT Authentication**: Secure API access with JWT tokens.

---

## Installation

### Prerequisites

- Python 3.9+
- Docker (for containerization)
- Docker Compose (for orchestration)

### Steps

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```


4. **Run Migrations:**

        ```sh
        python manage.py migrate
        ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

### Docker Setup

 **Run the Docker Compose:**

    ```sh
    docker-compose up --build
    ```
    
###  Endpoints blog Company Mangment
- **Authentication:**
    - Login: `POST /api/v1/auth/login/`, 
    - Create User: `POST /api/v1/auth/users/`,



- **Company:**
    - List all companies: `GET /company/`, `POST /blog/post/`
    - Retrieve a specific company: `/company/{id}/`,
- **Department:**
    - List all departments.: `GET /department/`,
    - Retrieve a specific department: `/department/{id}/`,
    - Create a new department: `POST /department/`
    - Update an existing department: `/departments/{id}/`
    -  Delete a department: `/departments/{id}/`

- **Employee:**
    - List all Employee.: `GET /employee/employees/`,
    - Retrieve a specific Employee: `/employee/employees/{id}/`,
    - Create a new Employee: `POST /employee/employees/`
    - Update an existing Employee: `/employee/employees/{id}/`
    -  Delete a Employee: `/employee/employees/{id}/`
- **Performance Review:**
    -  Transition the performance review of an employee.: `POST /employee/performance_reviews/{id}/transition`

###  Documintation of project Uo can Show 
`api/docs/swagger/` 
`api/docs/redoc/`




