from scrap_news import financial_express
from gemini_api import analyze_news


news = financial_express()
forecast = analyze_news(news)
print(f"==>> forecast: {forecast}")