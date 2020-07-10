# douyin video downloader

## directions
request url like https://v.douyin.com/JdtJGg1/<br>
It will return 302 and redirect,but if you curl it,it will return video id like below<br>
```html
<a href="https://www.iesdouyin.com/share/video/6837776970420407560/?region=TW&amp;mid=6837777324390304525&amp;u_code=0&amp;titleType=title&amp;timestamp=1592118519&amp;utm_campaign=client_share&amp;app=aweme&amp;utm_medium=ios&amp;tt_from=copy&amp;utm_source=copy">Found</a>.
```
<br>
then use api to find video link<br>
https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=6837776970420407560<br>
it will return json,it contents video url,then just download it