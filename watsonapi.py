import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("SzASqEF1bD4L5tzk1wl7YM3Ngk4rkk9wKBT1hJ1w98Wl")
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://gateway.watsonplatform.net/tone-analyzer/api')


songlyrics = open("lyrics.txt")
lyrics = (songlyrics).read()
text = lyrics

# BE CAREFUL only run this part a couple of times!!!!
tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='text/plain',
    sentences = False
).get_result()

# gets strongest tone in the song
primary_tone = tone_analysis['document_tone']['tones'][0]['tone_name']
primary_tone = tone_analysis['document_tone']['tones'][0]['score']

