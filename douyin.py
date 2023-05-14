# 封装了抖音API的模块

import requests
from config import COOKIE


class DouYinAPI:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": COOKIE
        }
        self.base_url = "https://www.douyin.com/"

    def get_live_info(self, room_id):
        # 获取直播间信息
        url = self.base_url + f"webcast/room/{room_id}"
        response = requests.get(url, headers=self.headers)
        # 解析响应，提取直播间信息
        # ...

    def get_comments(self, room_id, cursor=0):
        # 获取评论信息
        url = self.base_url + f"webcast/room/{room_id}/comment/list/?cursor={cursor}"
        response = requests.get(url, headers=self.headers)
        # 解析响应，提取评论信息
        # ...

    def get_danmus(self, room_id):
        # 获取弹幕信息
        url = self.base_url + f"webcast/room/{room_id}/danmu/list/"
        response = requests.get(url, headers=self.headers)
        # 解析响应，提取弹幕信息
        # ...

