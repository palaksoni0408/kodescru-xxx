# **KodesCRUxxx - AI Coding Assistant**

## **Overview**

KodesCRUxxx is an AI-powered coding assistant designed to help students and developers learn, debug, generate, and analyze code efficiently. It offers a rich set of features to enhance your programming journey, all accessible through a sleek, mobile-friendly interface.

---

## **Features**

- **Code Explanation:** Understand complex code snippets with beginner-friendly explanations.
- **Code Debugging:** Find and fix bugs and logical errors.
- **Code Generation:** Generate code snippets, templates, and solutions.
- **Logic to Code Conversion:** Convert pseudo-code or logic descriptions into actual code.
- **Complexity Analysis:** Analyze time and space complexity of algorithms.
- **Step-by-step Code Tracing:** Visualize code execution flow.
- **Snippets Library:** Access a collection of useful code snippets.
- **Project Ideas & Roadmaps:** Get project suggestions and personalized learning paths.
- **Motivation & Goals:** Set goals and receive motivational messages.
- **Collaborative Rooms:** Join real-time coding rooms for teamwork.
- **Resume Builder & Tutorials:** Create resumes and access curated tutorials and GitHub repos.
- **Dark Mode & Mobile Friendly:** Sleek, responsive UI optimized for all devices.

---

## **Getting Started**

### **Prerequisites**

- Python 3.8+
- API key for `euriai` (or OpenAI GPT)
- Required Python packages:
  - `streamlit`
  - `fastapi`
  - `requests`
  - `python-dotenv`
  - `langchain`
  - `euriai`

### **Installation**

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/kodescru-xxx.git
cd kodescru-xxx
```

## 2. Create and activate a virtual environment
```bash
# Create a virtual environment named 'venv'
python -m venv venv
# Activate the virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Set your API key (Create a .env file in the root directory:)
```bash
EURIAI_API_KEY=your_openai_or_euriai_api_key
```

## 5. Run the backend server
```bash
uvicorn main:app --reload
```

## 6. Run the frontend app
```bash
streamlit run app.py
```

## Usage
- Open the app URL (usually [http://localhost:8501](http://localhost:8501))
- Use the sidebar to navigate features
- Enter your language, topic, and code
- Explore explanations, debugging, code generation, and more
- Enjoy a mobile-responsive experience

## Deployment
- Deploy backend (`main.py`) on **Heroku**, **Vercel**, or **Render**
- Deploy frontend (`app.py`) on **Streamlit Cloud** or **Vercel**
- Configure custom domains and SSL for production

## Contributing
- Contributions are welcome! Please fork the repo, create a feature branch, and submit a pull request.

## Contact
- **Email:** your.email@example.com
- **GitHub:** [https://github.com/yourusername/kodescru-xxx](https://github.com/yourusername/kodescru-xxx)

## Future Enhancements
- Real-time collaborative editing
- User progress tracking
- Resume and portfolio generation
- Integration with tutorials and repositories
- Advanced code visualization

## 🎥 Demo Video

[▶ Watch Demo on YouTube]
( https://youtu.be/-gJqsESyilg )
