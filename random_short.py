import random
import string
import webbrowser
import requests


def gen_shorturl():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

def short_main():
    i = input('How many tabs? ')
    o = 0
    # try:
    while o < int(i):
        o += 1
        url = 'https://clck.ru/'+gen_shorturl()
        response = requests.get(url)
        if response.status_code == 200:
            webbrowser.open_new_tab(url)
            print(url + ' существует')
        else:
            print(url + ' не существует')
    # except:
    #     pass
    print("DONE")
if __name__ == "__main__":
    short_main()
