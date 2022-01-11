import json
import pprint


def get_post():
    with open('data/data.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)
    return posts


def get_comments():
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        comments = json.load(f)
    return comments


def get_post_pk(pk):
    posts = get_post()
    for i in posts:
        if i['pk'] == pk:
            return i
    return None


def get_comment(pk):
    comments = get_comments()
    post_com = []
    for i in comments:
        if i['post_id'] == pk:
            post_com.append(i)
    return post_com


def get_comments_posts():
    comments = get_comments()
    posts = get_post()

    comments_dict = {}
    for i in comments:
        post_id = i['post_id']
        if post_id in comments_dict:
            comments_dict[post_id] += 1
        else:
            comments_dict[post_id] = 1
    return comments_dict

