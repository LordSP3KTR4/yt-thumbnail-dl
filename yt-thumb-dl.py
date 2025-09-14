#Downloads the thumbnail of a youtube video because I was too lazy to remember the url everytime I wanted one

import requests
import os
try:
    os.makedirs("Thumbnails")  
except FileExistsError:
    videoId = input("Insert youtube video id \n")
    thumbnailUrl = "http://img.youtube.com/vi/"+videoId+"/maxresdefault.jpg"
    response = requests.get(thumbnailUrl)
    fileName = "thumbnails/"+ videoId+".jpg"
    if response.status_code == 200:
        open(fileName, 'wb').write(response.content)
        print('Thumbnail downloaded successfully in "thumbnails" folder.')
    elif response.status_code == 404:  
        print("Error finding thumbnail, check id and retry.")
    else:
        print('Error downloading thumbnail.')
input("Hit enter to close.")