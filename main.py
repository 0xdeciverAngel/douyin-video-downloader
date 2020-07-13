import re
from api import douyin_tools

def parse_url(url:str)->list:
    urls = re.findall(r"https://v\.douyin\.com/.*/",url)
    return urls

if __name__ == "__main__":
    # while 1:
    if __name__ == "__main__":
        user_input = 'https://v.douyin.com/JNTYPWK/'
        # user_input=input('input url')
        if user_input=='':
            exit()
            # break
        urls = parse_url(user_input)
        for i in urls:
            douyin_tools.download_video(i)
