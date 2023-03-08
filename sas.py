import requests, time
from lxml import html

from array import *

f = open('log.txt', 'r')
k = 0
a = array('i', [0, 0])
for line in f:
    a[k] = int(line)
    k = k + 1

k = a[0]
nach = a[1]
print(k)


def upda(page, fo):
    tree = html.fromstring(page.content)
    if fo == 0:
        stek = [x.attrib['src'] for x in tree.cssselect('img') if 'jpg' in x.attrib['src']]
    elif fo == 1:
        stek = [x.attrib['src'] for x in tree.cssselect('img') if 'png' in x.attrib['src']]
    return stek


def reka(fo):
    if fo == 1:
        for i in range(3):
            rek = a.pop(0)
    byI = 0
    for by in a:
        if 'https://www.' in by:
            rek = a.pop(byI)
            '''print("+")'''
            byI = byI - 1
        byI = byI + 1
    return a

for num in range(10000):
    print(str(num) + ' -- ' + str(k))
    url = 'https://chan.sankakucomplex.com/post/show/' + str(num + nach)
    '''url = 'https://chan.sankakucomplex.com/post/show/4420'''
    page = requests.get(url)
    a = upda(page, 0)

    print(url)

    print(a)
    a = reka(0)
    print(a)

    if a == []:
        print("GG")
        print(str(page)[11:14])
        if str(page)[11:14] == '429':
            print("Too many requests")
            time.sleep(20)
            print('Please wait.....')
            a = upda(page, 0)
            print(a)
            a = reka(0)
        else:
            a = upda(page, 1)
            print(a)
            reka(0)
            if a == []:
                print('GG - continue')
                time.sleep(5)
                continue

    '''print(a)'''

    '''a.remove('https://www.sankakucomplex.com/wp-content/uploads/2020/03/sony-playstation-5-backward-compatibility-overwhelming-majority-Cover-100x100.jpg')
    a.remove('https://www.sankakucomplex.com/wp-content/uploads/2020/03/gamestop-coronavirus-100x100.jpg')
    a.remove('https://www.sankakucomplex.com/wp-content/uploads/2020/03/Narita-Airport-Worker-Contaminates-Room-With-Coronavirus-Reagent-100x100.jpg')'''
    '''print(a)'''
    max = 0
    maK = 0
    for ma in a:
        if len(ma) > max:
            max = len(ma)
            maI = maK
        maK = maK + 1
    b = a.pop(maI)
    print(b)
    a.clear()
    if len(b) > 100:
        with open('test/' + str(k) + '.jpg', 'wb') as f:
            f.write(requests.get('https:' + b).content)
            k = k + 1
    else:
        a = upda(page, 1)
        print(a)
        reka(1)
        print(a)
        if (a == []):
            print('GG - continue')
            time.sleep(4)
            continue
        max = 0
        maK = 0
        for ma in a:
            if len(ma) > max:
                max = len(ma)
                maI = maK
            maK = maK + 1
        b = a.pop(maI)
        print(b)
        a.clear()
        if len(b) > 100:
            with open('test/' + str(k) + '.png', 'wb') as f:
                f.write(requests.get('https:' + b).content)
                k = k + 1
        else:
            f = open('nojpg.txt', 'a')
            f.write('https://chan.sankakucomplex.com/post/show/' + str(num + nach) + '\n')


    f = open('log.txt', 'w')
    f.write(str(k) + '\n')
    f.write(str(num + nach) + '\n')


    time.sleep(4)
'''
for pic_link in b:
    print(pic_link)
    with open('test/' + str(k) + '.jpg', 'wb') as f:
        f.write(requests.get('https:' + pic_link).content)
'''
''' pic_link.split('/')[-1] +'''


'''
//cs.sankakucomplex.com/data/sample/6c/9e/sample-6c9ecf72a486700ffbf450990a7969b9.jpg?e=1584974794&m=4hDkQ2VYEdEk9J8tErbHig
//cs.sankakucomplex.com/data/preview/bf/36/bf360b4e5c084777dcc25d68b0a7ec5a.jpg
//cs.sankakucomplex.com/data/sample/bf/36/sample-bf360b4e5c084777dcc25d68b0a7ec5a.jpg?e=1584974957&m=0cGLEEpFvEc728K5EsBjsA
'''