from instabot import Bot
bot = Bot()

# to follow who you want
bot.login(username="rupakparajuli07" , password = '1012343210123432')
bot.follow('nike')

# to upload photo

bot.upload_photo("C:/Users/paraj/OneDrive/Pictures/download.jpg " , caption="first photo")

# to unfollow someone
bot.login(username="rupakparajuli07" , password = '1012343210123432')
bot.unfollow("leomessi")

# to send multiple 

bot.send_message ("hello", ["cristiano" ,  "nike" ]  )

# to find detail followers list

followers=bot.get_user_followers("rupakparajuli07")
for follower in followers:
    print(bot.get_user_info(follower))


# to find detail following list

Following=bot.get_user_following("rupakparajuli07")
for Following in following:
    print(bot.get_user_info(Following))
    
    
    