# Multimodal Analysis AI

This repository contains scripts for multimodal analysis AI, including:
- **Audio Transcription**: Transcribes audio files to text.
- **Sentiment Classification**: Classifies the sentiment of given text as positive or negative.
- **Image Question Answering**: Analyzes an image and answers questions about it.
- **Natural Language-to-SQL Interface**: Converts natural language questions into SQL queries.

## Prerequisites

Ensure you have the following installed on your system:

1. **Python 3.7+**
2. **pip** (Python's package installer)

## Project Structure

- `audio.py`: Script for audio transcription using OpenAI's Whisper model.
- `sentiment_classification.py`: Script for sentiment classification using OpenAI's language models.
- `image_qa.py`: Script for answering questions about images.
- `nlqi.py`: Script for converting natural language questions to SQL queries.
- `README.md`: Project description and setup instructions.
- `LICENSE`: License for the project.

## Dependencies

The project relies on the following Python packages:

- `openai`: For accessing OpenAI API (e.g., Whisper for audio transcription, GPT models for text and image analysis).
- `argparse`: For handling command-line arguments (comes with Python standard library).
  
You can install the required dependencies with `pip`:

```bash
pip install openai
```
### Setting Up the Project

## Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```
## Set up a virtual environment (recommended but optional):

```bash
python3 -m venv venv
source venv/bin/activate    # For Windows: venv\Scripts\activate
```
## Install dependencies:

```bash
pip install openai
```
## Running the Scripts
1. Audio Transcription (audio.py)
This script transcribes an audio file using OpenAI’s Whisper model.

## Example Usage:

```bash
python audio.py <path-to-audio-file>
Replace <path-to-audio-file> with the actual path to your audio file.
```
2. Sentiment Classification (sentiment_classification.py)
This script classifies the sentiment of the input text as either positive or negative.

## Example Usage:

```bash
python sentiment_classification.py "This is a great product!"
```
3. Image Question Answering (image_qa.py)
This script answers questions about an image based on its URL.

## Example Usage:

```bash
python image_qa.py <image-url> "What is in the image?"
Replace <image-url> with the actual URL of the image and specify the question you want answered.
```
4. Natural Language-to-SQL Interface (nlqi.py)
This script translates a natural language question into a SQL query.

## Example Usage:

```bash
python nlqi.py "Show me all customers from New York."
```
## OpenAI API Key
All scripts require access to the OpenAI API. To use the OpenAI API, you'll need to set up an API key:

1. Sign up at OpenAI to get your API key.
2. Set the API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key'  # On Linux/MacOS
set OPENAI_API_KEY='your-api-key'     # On Windows
```
Alternatively, you can modify the code to include your API key directly in the client initialization like this:

```python
client = openai.OpenAI(api_key='your-api-key')
```

## Error Handling
Ensure your input data (such as the audio file path, image URL, and question text) is correct. The scripts rely on accurate inputs and proper formatting to function correctly.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
