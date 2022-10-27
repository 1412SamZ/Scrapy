from ast import keyword
from urllib import response
import requests
import pandas as pd





url_data = "https://api.bilibili.com/x/web-interface/popular/series/one?number={number}"
url = "https://api.bilibili.com/x/web-interface/search/all/v2?__refresh__=true&_extra=&context=&page={page}&page_size=42&order=&duration=&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E8%94%A1%E5%BE%90%E5%9D%A4&qv_id=HCHC6IWnO6n3sUD6eaElwpSGOEuBGZk4&preload=true&com2co=true"
params = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
          'cookie':"nostalgia_conf=-1; buvid3=1C10E8BC-3DED-F718-7DEF-A59D6F7DD86F33259infoc; b_nut=1665091133; i-wanna-go-back=-1; b_ut=7; _uuid=631FF64A-B7CD-568E-6B108-9AA10D616FE1333678infoc; buvid_fp=7d9dcd1b90c5577eff09063423be792e; buvid4=E0173FE1-5CB0-911E-F54F-2CF6F343BF2E34241-022100705-/WLqPjl1ibFVcgeV2ibcaw%3D%3D; rpdid=|(km)~m~YJ|)0J'uYYl|muumY; PVID=1; CURRENT_QUALITY=16; b_lsid=A12791A1_1841912F881; sid=6adghvdl; innersign=0; CURRENT_FNVAL=16; bsource=search_google"
          }

search_keyword = "蔡徐坤"


for i in range(1, 200):
    try:
        response = requests.get(url.format(page=i), headers=params)
        data = response.json()
        data = data["data"]["result"][10]["data"]
    except:
        print("Search ended!")
        break
    #response = requests.get(url_data.format(number=i), params=params)
    #print(data)
    
    for item in data:
        v_uploader = item["author"]
        v_title = item["title"].replace('<em class="keyword">{keyword}</em>'.format(keyword=search_keyword), search_keyword)
        v_tag = item["tag"]
        v_play = item["play"]
        v_like = item["like"]
        v_duration = item["duration"]
        v_id = item["bvid"]
        v_type = item["typename"]
        print("--------")
        print(v_uploader)
        print(v_title)
        print(v_tag)
        print(v_play)
        print(v_like)
        
        
        
    """video_items = data["data"]["list"]

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
        print("Up: ", video_views)
        """

    





print("debug")
