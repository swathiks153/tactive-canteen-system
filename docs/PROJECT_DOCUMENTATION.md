# Tactive Canteen System - Project Documentation

## 1. Project Overview

Tactive Canteen System is a simple web-based food ordering application developed using Flask and SQLite.

The system allows users to view available food items, select quantities, place orders, and view their previous orders. The system also manages food stock automatically after successful orders.

## 2. Objectives

- Provide a simple online canteen ordering system.
- Display available food items, prices, and stock.
- Allow users to place food orders.
- Validate order quantities.
- Prevent orders when stock is insufficient.
- Automatically update stock after successful orders.
- Store order details in an SQLite database.
- Provide an order history page.
- Test important application scenarios using pytest.

## 3. Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2
- Pytest

## 4. System Features

### Food Listing
The home page displays the available food items along with their prices and stock quantities.

### Order Placement
Users can select a food item and enter the required quantity to place an order.

### Order Validation
The application validates the requested quantity before processing an order.

### Stock Management
After a successful order, the corresponding food stock is automatically reduced.

### Insufficient Stock Handling
Orders are rejected when the requested quantity is greater than the available stock.

### Invalid Quantity Handling
Zero or invalid quantities are rejected by the application.

### Order History
Successfully placed orders are stored in SQLite and can be viewed through the order history page.

## 5. System Workflow

1. User opens the canteen application.
2. Available food items are displayed.
3. User selects a food item.
4. User enters the required quantity.
5. The application validates the quantity.
6. The application checks available stock.
7. If stock is sufficient, the order is processed.
8. The total order amount is calculated.
9. Food stock is updated.
10. Order details are stored in SQLite.
11. The user receives an order confirmation.
12. Previous orders can be viewed from the order history page.

## 6. Project Structure

```text
TACTIVE CANTEEN SYSTEM/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── PROJECT_DOCUMENTATION.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── orders.html
│   ├── success.html
│   └── error.html
│
├── tests/
│   └── test_app.py
│
├── docs/
│
└── evidence/