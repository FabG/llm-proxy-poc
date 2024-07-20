from time import sleep
import phoenix as px
from phoenix.trace.openai import OpenAIInstrumentor
from openai import OpenAI

# quickstart: https://docs.arize.com/phoenix/tracing/llm-traces

# To view traces in Phoenix, you will first have to start a Phoenix server. You can do this by running the following:
session = px.launch_app()

sleep(5)
print("Sending request to GPT 3.5... ")
# Now that phoenix is up and running, run the OpenAI API and debug the application as the traces stream in.

# Initialize OpenAI auto-instrumentation
OpenAIInstrumentor().instrument()

# Initialize an OpenAI client - need to set OPENAI_API_KEY as environment variable
client = OpenAI()

# Define a conversation with a user message
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, can you help me with something?"}
]

# Generate a response from the assistant
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation,
)

print("GPT 3.5 Response: " + response.choices[0].message.content)

# Extract and print the assistant's reply
# The traces will be available in the Phoenix App for the above messsages
assistant_reply = response.choices[0].message.content

# Once you've executed a sufficient number of queries (or chats) to your application, you can view the details of the UI by refreshing the browser url

# View the traces in the Phoenix UI
#px.active_session().url


# You can export a dataframe from the session
# df = px.Client().get_spans_dataframe()

# print("DF : " + df.to_string())

# Note that you can apply a filter if you would like to export only a sub-set of spans
# df = px.Client().get_spans_dataframe('span_kind == "RETRIEVER"')

