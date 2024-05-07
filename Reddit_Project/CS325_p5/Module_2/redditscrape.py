import praw
import requests
from bs4 import BeautifulSoup
import Module_1.config as config

def download_and_save_reddit_html(url):
    # Initialize a Reddit API instance
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        username=config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD,
        user_agent="my_bot",
    )

    try:
        submission = reddit.submission(url=url)    

        # Get the post's HTML content
        post_url = f"https://old.reddit.com{submission.permalink}"
        post_response = requests.get(post_url)
        post_html = post_response.text

        # Extract HTML content of comments
        comments_htmls = []
        comments = submission.comments.list()
        for comment in comments:
            if isinstance(comment, praw.models.Comment):
                comments_htmls.append(comment.body_html)

        # Combine post content and comments' HTML
        reddit_html = post_html + "\n\n" + "\n\n".join(comments_htmls)

        return reddit_html

    except Exception as e:
        print(f"Error for URL {url}: {e}")
        return None
