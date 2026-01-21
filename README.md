# GitHub_Explorer
A modern GitHub Explorer application built with Flask, following OOP, Clean Architecture, and microservice-ready principles.  
The application allows users to search GitHub profiles and explore repositories with a clean and modern dark UI (no raw JSON output).

## ✨ Features
- Search GitHub users by username
- View user profile information
- List public repositories
- Display stars and main language
- Modern dark UI
- OOP & layered architecture
- Microservice-ready backend design

## 🧠 Architecture
This project is designed as a microservice-ready monolith. Each service can be easily separated into its own microservice in the future.

Controller → Service → Model  
             ↓  
         GitHub API Client

User Service handles GitHub user data, Repo Service handles repository data.

## 📁 Project Structure
github-explorer/
├── services/
│   ├── user_service/
│   └── repo_service/
├── core/
│   ├── config.py
│   ├── github_client.py
│   └── exceptions.py
├── frontend/
│   ├── templates/
│   └── static/
├── app.py
└── requirements.txt

## ⚙️ Technologies
Flask, Python (OOP), REST API, Marshmallow, HTML, CSS, GitHub REST API

## ▶️ Getting Started
git clone https://github.com/<your-username>/github-explorer.git  
cd github-explorer  
python -m venv venv  
source venv/bin/activate  (Windows: venv\\Scripts\\activate)  
pip install -r requirements.txt  
python app.py  

Open in browser: http://127.0.0.1:5000

## 🔗 API Endpoints
GET /api/users/<username>  
GET /api/repos/<username>

## 🎯 Why This Project?
This project demonstrates clean backend architecture, separation of concerns, real-world GitHub API integration, and a structure that can easily scale into real microservices. It is suitable for portfolio and job applications.

## 🚀 Future Improvements
Docker and Docker Compose, Redis caching, rate limiting, authentication service, React or Vue frontend, unit and integration tests.

## 👨‍💻 Author
Hüseyin Doğdu  
Computer Engineer | AI & Backend Developer  
GitHub: https://github.com/huso987

## UI
<img width="1402" height="777" alt="image" src="https://github.com/user-attachments/assets/b0f78be2-21a9-4ac0-9fc0-4b62e0b36f0f" />

