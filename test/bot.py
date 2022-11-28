import praw

from helper import url_parser

class Bot:
    session = None
    subreddit = None

    def login(self):
        self.session = praw.Reddit(username = "wsdmy",
                password = "dmyws111",
                client_id = "xbIaIzNojitBYxDupi_3OA",
                client_secret = "zmQqs3Sx_V64H8rFY9SQZHdjAgLz4g",
                user_agent = "wsdmy by /u/wsdmy")

    def connect_subreddit(self, subreddit_name):
        self.subreddit = self.session.subreddit(subreddit_name)

    def get_posts_subreddit(self, number_of_posts = 10):
        for index, submission in enumerate(self.subreddit.stream.submissions()):
            if index < number_of_posts:
                print(url_parser(str(self.subreddit), str(submission))) #id del post
            else: break

    def get_front_page(self):
        for sub in self.session.front.hot(limit=256):
            print(sub)
