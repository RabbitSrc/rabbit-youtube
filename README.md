# README #

A utility to download youtube videos by user_id / playlist_id. 

Please note you'll need to have a google API key (Browser key) to use this application, you may get a key from: https://console.developers.google.com

### Main Features ###

* download all videos uploaded by the given user id
* download all videos in the given playlist
* skip the downloaded files


### How to use it ###

# install via pip: 
> pip install rabbit-youtube 

# run rabbit-youtube: 
> rabbit-youtube.py

# specify the Google API key
you may get a free Google API key (Browser key) from: https://console.developers.google.com 
the key will stored in your home folder ~/.rabbit_youtube/config.py:
> rabbit-youtube.py <br />
> no config file found, please input your google api key:

# download files: <br />
download all videos uploaded by the specified user: 
> rabbit-youtube.py -p PLyPg0ySdyY2b4EbCZFdGUScU1xC3RjkXo ~/tmp-test

download all videos in the specified playlist: 
> rabbit-youtube.py -u GoogleDevelopers ~/tmp-test