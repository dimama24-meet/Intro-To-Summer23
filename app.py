def create_youtube_video(title,description):
	youtube_video={"title":title ,"description": description,"likes": 0,"dislikes":0,"comments": {}}
	return youtube_video
def likes(youtube_video):
	if 'likes' in youtube_video:
		youtube_video['likes'] += 1
		return

def dislikes(youtube_video):
	if 'dislikes' in youtube_video:
		youtube_video['dislikes'] += 1
		return
def add_comments (youtubevideo,username,comment_text):
	youtubevideo['comments'][username]=comment_text
print (create_youtube_video("slime in 3 min","best way to do slime"))