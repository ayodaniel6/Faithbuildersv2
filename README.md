# 🛐 Faithbuilders — A Modular Django Blog Platform

Faithbuilders is a modern Django-based blog platform designed with modularity and extendability in mind. It integrates a full-featured content management system (CMS), REST API support, user authentication, and a smart chatbot assistant for seamless navigation and user support.

---

## 🚀 Live Demo

🔗 https://[your-app-name.onrender.com](https://faithbuildersv2.onrender.com)

---

## ✨ Key Features

- 📝 **Blog App**: Create, like, comment, and bookmark posts
- 🧠 **Bot App**: Chatbot assistant to guide users and request meetings with counselors
- 📚 **CMS App**: Admin and author panel to manage blog content dynamically
- 👤 **Accounts App**: User signup, login, logout, and profile handling
- 🌐 **REST API**: All content accessible via clean API endpoints (DRF)
- 🎨 **Tailwind CSS** integration for modern UI
- 🐘 **PostgreSQL** support in production
- ☁️ **Free Hosting** with [Render](https://render.com)

---

## 🛠️ Project Structure

Faithbuilders/
├── blog/ # Handles posts, comments, likes, bookmarks
├── cms/ # Author dashboard and content management
├── account/ # User registration and authentication
├── bot/ # Chatbot integration
├── Faithbuilders/ # Main project settings and routing
├── static/ # Static files
├── templates/ # Shared HTML templates
├── manage.py
└── requirements.txt



---

## 📦 Installation (Local)

### 1. Clone the repository

```bash
git clone https://github.com/ayodaniel6/Faithbuildersv2.git
cd Faithbuildersv2

---

##  Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux

---

## Install dependencies

pip install -r requirements.txt

---

## Configure environment variables

# Then open .env and fill in SECRET_KEY and optional DATABASE_URL
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3

# Use PostgreSQL in production
DATABASE_URL=postgres://<user>:<password>@<host>:5432/<db>

---

## Run migrations and start the server
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver

---

## 📡 REST API Overview
Faithbuilders exposes REST endpoints using Django REST Framework.

/api/posts/	GET	List all blog posts
/api/posts/<id>/	GET	Retrieve a single post
/api/comments/	POST	Submit a comment
/api/auth/login/	POST	Login endpoint
/api/search/?q=query	GET	Search posts via bot or keyword

#🔐 Authentication is required for certain actions (e.g., commenting, liking, bookmarking).

---

## ☁️ Deployment (Render)

# 🔧 Procfile

web: gunicorn Faithbuilders.wsgi:application

# 🔧 Build Command

pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

# 🔧 Start Command

gunicorn Faithbuilders.wsgi:application

---

## 🙏 Acknowledgements
Thanks to Django, Tailwind CSS, Render, and the open source community.

# Made with 💻 and 🙏 by @ayodaniel6