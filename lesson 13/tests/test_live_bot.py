from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from openai import OpenAI


def test_live_support_bot():
    # 1. Call your live LLM client
    client = OpenAI()
    user_prompt = "How do I reset my password?"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_prompt}]
    )
    ai_response = response.choices[0].message.content

    # 2. Feed the live output into DeepEval
    test_case = LLMTestCase(
        input=user_prompt,
        actual_output=ai_response
    )
    metric = AnswerRelevancyMetric(threshold=0.7)
    assert_test(test_case, [metric])


#     client = OpenAI(): Instantiates the OpenAI API client (automatically fetches your API key from the local environment or .env configuration).

# user_prompt = "...": Defines the live query string to be sent to the model.

# client.chat.completions.create(...): Sends a live network request to OpenAI's API using the specified model (gpt-4o) and input messages.

# response.choices[0].message.content: Extracts the raw text string returned by the live model response, capturing dynamic generative output.

# Dynamic wiring: Feeds the live model output directly into LLMTestCase so that every time Pytest runs, it evaluates real-time AI behavior instead of hardcoded strings.