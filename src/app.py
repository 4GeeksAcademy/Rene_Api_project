import os
import pandas as pd
import spotipy
#import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

client_id=os.environ.get("CLIENT_ID")
client_secret= os.environ.get("CLIENT_SECRET")

urn = 'spotify:artist:5TeBsszZQTyqBX4eDHdtNx' #La nva escuela
sp = spotipy.Spotify()

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)
