# AI Chatbot 🤖

A professional **AI-powered chatbot** built with **Python (Flask)** for the backend and a clean **HTML/CSS/JavaScript** frontend.  
This project demonstrates how to integrate machine learning models with a web interface to create an interactive conversational experience.

---

## 🚀 Features
- Interactive UI with chat bubbles, avatars, and smooth animations  
- Instant replies with placeholder responses for better user experience  
- Backend powered by Flask with REST API endpoints  
- Lightweight NLP model (Hugging Face `sentiment-analysis`) for intent detection  
- Error handling for unreachable backend  
- Professional design inspired by modern messaging apps  

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Flask  
- **NLP Model:** Hugging Face Transformers (`pipeline("sentiment-analysis")`)  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure
```
ai_chatbot/
│
├── app.py             # Flask backend server
├── chat_model.py      # NLP model integration
├── index.html         # Frontend UI
├── test_request.py    # Script to test backend API
├── venv/              # Virtual environment (ignored in Git)
└── README.md          # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai_chatbot.git
cd ai_chatbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Backend
```bash
python app.py
```
Backend will start at: `http://127.0.0.1:5000`

### 5. Run Frontend
- Open `index.html` in your browser  
- Type a message → see instant chatbot replies  

---

## 📸 Screenshots
*(Add screenshots of your chatbot UI here for visual appeal)*

---

## 🎯 Future Enhancements
- Add typing animation (three dots) for bot replies  
- Deploy backend to cloud (Heroku/AWS/Render)  
- Host frontend on GitHub Pages  
- Expand NLP model for richer conversations  

---

## 👨‍💻 Author
**Atharva Chopade**  
- PG Diploma in Big Data Analytics (CDAC, Pune, 2025)  
- BTech in Information Technology (Govt College of Engineering, Amravati, 2024)  
- Passionate about AI, Big Data, and building real‑world projects  

---
