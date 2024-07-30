from time import sleep
import phoenix as px
from phoenix.trace.openai import OpenAIInstrumentor
from openai import OpenAI

# start a Phoenix server (and UI)
session = px.launch_app()
sleep(3)

# Initialize OpenAI auto-instrumentation
OpenAIInstrumentor().instrument()

# Initialize an OpenAI client - need to set OPENAI_API_KEY as environment variable
client = OpenAI()


# Execute a  number of queries (or chats) then can view the details in the UI
message = {
    "role": "user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")
    }

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
    ]

while message["content"]!= "###":
    conversation.append(message)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou:")
    print()
    conversation.append(completion.choices[0].message)


px.close_app()