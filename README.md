# Flask Engineering Calculator

A modern **Engineering Calculator** built with **Flask, Python, HTML, CSS, JavaScript, and Bootstrap**. This web application provides a clean and responsive interface for performing common mathematical and engineering calculations.

---

## Features

* Modern and responsive UI
* Glassmorphism-inspired design
* Real-time form validation with JavaScript
* Supports decimal numbers
* Multiple mathematical operations:

  * Addition
  * Subtraction
  * Multiplication
  * Division
  * Power
  * Modulus
  * Logarithm
  * Square Root
* Error handling for invalid inputs
* Mobile-friendly interface
* Lightweight and easy to deploy

---

## Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **JavaScript:** Vanilla JavaScript
* **Template Engine:** Jinja2

---

## Project Structure

```text
Flask-Engineering-Calculator/
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
│

```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-engineering-calculator.git
```

### 2. Navigate to the project folder

```bash
cd flask-engineering-calculator
```

### 3. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000
```

If you run the application with:

```python
app.run(host="0.0.0.0", port=5000)
```

You can access it from other devices on the same local network using your computer's local IP address.

---

## Supported Operations

| Operation      | Example    |
| -------------- | ---------- |
| Addition       | 5 + 3      |
| Subtraction    | 10 − 4     |
| Multiplication | 6 × 8      |
| Division       | 20 ÷ 5     |
| Power          | 2^5        |
| Modulus        | 10 % 3     |
| Logarithm      | log₁₀(100) |
| Square Root    | √25        |

---

## Screenshots

Add screenshots of the application here.

Example:

```
screenshots/
├── home.png
└── result.png
```

---

## Future Improvements

* Scientific Calculator Mode
* Trigonometric Functions
* Factorial Calculator
* Unit Converter
* Currency Converter
* Calculation History
* Dark/Light Theme Toggle
* Export Results as PDF
* Keyboard Shortcuts
* Progressive Web App (PWA)

---

## Requirements

* Python 3.9+
* Flask

---

## Author

**Abhishek Mishra**

GitHub: https://github.com/ABHISHEK2004-BIT


---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.
