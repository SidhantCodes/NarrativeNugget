from bardapi import Bard
from youtube_transcript_api import YouTubeTranscriptApi

def summary(s1):
    token = 'xxxxx'
    bard = Bard(token=token)
    return bard.get_answer(s1 + "\ncan you summarise this text for me in short?")['content']

Vid = ""
link = input("Enter link: ")
if "?v=" in link:
    Vid += link[link.index("?v=") + 3:]

s = ""
trscrpt = YouTubeTranscriptApi.get_transcript(Vid)

for i in range(len(trscrpt)):
    s += trscrpt[i]['text'] + " "

i = 0
chunk_size = 2500
while i <= len(s):
    subStr = s[i:i + chunk_size]
    summary_text = summary(subStr)
    print(summary_text)
    i += chunk_size
