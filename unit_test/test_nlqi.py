import unittest
from unittest.mock import patch
from nlqi import create_prompt, call_llm

class TestNLQI(unittest.TestCase):

    def test_create_prompt(self):
        # Test the prompt creation function
        question = "Show me all customers in New York."
        expected_prompt = (
            "Database\n"
            "create table Customers(customerID int, customerName text, City text);\n"
            "Translate this question to SQL:\n"
            "Show me all customers in New York."
        )
        result = create_prompt(question)
        self.assertEqual(result, expected_prompt)

    @patch('openai.OpenAI.chat.completions.create')
    def test_call_llm(self, mock_create):
        # Mock the LLM response
        mock_create.return_value = {
            'choices': [{'message': {'content': 'SELECT * FROM Customers WHERE City="New York";'}}]
        }

        prompt = (
            "Database\n"
            "create table Customers(customerID int, customerName text, City text);\n"
            "Translate this question to SQL:\n"
            "Show me all customers in New York."
        )
        
        # Call the call_llm function with the mock response
        result = call_llm(prompt)
        
        # Ensure the OpenAI API is called with correct parameters
        mock_create.assert_called_once_with(
            model='gpt-4o', messages=[{'role': 'user', 'content': prompt}]
        )
        
        # Check if the result matches the mocked response
        self.assertEqual(result, 'SELECT * FROM Customers WHERE City="New York";')

if __name__ == '__main__':
    unittest.main()
