# Tactive Canteen System

A simple web-based canteen ordering system developed using **Python, Flask, SQLite, HTML, CSS, and Jinja2**.

The system allows users to view available food items, select quantities, place orders, automatically update stock, and view previous orders. It also includes input validation and automated testing using pytest.

---

## 1. Project Overview

The Tactive Canteen System is designed to provide a simple and reliable online food-ordering workflow for a canteen.

The application provides:

- Food item listing
- Food prices and stock availability
- Food ordering
- Quantity validation
- Maximum order quantity validation
- Insufficient-stock prevention
- Automatic stock reduction
- Order total calculation
- SQLite-based order storage
- Order history
- Error handling
- Automated testing using pytest

The project was developed using an iterative AI-assisted development process, including deliberate failure testing and correction.

---

## 2. Problem Statement

Traditional canteen ordering can involve manual processes for checking food availability, calculating order amounts, and maintaining stock.

The objective of this project is to provide a simple web-based system that:

1. Displays available food items.
2. Allows users to place orders.
3. Validates order quantities.
4. Prevents orders when stock is insufficient.
5. Automatically updates stock after successful orders.
6. Stores order information.
7. Provides an order history.
8. Verifies important functionality through automated tests.

---

## 3. Objectives

The main objectives of the project are:

- Develop a functional web-based canteen ordering application.
- Provide a simple user interface for food ordering.
- Maintain food stock automatically.
- Prevent invalid orders.
- Store completed orders in an SQLite database.
- Provide an order history feature.
- Implement automated testing.
- Demonstrate an AI-assisted development and correction loop.
- Provide clear project documentation and user instructions.

---

## 4. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Flask | Web application framework |
| SQLite | Database management |
| HTML | Web page structure |
| CSS | User interface styling |
| Jinja2 | Dynamic HTML rendering |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code repository |
| ChatGPT | AI-assisted development and documentation |

---

## 5. System Features

### 5.1 Food Listing

The home page displays the available food items with:

- Food name
- Price
- Current stock
- Ordering option

Initial food items are:

| Food | Price | Initial Stock |
|------|------:|--------------:|
| Burger | ₹80 | 10 |
| Pizza | ₹120 | 5 |
| Sandwich | ₹60 | 8 |

---

### 5.2 Food Ordering

Users can select a food item and enter the required quantity.

The system processes the order only when the entered quantity satisfies the validation rules.

---

### 5.3 Quantity Validation

The system prevents invalid quantities.

Zero or invalid quantities are rejected instead of being processed.

---

### 5.4 Maximum Order Quantity

The system limits the maximum quantity that can be ordered at one time.

The current maximum order quantity is:

