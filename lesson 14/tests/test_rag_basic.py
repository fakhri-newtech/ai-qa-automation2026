from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval.models import GPTModel

def test_basic_relevance():
    openai_judge = GPTModel(
        model="gpt-4o"
    )

    test_case = LLMTestCase(
        input="how do i reset my password?",
        actual_output="You can reset your password by clicking on 'Forgot Password' on the login screen."
    )

    metric = AnswerRelevancyMetric(threshold=0.7, model=openai_judge)
    assert_test(test_case, [metric])

# local_judge = OllamaModel(...): 
# Configures DeepEval to route grading requests to your local Ollama instance instead
# of the cloud, saving API costs during class.

# base_url="http://localhost:11434": 
# The default local network address where Ollama listens for API requests.

# LLMTestCase(...): 
# Packages the user query (input) and the system response (actual_output) 
# into a standardized test object.

# AnswerRelevancyMetric(...): 
# Initializes the relevance metric with a 70% passing threshold and 
# explicitly overrides the default OpenAI judge with our local model.

# assert_test(test_case, [metric]): 
# Executes DeepEval's evaluation pipeline locally on your machine 
# without requiring an internet connection.