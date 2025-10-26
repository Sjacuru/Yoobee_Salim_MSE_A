import openai
import os

#GCP project / region
PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "gen-lang-client-0210721034")
LOCATION = os.environ.get("GCP_LOCATION", "australia-southeast1")

#A Gemini API key (set GEMINI_API_KEY)
API_KEY = os.environ.get("GEMINI_API_KEY")

#OpenAI library but point to Google's OpenAI-compatible endpoint
base_url = "https://australia-southeast1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/australia-southeast1/endpoints/openapi"

#Official package's OpenAI client.
client = openai.OpenAI(
    base_url=base_url,
    api_key=(API_KEY),
)

def instructor_chatbot():
    """Command-line AI Itinerary Chatbot."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itenary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
    # fitness_goal = input("What is your fitness goal? (e.g., lose weight, build muscle, endurance, etc.): ")
    
    # Construct prompt
    prompt = f"""
    You are a professional trouist recommender. Provide an itinerary recommendation based on user data.
    
    User Details:
    - days: {days} days
    - destination: {location} city
    - Age: {age} years  
    
    Based on your personal information, 
    Then, give a structured itinerary with a name of the place, address and short description for each 
    day separetly in order with maximom three activities in a day.
    """
    
    try:
        response = client.chat.completions.create(
            model="google/gemini-1.5",
            messages=[
                {"role": "system", "content": "You are a professional itinerary recommender."},
                {"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        
        print("\n My Name is Hadi as AI Itinerary expert:")
        print(response.choices[0].message["content"])
        
    except Exception as e:
        print("Error communicating with Gemini API via Open Ai endpoint", e)

if __name__ == "__main__":
    instructor_chatbot()