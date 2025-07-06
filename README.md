# 📚 Django Library API

A Django REST Framework-based Library Management API supporting JWT Authentication, Book Management, and Borrowing System.

---

## 🚀 Features

- 📖 **Book Management** with ViewSets (CRUD)
- 🔁 **Borrowing System** with ViewSets
- 🧑‍💻 **User Registration & Logout**
- 🔐 **JWT Authentication** (login/logout/token refresh)

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 📂 API Endpoints

| Method | Endpoint        | Description                         |
|--------|------------------|-------------------------------------|
| GET    | `/books/`        | List all books                      |
| POST   | `/books/`        | Create a new book                   |
| GET    | `/borrow/`       | List borrowed books                 |
| POST   | `/borrow/`       | Borrow a book                       |
| POST   | `/register/`     | Register a new user                 |
| POST   | `/logout/`       | Logout and blacklist the JWT token |
| POST   | `/api/token/`    | Obtain JWT access & refresh token  |
| POST   | `/api/refresh/`  | Refresh access token                |

---

## 🧑‍💻 Installation

```bash
git clone https://github.com/YourUsername/library-api.git
cd library-api
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
