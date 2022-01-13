from flask import Flask, render_template, request

from utils import get_post_pk, get_comment, get_post, get_comments_posts, post_search, count_views, search_tag, user_feed_dict, tag

app = Flask(__name__)

@app.route('/',)
def main_page():
    post = get_post()
    comments_count = get_comments_posts()
    return render_template('index.html', post=post, comments_count=comments_count)

@app.route('/posts/<int:pk>',)
def posts(pk):
    post = get_post_pk(pk)
    comment = get_comment(pk)
    count_comments = len(comment)
    count_views(pk)
    return render_template('post.html', post=post, comment=comment, count_comments=count_comments)

@app.route('/bookmarks',)
def bookmarks():
    return render_template('bookmarks.html')

@app.route('/users/<user>',)
def user_feed(user):
    user_feed = user_feed_dict(user)
    return render_template('user-feed.html', user_feed=user_feed)


@app.route('/search/')
def search():
    s = request.args.get('s', '')
    if s is None:
        return render_template('search.html')
    s = s.lower()
    posts = post_search(s)
    count_posts = len(posts)
    comments_count = get_comments_posts()
    return render_template('search.html', posts=posts, s=s, count_posts=count_posts, comments_count=comments_count)

@app.route('/tag/<tags>')
def get_tag(tags):
    tags_post = []
    post = get_post()
    get_tag = tag(tags) #tag
    comments_count = get_comments_posts()
    title = f'TAG/{tags.upper()}'
    for i in post:
        if f'#{tags}' in i['content']:
            tags_post.append(i)
    # get_tag_up = get_tag.upper()
    return render_template('tag.html', post=post, get_tag=get_tag, tags_post=tags_post, title=title, tags=tags, comments_count=comments_count)


app.run(debug=True, port=8001)

