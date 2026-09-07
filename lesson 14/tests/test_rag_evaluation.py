from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, ContextualPrecisionMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from deepeval.models import GPTModel

def test_basic_relevance():
    local_judge = GPTModel(
        model="gpt-4o"
    )

    test_case = LLMTestCase(
        input="how do i reset my password?",
        actual_output="You can reset your password by clicking on 'login' on the login screen.",
        retrieval_context=["according to the company login guidebook whenever i need to change my password i need to click on login first"],
        expected_output="To reset your password, you must call the IT support hotline. Never click the login button."
    )

    context_metric = ContextualPrecisionMetric(threshold=0.7, model=local_judge)
    faithfulness_metric = FaithfulnessMetric(threshold=0.7, model=local_judge)
    relevance_metric = AnswerRelevancyMetric(threshold=0.7, model=local_judge)    
    
    assert_test(test_case, [context_metric, faithfulness_metric, relevance_metric])


# retrieval_context=[...]: 
# A list of text documents fetched from the company database that 
# act as the reference source for the RAG pipeline.

# ContextualPrecisionMetric(...): 
# Evaluates whether the retriever fetched documents that actually 
# contain the necessary information to answer the user's input.

# FaithfulnessMetric(...): 
# Evaluates whether the AI's actual output is strictly derived 
# from the retrieved documents, effectively catching hallucinations.

# AnswerRelevancyMetric(...): 
# Measures whether the final response directly addresses the user's original query.

# assert_test(test_case, [...]): 
# Runs all three RAG Triad metrics sequentially against the single test case.