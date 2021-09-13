import praw
from praw.models import MoreComments
import csv

reddit = praw.Reddit(
    user_agent="Comment Extraction (by LPX)",
    client_id="x",
    client_secret="x"
)

url = "https://www.reddit.com/r/CryptoCurrency/comments/pljjn1/ama_with_shapeshift_dao_the_largest_company_ever/"
submission = reddit.submission(url=url)
submission.comments.replace_more(limit=0)

with open('topcomments.csv', 'w', newline='') as csvfile:
    headers=['ID','Author','Content','Upvotes']
    writer = csv.writer(csvfile, delimiter='|')
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        try:
            data = {"{}|{}|{}|{}".format(top_level_comment, top_level_comment.author, str(top_level_comment.body), str(top_level_comment.score))}
            print(data)
            writer.writerow(data)
        except:
            pass
