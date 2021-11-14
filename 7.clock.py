import time
from datetime import datetime

def counter_clock():
    hours, minutes, seconds = 0, 0, 0
    
    while hours < 24:
        while minutes < 60:
            while seconds < 60:
                print(str(hours).zfill(2),":",str(minutes).zfill(2),':',str(seconds).zfill(2))
                seconds += 1
                time.sleep(1)
            minutes += 1
            seconds = 0
        hours += 1
        minutes = 0
        
def internal_clock():
    while True:
        now = datetime.now()
        print(f'{now.hour}:{now.minute}:{now.second}')
        time.sleep(1)

if __name__ == '__main__':
    counter_clock()