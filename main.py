# 程序入口

from douyin import DouYinAPI
from datetime import datetime
import time


def save_to_file(file_path, data):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(data + "\n")


def main():
    # 抖音直播间的房间号
    room_id = "这里填写直播间房间号"
    api = DouYinAPI()
    live_info = api.get_live_info(room_id)
    # 获取直播间名称、主播名称等信息
    # ...

    # 获取评论信息并保存到本地文件中
    comments_file = "data/comments.txt"
    cursor = 0
    while True:
        comments = api.get_comments(room_id, cursor)
        if not comments:
            break
        cursor = comments[-1]["cursor"]
        for comment in comments:
            comment_data = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t{comment['text']}"
