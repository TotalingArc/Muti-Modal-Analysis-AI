import argparse
import openai

client = openai.OpenAI()

def create_prompt(text):
    """ Create input promt for the langauge model.
    
    Args:
        text: text to classify.
        
    Returns:
        prompt for text classification.
    """
    instructions = 'Is the underlying sentiment positive or negative?'
    formatting = '"Positive" or "Negative"'
    return f'Text:{text}\n{instructions}\nAnswer ({formatting}):'

def call_llm(prompt):
    """ Call LLM with input propmt and return answer.
    
    Args:
        prompt: prompt to send to the language model.
        
    Returns:
        answer generated by LLM.
    """
    messages = [
        {'content':prompt, 'role':'user'}
    ]
    response = client.chat.completions.create(
        messages=messages, model='gpt-4o')
    return response 


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='A text to classify')
    args = parser.parse_args()

    prompt = create_prompt(args.text) 
    answer = call_llm(prompt)
    print(answer)



