import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import random

nltk.download('vader_lexicon')

# Sample Bible verse database (you can expand it with more verses)
bible_verses = {
    "sad": ["Psalm 34:18 - The LORD is close to the brokenhearted and saves those who are crushed in spirit.",
            "Psalm 30:5 - For his anger lasts only a moment, but his favor lasts a lifetime; weeping may stay for the night, but rejoicing comes in the morning."],
    # Add more emotions and corresponding verses as needed
}

def get_emotion(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']
    if sentiment_score <= -0.05:  # Adjust threshold as needed
        return "sad"
    elif sentiment_score >= 0.05:  # Adjust threshold as needed
        return "happy"
    else:
        return "neutral"

def get_bible_verse(emotion):
    if emotion in bible_verses:
        return random.choice(bible_verses[emotion])
    else:
        return "I couldn't find a relevant Bible verse for that emotion."

# Main function
def main():
    user_input = input("Enter your situation: ")
    emotion = get_emotion(user_input)
    verse = get_bible_verse(emotion)
    print("Here is a Bible verse for your situation:")
    print(verse)

if __name__ == "__main__":
    main()
