# 📊 BMI Calculator with Streamlit

This is a simple Python project built using Streamlit to calculate the Body Mass Index (BMI) in an interactive way.

---
---
## Printscreen
<img width="1899" height="829" alt="Captura de ecrã 2026-04-01 091306" src="https://github.com/user-attachments/assets/ab87ff18-b77c-43c1-9118-968eaee19a9b" />

---

## 🚀 Features

The application allows the user to:

* Enter their weight (in kg)
* Enter their height (in meters)
* Calculate BMI instantly
* See the BMI classification result

---

## 🧠 BMI Formula

The BMI is calculated using the following formula:

BMI = weight / (height²)

---

## 📂 Project Structure

```
IMC_Python/
│
├── venv/           # Virtual environment (not included in Git)
├── IMC.py          # Main application file
└── .gitignore      # Ignored files
```

---

## 🛠️ Technologies Used

* Python 3
* Streamlit

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repository.git
cd IMC_Python
```

---

### 2. Create and activate a virtual environment

#### Windows (PowerShell)

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Windows (CMD)

```
python -m venv venv
venv\Scripts\activate.bat
```

---

### 3. Install dependencies

```
pip install streamlit
```

---

### 4. Run the application

```
streamlit run IMC.py
```

---

## 📈 BMI Classification

| BMI         | Classification |
| ----------- | -------------- |
| < 18.5      | Underweight    |
| 18.5 - 24.9 | Normal weight  |
| 25 - 29.9   | Overweight     |
| ≥ 30        | Obesity        |

---

## 📌 Notes

* The `venv` folder should not be uploaded to GitHub
* Make sure Streamlit is installed correctly

---

---

## ✨ Author

Developed by Leone