```text
10
Orders above this limit are rejected with an appropriate error response.

5.5 Insufficient Stock Validation

The system checks the available stock before processing an order.
For example, if only 2 sandwiches are available and the user requests 5, the order is rejected.
This prevents the stock value from becoming negative.
5.6 Automatic Stock Update
After a successful order, the corresponding food stock is automatically reduced.
Example:
Initial Burger stock = 10
Ordered quantity = 2

Remaining Burger stock = 8
5.7 Order Total Calculation
The application calculates the total order amount using:
Total = Food Price × Quantity
5.8 Order History
Successful orders are stored in the SQLite database.
Users can view previously placed orders through the order history page.
5.9 Error Handling
The application provides appropriate error responses for invalid situations such as:
Zero quantity
Invalid quantity
Quantity above the maximum limit
Insufficient stock
Invalid food item
6. System Workflow
The application follows this workflow:
User opens application
        |
        v
View available food items
        |
        v
Select food item
        |
        v
Enter quantity
        |
        v
Validate quantity
        |
        +---- Invalid ----> Display error
        |
        v
Check available stock
        |
        +---- Insufficient ----> Display error
        |
        v
Calculate total amount
        |
        v
Update food stock
        |
        v
Store order in SQLite
        |
        v
Display order confirmation
        |
        v
View order history
7. Project Structure
TACTIVE CANTEEN SYSTEM/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
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
│   ├── PROJECT_DOCUMENTATION.md
│   └── USE_GUIDE.md
│
└── evidence/
    ├── home_page.png
    ├── order_success.png
    ├── order_history.png
    ├── insufficient_stock.png
    ├── zero_quantity.png
    └── tests_passed.png
The local SQLite database is used by the application but is excluded from version control through .gitignore.
8. Application Files
app.py
Contains the Flask application and application routes.
Main responsibilities include:
Displaying food items
Processing orders
Validating quantities
Checking stock
Calculating totals
Updating stock
Storing orders
Displaying order history
Handling errors
database.py
Contains SQLite database initialization and connection-related functionality.
The database contains food and order information.
templates/
Contains the HTML templates used by the Flask application.
index.html — Home page
orders.html — Order history
success.html — Successful order page
error.html — Error page
tests/test_app.py
Contains automated tests for important application scenarios.
9. Installation and Setup
Step 1: Clone the Repository
Clone the project repository from GitHub.
git clone <YOUR_GITHUB_REPOSITORY_URL>
Move into the project directory:
cd "tactive canteen system"
Step 2: Create a Virtual Environment
Create a Python virtual environment:
python -m venv venv
Step 3: Activate the Virtual Environment
On Windows PowerShell:
.\venv\Scripts\Activate.ps1
After activation, the terminal should display:
(venv)
Step 4: Install Dependencies
Install the required packages:
pip install -r requirements.txt
10. Running the Application
Start the Flask application:
python app.py
The application runs locally at:
http://127.0.0.1:5000
Open the address in a web browser.
11. Running the Tests
The project uses pytest for automated testing.
Run the complete test suite using:
python -m pytest -v
The final test suite contains five test cases:
Home page
Successful order
Zero quantity validation
Insufficient stock validation
Maximum order quantity validation
Expected final result:
5 passed
12. Test Results
The final automated test suite successfully passes all five tests.
Example:
tests/test_app.py::test_home_page PASSED
tests/test_app.py::test_successful_order PASSED
tests/test_app.py::test_zero_quantity PASSED
tests/test_app.py::test_insufficient_stock PASSED
tests/test_app.py::test_maximum_quantity PASSED

5 passed
A captured screenshot of the successful test run is available in:
evidence/tests_passed.png
13. Deliberate RED Test
As part of the development process, a deliberate failure was introduced to verify that the automated tests could detect incorrect behavior.
For the insufficient-stock validation, the expected HTTP response was:
400
The implementation was intentionally changed to return:
200
The test suite detected the incorrect behavior.
The resulting failure included:
FAILED tests/test_app.py::test_insufficient_stock
assert 200 == 400
This demonstrated that the test was actually checking the expected behavior rather than simply passing.
14. GREEN Test and Correction
After observing the RED test failure, the implementation was corrected by restoring the expected response code:
400
The test suite was executed again.
The final result was:
5 passed
This demonstrated the development cycle:
Feature
   ↓
AI-Assisted Change
   ↓
RED Test
   ↓
Failure Analysis
   ↓
Correction
   ↓
GREEN Test
The complete AI-assisted change-loop is documented in:
docs/PROJECT_DOCUMENTATION.md
15. AI-Assisted Development
AI tools were used as part of the development process.
AI Tool Used
ChatGPT
Uses of ChatGPT
ChatGPT was used for:
Understanding the project requirements
Developing and improving application logic
Debugging code
Creating and improving pytest test cases
Analysing test failures
Guiding the RED/GREEN testing cycle
Preparing project documentation
Preparing the user guide
Preparing presentation content
Preparing the demonstration video structure
The final implementation was tested locally using the project's automated test suite.
16. AI Change-Loop Evidence
The project followed an iterative AI-assisted development process.
Initial Feature
The application needed to reject orders when the requested quantity exceeded available stock.
AI-Assisted Change
The validation logic was reviewed and modified with AI assistance.
Deliberate Failure
An incorrect HTTP response status was intentionally introduced.
Expected:
400
Incorrect:
200
RED Result
The test detected the incorrect behavior:
FAILED
assert 200 == 400
Correction
The implementation was corrected and the expected response status was restored.
GREEN Result
The complete test suite passed:
5 passed
This evidence demonstrates that the test suite can detect incorrect behavior and verify the corrected implementation.
17. Security and Validation
The application includes basic validation to prevent invalid ordering behavior.
Implemented validation includes:
Quantity validation
Maximum order quantity validation
Stock availability checking
Prevention of negative stock
Validation of selected food items
Appropriate error responses
The project does not contain passwords, API keys, or other secrets in the repository.
18. Evidence Screenshots
The project contains captured evidence of important functionality.
Home Page
evidence/home_page.png
Shows the available food items, prices, and stock.
Successful Order
evidence/order_success.png
Shows successful order processing.
Order History
evidence/order_history.png
Shows previously placed orders.
Insufficient Stock
evidence/insufficient_stock.png
Shows rejection of an order when insufficient stock is available.
Zero Quantity Validation
evidence/zero_quantity.png
Shows rejection of an invalid zero quantity.
Test Results
evidence/tests_passed.png
Shows the successful automated test execution.
19. Documentation
The project includes the following documentation:
Project Documentation
docs/PROJECT_DOCUMENTATION.md
Contains:
Project overview
Objectives
Technologies
Features
System workflow
Project structure
AI-assisted change loop
User Guide
docs/USE_GUIDE.md
Contains instructions for a user to:
Start the application
View food items
Place an order
View order history
Understand validation and errors
20. Presentation
A presentation deck has been prepared for the project.
The presentation covers:
Problem statement
Proposed solution
System features
Technologies used
System workflow
Testing
AI-assisted development
Results
Conclusion
21. Video Demonstration
A five-minute project demonstration has been prepared.
The demonstration covers:
Problem and approach
Application workflow
Food ordering
Stock management
Order history
Input validation
Error handling
Automated test execution
AI-assisted development process
22. Expected Application Behaviour
Valid Order
If the requested quantity is valid and stock is available:
Order accepted
       ↓
Total calculated
       ↓
Stock reduced
       ↓
Order stored
       ↓
Confirmation displayed
Invalid Quantity
Invalid quantity
       ↓
Order rejected
       ↓
Error displayed
Insufficient Stock
Requested quantity > available stock
       ↓
Order rejected
       ↓
Error displayed
Maximum Quantity Exceeded
Requested quantity > 10
       ↓
Order rejected
       ↓
Validation error displayed
23. Final Test Status
The final application was tested using pytest.
5 tests passed
0 tests failed
The project therefore contains both functional implementation and automated verification of the main ordering scenarios.
24. Final Deliverables
The Tactive project submission contains the following six deliverables:
1. Source Code Repository
Contains:
Flask application
SQLite database logic
HTML templates
Automated tests
README
2. Test Suite and Captured Output
Contains:
Automated pytest tests
Successful test output
Deliberate RED test evidence
3. AI Change-Loop Evidence
Documents:
AI-assisted changes
Development attempts
Deliberate failure
Test failure
Correction
Final successful test
4. Documentation Set
Contains:
Architecture/project documentation
Design and workflow information
User Guide
5. Presentation
Contains the project presentation deck.
6. Video
Contains the five-minute project demonstration.
25. Conclusion
The Tactive Canteen System provides a complete web-based food ordering workflow using Flask and SQLite.
The system demonstrates:
Web application development
Database integration
Stock management
Input validation
Error handling
Automated testing
AI-assisted iterative development
Documentation
Presentation and live demonstration
The final implementation was verified through automated tests, including a deliberate RED test followed by a corrective GREEN test.
Tactive Canteen System
        |
        +-- Flask Web Application
        |
        +-- SQLite Database
        |
        +-- Food Ordering
        |
        +-- Stock Management
        |
        +-- Validation
        |
        +-- Order History
        |
        +-- Automated Testing
        |
        +-- AI-Assisted Change Loop
        |
        +-- Documentation
        |
        +-- Presentation
        |
        +-- Video Demonstration