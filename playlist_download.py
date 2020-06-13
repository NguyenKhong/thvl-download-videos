# -*- coding: utf-8 -*-
import sys, os
current_dir = os.path.dirname(__file__)
path1 = os.path.abspath(os.path.join(current_dir, 'Streamlink', 'Dependencies'))
path2 = os.path.abspath(os.path.join(current_dir))
path3 = os.path.abspath(os.path.join(current_dir, "packages"))

for path in [path1, path2, path3]:
    if not path in sys.path:
        sys.path.insert(0, path)

import requests
import subprocess
import re

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Origin": "https://www.thvli.vn"}
Session = requests.Session()
Session.headers.update(HEADERS)

FFMPEG = ""
def scanFFmpeg():
    global FFMPEG
    for path, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file in ["ffmpeg", "ffmpeg.exe"]:
                FFMPEG = os.path.join(path, file)
    if not FFMPEG:
        raise Exception("ffmpeg file not found")

def downloader(url, file):
    args = ["Streamlink.bat", "--http-timeout", "60", "--hls-segment-timeout", "60", "--ringbuffer-size", "64M", "--player-no-close", "--player", FFMPEG, "-a", '-i {filename} -y -c copy -bsf:a aac_adtstoasc "%s"' % file, "--fifo", "--hls-segment-threads", "6", "--http-header", 'User-Agent="%s"' % HEADERS["User-Agent"], url, "720p"]
    p = subprocess.Popen(args)
    p.wait()

_name_re = re.compile(r"^https://www.thvli.vn/detail/(\S+)/$")
def name2SeasonId(url):
    match = re.match(_name_re, url)
    if not match:
        raise Exception("Name not found")
    r = Session.get("https://api.thvli.vn/backend/cm/detail/%s/" % match[1])
    result = r.json()
    for season in result["seasons"]:
        yield season["id"]
    return

def main():
    scanFFmpeg()
    download_dir = os.path.join(os.getcwd(), "download")
    if not os.path.exists(download_dir): os.mkdir(download_dir)
    season_url = input(" URL: ")
    for Id in name2SeasonId(season_url):
        r = Session.get("https://api.thvli.vn/backend/cm/season_by_id/%s/" % Id)
        episodes = r.json()["episodes"]
        for episode in episodes:
            print (episode["episode"], episode["title"], episode["id"])
            downloader("https://www.thvli.vn/detail/me-ghe/%s" % episode["id"], os.path.join(download_dir, "%s.mp4" % episode["title"]))


if __name__ == '__main__':
    main()