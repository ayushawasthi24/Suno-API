import os
import json
import random
import re
import time
from typing import List, Optional
from curl_cffi import requests

COOKIE = os.getenv("SUNO_COOKIE", "")


class Client:

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    }

    def __init__(self, cookie: str) -> None:
        self.headers["cookie"] = cookie
        self._session = requests.Session(headers=self.headers)
        self._sid = None

    def request(self, *args, **kwargs) -> requests.Response:
        kwargs["impersonate"] = kwargs.get("impersonate", "chrome")
        return self._session.request(*args, **kwargs)

    def sleep(self, seconds: Optional[float] = None) -> None:
        if seconds is None:
            seconds = random.randint(1, 6)
        time.sleep(seconds)


class Suno(Client):

    def __init__(self, cookie: Optional[str] = None) -> None:
        if cookie is None:
            cookie = COOKIE
        if cookie == "":
            raise Exception("environment variable SUNO_COOKIE is not set")
        super().__init__(cookie)
        self._sid = self._get_sid()

    def _get_sid(self) -> str:
        url = "https://clerk.suno.com/v1/client?__clerk_api_version=2024-10-01&_clerk_js_version=5.43.2&_method=PATCH"
        response = super().request("GET", url)
        if not response.ok:
            raise Exception(f"failed to get SID: {response.json()}")
        data = response.json()
        return data.get("response").get("last_active_session_id")
        # return "sess_2r5DLbf68JHjBaPAnbqA9hGgcez"
        # return "sess_2r5NY5ENykgpTz8A6GENGORRAPX"

    def _get_jwt(self) -> str:
        url = f"https://clerk.suno.com/v1/client/sessions/{self._sid}/tokens?__clerk_api_version=2024-10-01&_clerk_js_version=5.43.2"
        response = super().request("POST", url)
        if not response.ok:
            raise Exception(f"failed to get JWT: {response.json()}")
        data = response.json()
        return data.get("jwt")

    def _is_ready(self, id: str) -> bool:
        song = self.get_song(id)
        return (song[0]["audio_url"] != "") and (song[0]["video_url"] != "")

    def _renew(self) -> None:
        self._session.headers["Authorization"] = f"Bearer {self._get_jwt()}"

    def request(self, *args, **kwargs) -> requests.Response:
        response = super().request(*args, **kwargs)
        while response.status_code == 401:
            self._renew()
            response = super().request(*args, **kwargs)
        return response

    def get_songs(self):
        url = "https://studio-api.prod.suno.com/api/feed"
        response = self.request("GET", url)
        if not response.ok:
            raise Exception(f"failed to get songs: {response.status_code}")
        data = response.json()
        return data

    def get_song(self, id: str):
        url = f"https://studio-api.prod.suno.com/api/feed/?ids={id}"
        response = self.request("GET", url)
        if not response.ok:
            return [{"audio_url": "", "video_url": ""}]
            # raise Exception(f"failed to get song: {response}")
        data = response.json()
        return data

    def get_credits(self) -> int:
        url = "https://studio-api.prod.suno.com/api/billing/info"
        response = self.request("GET", url)
        if not response.ok:
            raise Exception(f"failed to get credits: {response.status_code}")
        data = response.json()
        return data.get("total_credits_left")

    def generate_song(self, prompt, instrumental):
        timeout = 600
        url = "https://studio-api.prod.suno.com/api/generate/v2/"
        payload = {
            "generation_type": "TEXT",
            "gpt_description_prompt": prompt,
            "metadata": {"lyrics_model": "default"},
            "mv": "chirp-v2-xxl-alpha",
            "tags": "",
            "prompt": "",
            "token": self._get_jwt(),
            "make_instrumental": instrumental,
        }
        data = json.dumps(payload)
        response = self.request("POST", url, data=data)
        if not response.ok:
            raise Exception(f"failed to generate song: {response.json()}")
        data = response.json()
        clip_ids = [clip.get("id") for clip in data.get("clips")]
        print(clip_ids)
        start = time.time()
        while True:
            if time.time() - start > timeout:
                raise Exception("failed to generate songs: TIMEOUT")
            if sum([self._is_ready(id) for id in clip_ids]) == len(clip_ids):
                print("")
                break
            else:
                print(".", end="", flush=True)
        links = []
        for id in clip_ids:
            links.append(f"https://cdn1.suno.ai/{id}.mp3")
            print(f"Song link: https://cdn1.suno.ai/{id}.mp3")
        return links
