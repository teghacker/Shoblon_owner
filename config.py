from app.db.base import *

token="8362668115:AAEjOsvwxCUFi4UrLCEZL0xPgojfZp2Xt0Q"
admin=set()

def admin_add1():
    for i in Read_Admins():
        admin.add(i[1])

admin_add1()

def admin_add2():
    admin.clear()
    for i in Read_Admins():
        admin.add(i[1])

CHANNELS = []

def channels_view():
    CHANNELS.clear()
    for i in Read_Channels():
        CHANNELS.append(f'@{i[1]}')

channels_view()