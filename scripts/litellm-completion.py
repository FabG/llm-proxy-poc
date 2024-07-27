from litellm import completion

# Note -  Environment variables should be set, namely:
# Azure: OPENAI_API_KEY
# AWS: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and AWS_REGION_NAME
# Anthropic: ANTHROPIC_API_KEY

messages = [{ "content": "what does JPMC stand for?", "role": "user"}]

# models
openai_model="gpt-3.5-turbo"
bedrock_model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0"
anthropic_model="claude-2"

# openai call
print('Call to OpenAI chatGPT with model:' + openai_model)
response_azure = completion(model=openai_model, messages=messages)
print(response_azure)

# anthropic Claude-2
print('\nCall to Anthropic with model:' + anthropic_model)
response_anthropic = completion(model=anthropic_model, messages=messages)
print(response_anthropic)

# bedrock call
#print('\nCall to AWS Bedrock with model:' + bedrock_model)
#response_aws = completion(model=bedrock_model, messages=messages)
#print(response_aws)

