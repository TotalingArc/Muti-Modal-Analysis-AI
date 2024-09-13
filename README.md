# Multi-Modal-Analysis-AI

This project is a Python-based AI tool for analyzing both text and images using OpenAI’s GPT-4 model. It supports text-to-SQL translations, text sentiment analysis, and image-based question-answering.

# Features:
Text-to-SQL Translation: Converts natural language questions into SQL queries.
Sentiment Classification: Classifies the sentiment of input text as positive or negative.
Image Analysis: Answers questions about images by processing image URLs and text-based questions.
Multi-Modal Capability: Combines textual and visual inputs for more comprehensive AI analysis.

# Prerequisites
Python 3.x
OpenAI 
Python API: openai

## Install the required dependencies:
```bash
pip install openai argparse
```

## Getting Started

## 1. Set up OpenAI API Key
To authenticate the API, you’ll need to configure your OpenAI API key. Add this in the code where you see openai.OpenAI():
```python
openai.api_key = 'your-api-key'
```

## 2. Run the Script
The script supports three types of tasks:

Text-to-SQL Translation
Sentiment Classification
Image Analysis
Text-to-SQL Translation:
This function translates a natural language question into an SQL query. To run the translation:
```bash
python text_to_sql.py "<natural_language_question>"
```

## Sentiment Classification:
This function determines whether the sentiment of the input text is positive or negative. To classify sentiment:
```bash
python sentiment_analysis.py "<text_to_classify>"
```

## Image Analysis:
This function answers questions about images provided via URLs. To analyze an image:

```bash
python image_analysis.py "<image_url>" "<question>"
```

## Code Overview

## 1. Text-to-SQL Translation
The create_prompt function generates a prompt for converting a natural language question into SQL, and the call_llm function sends this prompt to the OpenAI API for translation.
```python
def create_prompt(question):
    """Creates a prompt for text-to-SQL translation."""
    # SQL prompt generation logic here
```
## 2. Sentiment Classification
The create_prompt function in the sentiment classification code creates a prompt that queries the sentiment of a given text. The LLM is called using the call_llm function to return the classification.
```python
def create_prompt(text):
    """Creates input prompt for sentiment analysis."""
    # Sentiment classification prompt generation logic
```

## 3. Image Analysis
The analyze_image function takes an image URL and a question as input. It sends both to the OpenAI API and retrieves an answer about the image.
```python
def analyze_image(image_url, question):
    """Answer question about input image."""
    # Multi-modal input handling and LLM call logic
```

## Example Usage
Text-to-SQL Example:
```bash
python text_to_sql.py "How many customers are in the city of New York?"
```
Expected Output:
```sql
SELECT COUNT(*) FROM Customers WHERE City = 'New York';
```

##Sentiment_Classification Example:
```bash
python sentiment_analysis.py "I love this product!"
```
Expected Output:
```mathematica
Positive
```

## Image Analysis Example:
```bash
python image_analysis.py "https://example.com/image.jpg" "What objects are in this image?"
```
## Expected Output:
```css
This image contains a car and a person.
```

## Future Improvements
Error Handling: Add better exception handling for invalid image URLs or poorly formatted text inputs.
Extended Model Integration: Experiment with other models to enhance the text-to-SQL accuracy and multi-modal processing.
Additional Analysis Types: Expand the project to include other forms of analysis like video, audio, or 3D data.

## License
This project is licensed under the MIT License.
