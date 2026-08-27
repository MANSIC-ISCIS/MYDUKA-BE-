# MY DUKA INVENTORY SYSTEM

Record keeping and stock taking are an essential part of every business entity, hence the creation of **My Duka**. This is used to make more informed decisions in regard to different aspects of operations, like the items needed, items in stock and items spoilt. This application is up-to-date with the advanced technology in our ever growing world.

---

# TABLE OF CONTENTS

- Project Overview
- Features
- Technologies Used
- Project Structure
- Database Design
- API Endpoints
- Installation
- Running the Application
- Authentication
- Deployment
- Future Improvements
- Contributors
- License

---

# 📚 Project Overview

This project is built using:

- React (Frontend)
- Flask (Backend)
- SQLite Database
- SQLAlchemy ORM
- Marshmallow
- JWT Authentication

The frontend communicates with the backend through RESTful API requests using JSON.

---

## Authentication

- JWT Login
- Protected Routes
- Role-Based Access
- Merchant Dashboard
- Store Admin Dashboard
- Clerk Dashboard

---

## Merchant Features

- Register account
- Login securely
- View dashboard
- Manage admin
- View all stores
- View reports
- Make and view payments

---

## Store Admin Features

- Register account
- Login securely
- View dashboard
- Manage clerks
- Manage stock
- Approve requests
- Manage payments

---

## Clerk Features

- Register account
- Login securely
- View dashboard
- Record stocks
- Record products
- Request more supplies


---

# 🛠 Technologies Used

## Frontend

- React
- React Router
- JavaScript
- HTML5
- CSS3
- Fetch API

---

## Backend

- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Flask Marshmallow
- Flask Migrate
- Flask CORS

---

## Database

- SQLite

---

# 📂 Project Structure

```
School-Management-System
│
├── backend
│
│   ├── app.py
│   ├── run.py
│   ├── config.py
│   ├── extensions.py
│   ├── schema.py
│   ├── requirements.txt
│
│   ├── models
│   │
│   ├── routes
│   │
│   ├── utils
│   │
│   └── instance
│
└── frontend
    │
    └── react-app
        │
        ├── src
        │
        ├── Components
        │
        ├── Pages
        │
        ├── App.jsx
        ├── main.jsx
        └── package.json
```

---

# 🗄 Database Models

## User

- id
- username
- email
- password

## Stores

- store id
- store name
- location
- admin id
- created at

## Store admin

- admin id
- admin name
- merchant id
- store id

## Clerk

- id
- clerk name
- admin id
- store id
- created at

## Products

- id 
- name
- category
- buying price
- selling price
- supplier id

## Suppliers

- id 
- name 
- phone number
- email
- address

## Record
- id
- product name
- product id
- admin name
- admin id
- store name
- store id
- buying price
- selling price
- created at

## Payments

- id
- product id
- product name
- supplier id
- supplier name
- amount
- status
- payment date
- paid by

## Supply Request

- id
- product name
- product id
- store name 
- store id
- clerk name
- clerk id
- quatity requested
- reason
- status
- created at

---

# 🌐 API Endpoints

## Authentication

POST /register

POST /login

---

## Merchants
 
 GET /Merchants

 ---

 ## Admin

 GET /Admin

 DELETE / Admin

 ---

 ## Clerk

 GET /Clerk

 DELETE /Clerk

 ---

 ## Store

 GET /Store

 PUT /Store

 DELETE /Store

 ---

 ## Products

 GET /Products

 PUT /Products

 DELETE /Products

 ---

 ## Record

 GET /Record

 PUT /Record

 DELETE /Record

 ---

## Payments

 GET /Payments

 PUT /Payments

 DELETE /Payments

 ---

 # 🔐 Authentication

JWT Tokens are used for authentication.

Example

```
Authorization

Bearer <your_token>
```
---

# ⚙ Installation

Clone the repository

```bash
https://github.com/winfreywekesa148-bit/MYDUKA-BE-/tree/main
```

Move into the project

```bash
cd MYDUKA-BE-
```

---

## Backend Setup

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run Flask

```bash
python run.py
```

Server runs on

```
http://127.0.0.1:5000
```

---

## Frontend Setup

Move into the React folder

```bash
cd react-app
```

Install packages

```bash
npm install
```

Run React

```bash
npm run dev
```

React runs on

```
http://localhost:5173
```

---

# 🔄 How React Connects to Flask

React sends requests using Fetch API.

Example

```javascript
fetch("http://127.0.0.1:5000/login")
```

Flask processes the request.

Flask returns JSON.

React updates the interface.

```
React

↓

Fetch Request

↓

Flask API

↓

SQLite Database

↓

JSON Response

↓

React Screen
```

---

# 🚀 Deployment

Frontend

Deploy using

- Vercel

Backend

Deploy using

- Render

Database

- SQLite (development)
- PostgreSQL (production recommended)

---

# 🔮 Future Improvements

- Report download

---

# 👥 Contributors

- Joelwise 
- Cynthia
- Duncan
- Winfrey

---

# 📄 License
MIT License

Copyright (c) 2026 Winkesa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---


Designed for inventory purposes.

