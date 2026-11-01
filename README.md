# LLM Project: Building a News Research Tool

## 1. Project Overview

The News Research Tool is a Python-based application that retrieves relevant news articles for a user-provided company, industry, or financial topic and generates an AI-powered summary.

The application uses NewsAPI to retrieve articles, Hugging Face Transformers to generate summaries using a locally running AI model, and Streamlit to provide an interactive web interface.

## 2. Project Objectives

- Retrieve relevant news articles based on a search query.
- Summarize news articles using an AI model.
- Display article titles, sources, publication dates, descriptions, and original links.
- Provide a simple and interactive interface for news research.
- Reduce dependence on paid AI API usage by running the summarization model locally.

## 3. Technologies Used

- Python
- Streamlit
- NewsAPI
- Hugging Face Transformers
LangChain Hugging Face integration (langchain-huggingface)
LangChain
- PyTorch
- Google T5-small (`google-t5/t5-small`)
- python-dotenv
- Visual Studio Code

## 4. Project Structure

```text
LLM_News_Research_Tool/
├── app.py
├── langchain_config.py
├── .env
├── .gitignore
├── README.md
└── .venv/
```

The `.env` file contains API credentials and must not be shared publicly. The `.venv` folder contains the project's Python environment and should not be uploaded to GitHub.

## 5. Application Features

### News Retrieval
Retrieves relevant English-language news articles using NewsAPI.

### AI Summarization
Uses the locally running Google T5-small model to generate a concise summary from article titles and descriptions.

### Interactive Interface
Provides a Streamlit interface where users can enter a research query and view the generated summary and article details.

### Original Sources
Displays links to the original news articles for further reading.

## 6. Installation and Setup

### Step 1: Create a virtual environment

```bash
python -m venv .venv
```

### Step 2: Activate the environment on Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install streamlit newsapi-python python-dotenv "transformers[torch]"
```
python -m pip install streamlit newsapi-python python-dotenv "transformers[torch]" langchain langchain-huggingface

### Step 4: Configure API keys

Create a `.env` file in the project folder and add:

```text
NEWS_API_KEY=your_newsapi_key_here
```

Replace the placeholder with your own NewsAPI key. Keep the `.env` file private.

### Step 5: Run the application

```bash
python -m streamlit run app.py
```

The application opens in a web browser. Enter a company, industry, or financial topic and click **Get News**.

## 7. AI Model

The application uses `google-t5/t5-small` through Hugging Face Transformers. The model is downloaded the first time it is loaded and then runs locally on the computer.

An internet connection is required for the initial model download and for retrieving current news through NewsAPI. The summarization step does not require OpenAI API credits.

## 8. Testing

The application was tested to verify that:

- The configuration module loads successfully.
- News articles can be retrieved from NewsAPI.
- The Streamlit interface runs successfully.
- AI-generated summaries are displayed with the retrieved articles.

Further testing should cover different search queries, empty queries, and API or network errors.

## 9. Limitations

- News retrieval depends on NewsAPI availability, account limits, and the selected API plan.
- Summary quality may vary because T5-small is a relatively small general-purpose model.
- The model summarizes the supplied article titles and descriptions, not necessarily the complete articles.
- The summary should be checked against the original sources before making business or investment decisions.

## 10. Conclusion

The project demonstrates how Python, news retrieval APIs, locally running language models, and Streamlit can be combined to build an interactive news research application. It provides a foundation for exploring AI-assisted news analysis while minimizing paid AI inference costs.