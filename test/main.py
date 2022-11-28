from bot import Bot


def main():

    bot = Bot()
    bot.login()
    bot.connect_subreddit("nuclearthrone")
    bot.get_posts_subreddit()
    #bot.get_front_page()


if __name__ == "__main__":
    main()