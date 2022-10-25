import requests
import pandas as pd





url_data = "https://api.bilibili.com/x/web-interface/popular/series/one?number={number}"
 
for i in range(1, 187):

    response = requests.get(url_data.format(number=i))
    data = response.json()

    video_items = data["data"]["list"]

    for item in video_items:

        video_name = item["title"]
        video_tag = item["tname"]
        video_description = item["desc"]
        video_length = item["duration"]
        video_uploader = item["owner"]
        video_uploader_name = video_uploader["name"]
        video_uploader_face = video_uploader["face"]
        
        # statistics about this video
        video_statistics = item["stat"]
        video_views = video_statistics["view"]
        video_danmakus = video_statistics["danmaku"]
        video_replies = video_statistics["reply"]
        video_favorites = video_statistics["favorite"]
        video_coins = video_statistics["coin"]
        video_shares = video_statistics["share"]
        now_rank = video_statistics["now_rank"]
        hist_rank = video_statistics["his_rank"]
        video_like = video_statistics["like"]

        
        # recommand reason
        item["desc"]

        print("Name: ", video_name)
        print("Up: ", video_uploader_name)







print("debug")
