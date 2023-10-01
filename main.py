import praw
r = praw.Reddit(username = "Independent_Song_441",
                password = "Broadneck1@",
                client_id = "ix0Ps9f_5LmE5p9WwiwLpA",
                client_secret = "CtwH8QNvw64iCVSip4qoO2tvl_hebQ",
                user_agent = "Jarvis-Bot-3")


# # Keywords
# This bot can check certain comments and, if there is a keyword in the comment, will do an action. 
subr = r.subreddit('copypasta') # this chooses a subreddit you want to get comments from
for comment in subr.stream.comments(skip_existing=True): # this iterates through the comments from that subreddit as new ones are coming in
  try:
    if "!bot" in comment.body: # "!bot" is the keyword in this case. replace "bot" with your keyword
      comment.reply("hello world...") # this is what your bot replies to the comment that has the keyword
  except praw.exceptions.APIException: # Reddit may have rate limits, this prevents your bot from dying due to rate limits
    print("probably a rate limit...")