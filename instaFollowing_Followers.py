import requests

ACCESS_TOKEN=''
client_id=''
base_url='https://api.instagram.com/v1'

userFollow=[]
userFollowers=[]

def followstore(a):
	for i in range(len(a)):
		userFollow.append(a[i]['full_name'])
def followerstore(a):
	for i in range(len(a)):
		userFollowers.append(a[i]['full_name'])

def user_follows(user_id="self"):

	user_follows_data=requests.get(base_url+'/users/'+user_id+'/follows?access_token='+ACCESS_TOKEN).json()
	followstore(user_follows_data['data'])
	print('yeah')
	while(user_follows_data['pagination']):
		print('working')
		user_follows_data=requests.get(user_follows_data['pagination']['next_url']).json()
		followstore(user_follows_data['data'])

	#return user_follows_data
def user_followers(user_id="self"):

	user_followers_data=requests.get(base_url+'/users/'+user_id+'/followed-by?access_token='+ACCESS_TOKEN).json()
	followerstore(user_followers_data['data'])
	print('yeah')
	while(user_followers_data['pagination']):
		print('working')
		user_followers_data=requests.get(user_followers_data['pagination']['next_url']).json()
		followerstore(user_followers_data['data'])
#sattu id : 1304318593
user_follows()
user_followers()

print(len(userFollow))

print("Followed By")

print(len(userFollowers))

result=list(set(userFollow)-set(userFollowers))

print(result)
