import requests

def send_message_tg(message):
    bot_token = "6450537541:AAHpVFkCt11KBHLd7WzOTJY54UF3omcZQ-o"
    chat_id =1564944477

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?text={message}&chat_id={chat_id}'

    requests.get(url)