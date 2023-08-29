# import requests
# import os
# from bs4 import BeautifulSoup

# # Set the URL of the first XKCD comic
# url = 'https://xkcd.com/1/'

# # Create a folder to store the comics
# if not os.path.exists('xkcd_comics'):
#     os.makedirs('xkcd_comics')

# # Loop through all the comics
# while True:
#     # Download the page content
#     res = requests.get(url)
#     res.raise_for_status()

#     # Parse the page content using BeautifulSoup
#     soup = BeautifulSoup(res.text, 'html.parser')

#     # Find the URL of the comic image
#     comic_elem = soup.select('#comic img')
#     if comic_elem == []:
#         print('Could not find comic image.')
#     else:
#         comic_url = 'https:' + comic_elem[0].get('src')

#         # Download the comic image
#         print(f'Downloading {comic_url}...')
#         res = requests.get(comic_url)
#         res.raise_for_status()

#         # Save the comic image to the xkcd_comics folder
#         image_file_path = os.path.join('xkcd_comics', os.path.basename(comic_url))
#         with open(image_file_path, 'wb') as image_file:
#             for chunk in res.iter_content(100000):
#                 image_file.write(chunk)

#     # Get the URL of the previous comic
#     prev_link = soup.select('a[rel="prev"]')[0]
#     if not prev_link:
#         break
#     url = 'https://xkcd.com' + prev_link.get('href')

# print('All comics downloaded.')

#import Section
import requests
import os
from bs4 import BeautifulSoup
#link to comic file
url = 'https://xkcd.com/1/'
#checking and retriving files
if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')
#downloading the images of comic
while True:
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    comic_elem = soup.select_one('#comic img')
    if comic_elem:
        comic_url = 'https:' + comic_elem['src']
        print(f'Downloading {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()
        
#storing the images of comic
        image_file_path = os.path.join('xkcd_comics', os.path.basename(comic_url))
        with open(image_file_path, 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)

#check if we have any older comic links
    prev_link = soup.select_one('a[rel="prev"]')
    if not prev_link:
        break
    url = 'https://xkcd.com' + prev_link['href']

#Print Result
print('All comics downloaded.')
