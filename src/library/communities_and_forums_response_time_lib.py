import requests
import urllib3
urllib3.disable_warnings()

def get_response_time(url):
    try:
        return(requests.get(url, verify=False).elapsed.total_seconds())
    except requests.exceptions.ConnectionError as e:
        print(e)
        return -1       

communities = {
        'chat.zcashcommunity.com': {'url': 'https://chat.zcashcommunity.com/home'},
        'forum.zcashcommunity.com': {'url': 'https://forum.zcashcommunity.com/'},
        'zcashcommunity.com': {'url': 'https://www.zcashcommunity.com/'},
        'z.cash': {'url': 'https://z.cash/'},
        'zfnd.org': {'url': 'https://www.zfnd.org/'}
    }

def communities_and_forums_response_time():
    response_time_list = []
    for community in communities.keys():
        community_url = communities[community]['url']
        response_time = get_response_time(community_url)
        response_time_list.append((community,response_time))

    return response_time_list



