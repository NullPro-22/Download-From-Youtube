from pafy import new
from os import system
system("clear")
video = input("Pleas Enter video url : ")
v = new(video)

stream = v.videostreams

print("")
print("Choose the desired Quality")
print("")

num = 0
for i in stream:
	print(num , "- " , i)
	num +=1

streamnum = input("")
print("The Video is Downloading...")
stream[int(streamnum)].download()
print("The file has been Downloaded : ")
