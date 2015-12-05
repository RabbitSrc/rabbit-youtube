import json
import os
import unittest
from urllib2 import urlopen
from pytube import YouTube
from rabbit_youtube import app_config


key = 'AIzaSyCYzucSKQxHcC88_k39VRYqpzG0kHMb4Ag'


class TestYoutubeAPI(unittest.TestCase):
    def test_get_channel_id_by_user_id(self):
        user_id = 'GoogleDevelopers'
        user_channel_url_base = 'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=%s&key=%s'

        response = urlopen(user_channel_url_base % (user_id, key))
        content = response.read().encode('utf-8')
        data = json.loads(content)

        print 'channel id data: \n%s: ' % data

        self.assertTrue(data is not None)

    def test_get_video_id_list(self):
        upload_playlist_id = 'UU_x5XG1OV2P6uZZ5FSM9Ttw'
        upload_playlist_url_base = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=%s&key=%s'
        url_playlist = upload_playlist_url_base % (upload_playlist_id, key)

        content = urlopen(url_playlist).read().decode('utf-8')
        data = json.loads(content)

        print 'Video Id List: \n%s' % data

        self.assertTrue(data is not None)


class TestPytube(unittest.TestCase):

    def test_get_videos_by_video_id(self):
        video_id = 'uFOWdNtUgvU'
        video_info_url_base = 'https://www.youtube.com/watch?v=%s'
        video_url = video_info_url_base % video_id
        youtube = YouTube(video_url)
        self.assertGreater(youtube.get_videos(), 1)

    def test_download_video(self):
        video_id = 'cr04UelmPqg'  # https://www.youtube.com/watch?v=cr04UelmPqg
        video_info_url_base = 'https://www.youtube.com/watch?v=%s'
        video_url = video_info_url_base % video_id
        youtube = YouTube(video_url)

        video = youtube.get_videos()[0]  # get_best_video(youtube)

        self.assertEqual('3gp', video.extension)

        # file_path = '/tmp/rabbit_youtube_test.%s' % video.extension
        #
        # video.download(file_path)
        # self.assertTrue(os.path.isfile(file_path))
        # os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
