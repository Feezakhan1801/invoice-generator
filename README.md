# 🧾 Invoice Generator System

A simple and efficient **Invoice Generator Web Application** built using Python.
This system allows users to create invoices by entering customer and product details and automatically generates a downloadable PDF invoice.

---

## 🚀 Features

* 🧾 Create invoices with customer details
* 📦 Add product name, quantity, and price
* 🧮 Automatically calculate total amount
* 📄 Generate professional PDF invoices using FPDF
* 💾 Save invoices locally
* 🖥️ Simple and user-friendly interface
* 🔐 User authentication (Login/Register)
* 📊 Invoice history dashboard

---

## 🛠️ Tech Stack

* **Python** 🐍
* **FastAPI** – Backend API
* **Streamlit** – Frontend UI
* **FPDF** – PDF generation
* **SQLite** – Database
* **Uvicorn** – ASGI server

---

## 📁 Project Structure

```
invoice_app/
│
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── models.py
│   ├── database.py
│   ├── invoice_pdf.py
│   └── pdf_generator.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/Feezakhan1801/invoice-generator.git
cd invoice-generator/invoice_app
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate environment

```
venv\Scripts\activate
```

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### 🔹 Start Backend (FastAPI)

```
uvicorn backend.main:app --reload
```

### 🔹 Start Frontend (Streamlit)

```
cd frontend
streamlit run app.py
```

---

## 🔄 How It Works

1. User registers or logs in
2. User fills invoice details
3. Data is sent to backend API
4. Backend calculates total amount
5. PDF invoice is generated using FPDF
6. File is saved and returned to user



## 👨‍💻 Author

**Feeza Khan**
🔗 GitHub: https://github.com/Feezakhan1801

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!
