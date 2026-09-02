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

# client = OpenAI(): 
#     Instantiates the OpenAI client, 
#     automatically fetching your API key 
#     from environment variables or .env.

# user_prompt = "...": 
#     Defines the live query string 
#     sent to the AI model.

# client.chat.completions.create(...): 
#     Sends a live network request 
#     to OpenAI using the specified 
#     model and messages.

# response.choices[0].message.content: 
#     Extracts the raw text string 
#     from the live model response.

# test_case = LLMTestCase(...): 
#     Packages the live prompt and 
#     live AI response into a test 
#     case object.

# metric = AnswerRelevancyMetric(threshold=0.7): 
#     Initializes the relevance metric 
#     with a 70% passing threshold.

# assert_test(test_case, [metric]): 
#     Runs DeepEval's evaluation pipeline 
#     on the live generative output.