# Multimodal Analysis AI - Unit Tests

This repository contains a collection of Python scripts for multimodal analysis AI, including audio transcription, sentiment classification, image question answering, and natural language-to-SQL interface. The unit tests for each script ensure the functionality of the code and simulate the OpenAI API calls using mocks.

## Prerequisites

Ensure you have the following installed:

1. **Python 3.7+**
2. **pip** (Python's package installer)

## Dependencies

Before running the unit tests, you need to install the necessary dependencies. The main dependencies for this project include:
- `openai`: For OpenAI API calls.
- `unittest`: Standard Python library for unit testing.
- `unittest.mock`: Standard Python library for mocking.
- `argparse`: Standard Python library for parsing command-line arguments.

### Installing Dependencies

1. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   ```
   ### Install the required dependencies:

```bash
pip install openai
```
## Install other testing libraries (mocking utilities are part of unittest, which is included in Python standard library).

### Running the Tests
To run the unit tests for each module, simply use the following command:

```bash
python -m unittest discover -s tests
```
This will automatically discover and run all the test files located in the tests directory.

## Individual Tests
If you'd like to run tests for a specific script (e.g., test_audio.py), you can use:

```bash
python -m unittest tests/test_audio.py
```
## Project Structure
- 'audio.py': Script for audio transcription.
- 'sentiment_classification.py': Script for sentiment analysis.
- 'image_qa.py': Script for image question answering.
- 'nlqi.py': Script for natural language to SQL query conversion.
- 'tests/': Directory containing the unit tests for each script.
  - 'test_audio.py': Unit tests for audio.py.
  - 'test_sentiment_classification.py': Unit tests for sentiment_classification.py.
  - 'test_image_qa.py': Unit tests for image_qa.py.
  - 'test_nlqi.py': Unit tests for nlqi.py.

## Example Unit Test Execution
To run the unit tests for the sentiment classification script:

```bash
python -m unittest tests/test_sentiment_classification.py
```
This will run the test cases and print the results.

### Mocking OpenAI API Calls
The OpenAI API calls in the unit tests are mocked using unittest.mock. This ensures that the tests do not make actual API requests, and you can test the behavior of your scripts without needing to connect to the internet or using actual API credits.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

   
   source venv/bin/activate    # For Windows: venv\Scripts\activate
