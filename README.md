# README #

[![Build Status](https://travis-ci.org/guoliang-dev/rabbit-youtube.svg)](https://travis-ci.org/guoliang-dev/rabbit-youtube) [![PyPI version](https://badge.fury.io/py/rabbit-youtube.svg)](https://badge.fury.io/py/rabbit-youtube)

A utility to download youtube videos by user id / playlist id. 

Please note that you'll need to have a google API key (Browser key) to use this application, you may get a key from: https://console.developers.google.com

### main features ###

* download all videos uploaded by user id
* download all videos by playlist id
* skip the previously downloaded files


### how to use it ###
http://guoliang-dev.github.io/rabbit-youtube/

### how it works###
* rabbit-youtube uses google api to retrieve the videos from youtube by user_id or playlist_id; // that's why we need a google api key. 
* rabbit-youtube uses pytube(https://github.com/nficano/pytube) to get the detail and download the video by the video id. 