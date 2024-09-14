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
