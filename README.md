# 🎓 Online Learning Management System (LMS) - Django

A full-featured Online Learning Management System (LMS) built using the **Django Framework**, inspired by platforms like **Udemy**. This project allows users to browse, enroll in, and learn from various courses. It also supports tutor registration, content upload, payment integration, and reviews.

## 🚀 Features

- ✅ User Registration & Authentication
- 🎓 Instructor / Tutor Dashboard
- 📚 Course Creation with Categories, Levels, and Languages
- 🎥 Lesson & Content Management (Videos, PDFs, Text)
- 💬 Course Reviews & Ratings
- 🛒 Add to Cart & Checkout System
- 💳 Payment Integration (e.g., Stripe, Razorpay)
- 👨‍🎓 User Dashboard to Track Progress
- 📈 Admin Dashboard with Analytics
- 🔍 Search and Filter Courses
- 🌐 SEO-Friendly URLs and Pages

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** PostgreSQL / SQLite (for development)
- **Authentication:** Django AllAuth or default auth
- **Payment Gateway:** Stripe / Razorpay (optional)
- **Deployment:** Gunicorn + Nginx + PostgreSQL on Ubuntu / Render / Vercel

## 📂 Project Structure

```bash
online_lms/
├── accounts/         # Custom user models and authentication
├── courses/          # Models for Course, Lessons, Reviews
├── dashboard/        # Instructor and student dashboards
├── payments/         # Payment handling logic
├── templates/        # All frontend HTML templates
├── static/           # CSS, JS, images
├── manage.py
└── requirements.txt
