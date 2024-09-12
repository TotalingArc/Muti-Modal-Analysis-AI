import argparse
import openai

client = openai.OpenAI()

def analyze_image(image_url, question):
    """ Answer question about input image.
    
    Args:
        image_url: URL of image to analyze.
        question: obtain answer to this question..
        
    Returns:
        Answer to input question. 
    """
    message = {'role' : 'user', 'content':[
        {'type' : 'text', 'text':question},
         {'type':'image_url', 'image_url':{'url':image_url}}
         ]}
    messages = [message]
    reply = client.chat.completions.create(
        model='gpt-4o',
        messages=messages
    )
    return reply.choices[0].message.content

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('image_url', type=str, help='image URL')
    parser.add_argument('question', type=str, help='Question about image')
    args = parser.parse_args()

    answer = analyze_image(args.image_url, args.question)
    print(answer)
