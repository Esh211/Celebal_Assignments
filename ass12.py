# -*- coding: utf-8 -*-
"""ass12

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/110y9rXQGxGs8O2YISifJQUOme1_YW_7D
"""

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Replace with your Azure Text Analytics subscription key and endpoint
subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "YOUR_ENDPOINT"

# Authenticate the client
def authenticate_client():
    ta_credential = AzureKeyCredential(subscription_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=ta_credential)
    return text_analytics_client

# Function to analyze sentiment of a list of reviews
def sentiment_analysis_example(client, reviews):
    response = client.analyze_sentiment(documents=reviews)
    for idx, doc in enumerate(response):
        print(f"Review {idx + 1}:")
        print(f"    Sentiment: {doc.sentiment}")
        print(f"    Positive: {doc.confidence_scores.positive:.2f}")
        print(f"    Neutral: {doc.confidence_scores.neutral:.2f}")
        print(f"    Negative: {doc.confidence_scores.negative:.2f}\n")

if __name__ == "__main__":
    # Authenticate the client
    client = authenticate_client()

    # Sample movie reviews
    reviews = [
        "I loved the movie! The performances were stellar and the plot was captivating.",
        "The movie was okay, but I found it a bit too long and some parts were boring.",
        "I didn't like the movie at all. The story was predictable and the acting was terrible."
    ]

# Analyze sentiment
    sentiment_analysis_example(client, reviews)