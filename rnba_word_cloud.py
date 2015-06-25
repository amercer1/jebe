import requests
import json
import pandas as pd

game_one_url = "http://www.reddit.com/r/nba/comments/38mef6/post_game_thread_the_golden_state_warriors_defeat/.json"
game_two_url = "http://www.reddit.com/r/nba/comments/38zfee/post_game_thread_the_cleveland_cavaliers_defeat/"
game_three_url = "http://www.reddit.com/r/nba/comments/39959f/post_game_thread_the_cleveland_cavaliers_defeat/"
game_four_url = "http://www.reddit.com/r/nba/comments/39jgj0/post_game_thread_the_golden_state_warriors_defeat/"
game_five_url = "http://www.reddit.com/r/nba/comments/39vd79/post_game_thread_the_golden_state_warriors_defeat/"
game_six_url = "http://www.reddit.com/r/nba/comments/3a4h3t/post_game_thread_the_golden_state_warriors_defeat/"

list_of_urls = [game_one_url, game_two_url, game_three_url, game_four_url, 
                game_five_url, game_six_url]

headers = {
    'User-Agent': 'linux:jebe.rnba.post.game.scraper:v0.1 (by /u/newTrickster)',
}

r = requests.get(list_of_urls[0], headers=headers)
print r.status_code
print r.headers['X-Ratelimit-Used']
print r.headers['X-Ratelimit-Remaining']
print r.headers['X-Ratelimit-Reset']

data = r.json()
print data.keys()
