import asyncio
import aiohttp
import time
import argparse
import os

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
if not os.path.exists('images'):
    os.makedirs('images')


async def img_saver(url):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        async with session.get(url) as response:
            cont = await response.read()
            filename = f'{url.split("/")[-1]}'
            with open(f'images/{filename}', 'wb') as f:
                f.write(cont)
                print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


async def main():
    tasks = []
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    # for url in args.url_list: # for args via cmd
    for url in URLS:
        task = asyncio.ensure_future(img_saver(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())