from random import choice
from tkn_file import TOKEN
import telebot
from telebot import types


API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)

CARD_RANKS = [
    '2', '3', '4', '5', '6',
    '7', '8', '9', '10',
    'J', 'D', 'K', 'A', 
    ]

CARD_SUITS = ['♥','♦','♣','♠']

card_ranks = choice(CARD_RANKS)
card_suits = choice(CARD_SUITS)
secret_card = card_ranks + card_suits

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    red_btn = types.InlineKeyboardButton('🟥', callback_data='R')
    black_btn = types.InlineKeyboardButton('⬛️', callback_data='B')

    bot.send_message(
        message.chat.id, 
        'Приветствую в игре "Угадай Карту!".\n'
        f'{card_ranks + card_suits}',
        reply_markup = types.InlineKeyboardMarkup().add(
            red_btn, black_btn
        )
    )


@bot.callback_query_handler(func=lambda call: call.data in ['R','B'])
def handle_user_callback(call):
    card_ranks = choice(CARD_RANKS)
    card_suits = choice(CARD_SUITS)
    
    if call.data == 'R' and card_suits in ['♥','♦'] or call.data == 'B' and card_suits in ['♣','♠']:
        msg = 'Отлично! Ты угадал!'

    else:
        msg = 'ГГ... Некст тайм'
        

    bot.send_message(
            call.message.chat.id,
            f'{msg}\n'
            f'Загаданная карта - {card_ranks + card_suits}'
        )

    send_welcome(call.message)

bot.infinity_polling()







# print('Приветствую в игре "Угадай масть карты"!')
# user_inp = (input('Введите "К" (красный) или "Ч" (черный): '))
# print('Вы ввели: ', user_inp)


#3


#4


# #6
# if user_inp == 'К' and card_suits in ['♥','♦'] or user_inp == 'Ч' and card_suits in ['♣','♠']:
#     print('Отлично! Ты угадал!')

# else:
#     print('ГГ... Некст тайм')
# print('Загаданная карта -', secret_card)


