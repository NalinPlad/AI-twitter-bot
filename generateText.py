import sys, json, time, tweepy

from textgenrnn import textgenrnn


def main():

    textgen = textgenrnn('/Users/ajitharaiza-singh/Downloads/coding/piffleManTwitterBot/realDonaldTrump_dril_twitter_weights.hdf5')

    # Authenticate to Twitter order: consumer_key, consumer_secret, access_token, access_token_secret
    auth = tweepy.OAuthHandler("FX4YidWBPnFL3XQr3EJ7s6jMZ", "JyGkyx5N0IrM6SYE1H6D6fef5HBPDxws17imVO2TXXakIBADxJ")
    auth.set_access_token("1255230049831264261-QaVaan6ZZ9NFeGW8id9N46gxs5CrEC", "IJWL5QHadzMgB85rTDJDHhxG86oFj3PXHHGh8aYnfD643")

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
