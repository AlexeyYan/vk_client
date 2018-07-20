import vk
import time

def copyFriends(api, f_name):
    r=api.friends.get(v='5.80')
    items=r['items']
    f=open(f_name+'.txt', 'a')
    f.write('\nFriends list\n---------------')
    for user in items:
           user_info=api.users.get(user_ids=user, v='5.80')
           first_name=user_info[0]['first_name']
           last_name=user_info[0]['last_name']
           f.write('\n'+str(user)+': '+first_name+' '+last_name)
           print(str(user)+': '+first_name+' '+last_name)
           time.sleep(0.33)
    f.write('\n---------------')
    f.close()

def fff():
 pass
