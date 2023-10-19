import openai
import os
openai.api_key = os.environ['KEY_API']

SENT = f"""raiva, alegria, medo, nojo, tristeza, satisfação, confiança, amor"""

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_sentiment(music):

    prompt = f"""
    De acordo com a lista com os sentimentos {SENT} \
    Me retorne um html indicando um sentimento dessa lista para cada trecho da música abaixo. \
    O html terá apenas tags <p>. Cada trecho vai ser uma tag <p> e o id da tag será o sentimento. \

    {music} \
    """

    response = get_completion(prompt)
    return {"html": response}
