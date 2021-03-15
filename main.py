from apiclient.discovery import build
import sys
import json, time, os

api_key =  "AIzaSyD9JDXhHNhwBLKCIVmUdjf2Bew8NfJ-UwE"
youtube = build('youtube', 'v3', developerKey=api_key)
# req = youtube.search().list(q='code with harry', part='snippet', type='video')
# res = req.execute()
# num = sys.argv[1]

# ----------------
nextPage = None
list = []
while True:
    res = youtube.playlistItems().list(
    part="snippet",
    playlistId="PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi",
    maxResults='50',
    pageToken=nextPage,
    ).execute()
    list += res['items']
    try:
        nextPage = res['nextPageToken']
    except :
        break


# list_title = [list['items'][i]['snippet']['title'] for i in range(len(list['items']))]

list_title = [i['snippet']['title'] for i in list]
# for i in range(len(list_title)):
#     print(i+1, list_title[i])
# --------------

title_list = list_title
# title_list = [res['items'][i]['snippet']['title'] for i in range(len(data['items']))]
names_list = [i for i in os.listdir() if '.mp4' in i]

title = [i.replace('[','_').replace(']','_').replace('?','_').replace(':','_').replace('|','_').replace('+','_').replace('*','_').replace('🔥', '_fire_') for i in title_list]
names = [i.replace(" ( 720 X 1280 ).mp4", "") for i in names_list]



def rename_files(list1,list2):
    title_count = 0
    for i in list1:
        title_count += 1
        name_count = 0
        for j in list2:
            name_count += 1
            if i in j:
                #print(f"{title_count} > '{i}'' found on index {name_count}***")
                #print(f"{title_list[title_count-1]}")
                #print(f"{title_count} {names_list[name_count-1]}")
                try:
                	os.rename(names_list[name_count-1], f"{title_count} {names_list[name_count-1]}")
                	print(f"{title_count} {names_list[name_count-1]}")
                except:
                	continue
                #print(names_list[name_count-1])
                #print(i)
               
                
# print(title)

# print(names)
rename_files(title, names)


