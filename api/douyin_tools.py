import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

api = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={video_id}"
def download_video(url:str):
    req=requests.get(url,headers)
    id=re.findall(r"video/(\d+)",req.url)[0]
    # print(video_id)
    req_api=requests.get(api.format(video_id=id),headers)
    api_json=req_api.json()
    video_download_url = api_json['item_list'][0]['video']["play_addr"]["url_list"][0]
    copywriting = api_json['item_list'][0]['share_info']['share_title']
    print(video_download_url,copywriting)
    req_video = requests.get(video_download_url, headers)
    with open('{}.mp4'.format(str(copywriting)), 'wb') as f:
        f.write(req_video.content)
