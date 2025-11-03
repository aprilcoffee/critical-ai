import ollama

def analyze_sentiment(text):
    
    prompt = f"""Analyze the sentiment of the following text. 
Respond with only one word: positive, negative, or neutral.

Text: {text}

Sentiment:"""
    
    response = ollama.generate(
        model='llama3.2',  # or any model you have pulled
        prompt=prompt
    )
    
    return response['response'].strip().lower()

text = input("Enter a text to analyze: ")
sentiment = analyze_sentiment(text)
print(f"Text: {text}\nSentiment: {sentiment}\n")