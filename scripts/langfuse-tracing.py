from langfuse.decorators import observe
from langfuse.openai import openai  # OpenAI integration

# Use a model from OpenAI
model_name="gpt-3.5-turbo"

@observe()
def chat_with_openai(prompt):
    """
    Sends the prompt to OpenAI API using the chat interface and gets the model's response.
    """
    message = {
        'role': 'user',
        'content': prompt
    }

    response = openai.chat.completions.create(
        model=model_name,
        messages=[message]
    )

    # Extract the chatbot's message from the response. Take the last one as the chatbot's reply.
    chatbot_response = response.choices[0].message.content
    return chatbot_response.strip()

@observe()
def main():
    """
    Main interaction loop for the chatbot.
    """
    print("Welcome to Chatbot powered by gpt3.5 and Langfuse Tracing! Type '###' to exit.")

    user_input = ""
    while user_input.lower() != "###":
        user_input = input("You: ")

        if user_input.lower() != "###":
            response = chat_with_openai(user_input)  # Pass user_input as an argument
            print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
