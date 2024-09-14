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
   source venv/bin/activate    # For Windows: venv\Scripts\activate
