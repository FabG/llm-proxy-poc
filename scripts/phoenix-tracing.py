from time import sleep
import phoenix as px
from phoenix.trace.openai import OpenAIInstrumentor
from openai import OpenAI

# quickstart: https://docs.arize.com/phoenix/tracing/llm-traces

# To view traces in Phoenix, you will first have to start a Phoenix server. You can do this by running the following:
session = px.launch_app()
sleep(3)

# Now that phoenix is up and running, run the OpenAI API and debug the application as the traces stream in.
# Initialize OpenAI auto-instrumentation
OpenAIInstrumentor().instrument()

# Initialize an OpenAI client - need to set OPENAI_API_KEY as environment variable
client = OpenAI()


# Once you've executed a sufficient number of queries (or chats) to your application, you can view the details of the UI by refreshing the browser url
message = {
    "role": "user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")
    }

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
    ]

while(message["content"]!="###"):
    conversation.append(message)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou:")
    print()
    conversation.append(completion.choices[0].message)


# You can export a dataframe from the session
# df = px.Client().get_spans_dataframe()

# Note that you can apply a filter if you would like to export only a sub-set of spans
# df = px.Client().get_spans_dataframe('span_kind == "RETRIEVER"')

px.close_app()