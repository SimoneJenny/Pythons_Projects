import time
#import timer

#define new function
def countdown(t):
    #as long as it is avalible
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}: {:02d}'.format(mins, secs)
        print(timer,  end="\r")
        #await 1 sec
        time.sleep(1)
        t -= 1


print('Timer done')

t = input ('Enter time in sec:  ')


countdown(int(t)) 
