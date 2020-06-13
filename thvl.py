import re
import logging
import time

from streamlink import StreamError
from streamlink.plugin import Plugin
from streamlink.stream import HLSStream

log = logging.getLogger(__name__)

class THVL(Plugin):
    url_re = re.compile(r'^^https:\/\/www.thvli.vn\/detail\/(?:.*?)\/(.*?)$')
    parse_src_re = r'source[\s]+src="(.*?)"'

    @classmethod
    def can_handle_url(cls, url):
        return cls.url_re.match(url) is not None

    def _get_streams(self):
        match = self.url_re.match(self.url)
        new_url = f"https://api.thvli.vn/backend/cm/detail/{match[1]}/"
        r = self.session.http.get(new_url, headers = {"Referer": self.url, "Origin": "https://www.thvli.vn", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"})
        try:
            result = r.json()
            link_play = result["play_info"]["data"]["hls_link_play"]
        except KeyError:
            link_play = ""
        if not link_play: 
            raise StreamError("Unable to find stream video from url %s" % self.url)
        streams = HLSStream.parse_variant_playlist(self.session, link_play, headers = {"Referer": self.url, "Origin": "https://www.thvli.vn", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"})
        return streams

__plugin__ = THVL