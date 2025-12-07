# cloudify_assesment
find the video explanation above and below are the steps for ultra hard challenge :---
# 1. Create project folder
mkdir <folder>
cd <folder>

# 2. Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows

# 3. Install dependencies
pip install fastapi uvicorn python-dotenv requests
pip install openai

#4.Create main.py
#5.create .env file
# OPENAI_API_KEY=your_openai_key_here
#6.Run FastAPI Server (Local-swaggerApi)
#7.Install & Configure ngrok
#8.Expose FastAPI via ngrok
Make sure FastAPI is running on port 3000:
uvicorn main:app --reload --port 3000
In a new terminal:--
ngrok http 3000
ngrok will show a URL like:
Forwarding  https://a6g7-hj34.ngrok-free.app -> http://localhost:3000
 Copy the HTTPS URL. and
#9.Test Public Endpoint
#10.Users can interact through chat(json formats) in postman
