# AI-twitter-bot
## A python thingy that you can use to automatically post AI generated messages from your own dataset or pre-trained weights

# How to use!

Go to https://developer.twitter.com and apply for a developer account. Once this is complete go to your dashboard and create a new app. Go to the auth and keys tab and generate your CONSUMER_KEY, CONSUMER_SECRET, ACCSESS_TOKEN, and ACCESS_TOKEN_SECRET.

Open up to the generateText.py file and type in your keys from above in the apropriate strings. You can also add your own file, or .hdf5 wieghts file to ttrain on. Go to https://github.com/minimaxir/textgenrnn for more information on this. You can also use the realDonaldTrump_dril_twitter_weights.hdf5 file that is typed in by default to train on(this is a dataset of donald trump tweets lol). The script will automaticly create tweets every 30 seconds.
