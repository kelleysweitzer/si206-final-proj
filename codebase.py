import requests
import spotipy
import spotipy.util as util

#   S P O T I F Y     A P I
scope = 'playlist-read-private'

username = input("Please enter your username: ")

while(len(username) < 1):
    username = input("Invalid Username, try again: ")


# initialize user credentials
token = util.prompt_for_user_token(username,scope,client_id='d194c2865a1547efa27d1f0496272c8a',client_secret='f05c8ca055744cdeb18ee42b9a9441c7',redirect_uri='https://example.com/callback/')


if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = True
    results = sp.current_user_playlists()
    
    tracks = sp.user_playlist_tracks('kelleysweitz')
    print(tracks)
    # for item in results['items']:
    #     track = item['track']
    #     print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)

#Theo test