# 🧮 Scientific Calculator

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

A clean, modular Python scientific calculator featuring a web user interface built with **Streamlit** and a unit-tested calculation engine powered by **Pytest**.

---

## ✨ Features

### ➕ Basic Mode
* **Addition (`+`)**: Standard sum of two numbers.
* **Subtraction (`-`)**: Difference between two numbers.
* **Multiplication (`*`)**: Product of two numbers.
* **Division (`/`)**: Quotient calculation with built-in zero division protection.

### 🔬 Scientific Mode
* **Square Root (`√`)**: Calculates $\sqrt{x}$ with domain error handling for negative inputs.
* **Power ($x^y$)**: Exponentiation supporting floating point base and exponent.
* **Factorial (`!`)**: Calculates $n!$ for non-negative integers.
* **Trigonometry**:
  * **Sine (`sin`)**: Calculates $\sin(\theta)$ with degree angle input.
  * **Cosine (`cos`)**: Calculates $\cos(\theta)$ with degree angle input.
* **Logarithm (`log`)**: Natural logarithm $\ln(x)$ with validation for non-positive numbers.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.8+ | Core application logic and mathematical engine |
| **Web UI** | Streamlit | Interactive browser interface with real-time feedback |
| **Testing** | Pytest | Automated unit test suite covering operations and edge cases |
| **Math Engine** | `math` module | Native Python mathematical functions and conversions |

---

## 📁 Project Structure

```text
my-first-scientific-calculator/
├── app.py                  # Streamlit web interface entry point
├── calculator.py           # Core Calculator engine class & validation logic
├── requirements.txt        # Project dependencies (Streamlit, Pytest)
├── pytest.ini              # Pytest framework configuration
├── tests/
│   └── test_calculator.py  # Unit tests covering all calculator functions
└── README.md               # Project documentation
