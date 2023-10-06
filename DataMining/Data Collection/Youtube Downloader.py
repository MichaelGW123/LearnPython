# Michael Williamson
# YouTube Video Downloader using pytube
# 1/2/2021

from pytube import YouTube

savePath = 'C:\\Users\\Michael JITN\\Documents\\Practice\\DataMining\\Data Collection\\Video-Downloads'

videoURL = input("What is the URL of the video you wish to download? ")

yt = YouTube(videoURL)
print("Now downloading \""+yt.title+"\" to the folder \'"+savePath+"\'")
yt.streams.first().download(savePath)
print("Program done.")