import sys, json, time, tweepy

from textgenrnn import textgenrnn


def main():

    # type in the path of your .hdf5 file
    textgen = textgenrnn('realDonaldTrump_dril_twitter_weights.hdf5')

    # Authenticate to Twitter order: consumer_key, consumer_secret, access_token, access_token_secret
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)

    while True:


        genData = textgen.generate(return_as_list = True, temperature=0.2)


        # Create a tweet
        if len(genData) > 280:
            finalTweet = genData[0:280]
        else:
            finalTweet = genData

        api.update_status(finalTweet)
        print(finalTweet)

        time.sleep(30)








#start process
if __name__ == '__main__':
    main()
