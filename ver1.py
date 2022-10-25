import requests
import re

def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text

def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})


def display_count(pic_urls, vid_urls):
    if(len(pic_urls) > 1 and len(vid_urls) > 1):
        print(f'Found {len(pic_urls)} pictures and {len(vid_urls)} videos.')
    else:
        if(len(pic_urls)> 1 and len(vid_urls) < 1):
            print(f'Found {len(pic_urls)} pictures and {len(vid_urls)} video.')
        elif(len(pic_urls) < 1 and len(vid_urls) < 1):
            print(f'Found {len(pic_urls)} picture and {len(vid_urls)} video.')
        else:
            print(f'Found {len(pic_urls)} picture and {len(vid_urls)} videos.')

def main():
    url = input('Enter Instagram post URL: ')
    print('Please wait, it may take a few minutes to download...')
    response = get_response(url)

    vid_matches = re.findall('"video_url":"([^"]+)"', response)
    pic_matches = re.findall('"display_url":"([^"]+)"', response)

    vid_urls = prepare_urls(vid_matches)
    pic_urls = prepare_urls(pic_matches)

    if vid_urls:
        print('Detected Videos:\n{0}'.format('\n'.join(vid_urls)))

    if pic_urls:
        print('Detected Pictures:\n{0}'.format('\n'.join(pic_urls)))

    if not (vid_urls or pic_urls):
        print('Could not recognize the media in the provided URL.')

    display_count(pic_urls, vid_urls)

if __name__ == '__main__':
    main()
