import vk
import random
import getpass
from auth import *
from functions import *

scope_list=['friends', 'photos', 'audio', 'video', 'stories', 'status', 'messages', 'wall', 'offline', 'groups', 'email'
]

key=input("Token(0) or login(1) authentication: ")
if key == '0':
    print ("Enter the token: ")
    vk_token=input('Token: ')

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

if vk_token != None and vk_token != '':
 session=vk.Session(vk_token)
 api = vk.API(session)
 r=api.account.getProfileInfo(v='5.80')
  name=r['first_name']+ '_' + r['last_name']
 f=open(name+'.txt','w')

 city='City: '+r['city']['title']
 country='Country: '+r['country']['title']
 phone='Phone: '+r['phone']
 home_town='Home town: '+r['home_town']
 f.write('Account info\n-------------------------\n' + 'Name: ' + name + '\n' + country + ' | ' + city + ' | ' + home_town + '\n' + phone + '\n-------------------------\n')
 f.close
 print('OK')

 while True:
     print('1- copy friends')
     print('2 - get list of conversations')
     print('3 - send message')
     print('4 - change the password')
     print('5 - delete accpunt')
     key=input('> ')
     if key=='1':
        copyFriends(vk_token)
     elif key=='2':
        list_of_Conversations(vk_token)
     elif key=='3':
        sendMessage(vk_token)
     elif key=='4':
        changePassword(vk_token)
     elif key=='5':
        delete()
        break
