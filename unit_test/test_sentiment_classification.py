import unittest
from unittest.mock import patch
from sentiment_classification import create_prompt, call_llm

class TestSentimentClassification(unittest.TestCase):

    def test_create_prompt(self):
        # Test the prompt creation function
        text = "I love this product!"
        expected_prompt = (
            'Text:I love this product!\n'
            'Is the underlying sentiment positive or negative?\n'
            'Answer ("Positive" or "Negative"):'
        )
        result = create_prompt(text)
        self.assertEqual(result, expected_prompt)

    @patch('openai.OpenAI.chat.completions.create')
    def test_call_llm(self, mock_create):
        # Mock the LLM response
        mock_create.return_value = {
            'choices': [{'message': {'content': 'Positive'}}]
        }
        
        prompt = "Test prompt"
        
        # Call the function with the mocked response
        result = call_llm(prompt)
        
        # Ensure the OpenAI API is called with correct arguments
        mock_create.assert_called_once_with(
            messages=[{'content': prompt, 'role': 'user'}],
            model='gpt-4o'
        )
        
        # Check if the result matches the mocked response
        self.assertEqual(result, {'choices': [{'message': {'content': 'Positive'}}]})

if __name__ == '__main__':
    unittest.main()
