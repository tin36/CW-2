from flask import Flask, render_template

from utils import get_post_pk, get_comment, get_post, get_comments_posts

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
    return render_template('post.html', post=post, comment=comment, count_comments=count_comments)

@app.route('/bookmarks',)
def bookmarks():
    return render_template('bookmarks.html')

@app.route('/users/user',)
def user_feed():
    return render_template('user_feed.html')
app.run(debug=True)

