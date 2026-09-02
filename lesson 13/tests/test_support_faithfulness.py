from deepeval import assert_test
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase


def test_support_faithfulness():
    test_case = LLMTestCase(
        input="Is shipping free?",
        actual_output="Standard shipping is free for orders over $50.",
        retrieval_context=["Orders exceeding $50 qualify for complimentary standard shipping."]
    )
    metric = FaithfulnessMetric(threshold=0.8)
    assert_test(test_case, [metric])
# def test_support_faithfulness(): 
#     Standard Pytest 
#     test function for 
#     checking model faithfulness.

# test_case = LLMTestCase(...): 
#     Combines prompt, output, 
#     and context into a test 
#     case structure.

# retrieval_context=[...]: 
#     Source documents provided 
#     to the model to help 
#     detect hallucinations.

# metric = FaithfulnessMetric(threshold=0.8): 
#     Initializes the faithfulness 
#     metric with an 80% 
#     passing threshold.

# assert_test(test_case, [metric]): 
#     Evaluates whether the output 
#     is strictly derived from context.