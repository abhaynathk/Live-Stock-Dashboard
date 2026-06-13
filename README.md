# 📈 Stock Live Dashboard
.

This project is the first milestone of a larger AI-powered Investment Advisor that will evolve into a multi-agent system capable of performing technical analysis, news sentiment analysis, portfolio management, and AI-driven investment recommendations using LangGraph.

---

## 🚀 Features

- Live stock price retrieval
- Historical OHLC data
- Interactive candlestick charts
- Company information
- Market capitalization
- 52 Week High & Low
- Trading volume
- REST API using FastAPI
- Interactive dashboard using Streamlit
- Modular service architecture

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend REST API |
| Streamlit | Frontend Dashboard |
| Yahoo Finance | Live Stock Data |
| Pandas | Data Processing |
| Plotly | Interactive Charts |
| Requests | API Communication |

---

## 📂 Project Structure

```
Stock-AI-Agent/

│
├── backend/
│   └── app.py
│
├── frontend/
│   └── app.py
│
├── services/
│   ├── stock_service.py
│   └── indicator_service.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Stock-AI-Agent.git

cd Stock-AI-Agent
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Backend

```bash
uvicorn backend.app:app --reload
```

Backend will be available at

```
http://127.0.0.1:8000
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Running the Frontend

Open another terminal

```bash
streamlit run frontend/app.py
```

Streamlit Dashboard

```
http://localhost:8501
```

---

## 📊 Current Features

✔ Live Stock Prices

✔ Historical Price Data

✔ Candlestick Charts

✔ Company Information

✔ Volume

✔ Market Cap

✔ 52 Week High/Low

---

## 🔜 Upcoming Features

- Technical Indicators (RSI, MACD, EMA)
- AI Buy/Sell Recommendations
- News Sentiment Analysis
- LangGraph Multi-Agent System
- Portfolio Tracker
- Risk Analysis
- Live WebSocket Streaming
- Kafka Integration
- PostgreSQL Database
- Docker Deployment
- Kubernetes Deployment

---

## 📸 Screenshots

Add screenshots of the application here.

Example:

```
screenshots/dashboard.png
```

---

## 📡 API Endpoints

### Get Stock Information

```
GET /stock/{symbol}
```

Example

```
GET /stock/AAPL
```

---

### Get Historical Data

```
GET /history/{symbol}
```

Example

```
GET /history/AAPL
```

---

## 💡 Future Architecture

```
User
   │
Streamlit Dashboard
   │
FastAPI Backend
   │
Stock Services
   │
Yahoo Finance API
```

Future

```
                User
                  │
                  ▼
            Streamlit Dashboard
                  │
                  ▼
          LangGraph Orchestrator
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
Technical     News Agent    Risk Agent
 Agent
     │            │            │
     └────────────┼────────────┘
                  ▼
          Decision Agent
                  │
                  ▼
          AI Recommendation
```

---



---

## 👨‍💻 Author

**Abhaynath K**

M.Tech AI & ML

VIT Vellore

GitHub: https://github.com/abhaynathk

LinkedIn: https://www.linkedin.com/in/abhaynathk/
