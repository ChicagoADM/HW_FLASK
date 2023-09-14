import argparse
import time
import os
import requests

URLS = [
    'https://bigfoto.name/uploads/posts/2022-03/1647169737_1-bigfoto-name-p-oboi-na-rabochii-stol-komnata-so-stolom-i-1.jpg',
    'https://gas-kvas.com/uploads/posts/2023-02/1675465057_gas-kvas-com-p-fonovie-risunki-na-rabochi-stol-1.jpg',
    'https://gagaru.club/uploads/posts/2023-02/1676251302_gagaru-club-p-krasivie-oboi-dlya-geimera-instagram-34.jpg',
    'https://sneg.top/uploads/posts/2023-03/1679062588_sneg-top-p-oboi-dlya-rabochego-stola-badfon-5.jpg',
    'https://oformi.net/uploads/gallery/main/31/7d-1.jpg',
    'https://bogatyr.club/uploads/posts/2023-03/1679562086_bogatyr-club-p-oboi-na-rabochii-stol-okean-foni-krasivo-1.jpg',
    'https://w.forfun.com/fetch/fe/fe2ef29225d23fe89dc65602713bc3aa.jpeg'
]


start_func_time = time.time()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    return args.url_list


def img_saver(urls):
    if not os.path.exists('images'):
        os.makedirs('images')
    for url in urls:
        start_time = time.time()
        response = requests.get(url)
        filename = f'{url.split("/")[-1]}'
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.content)
        print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


if __name__ == '__main__':
    img_saver(URLS)   # for regular urls list
    # img_saver(create_parser())  # for args via cmd
    print(f'Elapsed time: {(time.time() - start_func_time):.2f} seconds')