import requests
import time
import os
import concurrent.futures

img_urls = [
    "https://images.unsplash.com/photo-1534143826428-81fc61582afd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=588&q=80",
    "https://images.unsplash.com/photo-1494869042583-f6c911f04b4c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1514285490982-4130e9aefedb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
    "https://images.unsplash.com/photo-1541913299-273fd84d10c4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1489&q=80",
    "https://images.unsplash.com/photo-1515446134809-993c501ca304?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1567523976928-21c64032160f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1225&q=80",
    "https://images.unsplash.com/photo-1500042600524-37ecb686c775?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1529503257657-e0ce256b46d1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
    "https://images.unsplash.com/photo-1532377416656-e35d0e574765?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1267&q=80",
    "https://images.unsplash.com/photo-1529180979161-06b8b6d6f2be?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1351&q=80",
    "https://images.unsplash.com/photo-1579470696004-0365461b9131?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1618485476424-7dc9cd512c08?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80",
    "https://images.unsplash.com/photo-1611095790691-ff1be3430b22?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1351&q=80",
    "https://images.unsplash.com/photo-1618488628800-e833a05dcd9e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80",

]

t1 = time.perf_counter()


def download_image(url):
    img_bytes = requests.get(url=url).content
    img_name = url.split('/')[3][:25]
    img_name = f"{img_name}.jpg"
    path = os.path.dirname(__file__)+'\\ax\\'+img_name
    with open(path, 'wb')as file:
        file.write(img_bytes)
        print(F"file {img_name} is downloaded")


with concurrent.futures.ThreadPoolExecutor() as executer:
    result = executer.map(download_image, img_urls)

t2 = time.perf_counter()


print(f"all file has been downloaded in {round(t2-t1,2)} second(S)")
