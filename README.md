
# 🍜 Luffy Food Delivery Chatbot

**An AI-powered chatbot built with FastAPI, Dialogflow, and SQL to place, update, and track food orders.**

## 🧠 Overview

Luffy is an intelligent food ordering assistant designed to streamline the food delivery process. Leveraging Dialogflow for natural language understanding and FastAPI for backend operations, Luffy can handle tasks such as placing new orders, modifying existing ones, and tracking order statuses.

## ✨ Features

- 🗣️ **Natural Language Interaction**: Users can chat with Luffy using everyday language to manage food orders.
- 🍽️ **Order Management**: Place new orders, update existing ones, or cancel them seamlessly.
- ⏱️ **Real-Time Tracking**: Check the status of your orders on the go.
- 💻 **User-Friendly Interface**: Clean frontend with HTML and CSS.

## 🔧 Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: FastAPI (Python), Uvicorn
- **NLP Engine**: Dialogflow
- **Database**: SQL
- **Tunneling**: Ngrok

## 🛠️ Installation

To set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abhisek-Tiwari/Luffy-Food-Delivery-Chatbot.git
   cd Luffy-Food-Delivery-Chatbot
   ```

2. **Create a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Ensure a SQL DB is ready.
   - Update DB connection info in the backend.

5. **Run Backend Server**:
   ```bash
   uvicorn backend.main:app --reload
   ```

6. **Expose with Ngrok**:
   ```bash
   ngrok http 8000
   ```

   Use the HTTPS URL in Dialogflow as a webhook.

## 🚀 Usage

- Access the chatbot through Dialogflow or your integrated platform.
- Open `frontend/index.html` in your browser for the UI.

## 📁 Project Structure

- `backend/` - FastAPI code
- `frontend/` - HTML + CSS interface
- `README.md` - Project docs

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push and open a pull request


## 📬 Connect with Me

- **GitHub:** [Abhisek-Tiwari](https://github.com/Abhisek-Tiwari)
- **LinkedIn:** [abhisek-tiwari-a06315262](https://www.linkedin.com/in/abhisek-tiwari-a06315262/)


⭐️ If you like this project, don't forget to leave a star!
