# 🚀 Smart Disaster Response System

An AI-powered system to **prioritize emergency reports** and **assign the best volunteers automatically** using intelligent matching and basic RAG-based chatbot support.

---

## 📌 Features

- 📄 Report submission (issue, location, urgency, severity)
- 🧠 Priority scoring for emergency tasks
- 🤝 Volunteer matching based on:
  - Skill
  - Location
  - Availability
- 🔄 Auto assignment system
- 💬 Chatbot (RAG-based) to query priority tasks
- 📊 System statistics API
- 🌐 Simple frontend (HTML, CSS, JS)

---

## 🏗️ Tech Stack

### Backend
- Django
- Django REST Framework
- SQLite

### AI / Logic
- Rule-based priority scoring
- Matching algorithm (skill + location + availability)
- Basic RAG chatbot

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

---

## 📂 Project Structure
```

solution_challenge/
│
├── config/ # Django project
│ ├── api/ # Main app (models, views, urls)
│ └── config/ # Project settings
│
├── frontend/ # UI (HTML, CSS, JS)
│
├── requirements.txt
└── README.md

```
---

## ⚙️ Setup Instructions

### 1. Clone repo
```bash
git clone <your-repo-url>
cd solution_challenge
2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run migrations
cd config
python manage.py makemigrations
python manage.py migrate
5. Start server
python manage.py runserver
🌐 API Endpoints
Endpoint	Method	Description
/api/reports/	GET/POST	Create & view reports
/api/volunteers/	GET/POST	Add & view volunteers
/api/tasks/priority/	GET	Get priority reports
/api/match/<id>/	GET	Match volunteers for report
/api/assign/	POST	Assign volunteer
/api/chatbot/ask/	POST	Ask chatbot
/api/stats/	GET	System stats
📥 Sample Request
Assign Volunteer
POST /api/assign/

{
  "report_id": 1,
  "volunteer_id": 2
}
🤖 Chatbot Example
POST /api/chatbot/ask/

{
  "question": "what is the priority task"
}
📊 Example Output
{
  "answer": "Top priority: Water issue in Area A with score 72"
}
```
---
## 🚧 Future Improvements
🔥 ML-based matching (instead of rule-based)
🗺️ Geo-based distance matching
📱 Mobile app interface
🧠 Advanced LLM + real RAG pipeline
🔔 Notification system
---
👨‍💻 Authors
Padmavathi M (MERN stack Developer | DSA | AI Enthusiast)
Loga Mithra R (Web Developer | Web Security | CTF Player)
Roshini S (ML Engineer | Python Developer | GEN AI Alchemist)
Chanthru V (AI/ML Student | Developer | Hackathon Enthusiast)
