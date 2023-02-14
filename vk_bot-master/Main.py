import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# --
from commander.commander import Commander
from vk_bot import VkBot
# --


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
token = "vk1.a.n8dpkGYRpSla9MQ2omdBzEj1SbQ1Pnf79MRn9w5IsT6CggCyyiYM8la5RGyAq8haFc8jAgpyDgkY68nGaaLHp4r2XIsesiKj_Frvyl0WA2Cf43FRs3-07g5adbAlfBk5oCu2wU0nx7Tdx82cEAWAlJwE6rY6HfRYTi2O72iy9qyVZjymthb2ZyWYLvdMK_txssYdNttSZgiwnzmZzVTtWQ"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

commander = Commander()
print("Сервер запущен")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            print(f'New message from {event.user_id}', end='')

            bot = VkBot(event.user_id)

            if event.text[0] == "/":
                write_msg(event.user_id, commander.do(event.text[1::]))
            else:
                write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
            print("-------------------")
