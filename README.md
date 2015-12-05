# README #

[![Build Status](https://travis-ci.org/guoliang-dev/rabbit-youtube.svg)](https://travis-ci.org/guoliang-dev/rabbit-youtube)

A utility to download youtube videos by user id / playlist id. 

Please note that you'll need to have a google API key (Browser key) to use this application, you may get a key from: https://console.developers.google.com

### main features ###

* download all videos uploaded by user id
* download all videos by playlist id
* skip the previously downloaded files


### how to use it ###

# install via pip: 
> pip install rabbit-youtube 

# run rabbit-youtube: 
> rabbit-youtube.py

you'll need to specify the Google API key for the first time. you may get a free Google API key (Browser key) from: https://console.developers.google.com <br /> 
the key will be stored in your home folder ~/.rabbit_youtube/config.py:

> no config file found, please input your google api key: <br />
> // input your key

# download videos: <br />
download all videos uploaded by user id: 
> rabbit-youtube.py -p PLyPg0ySdyY2b4EbCZFdGUScU1xC3RjkXo ~/tmp-test

download all videos by playlist id: 
> rabbit-youtube.py -u GoogleDevelopers ~/tmp-test

### how it works###
* rabbit-youtube uses google api to retrieve the videos from youtube by user_id or playlist_id; // that's why we need a google api key. 
* rabbit-youtube uses pytube(https://github.com/nficano/pytube) to get the detail and download the video by the video id. 