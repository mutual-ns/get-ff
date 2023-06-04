# 必要なライブラリをインポート
import tweepy
import matplotlib.pyplot as plt

# 各種キーをセット
CONSUMER_KEY = 'xxxxxxxxxx'    
CONSUMER_SECRET = 'xxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxx'   #4つの情報を入力

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

#自分のフォロワーのIDを取得
ids = api.get_follower_ids(screen_name="xxxxxxx") #twitterID

#フォロワー数とフォロー数を格納するリストを用意
print(len(ids)) #フォロワー数

cnt=0

ff=[]

#API制限に引っかかる場合があるので、その場合はrangeを調整して段階に分ける
for i in range(len(ids)):
    id = ids[i]
    user_info=api.get_user(user_id=id)
    dd=str(user_info.screen_name)
    
    follower = int(user_info.followers_count)
    
    friend = int(user_info.friends_count)
    
    ff.append([dd,follower,friend])
    
    cnt+=1
    if cnt%50==0:
        print(cnt) #進捗


print(*ff,sep='\n') #名前、フォロワー数、フォロー数

ff_ratio=[] #FF比で管理するリスト

for i in ff:
    ff_ratio.append([i[2]/(i[1]+1),i[0]])

ff_ratio.sort()
print(*ff_ratio,sep='\n') #FF比が高い順に表示