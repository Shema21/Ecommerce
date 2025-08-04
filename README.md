# 🛒 E-Commerce Backend API

This is a professional-grade, scalable, and secure e-commerce backend built with Django and Django REST Framework (DRF). The API supports user authentication, product and category management, secure access controls, search/filtering, JWT authentication, rate limiting, and in-memory caching.

---

## 🚀 Features

### ✅ Core Features
- **User Authentication**
  - Registration, Login with JWT (access + refresh tokens)
  - Logout with refresh token blacklist
  - Password change
  - User profile update
  - Role-based access (admin/user)

- **Product & Category Management**
  - Product CRUD (create, retrieve, update, delete)
  - Category CRUD
  - Slug generation for SEO-friendly product URLs
  - Image uploads
  - Product status tracking (active, out of stock, archived)

- **Filtering & Search**
  - Filter by status, category, price range
  - Keyword search by title or description
  - Sorting by price, created date

- **Security**
  - JWT Refresh/Blacklist for secure logout
  - Rate limiting on login & sensitive endpoints
  - Input validation and password strength checks
  - CSRF protection (if cookie/session auth added)
  - Secure password hashing with Django

- **Performance**
  - In-memory caching using `LocMemCache` for product lists and featured queries

- **Documentation**
  - Swagger/OpenAPI documentation (coming in Phase 6)

---

## ⚙️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Database:** PostgreSQL (or SQLite for dev)
- **Caching:** Django LocMemCache
- **Version Control:** Git + GitHub
- **Deployment:** Docker-ready, supports PythonAnywhere/Heroku/DigitalOcean

---

## 📁 Project Structure

ecommerce_backend/
├── apikey/ # API Key management (optional)
├── users/ # Custom user model and auth endpoints
├── products/ # Product & category models, views
├── ecommerce_backend/ # Main project settings
├── media/ # Product images
└── requirements.txt

---

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/ecommerce-backend.git
cd ecommerce-backend
Set up Virtual Environment


python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
Install Dependencies


pip install -r requirements.txt
Run Migrations


python manage.py migrate
Create Superuser


python manage.py createsuperuser
Run Server


python manage.py runserver
🔐 API Authentication
Use JWT for login and protected routes.

Obtain token:


POST /api/users/login/
{
  "username": "admin",
  "password": "yourpassword"
}
Pass token in headers:

pgsql

Authorization: Bearer <your-access-token>
🔎 Example Endpoints
Method	Endpoint	Description
POST	/api/users/register/	Register user
POST	/api/users/login/	Login (JWT)
GET	/api/users/profile/	Get current user profile
PUT	/api/users/profile/update/	Update profile
POST	/api/users/logout/	Logout user (JWT blacklist)
GET	/api/products/	List products with filter/search
POST	/api/products/	Create product (admin)
GET	/api/categories/	List categories

📌 Filtering & Search Examples
http

GET /api/products/?category=shoes&status=active&min_price=50&max_price=200&ordering=-price
🧪 Testing
Use Django's built-in test framework:


python manage.py test
Add unit and integration tests in /tests/.

🚧 Roadmap
✅ Phase 1: Project Setup & Auth Flow
✅ Phase 2: User Management (CRUD, JWT, Logout, Password)
✅ Phase 3: Product & Category Models with CRUD
✅ Phase 4: Filtering, Search, and Slugs
✅ Phase 5: In-Memory Caching
🔜 Phase 6: Swagger Docs, Rate Limiting, HTTPS, Deployment

## 🧠 Advanced Features Coming
Swagger API Docs

Cart & Order System

Asynchronous tasks with Celery

Redis Caching

Product Reviews

CI/CD with GitHub Actions

Docker Deployment

### 👤 Author
Shema Landry
Backend Engineer, Python & Django Enthusiast
💼 Project Nexus ProDev BE Program