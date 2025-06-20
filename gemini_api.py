from langchain_google_genai import ChatGoogleGenerativeAI
import os

GOOGLE_API_KEY = 'AIzaSyAyr6RsRyqn1AfAujLyTtuoV59sewN-gCY'
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY
def get_chain():
    llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
        )
    return llm

def get_answer(message_list:list, chain:ChatGoogleGenerativeAI=None):
    if not chain:
        chain = get_chain()
    ai_msg = chain.invoke(message_list)
    return ai_msg.content

def analyze_news(news_list):
    prompt = """
        You are a professional stock trader and financial news analyst.
        I will provide you with a list of news headlines or summaries.
        Your task is to:

        1. Group the news items by the impacted stock (ignore news not related to a specific stock).
        2. Remove duplicates (do not consider repeated or near-identical news).
        3. For each stock, analyze the combined news sentiment and context.
        4. Provide a forecast for each stock: "Up", "Down", or "Neutral", along with a short reason.

        ---
        ### 🔁 Response Format (in JSON inside triple backticks):

        ```json
        [
        {
            "stock_name": "Name of Stock",
            "forecast": "Up" | "Down" | "Neutral",
            "reason": "Brief explanation based on news analysis"
        }
        ]"""
    msg_list = [
        (
            "system",
            prompt
        ),
        ("human", f" news list : {news_list}"),
    ]

    forecast = get_answer(msg_list)
    return forecast








