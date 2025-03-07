# Webshop Product Management System

## How to Run the Django App

### Running the Project Without Docker

1. **Create a Virtual Environment**
   ```bash
   python3 -m venv env
   ```

2. **Activate the Virtual Environment**
   - **For macOS/Linux:**
     ```bash
     source env/bin/activate
     ```
   - **For Windows:**
     ```bash
     source env/Scripts/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Django Server**
   ```bash
   python manage.py runserver
   ```

### Running the Project with Docker

To run the application using Docker, use the following command:
```bash
docker-compose up --build
```

## Technologies & Packages Used
- **Django** - Web framework for building the backend.
- **Django REST Framework (DRF)** - For building RESTful APIs.
- **drf-yasg** - For API documentation and Swagger UI generation.
