from transformers import pipeline

print("Loading model...")
nlp = pipeline("sentiment-analysis")   # load once

def get_intent(user_message: str):
    result = nlp(user_message)[0]
    return result['label'], result['score']


if __name__ == "__main__":
    print(get_intent("I want a refund"))
