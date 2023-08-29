from bardapi import Bard
from youtube_transcript_api import YouTubeTranscriptApi

def summary(s1):
    token = 'xxxxxxxxx'
    bard = Bard(token=token)
    ans =  bard.get_answer(s1 + "\ncan you summarise this text for me in short?")['content']
    return ans.replace("I hope this summary is helpful. Let me know if you have any other questions.", "").strip()

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
