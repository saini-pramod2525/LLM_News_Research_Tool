import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise ValueError("NewsAPI key is missing. Check your .env file.")

# Connect to NewsAPI
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# Local AI model
MODEL_NAME = "google-t5/t5-small"
local_llm = None


def load_local_model():
    global local_llm

    if local_llm is None:
        print("Loading local T5 model. Please wait...")

        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

        text_generation_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    do_sample=False
)

        local_llm = HuggingFacePipeline(
            pipeline=text_generation_pipeline
        )

        print("Local model connected to LangChain!")

    return local_llm


# Prompt used by LangChain
summary_prompt = PromptTemplate.from_template(
    "summarize: {articles}"
)


def get_news_articles(query, page_size=5):
    response = newsapi.get_everything(
        q=query,
        language="en",
        sort_by="relevancy",
        page_size=page_size
    )

    articles = []

    for article in response.get("articles", []):
        articles.append({
            "title": article.get("title") or "Untitled",
            "source": article.get("source", {}).get("name") or "Unknown source",
            "published_at": article.get("publishedAt"),
            "description": article.get("description") or "",
            "url": article.get("url") or ""
        })

    return articles


def get_summary(query):
    articles = get_news_articles(query)

    if not articles:
        return {
            "articles": [],
            "summary": "No relevant news articles were found."
        }

    article_text = "\n".join(
        f"Title: {article['title']}. "
        f"Description: {article['description']}"
        for article in articles
    )

    llm = load_local_model()

    # LangChain prompt → local Hugging Face model
    summary_chain = summary_prompt | llm

    summary = summary_chain.invoke({
        "articles": article_text
    })

    return {
        "articles": articles,
        "summary": summary
    }