import requests
import re
# import wget

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
headers = {
    ':authority':'aweme.snssdk.com',
    ':method':'GET',
    ':path':'{url_path}',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
    'dnt': '1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
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
    path=video_download_url.split('.com')[1]
    print(path)
    req_video = requests.get(video_download_url, headers[':path'].format(url_path=path))
    print(req_video)
    # with open('{}.mp4'.format(str(copywriting)), 'wb') as f:
        # f.write(req_video.content)
