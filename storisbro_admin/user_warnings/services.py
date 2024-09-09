import random
import string
import vk_api
import time
import requests

from django.core.mail import send_mail

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

TOKEN_GROUP = "Токен группы"
TOKEN_USER = "Токен пользователя"


# получение id пользователя в цифрах
def get_int_id_vk(user_id):
    session = vk_api.VkApi(token=TOKEN_USER)
    vk = session.get_api()

    result = vk.users.get(user_ids=user_id)
    return result[0]['id']


# отправка сообщения в вк
def send_message_vk(user_id, message_text):
    session = vk_api.VkApi(token=TOKEN_GROUP)
    vk = session.get_api()

    int_id = get_int_id_vk(user_id=user_id)

    random_id = random.getrandbits(31)

    vk.messages.send(user_id=int_id, message=message_text, random_id=random_id)


# отправка сообщений через почту
def send_message_email(email, text):
    email_receiver = email
    subject = 'Предупреждение'
    message = text
    email_sender = 'bekasovmaks20@gmail.com'
    
    send_mail(subject, message, email_sender, [email_receiver])


# Отправка сообщений на все почты:
def get_email_from_project1():
        url = f'http://31.129.96.225/api/notification/send-notification/get_users/'
        response = requests.get(url)
        email_list = []
        if response.status_code == 200:
            response_list = response.json()
            for i in response_list:
                email_list.append(i['email'])
            return email_list
        else:
            return None


def send_message_for_all_email(text):
    subject = 'Предупреждение'
    message = text
    email_sender = 'bekasovmaks20@gmail.com'

    list_email = get_email_from_project1()

    for email_receiver in list_email:  
        send_mail(subject, message, email_sender, [email_receiver])

# send_message_for_all_email("Привет!")
# print(get_email_from_project1())
 
# # Отправка сообщений для всех в VK
# def get_group_members(group_id):
#     session = vk_api.VkApi(token=TOKEN_GROUP)
#     vk = session.get_api()

#     members = []
#     offset = 0

#     while True:
#         response = vk.groups.getMembers(group_id=group_id, offset=offset)
#         members.extend(response['items'])

#         if offset + 1000 >= response['count']:
#             break

#         offset += 1000
#         time.sleep(0.34)  # Ограничение на количество запросов в секунду

#     return members

# def send_message_to_all_members(group_id, message_text):
#     members = get_group_members(group_id)
#     for member_id in members:
#         send_message_vk(user_id=member_id, message_text=message_text)
#         time.sleep(0.34)  # Ограничение на количество запросов в секунду

# # Использование:
# message_text = "Cообщение всем подписчикам группы"
# send_message_to_all_members("club224176416", message_text)