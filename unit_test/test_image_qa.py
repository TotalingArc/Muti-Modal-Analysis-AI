import unittest
from unittest.mock import patch
from image_qa import analyze_image

class TestImageQA(unittest.TestCase):

    @patch('openai.OpenAI.chat.completions.create')
    def test_analyze_image(self, mock_create):
        # Mock the OpenAI API response
        mock_create.return_value = {
            'choices': [{'message': {'content': 'This is a cat.'}}]
        }
        
        image_url = "http://example.com/image.jpg"
        question = "What is in the image?"
        
        # Call the analyze_image function
        result = analyze_image(image_url, question)
        
        # Ensure the OpenAI API was called with the correct parameters
        mock_create.assert_called_once_with(
            model='gpt-4o',
            messages=[
                {
                    'role': 'user',
                    'content': [
                        {'type': 'text', 'text': question},
                        {'type': 'image_url', 'image_url': {'url': image_url}}
                    ]
                }
            ]
        )
        
        # Check if the result matches the mocked response
        self.assertEqual(result, "This is a cat.")

if __name__ == '__main__':
    unittest.main()
