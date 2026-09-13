from openai import OpenAI
from openinference.instrumentation.openai import OpenAIInstrumentor
from phoenix.otel import register

# Setup telemetry to send logs to local Phoenix server
tracer_provider = register(endpoint="http://localhost:6006/v1/traces")

# Hook the instrumentor into the OpenAI library
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

# Initialize the client to point to local Ollama
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

# Make a standard generation request using Phi-3
response = client.chat.completions.create(
    model="phi3",
    messages=[{"role": "user", "content": "How much does a junior qa automation engineer make a month?"}],
    temperature=2
)

print(response.choices[0].message.content)



# register(endpoint="http://localhost:6006/v1/traces"): 
#   Configures the OpenTelemetry hook to send all captured data directly to your locally running Arize Phoenix dashboard.

# OpenAIInstrumentor().instrument(...): 
#   The core instrumentation magic. 
#   It automatically wraps every client.chat.completions call you make and extracts token usage, 
#   latency, and prompts without requiring you to change your core application logic.

# base_url="http://localhost:11434/v1": 
#   Instructs the OpenAI framework library to route the API request to your local Ollama setup instead of the internet.

# model="phi3": We are explicitly targeting the lightweight 
# Microsoft Phi-3 model running on our local Ollama instance.