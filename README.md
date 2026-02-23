# ML2API – Machine Learning Model Deployment using FastAPI

ML2API is a beginner-friendly project that demonstrates how to train a Machine Learning model and deploy it as a REST API using FastAPI.

This project covers the complete pipeline from model training → API creation → testing → deployment readiness.

---

# Project Objective

The main objective of this project is to:

- Train a simple Machine Learning model
- Convert the model into an API using FastAPI
- Test the API using Swagger UI
- Prepare the project for deployment

---

# Problem Statement

We built a model that predicts **salary based on years of experience**.

Example:

- Input: Experience = 3 years
- Output: Salary ≈ 50000

---

# Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- Uvicorn
- Joblib (Model Serialization)

---

# Project Structure

```
ML2API/
│
├── app/
│   ├── main.py        # FastAPI application
│   └── schema.py      # Input data schema
│
├── model/
│   ├── model.py       # Model training script
│   └── trained_model.pkl  # Saved ML model
│
├── requirements.txt   # Project dependencies
├── README.md          # Documentation
└── .gitignore
```

---

# Setup Instructions

## 1. Clone the Repository

```
git clone https://github.com/Kunalagarwal26/ML2API.git
cd ML2API
```

---

## 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Run the API Server

```
uvicorn app.main:app --reload
```

---

## 5. Open in Browser

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Home Endpoint

```
GET /
```

Response:

```
{
  "message": "ML2API is running 🚀"
}
```

---

## Prediction Endpoint

```
POST /predict
```

### Input:

```
{
  "experience": 3
}
```

### Output:

```
{
  "experience": 3,
  "predicted_salary": 50000
}
```

---

# Testing

You can test the API using:

- Swagger UI ([http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs))
- Postman
- cURL

---
