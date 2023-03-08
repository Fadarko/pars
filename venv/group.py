import time
from saya.VK import Vk


"""param = {
    'count': 1,
    'time_offset': 5,
    'filter': 'unread'
}
"""
g = vk.video.get(owner_id = -190778522)
print(g)
gg = g["response"]
#for key, value in g.items():
#    print(key, ':', value, sep='')
print(gg.keys())
print(gg.items())
x = gg['items']
print(x)

#print(vk.wall.post(message='Hello world!', owner_id = -190778522, from_group = 1))

"""for i in range (100):
    vk.messages.send(message="Пуська", user_id=236827263, random_id='')
    time.sleep(1)
    vk.messages.send(message="Пися", user_id=236827263, random_id='')
    time.sleep(1)
    vk.messages.send(message="<3", user_id=236827263, random_id='')
    time.sleep(3)
    print(i)
"""
#vk.messages.send(attachment = "video-190778522_456239054", user_id=249684299, random_id='')
#video-190778522_456239054
users = vk.users.get(user_ids="beatlegeyorgy")
print(users["response"])


"""
def write_msg(user_id, msg, random):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id': random
    })
"""
'''
try:
    while True:
        response = vk.method('messages.getConversations', param)
        if response['items']:
            item = response['items'][0]
            last_mess = item['last_message']
            random = last_mess['random_id']
            my_id = last_mess['peer_id']
            text = last_mess['text']
            write_msg(my_id, text, random)
        time.sleep(1)
except KeyboardInterrupt:
    print('Keyboard interrupt detected.')
finally:
    print('The program was stopped.')
'''
