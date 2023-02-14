import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from commander.commander import Commander


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
token = "vk1.a.n8dpkGYRpSla9MQ2omdBzEj1SbQ1Pnf79MRn9w5IsT6CggCyyiYM8la5RGyAq8haFc8jAgpyDgkY68nGaaLHp4r2XIsesiKj_Frvyl0WA2Cf43FRs3-07g5adbAlfBk5oCu2wU0nx7Tdx82cEAWAlJwE6rY6HfRYTi2O72iy9qyVZjymthb2ZyWYLvdMK_txssYdNttSZgiwnzmZzVTtWQ"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Commander
commander = Commander()

print("Бот запущен")
# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай, хочешь перейти по ссылке? , https://arizonarp.logsparser.info/")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            elif request.split()[0] == "command":
                write_msg(event.user_id, commander.do(request[8::]))
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")

