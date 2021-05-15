import sys
import os , subprocess , time

try:
    from pytube import YouTube , Playlist
except Exception:
    subprocess.check_call([sys.executable,'-m','pip','install','pytube'])
    from pytube import YouTube

def clear():    
    os.system('cls' if os.name == 'nt' else 'clear')
def note(note):
    print('-'*40+f'\n{note}\n'+'-'*40)
while True:
    clear()
    try:
        note('inter the video or playlist url\nthen press inter to start downloading ')
        url = input()
        if 'playlist' not in url:
            try:
                video = YouTube(url)
                print('wait a second....')
                video.streams.filter(type="video").get_highest_resolution().download()
                print('Done !')
                time.sleep(3)

            except Exception as e:
                print('an unvalued video url') , time.sleep(5) , clear()
                continue
        elif 'playlist' in url:
            try:
                p = Playlist(url)
                os.mkdir(p.title)
                os.chdir(p.title)
                for video in p.videos:
                    video.streams.filter(type = 'video').get_highest_resolution().download()
                    print(f"{video.title} is completed")
                print("Done!")
                time.sleep(3)
            except Exception:
                print('un unvalued playlist url')

    except Exception as e:
        print(e)
        note('sorry dude there is an error')
        time.sleep(4)