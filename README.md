# 🇮🇳 Bharat Biz-Agent

AI-powered chatbot assistant for Indian businesses to search products, place orders, and manage inventory using natural language in English and Hindi.

## 🚀 Features

- 🤖 Natural language processing using Google Gemini AI
- 🛍️ Product search and browsing
- 📦 Order placement and tracking
- 💬 Bilingual support (English & Hindi)
- 📊 Order history management
- 🎨 Beautiful WhatsApp-inspired UI

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **AI Model**: Google Gemini 2.5 Flash
- **Database**: MySQL
- **Frontend**: HTML/CSS/JavaScript
- **Containerization**: Docker

## 📋 Prerequisites

- Docker Desktop installed
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

## 🐳 Quick Start with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/darshan8bits/bharat-biz-agent.git
cd bharat-biz-agent
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Build and Run with Docker Compose

```bash
docker-compose up --build
```

This will:
- ✅ Start MySQL database
- ✅ Build and start the FastAPI backend
- ✅ Initialize the database with 150+ products
- ✅ Make the API available at `http://localhost:8000`

### 4. Access the Application

**Backend API:**
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

**Frontend:**
- Open `bharat-biz-frontend-BEAUTIFIED.html` in your browser
- The frontend connects to `http://localhost:8000`

## 🔧 Manual Docker Build (Alternative)

If you want to build just the backend:

```bash
# Build the image
docker build -t bharat-biz-backend .

# Run with environment variables
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=your_key \
  -e DB_HOST=host.docker.internal \
  -e DB_USER=root \
  -e DB_PASSWORD=billa \
  -e DB_NAME=ai_db \
  -e DB_PORT=3306 \
  bharat-biz-backend
```

## 💬 Testing the Chatbot

Try these example queries:

1. **Product Search:**
   - "Show me laptops"
   - "I'm looking for phones"
   - "Search for electronics"

2. **Place Order:**
   - "I want to order a laptop"
   - "Buy 2 phones"
   - "Order a sofa"

3. **Order History:**
   - "What are my recent orders?"
   - "Show my order history"

## 📁 Project Structure

```
bharat-biz-agent/
├── main.py                 # FastAPI application
├── llm.py                  # Gemini AI integration
├── database.py             # Database operations
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Multi-container setup
├── .env.example           # Environment variables template
└── bharat-biz-frontend-BEAUTIFIED.html  # Frontend UI
```

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | ✅ Yes |
| `DB_HOST` | MySQL host | ✅ Yes |
| `DB_USER` | MySQL username | ✅ Yes |
| `DB_PASSWORD` | MySQL password | ✅ Yes |
| `DB_NAME` | Database name | ✅ Yes |
| `DB_PORT` | MySQL port (default: 3306) | ✅ Yes |

## 🧪 API Endpoints

- `POST /chat` - Main chatbot endpoint
  ```json
  {
    "message": "Show me laptops"
  }
  ```

## 🛑 Stopping the Application

```bash
docker-compose down
```

To remove all data:
```bash
docker-compose down -v
```

## 🐛 Troubleshooting

### Database Connection Issues
- Ensure MySQL container is running: `docker ps`
- Check MySQL health: `docker logs bharat-biz-mysql`

### Gemini API Errors
- Verify your API key in `.env`
- Check rate limits (free tier: 20-250 requests/day)

### Port Already in Use
- Stop any services running on port 8000 or 3306
- Or change ports in `docker-compose.yml`

## 👥 Team

- Darshan Gupta

## 📄 License

MIT License

## 🙏 Acknowledgments

- Google Gemini AI
- FastAPI Framework
- MySQL Database
