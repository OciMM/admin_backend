import random
import string
import vk_api

from django.core.mail import send_mail

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

TOKEN_GROUP = "vk1.a.V10pA0TyYlsU2SDGQZN2JxF5gl19-ynnhYVO45H3AeI2_znCp-jqxGiOqWxu42SeQkAT-bsz4ExcTsm3i2IZeDZ1_hUP6KEMGRP0aiwSgEyAqp5hE41fCLxp6uY16fmLpN14FDIMKDtR3xU1KDy7R5r2Zx1rcUUvQ9NBGXV9f67Le-y75q-llKKC-Wvj8x7fmzNz2oVy_wI9JFzvif85zg"
TOKEN_USER = "vk1.a.t-d2Tk8DIPubLRyIkQ0_ka-TCU3E_e70vrQDzkXj6PnSKnDGjF9xnuIn6T4FpPkgULBZ4_r63uyDzV5vJxBE1oSDaxhyjRSPTAl9Ju3006jl1zWQvzcSBbHgU-CQ4aGpb3WMpzKqgyFwhVTjOh__kwb68LJymgDLg--iOcKaC884Z4hZANktZr4pdDNP-a7X4G14OijHxACzGqvuS4CiYA"
# создание UID
def create_user_id():
    # Задаем длину строки
    length = 10

    # Создаем строку из случайных букв и цифр
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    return random_string

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


