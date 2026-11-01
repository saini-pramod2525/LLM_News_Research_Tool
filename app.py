
import streamlit as st
from langchain_config import get_summary

# Configure the web page
st.set_page_config(
    page_title="Equity Research News Tool",
    page_icon="📰",
    layout="wide"
)

# Application heading
st.title("📰 Equity Research News Tool")

st.write(
    "Enter a company, industry, or financial topic "
    "to retrieve relevant news and generate an AI summary."
)

# Search input
query = st.text_input(
    "Enter your research query",
    placeholder="e.g., Tata Motors, Indian banking sector"
)

# Search button
if st.button("Get News", type="primary"):
    if not query.strip():
        st.warning("Please enter a research query.")
    else:
        try:
            with st.spinner("Fetching news and generating summary..."):
                result = get_summary(query.strip())

            st.subheader("AI-Generated Summary")
            st.write(result["summary"])

            st.subheader("News Articles")

            if result["articles"]:
                for article in result["articles"]:
                    with st.expander(article["title"]):
                        st.write("**Source:**", article["source"])
                        st.write("**Published:**", article["published_at"])
                        st.write(article["description"])

                        if article["url"]:
                            st.markdown(
                                f"[Read original article]({article['url']})"
                            )
            else:
                st.info("No articles were returned for this query.")

        except Exception as e:
            st.error(
                "Something went wrong while retrieving or "
                "summarizing the news."
            )
            st.caption(f"Error details: {e}")
