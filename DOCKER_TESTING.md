# 🧪 Docker Build Testing Instructions

## For Judges: How to Test This Submission

Follow these steps to verify the Dockerfile works correctly:

---

## ✅ Prerequisites Check

Make sure you have:
- [ ] Docker Desktop installed and running
- [ ] Google Gemini API key ready

---

## 📦 Step 1: Clone the Repository

```bash
git clone https://github.com/darshan8bits/bharat-biz-agent.git
cd bharat-biz-agent
```

---

## 🔑 Step 2: Create .env File

Create a `.env` file in the project root with your Gemini API key:

```bash
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

Replace `your_actual_api_key_here` with a valid Gemini API key.

---

## 🚀 Step 3: Build and Run with Docker Compose

This single command will:
- Build the Docker image
- Start MySQL database
- Start the FastAPI backend
- Initialize database with sample data

```bash
docker-compose up --build
```

**Expected Output:**
```
✅ MySQL container started
✅ Backend container built
✅ Database tables created
✅ 150 products inserted
✅ Server running on http://localhost:8000
```

---

## 🧪 Step 4: Test the API

### Option A: Browser (Interactive Docs)
Open: http://localhost:8000/docs

### Option B: Command Line
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Show me laptops"}'
```

### Option C: Frontend
Open `bharat-biz-frontend-BEAUTIFIED.html` in your browser

---

## ✅ Success Criteria

The build is successful if:
- [x] Docker containers start without errors
- [x] API responds at http://localhost:8000
- [x] `/docs` endpoint is accessible
- [x] Chat endpoint returns product data
- [x] No dependency conflicts
- [x] Database is populated

---

## 🛑 Stop the Application

```bash
docker-compose down
```

---

## 🐛 Common Issues & Solutions

### Issue: Port 8000 already in use
**Solution:**
```bash
# Find and stop the process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# Mac/Linux:
lsof -ti:8000 | xargs kill -9
```

### Issue: Port 3306 already in use (MySQL)
**Solution:** Stop local MySQL or change port in docker-compose.yml

### Issue: Gemini API errors
**Solution:** Verify API key in .env file is valid

### Issue: Database connection timeout
**Solution:** Wait 30 seconds for MySQL to initialize fully

---

## 📊 Resource Requirements

- **RAM:** ~1 GB
- **Disk:** ~500 MB
- **CPU:** Minimal
- **Network:** Internet required (for Gemini API)

---

## 🎯 What This Demonstrates

✅ **Isolated Environment:** Runs completely in Docker containers
✅ **No Dependency Conflicts:** All dependencies in requirements.txt
✅ **Reproducible Build:** Same result on any machine
✅ **Production-Ready:** Uses proper multi-stage build
✅ **Database Integration:** MySQL container with health checks
✅ **Environment Configuration:** Proper .env handling

---

## 📸 Expected Screenshots

After successful build, you should see:

1. **Terminal:** Logs showing both containers running
2. **Browser (http://localhost:8000/docs):** FastAPI Swagger UI
3. **API Response:** JSON with products when testing /chat
4. **Frontend:** Working chatbot interface

---

## ⏱️ Estimated Testing Time

- Clone repo: 1 min
- Build containers: 3-5 min (first time)
- Test API: 2 min
- **Total: ~10 minutes**

---

## 🏆 Evaluation Checklist

For judges to verify submission:

- [ ] Dockerfile present and valid
- [ ] docker-compose.yml present
- [ ] requirements.txt with all dependencies
- [ ] Containers build successfully
- [ ] No errors during startup
- [ ] API accessible and functional
- [ ] Database populated with data
- [ ] Clean shutdown with `docker-compose down`

---

## 📞 Support

If you encounter issues during testing, common fixes:
1. Ensure Docker Desktop is running
2. Check .env file has valid Gemini API key
3. Wait for MySQL health check to pass (~30 sec)
4. Try `docker-compose down -v` then rebuild

---

**Happy Testing! 🚀**
