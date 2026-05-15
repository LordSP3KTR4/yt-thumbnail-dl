#Downloads the thumbnail of a youtube video because I was too lazy to remember the url everytime I wanted one

import requests
import os
from urllib.parse import urlsplit



def obtainVidId(url):
    splitUrl= urlsplit(url)
    if splitUrl.netloc == "youtu.be":
        videoId = splitUrl.path[1:]

    elif splitUrl.netloc == "www.youtube.com":
        videoId = splitUrl.query[2:]

    else:
        print("error obtaining id")

    thumbnailDownloader(videoId)

def thumbnailDownloader(videoId):
    
    thumbnailUrl = "http://img.youtube.com/vi/"+videoId+"/maxresdefault.jpg"
    response = requests.get(thumbnailUrl)
    if response.status_code == 200:
        open("thumbnails/"+ videoId+".jpg", 'wb').write(response.content)
        print('Thumbnail downloaded successfully in "thumbnails" folder.')

    elif response.status_code == 404:  
        print("Error finding thumbnail, check id and retry.")

    else:
        print('Error downloading thumbnail.')
    input("Hit enter to close.")


url = input("Insert youtube video url\n")
try:
    print("'thumbnails' folder not found, it will be created now.")
    os.makedirs("thumbnails")
    obtainVidId(url)
    
except FileExistsError:
    obtainVidId(url)

