# Truedge - E-Commerce Platform

Truedge is a modern, full-featured e-commerce web application built with Django. It features a sleek monochrome design, comprehensive product management, and a seamless shopping experience for users.

## 🚀 Features

### Front-Office (User)
*   **Modern UI/UX:** Responsive design with a clean, monochrome aesthetic using the Inter font family.
*   **User Authentication:** Secure Login and Registration system with automated HTML welcome emails.
*   **Product Browsing:** View curated collections and dynamic product grids.
*   **Shopping Cart:** Fully functional, database-backed cart (Add, Remove, Update quantity) using AJAX for smooth interactions.
*   **Checkout System:** Integrated checkout logic that converts cart items into persistent orders.
*   **User Dashboard:** Personal hub for users to view their "My Orders" history and status.

### Back-Office (Admin)
*   **Admin Dashboard:** Comprehensive control panel displaying "Recent Orders" and system stats.
*   **Product Management:** CRUD capabilities (Create, Read, Update, Delete) for products and collections.
*   **Order Tracking:** Monitor incoming orders with User, Product, Price, and Status details.
*   **User Management:** View list of registered users.

## 🛠️ Tech Stack
*   **Backend:** Django 5.x (Python)
*   **Frontend:** HTML5, CSS3 (Custom Monochrome Theme), JavaScript (Fetch API/AJAX)
*   **Database:** SQLite (Default dev DB)
*   **Utilities:** FontAwesome (Icons), Google Fonts (Inter/Nunito)

## 📦 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/truedge.git
    cd truedge
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install django pillow
    ```

4.  **Apply Database Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create Admin User:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run Development Server:**
    ```bash
    python manage.py runserver
    ```
    - **Website:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - **Admin Panel:** [http://127.0.0.1:8000/admindashboard/](http://127.0.0.1:8000/admindashboard/)

## 📂 Project Structure
*   `truedge/`: Project configuration and settings.
*   `mainapp/`: Core views (Home, Auth, Static pages) and Email logic.
*   `userapp/`: User-centric features (Cart models, Checkout logic, Dashboard).
*   `adminapp/`: Custom admin views for managing products and orders.
*   `templates/`: HTML templates reusing a common `navbar.html` and `footer.html`.
*   `media/`: Hosted product images.

## 📧 Email Configuration
The system is configured to send welcome emails upon registration. Ensure you have your SMTP settings configured in `truedge/settings.py` for this feature to work in production.

---
Developed for the **Truedge** project.
