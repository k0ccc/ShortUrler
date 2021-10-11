import random
import string
import webbrowser
import requests


def gen_shorturl(number):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(number))

# Допилить кнопку назад, сделать что-то с шортюрл, и oomoney
def site_get(site, url_aft_site):
    i = int(input('How many tabs? '))
    o = 0
    while True:
        while o < i:
            o += 1
            url = site+'/'+gen_shorturl(url_aft_site)
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    webbrowser.open_new_tab(url)
                    print(url + ' существует')

                # elif site in url:
                #     print(url + ' ссылаеться сам на себя')
                else:
                    print(url + ' не существует')

            except:
                print("Чтот-то страшное: ", url)
        print("DONE")
        repeat = int(input("Закончить = 0, Любое другое кол-во вкладок "))
        if repeat == 0:
            break
        else:
            i = repeat
            o=0

URLs = {1 :"https://www.clck.ru",
        2 :"https://www.shorturl.at"
        }


aft_site = {"https://www.clck.ru"       :5,
            "https://www.shorturl.at"   :5
        }

def main():
    u = 0
    for url in URLs.values():
        u +=1
        print(u,url[12:])
    input_number = int(input())
    for w,i in URLs.items():
        for o in aft_site.keys():
            if o in i and input_number == w:
                site_get(URLs[w],aft_site[i])

if __name__ == "__main__":
    main()
