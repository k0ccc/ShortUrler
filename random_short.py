import random
import string
import webbrowser

def gen_shorturl():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

def short_main():
    i = input('How many tabs?')
    o = 0
    while o < int(i):
        o += 1
        webbrowser.open_new_tab('https://clck.ru/'+gen_shorturl())
if __name__ == "__main__":
    short_main()
