import json


def get_post():
    '''Чтение файла с постами'''
    with open('data/data.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)
    return posts


def get_comments():
    '''Чтение файла с комментариями'''
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        comments = json.load(f)
    return comments


def get_post_pk(pk):
    '''Выборка по номера поста'''
    posts = get_post()
    for i in posts:
        if i['pk'] == pk:
            return i
    return None


def get_comment(pk):
    '''Выборка всех комментариев по определенному посту'''
    comments = get_comments()
    post_com = []
    for i in comments:
        if i['post_id'] == pk:
            post_com.append(i)
    return post_com


def get_comments_posts():
    '''Счетчик комментариев'''
    comments = get_comments()
    comments_dict = {}
    for i in comments:
        post_id = i['post_id']
        if post_id in comments_dict:
            comments_dict[post_id] += 1
        else:
            comments_dict[post_id] = 1
    return comments_dict


def post_search(word):

    post_search = []
    posts = get_post()
    for i in posts:
        if word in i['content']:
            post_search.append(i)


    return post_search
