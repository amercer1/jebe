import sys
import string
import re

import requests
import json

def extract_from_block(comment_block):
    if comment_block.has_key("data"):
        comment_block = comment_block["data"]
        if comment_block.has_key("body"):
            line = comment_block["body"]
            line = line.split()
            for str_item in line:
                str_list.append(clean_string(str_item))
            #str_list.append(line)
        if comment_block.has_key("replies"):
            extract_child_blocks(comment_block["replies"])

def extract_child_blocks(replies):
  if hasattr(replies, 'has_key') is False:
    return
  if replies.has_key("data"):
    replies_data = replies["data"]
    if replies_data.has_key("children"):
      replies_data_children = replies_data["children"]
      for child in replies_data_children:
          if child.has_key("data"):
              child_data = child["data"]
              if child_data.has_key("body"):
                  line = child_data["body"]
                  line = line.split()
                  for str_item in line:
                      str_list.append(clean_string(str_item))
                  #str_list.append(line)
              if child_data.has_key("replies"):
                  extract_child_blocks(child_data["replies"])
def clean_string(s):
    s = s.lower()
    s = re.sub(r'\W+', '', s)
    return s

def build_and_send_requests(url):
    headers = {
        'User-Agent': 'linux:jebe.rnba.post.game.scraper:v0.1 (by /u/newTrickster)',
    }

    r = requests.get(url, headers=headers)
    return r

def parse_data(r):
    if r.status_code == 200:
      print "Json data returned"
    else:
      print "Bad request"
      return
    data = r.json()
    comments = data[1]
    comment_data = comments["data"]
    comment_data = comment_data["children"]

    if (comment_data):
        print "Begin adata extraction"
    else:
        sys.exit(0)
  
    str_list = []
    #Now start looping through comment blocks
    for child in comment_data:
      str_list =  extract_from_block(child)
      print "BUILT STRING LIST"
      print len(str_list)

def main():
    game_one_url = "http://www.reddit.com/r/nba/comments/38mef6/post_game_thread_the_golden_state_warriors_defeat/comments/.json"
    game_two_url = "http://www.reddit.com/r/nba/comments/38zfee/post_game_thread_the_cleveland_cavaliers_defeat/comments/.json"
    game_three_url = "http://www.reddit.com/r/nba/comments/39959f/post_game_thread_the_cleveland_cavaliers_defeat/comments/.json"
    game_four_url = "http://www.reddit.com/r/nba/comments/39jgj0/post_game_thread_the_golden_state_warriors_defeat/comments/.json"
    game_five_url = "http://www.reddit.com/r/nba/comments/39vd79/post_game_thread_the_golden_state_warriors_defeat/comments/.json"
    game_six_url = "http://www.reddit.com/r/nba/comments/3a4h3t/post_game_thread_the_golden_state_warriors_defeat/comments/.json"
    
    list_of_urls = [game_one_url, game_two_url, game_three_url, game_four_url, 
                    game_five_url, game_six_url]

    for url in list_of_urls:
        r = build_and_send_requests(url) 
        parse_data(r)

    
