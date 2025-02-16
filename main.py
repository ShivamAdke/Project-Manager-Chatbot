from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Fetch API Key securely from environment variables

def chatbot():
    print("Project Manager Chatbot: Ask me anything about project management! (Type 'exit' to quit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        # OpenAI API Request (Updated for new OpenAI v1.0 API)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI Project Manager assistant. Your role is to provide structured, concise, and practical guidance on project management, including task prioritization, stakeholder communication, risk assessment, and Agile methodologies. Responses should be professional and actionable."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=976,
            stop=["\"Chatbot: \""],
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print("Chatbot:", response.choices[0].message.content.strip())

# Run the chatbot
if __name__ == "__main__":
    chatbot()