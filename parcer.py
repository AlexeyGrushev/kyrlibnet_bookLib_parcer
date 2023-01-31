import urllib.request
from selenium import webdriver
# Функция загрузки файлов по ссылке
def download(bookName,url):
    print("Начинаю скачивание...")
    destination = f'downloadData/{bookName}'
    urllib.request.urlretrieve(url, destination)
    print("Скачивание завершено")

# Функция по определению языка
def lang(url):
    try:
        driver = webdriver.Chrome()
        driver.get(str(url))
        p = driver.find_elements("tag name","p") # поиск <p/> элементов
        h = driver.find_elements("tag name","a") # поиск <href/>
        for i in p:
            if i.text == "Кыргызский":
                print(p[15].text)
                for j in h:
                    if 'download&nadd' in j.get_attribute('href').split('='):
                        for n in p:
                            if 'pdf' in n.text.split('.') or 'djvu' in n.text.split('.'):
                                download(n.text,j.get_attribute('href'))
                                break
                        break
    except: print("Не удалось скачать")
    return

link = str(input("Введите ссылку на коллекцию: "))
driver = webdriver.Chrome() # ЯДРО БРАУЗЕРА, НА КОТОРОМ БУДЕТ ОТКРЫВАТЬСЯ САЙТ
driver.get(link)
p = driver.find_elements("tag name", 'a')

p.pop(len(p)-1)

for i in range(7,(len(p))):
    lang(p[i].get_attribute("href"))

print("Выполнено")