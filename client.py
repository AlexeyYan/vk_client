import vk
import random
import getpass
from auth import *
from functions import *

scope_list=['friends', 'photos', 'audio', 'video', 'stories', 'status', 'messages', 'wall', 'offline', 'groups', 'email']

key=input("Token(0) or login(1) authentication: ")
if key == '0':
    print ("Enter the token: ")
    input(token)
    session=vk.Session(vk_token)
    api = vk.API(session)

elif key =='1':
    email=input("Email or phone: ")
    pswd=getpass.getpass("Password: ")
    two_factor_auth_req=input("Do you have two factor auth(y/n): ")
    if two_factor_auth_req in ['y','n']:
        if two_factor_auth_req=='y': two_factor_auth=True
        else: two_factor_auth=False
    connect=VKAuth(scope_list, '5970100', '5.80', two_factor_auth=two_factor_auth, email=email, pswd=pswd)
    connect.auth()
    vk_token=connect.get_token()
    session=vk.Session(vk_token)
    api = vk.API(session)
while true:
    print('1- copy friends')
    print('2 - get list of conversations')
    print('3 - send message')
    print('4 - change the password')
    print('5 - delete accpunt')
    key=input('> ')

