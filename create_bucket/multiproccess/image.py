import time
from PIL import Image, ImageFilter
import os
import concurrent.futures

PATH = "D:\\job\Code\\create_bucket\\ax\\"


def resize_image(path):
    size = (200, 200)
    img_byte = Image.open(path)
    # img = img_byte.filter(ImageFilter.BoxBlur(15))


    img=img_byte.convert('1')
    img.thumbnail(size)

    save_path = PATH + '\\' + 'thumbnail\\' + path.split('\\')[5]
    img.save(save_path)
    print(F"image {path} was saved successfully")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('process startted')
    t1 = time.perf_counter()
    for img_dir, _, image_name in os.walk(PATH):
        image_list = [img_dir + x for x in image_name]

        break
    with concurrent.futures.ThreadPoolExecutor() as ex:
        ex.map(resize_image, image_list)
    t2 = time.perf_counter()
    resize_image(image_list[0])
    print(f"total time {round(t2 - t1, 2)}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
