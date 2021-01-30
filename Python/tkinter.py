from bs4 import BeautifulSoup
import requests
import shutil
import os

from tkinter import *
from PIL import ImageTk, Image

req = requests.get('https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1223&weekday=tue')
html = req.text

soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select('#comic_view_area > div.wt_viewer > img')


directory = os.path.dirname('./img/')
if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(len(my_titles)):
    img = soup.find("img", {"id": "content_image_" + str(i)})
    img_src = img.get("src")
    img_name = str(i) + "pic"
    r = requests.get(img_src, stream=True, headers={'User-agent': 'Mozilla/5.0'})

    if r.status_code == 200:
        with open('./img/'+img_name+'.png', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


master = Tk()

img_size = Image.open("./img/0pic.png")

canvas_width, canvas_height = img_size.size

canvas_width = int(canvas_width/2)
canvas_height = int(canvas_height/2)

canvas = Canvas(master, width=canvas_width, height=canvas_height)

canvas.pack()

my_images = []
my_image_number = 0

for i in range(0, len(my_titles)):
        img = Image.open("./img/"+str(i)+"pic.png")
        img = img.resize((canvas_width, canvas_height), Image.ANTIALIAS)
        my_images.append(ImageTk.PhotoImage(img))

image_on_canvas = canvas.create_image(0, 0, anchor=NW, image=my_images[my_image_number])

def onButton():
    global my_image_number, my_images, image_on_canvas

    my_image_number += 1
    if( my_image_number == len(my_images)):
        my_image_number = 0
    canvas.itemconfig(image_on_canvas, image = my_images[my_image_number])

button = Button(master, text="다음", command=onButton)
button.pack(side="bottom")

master.mainloop()
