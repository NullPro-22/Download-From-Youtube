from pafy import new
from os import system

system("clear")
video = input("Pleas Enter video url : ")
v = new(video)
type = input("For video [1] for audio [2]: ")
stream = None

if (int(type) == 1):
	stream = v.videostreams
else:
	stream = v.m4astreams

print("")
print("Choose the desired Quality")
print("")

num = 0
for i in stream:
	print(num , "- " , i)
	num +=1

streamnum = input("")
stream[int(streamnum)].download()
print("The file has been Downloaded : ")
