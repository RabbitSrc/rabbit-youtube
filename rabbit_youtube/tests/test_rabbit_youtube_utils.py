import os
import shutil
import logging
import unittest
from rabbit_youtube import youtube_utils, app_config

key = app_config.get_google_api_key()


class TestRabbitYoutube(unittest.TestCase):

    def setUp(self):
        self.destination_folder = '/tmp/test_rabbit_youtube'
        if os.path.exists(self.destination_folder):
            shutil.rmtree(self.destination_folder)
        os.makedirs(self.destination_folder)

    def test_get_channel_id_by_user_id(self):
        user_id = 'GoogleDevelopers'
        uploads_playlist_id = youtube_utils.get_upload_playlist_id_by_user_id(user_id)

        self.assertEqual('UU_x5XG1OV2P6uZZ5FSM9Ttw', uploads_playlist_id)

    def test_get_video_id_list_by_playlist_id(self):
        playlist_id = 'PLyPg0ySdyY2b4EbCZFdGUScU1xC3RjkXo'
        video_id_list = youtube_utils.get_video_id_list_by_playlist_id(playlist_id)

        self.assertEqual(1, len(video_id_list))

    def test_get_best_video_by_video_id(self):
        video_id = 'cr04UelmPqg'
        best_video = youtube_utils.get_best_video_by_video_id(video_id)

        self.assertEqual('360p', best_video.resolution)
        self.assertEqual('Strava 2014 - cycling', best_video.filename)
        self.assertEqual('mp4', best_video.extension)

    def test_generate_file_name(self):
        video_id = 'cr04UelmPqg'
        video = youtube_utils.get_best_video_by_video_id(video_id)
        file_name = youtube_utils.generate_file_name(video_id, video)

        self.assertEqual('cr04UelmPqg_Strava 2014 - cycling_360p.mp4', file_name)

    def test_download_all_videos_in_playlist_typical(self):
        playlist_id = 'PLyPg0ySdyY2b4EbCZFdGUScU1xC3RjkXo'
        total_files_downloaded = youtube_utils.download_all_videos_in_playlist(playlist_id, self.destination_folder)
        downloaded_file_path = os.path.join(self.destination_folder, playlist_id, 'cr04UelmPqg_Strava 2014 - cycling_360p.mp4')

        self.assertTrue(os.path.isfile(downloaded_file_path))
        self.assertEqual(1336405, os.path.getsize(downloaded_file_path))
        self.assertEqual(1, total_files_downloaded)

    def test_download_all_videos_in_playlist_video_file_existing(self):
        playlist_id = 'PLyPg0ySdyY2b4EbCZFdGUScU1xC3RjkXo'
        destination_folder = os.path.join(self.destination_folder, playlist_id)
        youtube_utils.ensure_folder(destination_folder)
        downloaded_file_path = os.path.join(destination_folder, 'cr04UelmPqg_Strava 2014 - cycling_360p.mp4')

        open(downloaded_file_path, 'w+')
        self.assertEqual(0, os.path.getsize(downloaded_file_path))

        total_files_downloaded = youtube_utils.download_all_videos_in_playlist(playlist_id, self.destination_folder)
        self.assertEqual(0, total_files_downloaded)

    def tearDown(self):
        if os.path.exists(self.destination_folder):
            shutil.rmtree(self.destination_folder)

if __name__ == '__main__':
    log_format = "%(asctime)s [%(name)s] [%(levelname)-5.5s]  %(message)s"
    logging.basicConfig(level=logging.DEBUG,
                        format=log_format,
                        datefmt="%H:%M:%S", filemode='a')
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(logging.Formatter(log_format))
    logging.getLogger(__name__).addHandler(consoleHandler)
    unittest.main()
