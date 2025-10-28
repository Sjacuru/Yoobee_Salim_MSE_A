import os
from google.genai import client as genai_client
from google.genai import types as genai_types
from google import genai

# API_KEY = ""
API_KEY = os.environ.get("GEMINI_API_KEY") or "AIzaSyDIiqaYvnvVzn-2R5g8z1kTy9TWp0iP6Mg"

if not API_KEY:
    raise RuntimeError("Set GEMINI_API_KEY environment variable with your Gemini API key.")

# client
client = genai.Client(api_key=API_KEY) 
    
def instructor_chatbot():
    """Command-line AI Itinerary Chatbot using Gemini (google-genai)."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itinerary advice.\n")
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")

    prompt = f"""
---Role---
You are a professional tourist recommender, especialized in provide itineraries recommendation
based on user data.

---Input data---
User Details:
- days: {days} days
- destination: {location} city
- Age: {age} years

---Instructions---
Give a structured itinerary with the place`s name, address and a short description for each day 
separately in order, with a maximum of ***TWO*** activities per day, considering visits, if available,
to the ***main and well known activities of the city***. Ensure there is a balance between 
guided tours and free time for exploration. Each day should have suggestions for breakfast, 
lunch, and dinner, with brief descriptions of each activity and restaurant.

explore the city's highlights and vibrant atmosphere

---Context---
Consider the traveller has never been to chosen city before and wants to experience both the well-known and hidden
gems of the city. They are particularly interested in the history of the city. They are comfortable using public 
transport and enjoy walking tours.

---Negative Prompting---
Do not include MORE THAN ONE ATCIVITY IN THE FIRST AND LAST DAYS that are primarily for children or family, avoid overly touristy restaurants, and exclude
any activities that require extensive travel outside of the chosen city.
"""

    try:
        # Create a chat completion (model names vary; change to the Gemini model you have access to)
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # "gemini-1.5-pro" "gemini-1.5" "gemini-2.0-flash-001" "gemini-1.5-flash" "gemini-2.0-flash"(Gemini API for New Zealand) "gemini-2.0-flash-thinking-exp" 
            contents=prompt,
            config=genai_types.GenerateContentConfig(
                temperature=0.2,                # 0..1 typical — lower = more deterministic
                top_p=0.95,                     # nucleus sampling: 0 to 1
                top_k=30,                       # More coherent: 10 - 500 More diverse and creative 
                max_output_tokens=4000,         # how long the generation can be
                stop_sequences=["\n\nHuman:"],  # generation will stop when any of these appear
                candidate_count=1,              # ask for multiple candidate responses if you want
                presence_penalty=0.0,           # optional - discourage/encourage new tokens
                frequency_penalty=0.0           # optional - penalize repetition
    )
        )

        text = response.text
        print("\nMy Name is Hadi as AI Itinerary expert:")
        print(text)

    except Exception as e:
        print("Error communicating with Gemini API:", e)

if __name__ == "__main__":
    instructor_chatbot()
