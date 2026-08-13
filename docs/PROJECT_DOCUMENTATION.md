# Tactive Canteen System - Project Documentation

## 1. Project Overview

Tactive Canteen System is a Flask-based web application for managing food ordering in a canteen.

The system allows users to select food items, specify quantities, place orders, update stock, and view order history.

## 2. System Components

### Frontend

The frontend is implemented using HTML and CSS with Flask Jinja2 templates.

Main pages:

- `index.html` - Food selection and order placement
- `success.html` - Order confirmation
- `orders.html` - Order history

### Backend

The backend is implemented using Python and Flask.

Main application file:

- `app.py`

It handles:

- Home page
- Order processing
- Quantity validation
- Stock validation
- Total calculation
- Stock updates
- Order storage
- Order history

### Database

SQLite is used for persistent data storage.

Database file:

```text
canteen.db