# 🇮🇳 Bharat Biz-Agent  
### AI-Powered Business Assistant for Retail

Bharat Biz-Agent is an AI-driven conversational assistant designed for businesses to search products, place orders, and manage inventory using natural language.  
The system combines LLM-powered reasoning with structured database queries, allowing businesses to interact with their inventory using simple conversational commands in English and Hindi.

The project demonstrates how modern AI systems can be integrated with backend APIs and databases to automate business workflows.

---

# 🚀 Key Features

### 🤖 AI Conversational Assistant
- Natural language interaction powered by Google Gemini
- Understands business queries and converts them into structured actions

### 🛍️ Smart Product Discovery
Users can search products using conversational queries like:

```
Show me laptops
Find electronics under budget
I want to buy a phone
```

### 📦 Order Management
The system allows users to:
- Place product orders
- Track existing orders
- View order history

### 🌐 Bilingual Interaction
Supports natural language queries in:

- English
- Hindi

### 📊 Database-Driven Business Operations
Inventory and orders are stored in a structured relational database using MySQL.

### 🎨 Interactive UI
Frontend interface inspired by WhatsApp-style conversational UI for intuitive interaction.

---

# 🛠️ Tech Stack

| Layer | Technology |
|------|-------------|
| Backend API | FastAPI (Python) |
| AI Model | Google Gemini |
| Database | MySQL |
| Frontend | HTML / CSS / JavaScript |
| Containerization | Docker |

---

# 🧠 My Contributions

I played a major role in designing and implementing the backend intelligence layer of the system.

### Backend Architecture
- Designed and implemented the entire backend API using FastAPI
- Built RESTful endpoints to process chatbot queries and interact with the database
- Implemented request validation, structured responses, and API documentation

### LLM Integration
- Developed the LLM integration layer using Google Gemini
- Implemented prompt pipelines that convert user queries into business operations
- Designed system prompts and user prompts to control the AI's reasoning and responses

### Prompt Engineering
Created optimized prompts enabling the AI to:

- Understand business intent
- Identify product queries
- Convert conversations into structured database queries
- Handle order placement logic

### Database Design
Designed the raw MySQL database schema including:

**Products Table**
- Product ID
- Name
- Category
- Price
- Description

**Orders Table**
- Order ID
- Product ID
- Quantity
- Order Timestamp

Also populated the database with **150+ enriched product records** to simulate real-world retail data.

### AI-Database Bridge

Implemented logic to connect the LLM output with backend database operations:

```
User Query → AI Intent Detection → Backend Logic → SQL Query → Response
```

This architecture allows conversational queries to directly perform real business operations.

---

# 📋 Prerequisites

Before running the project ensure you have:

- Docker Desktop installed
- A Google Gemini API Key

Get API Key:

https://aistudio.google.com/app/apikey

---

# 🐳 Running the Project (Docker)

## 1 Clone Repository

```bash
git clone https://github.com/darshan8bits/bharat-biz-agent.git
cd bharat-biz-agent
```

## 2 Create Environment File

Create `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

## 3 Start Application

```bash
docker-compose up --build
```

This will automatically:

- Start MySQL database
- Build FastAPI backend container
- Initialize database tables
- Load product dataset

---

## 4 Access the Application

Backend API

```
http://localhost:8000
```

Interactive API Docs

```
http://localhost:8000/docs
```

Frontend

Open:

```
bharat-biz-frontend-BEAUTIFIED.html
```

---

# 💬 Example Queries

### Product Search

```
Show me laptops
Search electronics
Find phones
```

### Place Orders

```
Order a laptop
Buy 2 phones
Place an order for a sofa
```

### Order History

```
Show my recent orders
What did I buy last week
```

---

# 📁 Project Structure

```
bharat-biz-agent/

main.py
FastAPI backend application

llm.py
Gemini AI integration and prompt logic

database.py
Database connection and SQL operations

requirements.txt
Python dependencies

Dockerfile
Docker container configuration

docker-compose.yml
Multi-container orchestration

.env.example
Environment variable template

bharat-biz-frontend-BEAUTIFIED.html
Chat UI frontend
```

---

# 🧪 API Endpoint

### Chatbot API

```
POST /chat
```

Request Example

```json
{
 "message": "Show me laptops"
}
```

The backend:

1. Sends the message to Gemini
2. Extracts the business intent
3. Executes the corresponding database query
4. Returns a structured response

---

# 🛑 Stopping the Application

Stop containers:

```bash
docker-compose down
```

Remove containers and volumes:

```bash
docker-compose down -v
```

---

# 👥 Team

This project was developed collaboratively as part of a team project.

Team Members:

- Darshan Gupta  
- **Kausthuv Narayan Medhi (Backend & AI Integration)**  
- Swapnil Borgohain  
- Arup Saud  

---

# 📄 License

MIT License

---

# 🙏 Acknowledgments

- Google Gemini AI
- FastAPI Framework
- MySQL Database
